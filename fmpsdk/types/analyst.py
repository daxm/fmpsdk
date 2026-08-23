"""Response shapes returned by ``client.analyst`` methods."""

from __future__ import annotations

from typing import TypedDict

# --- client.analyst ----------------------------------------------------------


class AnalystEstimatesResult(TypedDict):
    """Consensus revenue/EPS/margin forecast for one period. Returned by
    `analyst_estimates()`."""

    symbol: str
    date: str
    revenueLow: float
    revenueHigh: float
    revenueAvg: float
    ebitdaLow: float
    ebitdaHigh: float
    ebitdaAvg: float
    ebitLow: float
    ebitHigh: float
    ebitAvg: float
    netIncomeLow: float
    netIncomeHigh: float
    netIncomeAvg: float
    sgaExpenseLow: float
    sgaExpenseHigh: float
    sgaExpenseAvg: float
    epsAvg: float
    epsHigh: float
    epsLow: float
    numAnalystsRevenue: int
    numAnalystsEps: int


class RatingsSnapshotResult(TypedDict):
    """Current overall rating and per-factor scores (DCF, ROE, ROA,
    debt/equity, P/E, P/B). Returned by `ratings_snapshot()`."""

    symbol: str
    rating: str
    overallScore: int
    discountedCashFlowScore: int
    returnOnEquityScore: int
    returnOnAssetsScore: int
    debtToEquityScore: int
    priceToEarningsScore: int
    priceToBookScore: int


class RatingsHistoricalResult(TypedDict):
    """Same score fields as `RatingsSnapshotResult` plus `date`, but kept
    separate: a point-in-time snapshot and a dated history entry answer
    different questions even where every other field lines up."""

    symbol: str
    date: str
    rating: str
    overallScore: int
    discountedCashFlowScore: int
    returnOnEquityScore: int
    returnOnAssetsScore: int
    debtToEquityScore: int
    priceToEarningsScore: int
    priceToBookScore: int


class PriceTargetSummaryResult(TypedDict):
    """Average analyst price targets over the last month/quarter/year/
    all-time, with publisher list. Returned by `price_target_summary()`."""

    symbol: str
    lastMonthCount: int
    lastMonthAvgPriceTarget: float
    lastQuarterCount: int
    lastQuarterAvgPriceTarget: float
    lastYearCount: int
    lastYearAvgPriceTarget: float
    allTimeCount: int
    allTimeAvgPriceTarget: float
    publishers: (
        str  # FMP sends this field as a JSON-encoded string, not a native array.
    )


class PriceTargetConsensusResult(TypedDict):
    """High/low/median/consensus analyst price targets. Returned by
    `price_target_consensus()`."""

    symbol: str
    targetHigh: float
    targetLow: float
    targetConsensus: float
    targetMedian: float


class GradesResult(TypedDict):
    """One analyst grading action (upgrade, downgrade, maintain).
    Returned by `grades()`."""

    symbol: str
    date: str
    gradingCompany: str
    previousGrade: str
    newGrade: str
    action: str


class GradesHistoricalResult(TypedDict):
    """Dated counts of strong-buy/buy/hold/sell/strong-sell ratings in
    force, one row per date. Returned by `grades_historical()`."""

    symbol: str
    date: str
    analystRatingsStrongBuy: int
    analystRatingsBuy: int
    analystRatingsHold: int
    analystRatingsSell: int
    analystRatingsStrongSell: int


class GradesConsensusResult(TypedDict):
    """Current consensus grade counts and overall consensus label (e.g.
    ``"Buy"``). Returned by `grades_consensus()`."""

    symbol: str
    strongBuy: int
    buy: int
    hold: int
    sell: int
    strongSell: int
    consensus: str
