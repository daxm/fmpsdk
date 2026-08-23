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
    symbol: str
    filingDate: str
    acceptedDate: str
    effectivenessDate: str
    cik: str
    form: str
    url: str


class IposProspectusResult(TypedDict):
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


class ProfileResult(TypedDict):
    """Shape shared by `profile` (lookup by symbol) and `profile_cik`
    (lookup by CIK) — identical fields in both documented examples, and
    both answer the same question (the company profile record), just
    keyed differently."""

    symbol: str
    price: float
    marketCap: float
    beta: float
    lastDividend: float
    range: str
    change: float
    changePercentage: float
    volume: int
    averageVolume: int
    companyName: str
    currency: str
    cik: str
    isin: str
    cusip: str
    exchangeFullName: str
    exchange: str
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
    image: str
    ipoDate: str
    defaultImage: bool
    isEtf: bool
    isActivelyTrading: bool
    isAdr: bool
    isFund: bool


class CompanyNotesResult(TypedDict):
    cik: str
    symbol: str
    title: str
    exchange: str


class StockPeersResult(TypedDict):
    symbol: str
    companyName: str
    price: float
    mktCap: float


class DelistedCompanyResult(TypedDict):
    symbol: str
    companyName: str
    exchange: str
    ipoDate: str
    delistedDate: str


class EmployeeCountResult(TypedDict):
    """Shape shared by `employee_count` (latest filing) and
    `historical_employee_count` (full history) — identical fields in both
    documented examples, same question at different scope."""

    symbol: str
    cik: str
    acceptanceTime: str
    periodOfReport: str
    companyName: str
    formType: str
    filingDate: str
    employeeCount: int
    source: str


class MarketCapResult(TypedDict):
    """Shape shared by `market_capitalization` (one symbol, latest),
    `market_capitalization_batch` (many symbols, latest), and
    `historical_market_capitalization` (one symbol, date range) —
    identical fields in all three documented examples, same question at
    different scope."""

    symbol: str
    date: str
    marketCap: float


class SharesFloatResult(TypedDict):
    symbol: str
    date: str
    freeFloat: float
    floatShares: int
    outstandingShares: int
    source: str


class SharesFloatAllResult(TypedDict):
    """Same as `SharesFloatResult` minus `source` — the market-wide
    listing's documented example doesn't include a per-row filing link."""

    symbol: str
    date: str
    freeFloat: float
    floatShares: int
    outstandingShares: int


class MergersAcquisitionsResult(TypedDict):
    """Shape shared by `mergers_acquisitions_latest` (recent, unfiltered)
    and `mergers_acquisitions_search` (filtered by company name) —
    identical fields in both documented examples, same question at
    different scope."""

    symbol: str
    companyName: str
    cik: str
    targetedCompanyName: str
    targetedCik: str
    targetedSymbol: str
    transactionDate: str
    acceptedDate: str
    link: str


class KeyExecutiveResult(TypedDict):
    title: str
    name: str
    pay: float | None
    currencyPay: str
    gender: str
    yearBorn: int | None
    # Type inferred, not verified: the documented example's only value is
    # `null`, so whether this is a date string, a year, or a timestamp is
    # unconfirmed. Flag for correction if a live response disagrees.
    titleSince: int | None
    active: bool


class ExecutiveCompensationResult(TypedDict):
    cik: str
    symbol: str
    companyName: str
    filingDate: str
    acceptedDate: str
    nameAndPosition: str
    year: int
    salary: float
    bonus: float
    stockAward: float
    optionAward: float
    incentivePlanCompensation: float
    allOtherCompensation: float
    total: float
    link: str


class ExecutiveCompensationBenchmarkResult(TypedDict):
    industryTitle: str
    year: int
    averageCompensation: float


# --- client.commitment_of_traders -----------------------------------------


class CommitmentOfTradersReportResult(TypedDict):
    """CFTC COT report, one row per market per date. ~140 fields — kept
    fully typed per the project's response-typing contract (§8.4) rather
    than collapsed to a looser type; field names are verbatim from the
    documented example, including its two `Spead`/`Spread` inconsistencies
    (not our typo to fix)."""

    symbol: str
    date: str
    name: str
    sector: str
    marketAndExchangeNames: str
    cftcContractMarketCode: str
    cftcMarketCode: str
    cftcRegionCode: str
    cftcCommodityCode: str
    openInterestAll: int
    noncommPositionsLongAll: int
    noncommPositionsShortAll: int
    noncommPositionsSpreadAll: int
    commPositionsLongAll: int
    commPositionsShortAll: int
    totReptPositionsLongAll: int
    totReptPositionsShortAll: int
    nonreptPositionsLongAll: int
    nonreptPositionsShortAll: int
    openInterestOld: int
    noncommPositionsLongOld: int
    noncommPositionsShortOld: int
    noncommPositionsSpreadOld: int
    commPositionsLongOld: int
    commPositionsShortOld: int
    totReptPositionsLongOld: int
    totReptPositionsShortOld: int
    nonreptPositionsLongOld: int
    nonreptPositionsShortOld: int
    openInterestOther: int
    noncommPositionsLongOther: int
    noncommPositionsShortOther: int
    noncommPositionsSpreadOther: int
    commPositionsLongOther: int
    commPositionsShortOther: int
    totReptPositionsLongOther: int
    totReptPositionsShortOther: int
    nonreptPositionsLongOther: int
    nonreptPositionsShortOther: int
    changeInOpenInterestAll: int
    changeInNoncommLongAll: int
    changeInNoncommShortAll: int
    changeInNoncommSpeadAll: int
    changeInCommLongAll: int
    changeInCommShortAll: int
    changeInTotReptLongAll: int
    changeInTotReptShortAll: int
    changeInNonreptLongAll: int
    changeInNonreptShortAll: int
    pctOfOpenInterestAll: float
    pctOfOiNoncommLongAll: float
    pctOfOiNoncommShortAll: float
    pctOfOiNoncommSpreadAll: float
    pctOfOiCommLongAll: float
    pctOfOiCommShortAll: float
    pctOfOiTotReptLongAll: float
    pctOfOiTotReptShortAll: float
    pctOfOiNonreptLongAll: float
    pctOfOiNonreptShortAll: float
    pctOfOpenInterestOl: float
    pctOfOiNoncommLongOl: float
    pctOfOiNoncommShortOl: float
    pctOfOiNoncommSpreadOl: float
    pctOfOiCommLongOl: float
    pctOfOiCommShortOl: float
    pctOfOiTotReptLongOl: float
    pctOfOiTotReptShortOl: float
    pctOfOiNonreptLongOl: float
    pctOfOiNonreptShortOl: float
    pctOfOpenInterestOther: float
    pctOfOiNoncommLongOther: float
    pctOfOiNoncommShortOther: float
    pctOfOiNoncommSpreadOther: float
    pctOfOiCommLongOther: float
    pctOfOiCommShortOther: float
    pctOfOiTotReptLongOther: float
    pctOfOiTotReptShortOther: float
    pctOfOiNonreptLongOther: float
    pctOfOiNonreptShortOther: float
    tradersTotAll: int
    tradersNoncommLongAll: int
    tradersNoncommShortAll: int
    tradersNoncommSpreadAll: int
    tradersCommLongAll: int
    tradersCommShortAll: int
    tradersTotReptLongAll: int
    tradersTotReptShortAll: int
    tradersTotOl: int
    tradersNoncommLongOl: int
    tradersNoncommShortOl: int
    tradersNoncommSpeadOl: int
    tradersCommLongOl: int
    tradersCommShortOl: int
    tradersTotReptLongOl: int
    tradersTotReptShortOl: int
    tradersTotOther: int
    tradersNoncommLongOther: int
    tradersNoncommShortOther: int
    tradersNoncommSpreadOther: int
    tradersCommLongOther: int
    tradersCommShortOther: int
    tradersTotReptLongOther: int
    tradersTotReptShortOther: int
    concGrossLe4TdrLongAll: float
    concGrossLe4TdrShortAll: float
    concGrossLe8TdrLongAll: float
    concGrossLe8TdrShortAll: float
    concNetLe4TdrLongAll: float
    concNetLe4TdrShortAll: float
    concNetLe8TdrLongAll: float
    concNetLe8TdrShortAll: float
    concGrossLe4TdrLongOl: float
    concGrossLe4TdrShortOl: float
    concGrossLe8TdrLongOl: float
    concGrossLe8TdrShortOl: float
    concNetLe4TdrLongOl: float
    concNetLe4TdrShortOl: float
    concNetLe8TdrLongOl: float
    concNetLe8TdrShortOl: float
    concGrossLe4TdrLongOther: float
    concGrossLe4TdrShortOther: float
    concGrossLe8TdrLongOther: float
    concGrossLe8TdrShortOther: float
    concNetLe4TdrLongOther: float
    concNetLe4TdrShortOther: float
    concNetLe8TdrLongOther: float
    concNetLe8TdrShortOther: float
    contractUnits: str


class CommitmentOfTradersAnalysisResult(TypedDict):
    symbol: str
    date: str
    name: str
    sector: str
    exchange: str
    currentLongMarketSituation: float
    currentShortMarketSituation: float
    marketSituation: str
    previousLongMarketSituation: float
    previousShortMarketSituation: float
    previousMarketSituation: str
    netPostion: int  # Verbatim from FMP's documented example — not our typo to fix.
    previousNetPosition: int
    changeInNetPosition: float
    marketSentiment: str
    reversalTrend: bool


class CommitmentOfTradersListResult(TypedDict):
    symbol: str
    name: str


# --- client.dcf -------------------------------------------------------------

# Functional form, not class syntax: the response's `Stock Price` field
# contains a space, which class-body TypedDict syntax can't express.
DiscountedCashFlowResult = TypedDict(
    "DiscountedCashFlowResult",
    {
        "symbol": str,
        "date": str,
        "dcf": float,
        "Stock Price": float,
    },
)


# Deliberately not shared with DiscountedCashFlowResult despite the
# identical field set: unlevered and levered DCF answer different
# valuation questions (§7.8's `profile` precedent — same rationale as
# HistoricalPriceEodNonSplitAdjustedResult vs. …DividendAdjustedResult).
LeveredDiscountedCashFlowResult = TypedDict(
    "LeveredDiscountedCashFlowResult",
    {
        "symbol": str,
        "date": str,
        "dcf": float,
        "Stock Price": float,
    },
)


class CustomDiscountedCashFlowResult(TypedDict):
    year: str
    symbol: str
    revenue: float
    revenuePercentage: float
    ebitda: float
    ebitdaPercentage: float
    ebit: float
    ebitPercentage: float
    depreciation: float
    depreciationPercentage: float
    totalCash: float
    totalCashPercentage: float
    receivables: float
    receivablesPercentage: float
    inventories: float
    inventoriesPercentage: float
    payable: float
    payablePercentage: float
    capitalExpenditure: float
    capitalExpenditurePercentage: float
    price: float
    beta: float
    dilutedSharesOutstanding: int
    costofDebt: float
    taxRate: float
    afterTaxCostOfDebt: float
    riskFreeRate: float
    marketRiskPremium: float
    costOfEquity: float
    totalDebt: float
    totalEquity: float
    totalCapital: float
    debtWeighting: float
    equityWeighting: float
    wacc: float
    taxRateCash: float
    ebiat: float
    ufcf: float
    sumPvUfcf: float
    longTermGrowthRate: float
    terminalValue: float
    presentTerminalValue: float
    enterpriseValue: float
    netDebt: float
    equityValue: float
    equityValuePerShare: float
    freeCashFlowT1: float


class CustomLeveredDiscountedCashFlowResult(TypedDict):
    year: str
    symbol: str
    revenue: float
    revenuePercentage: float
    capitalExpenditure: float
    capitalExpenditurePercentage: float
    price: float
    beta: float
    dilutedSharesOutstanding: int
    costofDebt: float
    taxRate: float
    afterTaxCostOfDebt: float
    riskFreeRate: float
    marketRiskPremium: float
    costOfEquity: float
    totalDebt: float
    totalEquity: float
    totalCapital: float
    debtWeighting: float
    equityWeighting: float
    wacc: float
    operatingCashFlow: float
    pvLfcf: float
    sumPvLfcf: float
    longTermGrowthRate: float
    freeCashFlow: float
    terminalValue: float
    presentTerminalValue: float
    enterpriseValue: float
    netDebt: float
    equityValue: float
    equityValuePerShare: float
    freeCashFlowT1: float
    operatingCashFlowPercentage: float


# --- client.economics --------------------------------------------------------


class TreasuryRatesResult(TypedDict):
    date: str
    month1: float
    month2: float
    month3: float
    month6: float
    year1: float
    year2: float
    year3: float
    year5: float
    year7: float
    year10: float
    year20: float
    year30: float


class EconomicIndicatorsResult(TypedDict):
    name: str
    date: str
    value: float


class EconomicCalendarResult(TypedDict):
    date: str
    country: str
    event: str
    currency: str
    previous: float
    estimate: float
    actual: float
    change: float
    impact: str
    changePercentage: float
    unit: str


class MarketRiskPremiumResult(TypedDict):
    country: str
    continent: str
    countryRiskPremium: float
    totalEquityRiskPremium: float


# --- client.esg ---------------------------------------------------------


class EsgDisclosuresResult(TypedDict):
    date: str
    acceptedDate: str
    symbol: str
    cik: str
    companyName: str
    formType: str
    environmentalScore: float
    socialScore: float
    governanceScore: float
    ESGScore: float
    url: str


class EsgRatingsResult(TypedDict):
    symbol: str
    cik: str
    companyName: str
    industry: str
    fiscalYear: int
    ESGRiskRating: str
    industryRank: str


class EsgBenchmarkResult(TypedDict):
    fiscalYear: int
    sector: str
    environmentalScore: float
    socialScore: float
    governanceScore: float
    ESGScore: float


class HistoricalChartResult(TypedDict):
    """Response for the 6 `historical_chart` intraday timeframes (§5.3
    collapse: `1min`/`5min`/`15min`/`30min`/`1hour`/`4hour` share one
    method and one shape). No `symbol` field in any documented example —
    unlike every other chart shape, the caller already knows which symbol
    they asked for."""

    date: str
    open: float
    low: float
    high: float
    close: float
    volume: int


class HistoricalPriceEodLightResult(TypedDict):
    symbol: str
    date: str
    price: float
    volume: int


class HistoricalPriceEodFullResult(TypedDict):
    symbol: str
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    change: float
    changePercent: float
    vwap: float


class HistoricalPriceEodNonSplitAdjustedResult(TypedDict):
    """Same field set as `HistoricalPriceEodDividendAdjustedResult`, but
    kept separate: split-adjustment and dividend-adjustment are different
    questions about "true" price, not the same query at different scope
    (contrast `DividendResult`/`SplitResult` above, §7.8's `profile`
    precedent)."""

    symbol: str
    date: str
    adjOpen: float
    adjHigh: float
    adjLow: float
    adjClose: float
    volume: int


class HistoricalPriceEodDividendAdjustedResult(TypedDict):
    """See `HistoricalPriceEodNonSplitAdjustedResult` — same shape,
    deliberately separate type."""

    symbol: str
    date: str
    adjOpen: float
    adjHigh: float
    adjLow: float
    adjClose: float
    volume: int


class SplitResult(TypedDict):
    """Shape shared by `splits` (one company's history) and
    `splits_calendar` (market-wide, one date range) — same rationale as
    `DividendResult`."""

    symbol: str
    date: str
    numerator: int
    denominator: int
    splitType: str
