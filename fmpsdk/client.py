"""The fmpsdk Client: owns the API key, HTTP session, timeouts, and retry
policy, and is the single request/response/error-mapping path that every
API method funnels through.

The methods themselves are grouped into mixin classes under
``endpoints/`` (one module per FMP data category), composed onto
:class:`Client` below. Each is also reachable through a matching
namespace attribute, e.g. ``client.quote.aftermarket_quote(...)``
alongside ``client.aftermarket_quote(...)`` — see ``groups.py``. (The
one exception is ``quote()`` itself, whose namespace attribute
``client.quote`` shadows the top-level method of the same name — call
it as ``client.quote.quote(...)``.)
"""

from __future__ import annotations

import logging
import os
import random
import time

import requests

from .exceptions import (
    FMPAuthenticationError,
    FMPError,
    FMPNotFoundError,
    FMPPlanLimitError,
    FMPRateLimitError,
    FMPServerError,
    FMPValidationError,
)
from .groups import attach_groups
from .endpoints.analyst import AnalystEndpoints
from .endpoints.bulk import BulkEndpoints
from .endpoints.calendar import CalendarEndpoints
from .endpoints.chart import ChartEndpoints
from .endpoints.commitment_of_traders import CommitmentOfTradersEndpoints
from .endpoints.commodity import CommodityEndpoints
from .endpoints.company import CompanyEndpoints
from .endpoints.congress import CongressEndpoints
from .endpoints.crypto import CryptoEndpoints
from .endpoints.dcf import DcfEndpoints
from .endpoints.directory import DirectoryEndpoints
from .endpoints.earnings_transcript import EarningsTranscriptEndpoints
from .endpoints.economics import EconomicsEndpoints
from .endpoints.esg import EsgEndpoints
from .endpoints.forex import ForexEndpoints
from .endpoints.funds import FundsEndpoints
from .endpoints.fundraisers import FundraisersEndpoints
from .endpoints.indexes import IndexesEndpoints
from .endpoints.insider_trades import InsiderTradesEndpoints
from .endpoints.institutional_ownership import InstitutionalOwnershipEndpoints
from .endpoints.market_hours import MarketHoursEndpoints
from .endpoints.market_performance import MarketPerformanceEndpoints
from .endpoints.news import NewsEndpoints
from .endpoints.quote import QuoteEndpoints
from .endpoints.search import SearchEndpoints
from .endpoints.sec_filings import SecFilingsEndpoints
from .endpoints.statements import StatementsEndpoints
from .endpoints.technical_indicators import TechnicalIndicatorsEndpoints
from .endpoints.tipranks import TipranksEndpoints

logger = logging.getLogger("fmpsdk")

BASE_URL = "https://financialmodelingprep.com/stable/"
DEFAULT_CONNECT_TIMEOUT = 5.0
DEFAULT_READ_TIMEOUT = 30.0
DEFAULT_MAX_RETRIES = 3

# Never retried, per brief 3.6: these are the caller's problem (bad params,
# bad key, plan doesn't cover it, resource doesn't exist), not a transient
# condition that a retry could fix.
_NON_RETRYABLE_STATUS_TO_EXCEPTION: dict[int, type[FMPError]] = {
    400: FMPValidationError,
    401: FMPAuthenticationError,
    403: FMPAuthenticationError,
    404: FMPNotFoundError,
}


def _compute_backoff_delay(attempt: int) -> float:
    """Seconds to sleep before retry number ``attempt`` (0-indexed).

    Exponential backoff with jitter: ``2**attempt`` seconds plus up to 1s
    of random jitter, so ``max_retries=3`` (the default) spaces retries at
    roughly 1-2s, 2-3s, 4-5s. The jitter keeps retries from synchronizing
    if this is ever driven concurrently; the exponential growth means a
    429 that won't clear for a bit doesn't get hammered repeatedly.

    Only 429 (rate limit) and 5xx (FMP-side failure) ever reach this
    function — 400/401/402/404 raise immediately in ``Client._get``, never
    retried, so they don't cost extra calls against the daily quota.

    :param attempt: 0 for the first retry, 1 for the second, etc.
    :return: seconds to sleep before the retry.
    """
    return (2.0**attempt) + random.uniform(0, 1)


def _map_error(response: requests.Response) -> FMPError:
    """Translate a non-2xx FMP response into the matching typed exception."""
    status = response.status_code
    body = response.text

    if status == 402:
        return FMPPlanLimitError(status_code=status, response_text=body)

    exception_cls = _NON_RETRYABLE_STATUS_TO_EXCEPTION.get(status)
    if exception_cls is None:
        exception_cls = FMPRateLimitError if status == 429 else FMPServerError

    message = f"FMP API returned {status} for {response.url}: {body[:500]}"
    return exception_cls(message, status_code=status, response_text=body)


def _is_retryable(response: requests.Response) -> bool:
    return response.status_code == 429 or response.status_code >= 500


class Client(
    SearchEndpoints,
    DirectoryEndpoints,
    AnalystEndpoints,
    CalendarEndpoints,
    ChartEndpoints,
    CompanyEndpoints,
    CommitmentOfTradersEndpoints,
    DcfEndpoints,
    EconomicsEndpoints,
    EsgEndpoints,
    FundsEndpoints,
    StatementsEndpoints,
    InstitutionalOwnershipEndpoints,
    IndexesEndpoints,
    CommodityEndpoints,
    CryptoEndpoints,
    FundraisersEndpoints,
    ForexEndpoints,
    InsiderTradesEndpoints,
    MarketPerformanceEndpoints,
    MarketHoursEndpoints,
    TechnicalIndicatorsEndpoints,
    NewsEndpoints,
    QuoteEndpoints,
    SecFilingsEndpoints,
    EarningsTranscriptEndpoints,
    CongressEndpoints,
    BulkEndpoints,
    TipranksEndpoints,
):
    """fmpsdk client.

    >>> client = Client()  # reads FMP_API_KEY from the environment
    >>> client = Client(api_key="...")  # or pass it explicitly
    """

    def __init__(
        self,
        api_key: str | None = None,
        *,
        connect_timeout: float = DEFAULT_CONNECT_TIMEOUT,
        read_timeout: float = DEFAULT_READ_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        session: requests.Session | None = None,
    ) -> None:
        self.api_key = api_key or os.environ.get("FMP_API_KEY")
        if not self.api_key:
            raise FMPAuthenticationError(
                "No API key provided. Pass api_key=... to Client() or set "
                "the FMP_API_KEY environment variable."
            )
        self.connect_timeout = connect_timeout
        self.read_timeout = read_timeout
        self.max_retries = max_retries
        self._session = session or requests.Session()
        attach_groups(self)

    def _get(self, path: str, params: dict) -> list | dict:
        """Issue one GET against ``stable/{path}``, retrying transient
        failures per the backoff policy above, and raise a typed
        :class:`~fmpsdk.exceptions.FMPError` on any non-2xx response.
        Parses the response body as JSON — every method uses this except
        ``financial_reports_xlsx``, which needs raw bytes and uses
        :meth:`_get_bytes` instead.

        :param path: the FMP ``stable/`` path, e.g. ``"search-symbol"``.
        :param params: query parameters. ``None`` values are dropped rather
            than sent, so FMP's own per-endpoint defaults apply.
        """
        return self._request(path, params, _parse_json)

    def _get_bytes(self, path: str, params: dict) -> bytes:
        """Same request/retry/error-mapping path as :meth:`_get`, but
        returns the raw response body instead of parsing it as JSON.

        Exists for exactly one caller: ``financial_reports_xlsx``, whose
        FMP response is a binary XLSX (ZIP-container) despite an
        ``application/json`` content-type header. ``response.json()``
        would raise ``JSONDecodeError`` against real XLSX bytes, so this
        endpoint cannot share :meth:`_get`'s parsing path.
        """
        return self._request(path, params, lambda response: response.content)

    def _request(self, path: str, params: dict, parse):
        """Shared GET/retry/error-mapping core for :meth:`_get` and
        :meth:`_get_bytes` — identical policy, different body handling."""
        url = f"{BASE_URL}{path}"
        query = {key: value for key, value in params.items() if value is not None}
        headers = {"apikey": self.api_key}

        attempt = 0
        while True:
            try:
                response = self._session.get(
                    url,
                    params=query,
                    headers=headers,
                    timeout=(self.connect_timeout, self.read_timeout),
                )
            except (requests.ConnectionError, requests.Timeout) as exc:
                if attempt >= self.max_retries:
                    raise FMPServerError(
                        f"Connection to {url} failed after {attempt + 1} attempt(s): {exc}"
                    ) from exc
                time.sleep(_compute_backoff_delay(attempt))
                attempt += 1
                continue

            if response.ok:
                return parse(response)

            if _is_retryable(response) and attempt < self.max_retries:
                time.sleep(_compute_backoff_delay(attempt))
                attempt += 1
                continue

            raise _map_error(response)


def _parse_json(response: requests.Response) -> list | dict:
    if not response.content:
        return []
    return response.json()
