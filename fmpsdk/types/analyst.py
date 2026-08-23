"""Response shapes returned by ``client.analyst`` methods."""

from __future__ import annotations

from typing import TypedDict

# --- client.analyst ----------------------------------------------------------


class AnalystEstimatesResult(TypedDict):
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
    symbol: str
    targetHigh: float
    targetLow: float
    targetConsensus: float
    targetMedian: float


class GradesResult(TypedDict):
    symbol: str
    date: str
    gradingCompany: str
    previousGrade: str
    newGrade: str
    action: str


class GradesHistoricalResult(TypedDict):
    symbol: str
    date: str
    analystRatingsStrongBuy: int
    analystRatingsBuy: int
    analystRatingsHold: int
    analystRatingsSell: int
    analystRatingsStrongSell: int


class GradesConsensusResult(TypedDict):
    symbol: str
    strongBuy: int
    buy: int
    hold: int
    sell: int
    strongSell: int
    consensus: str
