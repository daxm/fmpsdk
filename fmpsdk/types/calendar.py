"""Response shapes returned by ``client.calendar`` methods."""

from __future__ import annotations

from typing import TypedDict

# --- client.calendar -----------------------------------------------------


# Functional form, not class syntax: the response's `yield` field collides
# with the Python keyword, which class-body TypedDict syntax can't express.
DividendResult = TypedDict(
    "DividendResult",
    {
        # Shape shared by `dividends` (one company's history) and
        # `dividends_calendar` (market-wide, one date range) — identical
        # fields in both documented examples, and both answer the same
        # question (a dividend event record), just scoped differently.
        "symbol": str,
        "date": str,
        "recordDate": str,
        "paymentDate": str,
        "declarationDate": str,
        "adjDividend": float,
        "dividend": float,
        "yield": float,
        "frequency": str,
    },
)


class EarningsResult(TypedDict):
    """Shape shared by `earnings` (one company's history) and
    `earnings_calendar` (market-wide, one date range) — same rationale as
    `DividendResult`."""

    symbol: str
    date: str
    epsActual: float | None
    epsEstimated: float | None
    revenueActual: float | None
    revenueEstimated: float | None
    lastUpdated: str


class IposCalendarResult(TypedDict):
    """One upcoming or recent IPO. Returned by `ipos_calendar()`."""

    symbol: str
    date: str
    daa: str  # Verbatim from FMP's documented example — not a typo we're introducing.
    company: str
    exchange: str
    actions: str
    shares: int | None
    priceRange: str | None
    marketCap: float | None


class IposDisclosureResult(TypedDict):
    """One SEC IPO disclosure filing. Returned by `ipos_disclosure()`."""

    symbol: str
    filingDate: str
    acceptedDate: str
    effectivenessDate: str
    cik: str
    form: str
    url: str


class IposProspectusResult(TypedDict):
    """One SEC IPO prospectus filing, with offering-price detail.
    Returned by `ipos_prospectus()`."""

    symbol: str
    acceptedDate: str
    filingDate: str
    ipoDate: str
    cik: str
    pricePublicPerShare: float
    pricePublicTotal: float
    discountsAndCommissionsPerShare: float
    discountsAndCommissionsTotal: float
    proceedsBeforeExpensesPerShare: float
    proceedsBeforeExpensesTotal: float
    form: str
    url: str


class SplitResult(TypedDict):
    """Shape shared by `splits` (one company's history) and
    `splits_calendar` (market-wide, one date range) — same rationale as
    `DividendResult`."""

    symbol: str
    date: str
    numerator: int
    denominator: int
    splitType: str
