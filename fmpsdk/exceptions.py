"""Typed exception hierarchy for fmpsdk.

Every non-2xx response from FMP raises one of these instead of returning
``None`` or an error-shaped ``dict`` that a caller could mistake for
data. Catch :class:`FMPError` for "something went wrong," or one of the
subclasses below for a specific cause.
"""

from __future__ import annotations

PLAN_LIMIT_MESSAGE = (
    "Your current FMP plan doesn't include this request. See FMP's pricing "
    "plans to upgrade: https://site.financialmodelingprep.com/pricing-plans"
)


class FMPError(Exception):
    """Base class for all fmpsdk errors raised from an FMP API response.

    :ivar status_code: the HTTP status code returned by FMP, if any.
    :ivar response_text: FMP's raw response body, for detail beyond the
        message above it.
    """

    def __init__(
        self, message: str, status_code: int | None = None, response_text: str = ""
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.response_text = response_text


class FMPAuthenticationError(FMPError):
    """Raised on 401/403 — missing, invalid, or unauthorized API key."""


class FMPPlanLimitError(FMPError):
    """Raised on 402 — the current FMP plan doesn't cover this request.

    Deliberately worded as "this request," not "this endpoint": FMP gates
    some endpoints per-symbol rather than wholesale (e.g. a single gated
    ticker on an otherwise-working ``quote`` call), so an endpoint-level
    message would be misleading.
    """

    def __init__(self, status_code: int | None = None, response_text: str = "") -> None:
        super().__init__(
            PLAN_LIMIT_MESSAGE, status_code=status_code, response_text=response_text
        )


class FMPRateLimitError(FMPError):
    """Raised on 429 — too many requests."""


class FMPNotFoundError(FMPError):
    """Raised on 404 — no such endpoint/resource."""


class FMPValidationError(FMPError):
    """Raised on 400 — invalid request parameters."""


class FMPServerError(FMPError):
    """Raised on 5xx — an FMP-side failure."""
