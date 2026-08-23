"""The fmpsdk Client: owns the API key, HTTP session, timeouts, and retry
policy, and is the single request/response/error-mapping path that every
canonical method funnels through.

Canonical methods themselves are NOT defined here — they live in
``endpoints/<group>.py`` as mixin classes, and this module composes them
onto :class:`Client` (REWRITE_ARCHITECTURE.md §11). Alias groups
(``client.search``, ``client.quote``, ...) are attached in ``groups.py``.
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
from .endpoints.calendar import CalendarEndpoints
from .endpoints.chart import ChartEndpoints
from .endpoints.company import CompanyEndpoints
from .endpoints.directory import DirectoryEndpoints
from .endpoints.search import SearchEndpoints

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

        :param path: the FMP ``stable/`` path, e.g. ``"search-symbol"``.
        :param params: query parameters. ``None`` values are dropped rather
            than sent — FMP's own per-endpoint defaults apply, and we never
            invent a package-wide default for things like ``limit``/``page``
            (§8.8).
        """
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
                return _parse_json(response)

            if _is_retryable(response) and attempt < self.max_retries:
                time.sleep(_compute_backoff_delay(attempt))
                attempt += 1
                continue

            raise _map_error(response)


def _parse_json(response: requests.Response) -> list | dict:
    if not response.content:
        return []
    return response.json()
