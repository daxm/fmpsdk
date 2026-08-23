"""TypedDicts for FMP response shapes, generated from api-docs.md example
responses (REWRITE_ARCHITECTURE.md §8.4, §11). Cast at the JSON boundary in
each endpoint method via ``typing.cast()`` — zero runtime cost, no new
dependency.

One TypedDict per response *shape*, not per method: methods verified
identical under §5.1's V2 test (e.g. ``search_symbol`` / ``search_name``)
share a type. Methods that merely sit in the same group but answer
different questions (§7.8: ``profile`` means five different things across
the catalog) always get separate types.
"""

from __future__ import annotations

from typing import TypedDict

# --- client.search ---------------------------------------------------------


class SearchSymbolResult(TypedDict):
    """Shape shared by `search_symbol` and `search_name` (identical in both
    documented examples)."""

    symbol: str
    name: str
    currency: str
    exchangeFullName: str
    exchange: str


class SearchCikResult(TypedDict):
    symbol: str
    companyName: str
    cik: str
    exchangeFullName: str
    exchange: str
    currency: str


class SearchCusipResult(TypedDict):
    symbol: str
    companyName: str
    cusip: str
    marketCap: float


class SearchIsinResult(TypedDict):
    symbol: str
    name: str
    isin: str
    marketCap: float


class CompanyScreenerResult(TypedDict):
    symbol: str
    companyName: str
    marketCap: float
    sector: str
    industry: str
    beta: float
    price: float
    lastAnnualDividend: float
    volume: int
    exchange: str
    exchangeShortName: str
    country: str
    isEtf: bool
    isFund: bool
    isActivelyTrading: bool


class SearchExchangeVariantsResult(TypedDict):
    symbol: str
    price: float
    beta: float
    volAvg: int
    mktCap: float
    lastDiv: float
    range: str
    changes: float
    companyName: str
    currency: str
    cik: str
    isin: str
    cusip: str
    exchange: str
    exchangeShortName: str
    industry: str
    website: str
    description: str
    ceo: str
    sector: str
    country: str
    fullTimeEmployees: str
    phone: str
    address: str
    city: str
    state: str
    zip: str
    dcfDiff: float
    dcf: float
    image: str
    ipoDate: str
    defaultImage: bool
    isEtf: bool
    isActivelyTrading: bool
    isAdr: bool
    isFund: bool


# --- client.directory --------------------------------------------------------

# `stock_list` and `actively_trading_list`/`etf_list` share the {symbol, name}
# field set in FMP's docs, but per the module docstring's "different question"
# rule they stay separate types: whole-universe listing vs. two distinct
# filtered subsets, not the same query with different inputs.


class StockListResult(TypedDict):
    symbol: str
    companyName: str


class FinancialStatementSymbolListResult(TypedDict):
    symbol: str
    companyName: str
    tradingCurrency: str
    reportingCurrency: str


class CikListResult(TypedDict):
    cik: str
    companyName: str


class SymbolChangeResult(TypedDict):
    date: str
    companyName: str
    oldSymbol: str
    newSymbol: str


class EtfListResult(TypedDict):
    symbol: str
    name: str


class ActivelyTradingListResult(TypedDict):
    symbol: str
    name: str


class AvailableExchangeResult(TypedDict):
    exchange: str
    name: str
    countryName: str
    countryCode: str
    symbolSuffix: str
    delay: str


class AvailableSectorResult(TypedDict):
    sector: str


class AvailableIndustryResult(TypedDict):
    industry: str


class AvailableCountryResult(TypedDict):
    country: str


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
    publishers: str  # FMP sends this field as a JSON-encoded string, not a native array.


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
