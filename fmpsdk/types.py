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


# --- client.funds ------------------------------------------------------------


class EtfHoldingsResult(TypedDict):
    symbol: str
    asset: str
    name: str
    isin: str
    securityCusip: str
    sharesNumber: int
    weightPercentage: float
    marketValue: float
    updatedAt: str


class EtfInfoSectorExposure(TypedDict):
    """Nested shape of `EtfInfoResult`'s `sectorsList`."""

    industry: str
    exposure: float


class EtfInfoResult(TypedDict):
    symbol: str
    name: str
    description: str
    isin: str
    assetClass: str
    securityCusip: str
    domicile: str
    website: str
    etfCompany: str
    expenseRatio: float
    assetsUnderManagement: float
    avgVolume: int
    inceptionDate: str
    nav: float
    navCurrency: str
    holdingsCount: int
    isActivelyTrading: bool
    updatedAt: str
    sectorsList: list[EtfInfoSectorExposure]


class EtfCountryWeightingsResult(TypedDict):
    country: str
    # Verbatim from FMP's documented example: sent as a "97.26%"-style
    # string, not a float, unlike EtfSectorWeightingsResult below.
    weightPercentage: str


class EtfAssetExposureResult(TypedDict):
    """Different shape from `EtfHoldingsResult` despite the overlapping
    field names: this answers "which ETFs hold this asset" (one row per
    ETF), not "what does this ETF hold" (one row per asset) — no
    `name`/`isin`/`securityCusip` in the documented example."""

    symbol: str
    asset: str
    sharesNumber: int
    weightPercentage: float
    marketValue: float


class EtfSectorWeightingsResult(TypedDict):
    symbol: str
    sector: str
    weightPercentage: float


class FundsDisclosureHoldersLatestResult(TypedDict):
    cik: str
    holder: str
    securityCusip: str
    shares: int
    dateReported: str
    change: int
    weightPercent: float


class FundsDisclosureResult(TypedDict):
    cik: str
    date: str
    acceptedDate: str
    symbol: str
    name: str
    lei: str
    title: str
    cusip: str
    isin: str
    balance: float
    units: str
    cur_cd: str
    valUsd: float
    pctVal: float
    payoffProfile: str
    assetCat: str
    issuerCat: str
    invCountry: str
    isRestrictedSec: str
    fairValLevel: str
    isCashCollateral: str
    isNonCashCollateral: str
    isLoanByFund: str


class FundsDisclosureHoldersSearchResult(TypedDict):
    symbol: str
    cik: str
    classId: str
    seriesId: str
    entityName: str
    entityOrgType: str
    seriesName: str
    className: str
    reportingFileNumber: str
    address: str
    city: str
    zipCode: str
    state: str


class FundsDisclosureDatesResult(TypedDict):
    date: str
    year: int
    quarter: int


# --- client.statements ---------------------------------------------------


class IncomeStatementResult(TypedDict):
    """Shape shared by `income_statement` (periodic) and
    `income_statement_ttm` (trailing twelve months) — identical fields in
    both documented examples, same question at different scope."""

    date: str
    symbol: str
    reportedCurrency: str
    cik: str
    filingDate: str
    acceptedDate: str
    fiscalYear: str
    period: str
    revenue: float
    costOfRevenue: float
    grossProfit: float
    researchAndDevelopmentExpenses: float
    generalAndAdministrativeExpenses: float
    sellingAndMarketingExpenses: float
    sellingGeneralAndAdministrativeExpenses: float
    otherExpenses: float
    operatingExpenses: float
    costAndExpenses: float
    netInterestIncome: float
    interestIncome: float
    interestExpense: float
    depreciationAndAmortization: float
    ebitda: float
    ebit: float
    nonOperatingIncomeExcludingInterest: float
    operatingIncome: float
    totalOtherIncomeExpensesNet: float
    incomeBeforeTax: float
    incomeTaxExpense: float
    netIncomeFromContinuingOperations: float
    netIncomeFromDiscontinuedOperations: float
    otherAdjustmentsToNetIncome: float
    netIncome: float
    netIncomeDeductions: float
    bottomLineNetIncome: float
    eps: float
    epsDiluted: float
    weightedAverageShsOut: float
    weightedAverageShsOutDil: float


class BalanceSheetStatementResult(TypedDict):
    """`balance_sheet_statement` only — not shared with
    `balance_sheet_statement_ttm`: the TTM documented example is missing
    `capitalLeaseObligationsNonCurrent`, a genuine (if narrow) shape
    difference, not just a scope change."""

    date: str
    symbol: str
    reportedCurrency: str
    cik: str
    filingDate: str
    acceptedDate: str
    fiscalYear: str
    period: str
    cashAndCashEquivalents: float
    shortTermInvestments: float
    cashAndShortTermInvestments: float
    netReceivables: float
    accountsReceivables: float
    otherReceivables: float
    inventory: float
    prepaids: float
    otherCurrentAssets: float
    totalCurrentAssets: float
    propertyPlantEquipmentNet: float
    goodwill: float
    intangibleAssets: float
    goodwillAndIntangibleAssets: float
    longTermInvestments: float
    taxAssets: float
    otherNonCurrentAssets: float
    totalNonCurrentAssets: float
    otherAssets: float
    totalAssets: float
    totalPayables: float
    accountPayables: float
    otherPayables: float
    accruedExpenses: float
    shortTermDebt: float
    capitalLeaseObligationsCurrent: float
    taxPayables: float
    deferredRevenue: float
    otherCurrentLiabilities: float
    totalCurrentLiabilities: float
    longTermDebt: float
    capitalLeaseObligationsNonCurrent: float
    deferredRevenueNonCurrent: float
    deferredTaxLiabilitiesNonCurrent: float
    otherNonCurrentLiabilities: float
    totalNonCurrentLiabilities: float
    otherLiabilities: float
    capitalLeaseObligations: float
    totalLiabilities: float
    treasuryStock: float
    preferredStock: float
    commonStock: float
    retainedEarnings: float
    additionalPaidInCapital: float
    accumulatedOtherComprehensiveIncomeLoss: float
    otherTotalStockholdersEquity: float
    totalStockholdersEquity: float
    totalEquity: float
    minorityInterest: float
    totalLiabilitiesAndTotalEquity: float
    totalInvestments: float
    totalDebt: float
    netDebt: float


class BalanceSheetStatementTtmResult(TypedDict):
    """`balance_sheet_statement_ttm` only — see
    `BalanceSheetStatementResult` for why this isn't shared."""

    date: str
    symbol: str
    reportedCurrency: str
    cik: str
    filingDate: str
    acceptedDate: str
    fiscalYear: str
    period: str
    cashAndCashEquivalents: float
    shortTermInvestments: float
    cashAndShortTermInvestments: float
    netReceivables: float
    accountsReceivables: float
    otherReceivables: float
    inventory: float
    prepaids: float
    otherCurrentAssets: float
    totalCurrentAssets: float
    propertyPlantEquipmentNet: float
    goodwill: float
    intangibleAssets: float
    goodwillAndIntangibleAssets: float
    longTermInvestments: float
    taxAssets: float
    otherNonCurrentAssets: float
    totalNonCurrentAssets: float
    otherAssets: float
    totalAssets: float
    totalPayables: float
    accountPayables: float
    otherPayables: float
    accruedExpenses: float
    shortTermDebt: float
    capitalLeaseObligationsCurrent: float
    taxPayables: float
    deferredRevenue: float
    otherCurrentLiabilities: float
    totalCurrentLiabilities: float
    longTermDebt: float
    deferredRevenueNonCurrent: float
    deferredTaxLiabilitiesNonCurrent: float
    otherNonCurrentLiabilities: float
    totalNonCurrentLiabilities: float
    otherLiabilities: float
    capitalLeaseObligations: float
    totalLiabilities: float
    treasuryStock: float
    preferredStock: float
    commonStock: float
    retainedEarnings: float
    additionalPaidInCapital: float
    accumulatedOtherComprehensiveIncomeLoss: float
    otherTotalStockholdersEquity: float
    totalStockholdersEquity: float
    totalEquity: float
    minorityInterest: float
    totalLiabilitiesAndTotalEquity: float
    totalInvestments: float
    totalDebt: float
    netDebt: float


class CashFlowStatementResult(TypedDict):
    """Shape shared by `cash_flow_statement` (periodic) and
    `cash_flow_statement_ttm` (trailing twelve months) — identical fields
    in both documented examples, same question at different scope."""

    date: str
    symbol: str
    reportedCurrency: str
    cik: str
    filingDate: str
    acceptedDate: str
    fiscalYear: str
    period: str
    netIncome: float
    depreciationAndAmortization: float
    deferredIncomeTax: float
    stockBasedCompensation: float
    changeInWorkingCapital: float
    accountsReceivables: float
    inventory: float
    accountsPayables: float
    otherWorkingCapital: float
    otherNonCashItems: float
    netCashProvidedByOperatingActivities: float
    investmentsInPropertyPlantAndEquipment: float
    acquisitionsNet: float
    purchasesOfInvestments: float
    salesMaturitiesOfInvestments: float
    otherInvestingActivities: float
    netCashProvidedByInvestingActivities: float
    netDebtIssuance: float
    longTermNetDebtIssuance: float
    shortTermNetDebtIssuance: float
    netStockIssuance: float
    netCommonStockIssuance: float
    commonStockIssuance: float
    commonStockRepurchased: float
    netPreferredStockIssuance: float
    netDividendsPaid: float
    commonDividendsPaid: float
    preferredDividendsPaid: float
    otherFinancingActivities: float
    netCashProvidedByFinancingActivities: float
    effectOfForexChangesOnCash: float
    netChangeInCash: float
    cashAtEndOfPeriod: float
    cashAtBeginningOfPeriod: float
    operatingCashFlow: float
    capitalExpenditure: float
    freeCashFlow: float
    incomeTaxesPaid: float
    interestPaid: float


class LatestFinancialStatementsResult(TypedDict):
    symbol: str
    calendarYear: int
    period: str
    date: str
    dateAdded: str


class KeyMetricsResult(TypedDict):
    symbol: str
    date: str
    fiscalYear: str
    period: str
    reportedCurrency: str
    marketCap: float
    enterpriseValue: float
    evToSales: float
    evToOperatingCashFlow: float
    evToFreeCashFlow: float
    evToEBITDA: float
    netDebtToEBITDA: float
    currentRatio: float
    incomeQuality: float
    grahamNumber: float
    grahamNetNet: float
    taxBurden: float
    interestBurden: float
    workingCapital: float
    investedCapital: float
    returnOnAssets: float
    operatingReturnOnAssets: float
    returnOnTangibleAssets: float
    returnOnEquity: float
    returnOnInvestedCapital: float
    returnOnCapitalEmployed: float
    earningsYield: float
    freeCashFlowYield: float
    capexToOperatingCashFlow: float
    capexToDepreciation: float
    capexToRevenue: float
    salesGeneralAndAdministrativeToRevenue: float
    researchAndDevelopementToRevenue: float
    stockBasedCompensationToRevenue: float
    intangiblesToTotalAssets: float
    averageReceivables: float
    averagePayables: float
    averageInventory: float
    daysOfSalesOutstanding: float
    daysOfPayablesOutstanding: float
    daysOfInventoryOutstanding: float
    operatingCycle: float
    cashConversionCycle: float
    freeCashFlowToEquity: float
    freeCashFlowToFirm: float
    tangibleAssetValue: float
    netCurrentAssetValue: float


class KeyMetricsTtmResult(TypedDict):
    """Not shared with `KeyMetricsResult`: every field carries a `TTM`
    suffix and the date/fiscalYear/period/reportedCurrency fields are
    dropped entirely — a genuinely different shape, not just a scope
    change."""

    symbol: str
    marketCap: float
    enterpriseValueTTM: float
    evToSalesTTM: float
    evToOperatingCashFlowTTM: float
    evToFreeCashFlowTTM: float
    evToEBITDATTM: float
    netDebtToEBITDATTM: float
    currentRatioTTM: float
    incomeQualityTTM: float
    grahamNumberTTM: float
    grahamNetNetTTM: float
    taxBurdenTTM: float
    interestBurdenTTM: float
    workingCapitalTTM: float
    investedCapitalTTM: float
    returnOnAssetsTTM: float
    operatingReturnOnAssetsTTM: float
    returnOnTangibleAssetsTTM: float
    returnOnEquityTTM: float
    returnOnInvestedCapitalTTM: float
    returnOnCapitalEmployedTTM: float
    earningsYieldTTM: float
    freeCashFlowYieldTTM: float
    capexToOperatingCashFlowTTM: float
    capexToDepreciationTTM: float
    capexToRevenueTTM: float
    salesGeneralAndAdministrativeToRevenueTTM: float
    researchAndDevelopementToRevenueTTM: float
    stockBasedCompensationToRevenueTTM: float
    intangiblesToTotalAssetsTTM: float
    averageReceivablesTTM: float
    averagePayablesTTM: float
    averageInventoryTTM: float
    daysOfSalesOutstandingTTM: float
    daysOfPayablesOutstandingTTM: float
    daysOfInventoryOutstandingTTM: float
    operatingCycleTTM: float
    cashConversionCycleTTM: float
    freeCashFlowToEquityTTM: float
    freeCashFlowToFirmTTM: float
    tangibleAssetValueTTM: float
    netCurrentAssetValueTTM: float


class RatiosResult(TypedDict):
    symbol: str
    date: str
    fiscalYear: str
    period: str
    reportedCurrency: str
    grossProfitMargin: float
    ebitMargin: float
    ebitdaMargin: float
    operatingProfitMargin: float
    pretaxProfitMargin: float
    continuousOperationsProfitMargin: float
    netProfitMargin: float
    bottomLineProfitMargin: float
    receivablesTurnover: float
    payablesTurnover: float
    inventoryTurnover: float
    fixedAssetTurnover: float
    assetTurnover: float
    currentRatio: float
    quickRatio: float
    solvencyRatio: float
    cashRatio: float
    priceToEarningsRatio: float
    priceToEarningsGrowthRatio: float
    forwardPriceToEarningsGrowthRatio: float
    priceToEarningsDilutedRatio: float
    priceToEarningsDilutedGrowthRatio: float
    priceToBookRatio: float
    priceToSalesRatio: float
    priceToFreeCashFlowRatio: float
    priceToOperatingCashFlowRatio: float
    debtToAssetsRatio: float
    debtToEquityRatio: float
    debtToCapitalRatio: float
    longTermDebtToCapitalRatio: float
    financialLeverageRatio: float
    workingCapitalTurnoverRatio: float
    operatingCashFlowRatio: float
    operatingCashFlowSalesRatio: float
    freeCashFlowOperatingCashFlowRatio: float
    debtServiceCoverageRatio: float
    interestCoverageRatio: float
    shortTermOperatingCashFlowCoverageRatio: float
    operatingCashFlowCoverageRatio: float
    capitalExpenditureCoverageRatio: float
    dividendPaidAndCapexCoverageRatio: float
    dividendPayoutRatio: float
    dividendYield: float
    dividendYieldPercentage: float
    revenuePerShare: float
    netIncomePerShare: float
    interestDebtPerShare: float
    cashPerShare: float
    bookValuePerShare: float
    tangibleBookValuePerShare: float
    shareholdersEquityPerShare: float
    operatingCashFlowPerShare: float
    capexPerShare: float
    freeCashFlowPerShare: float
    netIncomePerEBT: float
    ebtPerEbit: float
    priceToFairValue: float
    debtToMarketCap: float
    effectiveTaxRate: float
    enterpriseValueMultiple: float
    dividendPerShare: float


class RatiosTtmResult(TypedDict):
    """Not shared with `RatiosResult`: every field carries a `TTM` suffix
    and date/fiscalYear/period/reportedCurrency are dropped — a
    genuinely different shape, not just a scope change."""

    symbol: str
    grossProfitMarginTTM: float
    ebitMarginTTM: float
    ebitdaMarginTTM: float
    operatingProfitMarginTTM: float
    pretaxProfitMarginTTM: float
    continuousOperationsProfitMarginTTM: float
    netProfitMarginTTM: float
    bottomLineProfitMarginTTM: float
    receivablesTurnoverTTM: float
    payablesTurnoverTTM: float
    inventoryTurnoverTTM: float
    fixedAssetTurnoverTTM: float
    assetTurnoverTTM: float
    currentRatioTTM: float
    quickRatioTTM: float
    solvencyRatioTTM: float
    cashRatioTTM: float
    priceToEarningsRatioTTM: float
    priceToEarningsGrowthRatioTTM: float
    forwardPriceToEarningsGrowthRatioTTM: float
    priceToEarningsDilutedRatioTTM: float
    priceToEarningsDilutedGrowthRatioTTM: float
    priceToBookRatioTTM: float
    priceToSalesRatioTTM: float
    priceToFreeCashFlowRatioTTM: float
    priceToOperatingCashFlowRatioTTM: float
    debtToAssetsRatioTTM: float
    debtToEquityRatioTTM: float
    debtToCapitalRatioTTM: float
    longTermDebtToCapitalRatioTTM: float
    financialLeverageRatioTTM: float
    workingCapitalTurnoverRatioTTM: float
    operatingCashFlowRatioTTM: float
    operatingCashFlowSalesRatioTTM: float
    freeCashFlowOperatingCashFlowRatioTTM: float
    debtServiceCoverageRatioTTM: float
    interestCoverageRatioTTM: float
    shortTermOperatingCashFlowCoverageRatioTTM: float
    operatingCashFlowCoverageRatioTTM: float
    capitalExpenditureCoverageRatioTTM: float
    dividendPaidAndCapexCoverageRatioTTM: float
    dividendPayoutRatioTTM: float
    dividendYieldTTM: float
    enterpriseValueTTM: float
    revenuePerShareTTM: float
    netIncomePerShareTTM: float
    interestDebtPerShareTTM: float
    cashPerShareTTM: float
    bookValuePerShareTTM: float
    tangibleBookValuePerShareTTM: float
    shareholdersEquityPerShareTTM: float
    operatingCashFlowPerShareTTM: float
    capexPerShareTTM: float
    freeCashFlowPerShareTTM: float
    netIncomePerEBTTTM: float
    ebtPerEbitTTM: float
    priceToFairValueTTM: float
    debtToMarketCapTTM: float
    effectiveTaxRateTTM: float
    enterpriseValueMultipleTTM: float
    dividendPerShareTTM: float


class FinancialScoresResult(TypedDict):
    symbol: str
    reportedCurrency: str
    altmanZScore: float
    piotroskiScore: int
    workingCapital: float
    totalAssets: float
    retainedEarnings: float
    ebit: float
    marketCap: float
    totalLiabilities: float
    revenue: float


class OwnerEarningsResult(TypedDict):
    symbol: str
    reportedCurrency: str
    fiscalYear: str
    period: str
    date: str
    averagePPE: float
    maintenanceCapex: float
    ownersEarnings: float
    growthCapex: float
    ownersEarningsPerShare: float


class EnterpriseValuesResult(TypedDict):
    symbol: str
    date: str
    stockPrice: float
    numberOfShares: float
    marketCapitalization: float
    minusCashAndCashEquivalents: float
    addTotalDebt: float
    enterpriseValue: float


class IncomeStatementGrowthResult(TypedDict):
    symbol: str
    date: str
    fiscalYear: str
    period: str
    reportedCurrency: str
    growthRevenue: float
    growthCostOfRevenue: float
    growthGrossProfit: float
    growthGrossProfitRatio: float
    growthResearchAndDevelopmentExpenses: float
    growthGeneralAndAdministrativeExpenses: float
    growthSellingAndMarketingExpenses: float
    growthOtherExpenses: float
    growthOperatingExpenses: float
    growthCostAndExpenses: float
    growthInterestIncome: float
    growthInterestExpense: float
    growthDepreciationAndAmortization: float
    growthEBITDA: float
    growthOperatingIncome: float
    growthIncomeBeforeTax: float
    growthIncomeTaxExpense: float
    growthNetIncome: float
    growthEPS: float
    growthEPSDiluted: float
    growthWeightedAverageShsOut: float
    growthWeightedAverageShsOutDil: float
    growthEBIT: float
    growthNonOperatingIncomeExcludingInterest: float
    growthNetInterestIncome: float
    growthTotalOtherIncomeExpensesNet: float
    growthNetIncomeFromContinuingOperations: float
    growthOtherAdjustmentsToNetIncome: float
    growthNetIncomeDeductions: float


class BalanceSheetStatementGrowthResult(TypedDict):
    symbol: str
    date: str
    fiscalYear: str
    period: str
    reportedCurrency: str
    growthCashAndCashEquivalents: float
    growthShortTermInvestments: float
    growthCashAndShortTermInvestments: float
    growthNetReceivables: float
    growthInventory: float
    growthOtherCurrentAssets: float
    growthTotalCurrentAssets: float
    growthPropertyPlantEquipmentNet: float
    growthGoodwill: float
    growthIntangibleAssets: float
    growthGoodwillAndIntangibleAssets: float
    growthLongTermInvestments: float
    growthTaxAssets: float
    growthOtherNonCurrentAssets: float
    growthTotalNonCurrentAssets: float
    growthOtherAssets: float
    growthTotalAssets: float
    growthAccountPayables: float
    growthShortTermDebt: float
    growthTaxPayables: float
    growthDeferredRevenue: float
    growthOtherCurrentLiabilities: float
    growthTotalCurrentLiabilities: float
    growthLongTermDebt: float
    growthDeferredRevenueNonCurrent: float
    growthDeferredTaxLiabilitiesNonCurrent: float
    growthOtherNonCurrentLiabilities: float
    growthTotalNonCurrentLiabilities: float
    growthOtherLiabilities: float
    growthTotalLiabilities: float
    growthPreferredStock: float
    growthCommonStock: float
    growthRetainedEarnings: float
    growthAccumulatedOtherComprehensiveIncomeLoss: float
    growthOthertotalStockholdersEquity: float
    growthTotalStockholdersEquity: float
    growthMinorityInterest: float
    growthTotalEquity: float
    growthTotalLiabilitiesAndStockholdersEquity: float
    growthTotalInvestments: float
    growthTotalDebt: float
    growthNetDebt: float
    growthAccountsReceivables: float
    growthOtherReceivables: float
    growthPrepaids: float
    growthTotalPayables: float
    growthOtherPayables: float
    growthAccruedExpenses: float
    growthCapitalLeaseObligationsCurrent: float
    growthAdditionalPaidInCapital: float
    growthTreasuryStock: float


class CashFlowStatementGrowthResult(TypedDict):
    symbol: str
    date: str
    fiscalYear: str
    period: str
    reportedCurrency: str
    growthNetIncome: float
    growthDepreciationAndAmortization: float
    growthDeferredIncomeTax: float
    growthStockBasedCompensation: float
    growthChangeInWorkingCapital: float
    growthAccountsReceivables: float
    growthInventory: float
    growthAccountsPayables: float
    growthOtherWorkingCapital: float
    growthOtherNonCashItems: float
    growthNetCashProvidedByOperatingActivites: float
    growthInvestmentsInPropertyPlantAndEquipment: float
    growthAcquisitionsNet: float
    growthPurchasesOfInvestments: float
    growthSalesMaturitiesOfInvestments: float
    growthOtherInvestingActivites: float
    growthNetCashUsedForInvestingActivites: float
    growthDebtRepayment: float
    growthCommonStockIssued: float
    growthCommonStockRepurchased: float
    growthDividendsPaid: float
    growthOtherFinancingActivites: float
    growthNetCashUsedProvidedByFinancingActivities: float
    growthEffectOfForexChangesOnCash: float
    growthNetChangeInCash: float
    growthCashAtEndOfPeriod: float
    growthCashAtBeginningOfPeriod: float
    growthOperatingCashFlow: float
    growthCapitalExpenditure: float
    growthFreeCashFlow: float
    growthNetDebtIssuance: float
    growthLongTermNetDebtIssuance: float
    growthShortTermNetDebtIssuance: float
    growthNetStockIssuance: float
    growthPreferredDividendsPaid: float
    growthIncomeTaxesPaid: float
    growthInterestPaid: float


class FinancialGrowthResult(TypedDict):
    symbol: str
    date: str
    fiscalYear: str
    period: str
    reportedCurrency: str
    revenueGrowth: float
    grossProfitGrowth: float
    ebitgrowth: float
    operatingIncomeGrowth: float
    netIncomeGrowth: float
    epsgrowth: float
    epsdilutedGrowth: float
    weightedAverageSharesGrowth: float
    weightedAverageSharesDilutedGrowth: float
    dividendsPerShareGrowth: float
    operatingCashFlowGrowth: float
    receivablesGrowth: float
    inventoryGrowth: float
    assetGrowth: float
    bookValueperShareGrowth: float
    debtGrowth: float
    rdexpenseGrowth: float
    sgaexpensesGrowth: float
    freeCashFlowGrowth: float
    tenYRevenueGrowthPerShare: float
    fiveYRevenueGrowthPerShare: float
    threeYRevenueGrowthPerShare: float
    tenYOperatingCFGrowthPerShare: float
    fiveYOperatingCFGrowthPerShare: float
    threeYOperatingCFGrowthPerShare: float
    tenYNetIncomeGrowthPerShare: float
    fiveYNetIncomeGrowthPerShare: float
    threeYNetIncomeGrowthPerShare: float
    tenYShareholdersEquityGrowthPerShare: float
    fiveYShareholdersEquityGrowthPerShare: float
    threeYShareholdersEquityGrowthPerShare: float
    tenYDividendperShareGrowthPerShare: float
    fiveYDividendperShareGrowthPerShare: float
    threeYDividendperShareGrowthPerShare: float
    ebitdaGrowth: float
    growthCapitalExpenditure: float
    tenYBottomLineNetIncomeGrowthPerShare: float
    fiveYBottomLineNetIncomeGrowthPerShare: float
    threeYBottomLineNetIncomeGrowthPerShare: float


class FinancialReportsDatesResult(TypedDict):
    symbol: str
    fiscalYear: int
    period: str
    linkJson: str
    linkXlsx: str


# `financial_reports_json` returns a per-filing document broken into
# named report sections ("Cover Page", "Auditor Information", ...) whose
# set is not fixed across filings/companies — genuinely dynamic, not a
# knowable static shape. A plain dict alias is the honest type here,
# same spirit as the loose typing on `financial_statement_full_as_reported`
# below, rather than forcing an inaccurate TypedDict onto free-form XBRL
# section data. Also: verified live that the real response is a single
# bare object, not the array FMP's own docs show it as (§8.4's second
# documented response-contract exception) — `financial_reports_json`
# returns `FinancialReportsJsonResult` directly, never
# `list[FinancialReportsJsonResult]`. `financial_reports_xlsx` (the first
# such exception) shares the same underlying report but returns raw XLSX
# bytes instead — also verified live, not assumed from the docs (whose
# example response for it is a byte-for-byte copy of this JSON shape).
FinancialReportsJsonResult = dict[str, object]


class IncomeStatementAsReportedResult(TypedDict):
    """Outer shape shared structurally with
    `BalanceSheetStatementAsReportedResult` and
    `CashFlowStatementAsReportedResult` (same `{..., data: dict}` wrapper)
    but kept as a separate named type — different statement, different
    question, same precedent as the EOD-adjustment types above."""

    symbol: str
    fiscalYear: int
    period: str
    reportedCurrency: str
    date: str
    data: dict[str, float]


class BalanceSheetStatementAsReportedResult(TypedDict):
    symbol: str
    fiscalYear: int
    period: str
    reportedCurrency: str
    date: str
    data: dict[str, float]


class CashFlowStatementAsReportedResult(TypedDict):
    symbol: str
    fiscalYear: int
    period: str
    reportedCurrency: str
    date: str
    data: dict[str, float]


class FinancialStatementFullAsReportedResult(TypedDict):
    """Like the three single-statement `*AsReportedResult` types, but
    `data` here is genuinely heterogeneous in the documented example —
    strings, boolean-as-string, and numbers side by side (this is the
    combined income+balance+cashflow filing, XBRL tag soup). Typed loosely
    on purpose, not an oversight."""

    symbol: str
    fiscalYear: int
    period: str
    reportedCurrency: str
    date: str
    data: dict[str, object]


class RevenueProductSegmentationResult(TypedDict):
    """Outer shape structurally identical to
    `RevenueGeographicSegmentationResult` but kept separate: product-line
    vs. geographic revenue breakdown are different questions, same
    precedent as the EOD-adjustment types above."""

    symbol: str
    fiscalYear: int
    period: str
    reportedCurrency: str
    date: str
    data: dict[str, float]


class RevenueGeographicSegmentationResult(TypedDict):
    symbol: str
    fiscalYear: int
    period: str
    reportedCurrency: str
    date: str
    data: dict[str, float]


# --- client.institutional_ownership --------------------------------------


class InstitutionalOwnershipLatestResult(TypedDict):
    cik: str
    name: str
    date: str
    filingDate: str
    acceptedDate: str
    formType: str
    link: str
    finalLink: str


class InstitutionalOwnershipExtractResult(TypedDict):
    date: str
    filingDate: str
    acceptedDate: str
    cik: str
    securityCusip: str
    symbol: str
    nameOfIssuer: str
    shares: int
    titleOfClass: str
    sharesType: str
    putCallShare: str
    value: float
    link: str
    finalLink: str


class InstitutionalOwnershipDatesResult(TypedDict):
    date: str
    year: int
    quarter: int


class InstitutionalOwnershipExtractAnalyticsHolderResult(TypedDict):
    date: str
    cik: str
    filingDate: str
    investorName: str
    symbol: str
    securityName: str
    typeOfSecurity: str
    securityCusip: str
    sharesType: str
    putCallShare: str
    investmentDiscretion: str
    industryTitle: str
    weight: float
    lastWeight: float
    changeInWeight: float
    changeInWeightPercentage: float
    marketValue: float
    lastMarketValue: float
    changeInMarketValue: float
    changeInMarketValuePercentage: float
    sharesNumber: int
    lastSharesNumber: int
    changeInSharesNumber: int
    changeInSharesNumberPercentage: float
    quarterEndPrice: float
    avgPricePaid: float
    isNew: bool
    isSoldOut: bool
    ownership: float
    lastOwnership: float
    changeInOwnership: float
    changeInOwnershipPercentage: float
    holdingPeriod: int
    firstAdded: str
    performance: float
    performancePercentage: float
    lastPerformance: float
    changeInPerformance: float
    isCountedForPerformance: bool


class InstitutionalOwnershipHolderPerformanceSummaryResult(TypedDict):
    date: str
    cik: str
    investorName: str
    portfolioSize: int
    securitiesAdded: int
    securitiesRemoved: int
    marketValue: float
    previousMarketValue: float
    changeInMarketValue: float
    changeInMarketValuePercentage: float
    averageHoldingPeriod: int
    averageHoldingPeriodTop10: int
    averageHoldingPeriodTop20: int
    turnover: float
    turnoverAlternateSell: float
    turnoverAlternateBuy: float
    performance: float
    performancePercentage: float
    lastPerformance: float
    changeInPerformance: float
    performance1year: float
    performancePercentage1year: float
    performance3year: float
    performancePercentage3year: float
    performance5year: float
    performancePercentage5year: float
    performanceSinceInception: float
    performanceSinceInceptionPercentage: float
    performanceRelativeToSP500Percentage: float
    performance1yearRelativeToSP500Percentage: float
    performance3yearRelativeToSP500Percentage: float
    performance5yearRelativeToSP500Percentage: float
    performanceSinceInceptionRelativeToSP500Percentage: float


class InstitutionalOwnershipHolderIndustryBreakdownResult(TypedDict):
    date: str
    cik: str
    investorName: str
    industryTitle: str
    weight: float
    lastWeight: float
    changeInWeight: float
    changeInWeightPercentage: float
    performance: float
    performancePercentage: float
    lastPerformance: float
    changeInPerformance: float


class InstitutionalOwnershipSymbolPositionsSummaryResult(TypedDict):
    symbol: str
    cik: str
    date: str
    investorsHolding: int
    lastInvestorsHolding: int
    investorsHoldingChange: int
    numberOf13Fshares: int
    lastNumberOf13Fshares: int
    numberOf13FsharesChange: int
    totalInvested: float
    lastTotalInvested: float
    totalInvestedChange: float
    ownershipPercent: float
    lastOwnershipPercent: float
    ownershipPercentChange: float
    newPositions: int
    lastNewPositions: int
    newPositionsChange: int
    increasedPositions: int
    lastIncreasedPositions: int
    increasedPositionsChange: int
    closedPositions: int
    lastClosedPositions: int
    closedPositionsChange: int
    reducedPositions: int
    lastReducedPositions: int
    reducedPositionsChange: int
    totalCalls: int
    lastTotalCalls: int
    totalCallsChange: int
    totalPuts: int
    lastTotalPuts: int
    totalPutsChange: int
    putCallRatio: float
    lastPutCallRatio: float
    putCallRatioChange: float


class InstitutionalOwnershipIndustrySummaryResult(TypedDict):
    industryTitle: str
    industryValue: float
    date: str


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


# --- client.indexes ---------------------------------------------------------


class IndexListResult(TypedDict):
    symbol: str
    name: str
    exchange: str
    currency: str


class IndexConstituentResult(TypedDict):
    """Shape shared by `sp500_constituent`, `nasdaq_constituent`, and
    `dowjones_constituent` — same question (current index membership) at
    different index scope, identical fields in all three documented
    examples."""

    symbol: str
    name: str
    sector: str
    subSector: str
    headQuarter: str
    dateFirstAdded: str | None
    cik: str
    founded: str


class HistoricalIndexConstituentResult(TypedDict):
    """Shape shared by `historical_sp500_constituent`,
    `historical_nasdaq_constituent`, and `historical_dowjones_constituent`
    — same rationale as `IndexConstituentResult`."""

    dateAdded: str
    addedSecurity: str
    removedTicker: str | None
    removedSecurity: str | None
    date: str
    symbol: str
    reason: str


# --- client.commodity --------------------------------------------------------


class CommoditiesListResult(TypedDict):
    symbol: str
    name: str
    exchange: str | None
    tradeMonth: str
    currency: str


# --- client.crypto ------------------------------------------------------------


class CryptocurrencyListResult(TypedDict):
    symbol: str
    name: str
    exchange: str
    icoDate: str | None
    circulatingSupply: float
    totalSupply: float | None


# --- client.fundraisers -------------------------------------------------------


class CrowdfundingOfferingResult(TypedDict):
    """Shape shared by `crowdfunding_offerings` (one issuer's campaigns by
    CIK) and `crowdfunding_offerings_latest` (market-wide, paginated) —
    identical fields in both documented examples."""

    cik: str
    companyName: str
    date: str | None
    filingDate: str
    acceptedDate: str
    formType: str
    formSignification: str
    nameOfIssuer: str
    legalStatusForm: str
    jurisdictionOrganization: str
    issuerStreet: str
    issuerCity: str
    issuerStateOrCountry: str
    issuerZipCode: str
    issuerWebsite: str | None
    intermediaryCompanyName: str
    intermediaryCommissionCik: str
    intermediaryCommissionFileNumber: str
    compensationAmount: str
    financialInterest: str | None
    securityOfferedType: str
    securityOfferedOtherDescription: str | None
    numberOfSecurityOffered: int
    offeringPrice: float
    offeringAmount: float
    overSubscriptionAccepted: str
    overSubscriptionAllocationType: str
    maximumOfferingAmount: float
    offeringDeadlineDate: str
    currentNumberOfEmployees: int
    totalAssetMostRecentFiscalYear: float
    totalAssetPriorFiscalYear: float
    cashAndCashEquiValentMostRecentFiscalYear: float
    cashAndCashEquiValentPriorFiscalYear: float
    accountsReceivableMostRecentFiscalYear: float
    accountsReceivablePriorFiscalYear: float
    shortTermDebtMostRecentFiscalYear: float
    shortTermDebtPriorFiscalYear: float
    longTermDebtMostRecentFiscalYear: float
    longTermDebtPriorFiscalYear: float
    revenueMostRecentFiscalYear: float
    revenuePriorFiscalYear: float
    costGoodsSoldMostRecentFiscalYear: float
    costGoodsSoldPriorFiscalYear: float
    taxesPaidMostRecentFiscalYear: float
    taxesPaidPriorFiscalYear: float
    netIncomeMostRecentFiscalYear: float
    netIncomePriorFiscalYear: float


class CrowdfundingOfferingSearchResult(TypedDict):
    cik: str
    name: str
    date: str | None


class FundraisingResult(TypedDict):
    """Shape shared by `fundraising` (one issuer's Reg D filings by CIK)
    and `fundraising_latest` (market-wide, paginated) — identical fields
    in both documented examples."""

    cik: str
    companyName: str
    date: str
    filingDate: str
    acceptedDate: str
    formType: str
    formSignification: str
    entityName: str
    issuerStreet: str
    issuerCity: str
    issuerStateOrCountry: str
    issuerStateOrCountryDescription: str
    issuerZipCode: str
    issuerPhoneNumber: str
    jurisdictionOfIncorporation: str
    entityType: str
    incorporatedWithinFiveYears: bool | None
    yearOfIncorporation: str
    relatedPersonFirstName: str
    relatedPersonLastName: str
    relatedPersonStreet: str
    relatedPersonCity: str
    relatedPersonStateOrCountry: str
    relatedPersonStateOrCountryDescription: str
    relatedPersonZipCode: str
    relatedPersonRelationship: str
    industryGroupType: str
    revenueRange: str
    federalExemptionsExclusions: str
    isAmendment: bool
    dateOfFirstSale: str
    durationOfOfferingIsMoreThanYear: bool
    securitiesOfferedAreOfEquityType: bool
    isBusinessCombinationTransaction: bool
    minimumInvestmentAccepted: float
    totalOfferingAmount: float
    totalAmountSold: float
    totalAmountRemaining: float
    hasNonAccreditedInvestors: bool
    totalNumberAlreadyInvested: int
    salesCommissions: float
    findersFees: float
    grossProceedsUsed: float


class FundraisingSearchResult(TypedDict):
    cik: str
    name: str
    date: str | None


# --- client.forex --------------------------------------------------------------


class ForexListResult(TypedDict):
    symbol: str
    fromCurrency: str
    toCurrency: str
    fromName: str
    toName: str


# --- client.insider_trades -----------------------------------------------------


class InsiderTradingResult(TypedDict):
    """Shape shared by `insider_trading_latest` and
    `insider_trading_search` — identical fields in both documented
    examples."""

    symbol: str
    filingDate: str
    transactionDate: str
    reportingCik: str
    companyCik: str
    transactionType: str
    securitiesOwned: float
    reportingName: str
    typeOfOwner: str
    acquisitionOrDisposition: str
    directOrIndirect: str
    formType: str
    securitiesTransacted: float
    price: float
    securityName: str
    url: str


class InsiderTradingReportingNameResult(TypedDict):
    reportingCik: str
    reportingName: str


class InsiderTradingTransactionTypeResult(TypedDict):
    transactionType: str


class InsiderTradingStatisticsResult(TypedDict):
    symbol: str
    cik: str
    year: int
    quarter: int
    acquiredTransactions: int
    disposedTransactions: int
    acquiredDisposedRatio: float
    totalAcquired: float
    totalDisposed: float
    averageAcquired: float
    averageDisposed: float
    totalPurchases: int
    totalSales: int


class AcquisitionOfBeneficialOwnershipResult(TypedDict):
    cik: str
    symbol: str
    filingDate: str
    acceptedDate: str
    cusip: str
    nameOfReportingPerson: str
    citizenshipOrPlaceOfOrganization: str
    soleVotingPower: str
    sharedVotingPower: str
    soleDispositivePower: str
    sharedDispositivePower: str
    amountBeneficiallyOwned: str
    percentOfClass: str
    typeOfReportingPerson: str
    url: str


# --- client.market_performance --------------------------------------------------


class MarketMoverResult(TypedDict):
    """Shape shared by `biggest_gainers`, `biggest_losers`, and
    `most_actives` — same question (a ranked list of stocks) at different
    ranking criteria, identical fields in all three documented examples."""

    symbol: str
    price: float
    name: str
    change: float
    changesPercentage: float
    exchange: str


class SectorPerformanceResult(TypedDict):
    """Shape shared by `sector_performance_snapshot` (one date) and
    `historical_sector_performance` (a date range) — identical fields."""

    date: str
    sector: str
    exchange: str
    averageChange: float


class IndustryPerformanceResult(TypedDict):
    """Shape shared by `industry_performance_snapshot` (one date) and
    `historical_industry_performance` (a date range) — identical fields."""

    date: str
    industry: str
    exchange: str
    averageChange: float


class SectorPeResult(TypedDict):
    """Shape shared by `sector_pe_snapshot` (one date) and
    `historical_sector_pe` (a date range) — identical fields."""

    date: str
    sector: str
    exchange: str
    pe: float


class IndustryPeResult(TypedDict):
    """Shape shared by `industry_pe_snapshot` (one date) and
    `historical_industry_pe` (a date range) — identical fields."""

    date: str
    industry: str
    exchange: str
    pe: float


# --- client.market_hours --------------------------------------------------------


class ExchangeMarketHoursResult(TypedDict):
    """Shape shared by `exchange_market_hours` (one exchange) and
    `all_exchange_market_hours` (every exchange) — identical fields."""

    exchange: str
    name: str
    openingHour: str
    closingHour: str
    timezone: str
    isMarketOpen: bool


class HolidaysByExchangeResult(TypedDict):
    exchange: str
    date: str
    name: str
    isClosed: bool
    adjOpenTime: str | None
    adjCloseTime: str | None


# --- client.technical_indicators -------------------------------------------------
# One TypedDict per indicator, not shared: the indicator's own value lives
# under a key literally named after the indicator (`sma`, `rsi`, ...), so
# the shapes differ in key name, not just semantics — can't be the same
# TypedDict. All 9 share the same 6 OHLCV+date base fields otherwise.


class SmaResult(TypedDict):
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    sma: float


class EmaResult(TypedDict):
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    ema: float


class WmaResult(TypedDict):
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    wma: float


class DemaResult(TypedDict):
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    dema: float


class TemaResult(TypedDict):
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    tema: float


class RsiResult(TypedDict):
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    rsi: float


class StandardDeviationResult(TypedDict):
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    standardDeviation: float


class WilliamsResult(TypedDict):
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    williams: float


class AdxResult(TypedDict):
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    adx: float
    splitType: str
