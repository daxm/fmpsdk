"""Response shapes returned by ``client.bulk`` methods.

**Every method except `profile_bulk` returns every field as a JSON
string, including fields that are semantically numeric or boolean** —
e.g. `rating_bulk`'s `"discountedCashFlowScore": "5"`,
`earnings_surprises_bulk`'s `"epsActual": "0.3631"`. Don't assume
`int`/`float` on these without converting first. `profile_bulk` is the
lone exception, with real JSON numbers/booleans (it shares its shape
with `ProfileResult`, from `profile`/`profile_cik`). This whole group
is Ultimate-gated on FMP's free tier, so the all-string typing is taken
from FMP's documented examples rather than a live response — worth a
sanity check against a real response if you're on a paid plan.

`cash_flow_statement_growth_bulk`'s field names preserve FMP's own
typos verbatim (`...Activites`, missing the second `i`, on 3 fields) —
not fixed here, since that would break parsing a real response.
"""

from __future__ import annotations

from typing import TypedDict


class RatingBulkResult(TypedDict):
    """Current overall rating and component scores for every company at once. Returned by `rating_bulk()`."""

    symbol: str
    date: str
    rating: str
    discountedCashFlowScore: str
    returnOnEquityScore: str
    returnOnAssetsScore: str
    debtToEquityScore: str
    priceToEarningsScore: str
    priceToBookScore: str


# Functional form, not class syntax: `"Stock Price"` contains a literal
# space (same reason as `DiscountedCashFlowResult` in types/dcf.py).
DcfBulkResult = TypedDict(
    "DcfBulkResult",
    {
        "symbol": str,
        "date": str,
        "dcf": str,
        "Stock Price": str,
    },
)


class ScoresBulkResult(TypedDict):
    """Altman Z-Score, Piotroski score, and related financial-health metrics for every company at once. Returned by `scores_bulk()`."""

    symbol: str
    reportedCurrency: str
    altmanZScore: str
    piotroskiScore: str
    workingCapital: str
    totalAssets: str
    retainedEarnings: str
    ebit: str
    marketCap: str
    totalLiabilities: str
    revenue: str


class PriceTargetSummaryBulkResult(TypedDict):
    """Analyst price-target summary (last month/quarter/year/all-time) for every company at once. Returned by `price_target_summary_bulk()`."""

    symbol: str
    lastMonthCount: str
    lastMonthAvgPriceTarget: str
    lastQuarterCount: str
    lastQuarterAvgPriceTarget: str
    lastYearCount: str
    lastYearAvgPriceTarget: str
    allTimeCount: str
    allTimeAvgPriceTarget: str
    publishers: str


class EtfHolderBulkResult(TypedDict):
    """ETF holdings for a whole page of the universe at once. Returned by `etf_holder_bulk()`."""

    symbol: str
    name: str
    sharesNumber: str
    asset: str
    weightPercentage: str
    cusip: str
    isin: str
    marketValue: str
    lastUpdated: str


class UpgradesDowngradesConsensusBulkResult(TypedDict):
    """Analyst upgrade/downgrade consensus for every company at once. Returned by `upgrades_downgrades_consensus_bulk()`."""

    symbol: str
    strongBuy: str
    buy: str
    hold: str
    sell: str
    strongSell: str
    consensus: str


class KeyMetricsTtmBulkResult(TypedDict):
    """Trailing-twelve-month key metrics for every company at once. Returned by `key_metrics_ttm_bulk()`."""

    symbol: str
    marketCap: str
    enterpriseValueTTM: str
    evToSalesTTM: str
    evToOperatingCashFlowTTM: str
    evToFreeCashFlowTTM: str
    evToEBITDATTM: str
    netDebtToEBITDATTM: str
    currentRatioTTM: str
    incomeQualityTTM: str
    grahamNumberTTM: str
    grahamNetNetTTM: str
    taxBurdenTTM: str
    interestBurdenTTM: str
    workingCapitalTTM: str
    investedCapitalTTM: str
    returnOnAssetsTTM: str
    operatingReturnOnAssetsTTM: str
    returnOnTangibleAssetsTTM: str
    returnOnEquityTTM: str
    returnOnInvestedCapitalTTM: str
    returnOnCapitalEmployedTTM: str
    earningsYieldTTM: str
    freeCashFlowYieldTTM: str
    capexToOperatingCashFlowTTM: str
    capexToDepreciationTTM: str
    capexToRevenueTTM: str
    salesGeneralAndAdministrativeToRevenueTTM: str
    researchAndDevelopementToRevenueTTM: str
    stockBasedCompensationToRevenueTTM: str
    intangiblesToTotalAssetsTTM: str
    averageReceivablesTTM: str
    averagePayablesTTM: str
    averageInventoryTTM: str
    daysOfSalesOutstandingTTM: str
    daysOfPayablesOutstandingTTM: str
    daysOfInventoryOutstandingTTM: str
    operatingCycleTTM: str
    cashConversionCycleTTM: str
    freeCashFlowToEquityTTM: str
    freeCashFlowToFirmTTM: str
    tangibleAssetValueTTM: str
    netCurrentAssetValueTTM: str


class RatiosTtmBulkResult(TypedDict):
    """Trailing-twelve-month financial ratios for every company at once. Returned by `ratios_ttm_bulk()`."""

    symbol: str
    grossProfitMarginTTM: str
    ebitMarginTTM: str
    ebitdaMarginTTM: str
    operatingProfitMarginTTM: str
    pretaxProfitMarginTTM: str
    continuousOperationsProfitMarginTTM: str
    netProfitMarginTTM: str
    bottomLineProfitMarginTTM: str
    receivablesTurnoverTTM: str
    payablesTurnoverTTM: str
    inventoryTurnoverTTM: str
    fixedAssetTurnoverTTM: str
    assetTurnoverTTM: str
    currentRatioTTM: str
    quickRatioTTM: str
    solvencyRatioTTM: str
    cashRatioTTM: str
    priceToEarningsRatioTTM: str
    priceToEarningsGrowthRatioTTM: str
    forwardPriceToEarningsGrowthRatioTTM: str
    priceToBookRatioTTM: str
    priceToSalesRatioTTM: str
    priceToFreeCashFlowRatioTTM: str
    priceToOperatingCashFlowRatioTTM: str
    debtToAssetsRatioTTM: str
    debtToEquityRatioTTM: str
    debtToCapitalRatioTTM: str
    longTermDebtToCapitalRatioTTM: str
    financialLeverageRatioTTM: str
    workingCapitalTurnoverRatioTTM: str
    operatingCashFlowRatioTTM: str
    operatingCashFlowSalesRatioTTM: str
    freeCashFlowOperatingCashFlowRatioTTM: str
    debtServiceCoverageRatioTTM: str
    interestCoverageRatioTTM: str
    shortTermOperatingCashFlowCoverageRatioTTM: str
    operatingCashFlowCoverageRatioTTM: str
    capitalExpenditureCoverageRatioTTM: str
    dividendPaidAndCapexCoverageRatioTTM: str
    dividendPayoutRatioTTM: str
    dividendYieldTTM: str
    enterpriseValueTTM: str
    revenuePerShareTTM: str
    netIncomePerShareTTM: str
    interestDebtPerShareTTM: str
    cashPerShareTTM: str
    bookValuePerShareTTM: str
    tangibleBookValuePerShareTTM: str
    shareholdersEquityPerShareTTM: str
    operatingCashFlowPerShareTTM: str
    capexPerShareTTM: str
    freeCashFlowPerShareTTM: str
    netIncomePerEBTTTM: str
    ebtPerEbitTTM: str
    priceToFairValueTTM: str
    debtToMarketCapTTM: str
    effectiveTaxRateTTM: str
    enterpriseValueMultipleTTM: str
    dividendPerShareTTM: str


class PeersBulkResult(TypedDict):
    """Peer-company list for every company at once. Returned by `peers_bulk()`."""

    symbol: str
    peers: str


class EarningsSurprisesBulkResult(TypedDict):
    """Actual vs. estimated EPS for every company, for one fiscal year. Returned by `earnings_surprises_bulk()`."""

    symbol: str
    date: str
    epsActual: str
    epsEstimated: str
    lastUpdated: str


class IncomeStatementBulkResult(TypedDict):
    """Income statement for every company, for one fiscal period. Returned by `income_statement_bulk()`."""

    date: str
    symbol: str
    reportedCurrency: str
    cik: str
    filingDate: str
    acceptedDate: str
    fiscalYear: str
    period: str
    revenue: str
    costOfRevenue: str
    grossProfit: str
    researchAndDevelopmentExpenses: str
    generalAndAdministrativeExpenses: str
    sellingAndMarketingExpenses: str
    sellingGeneralAndAdministrativeExpenses: str
    otherExpenses: str
    operatingExpenses: str
    costAndExpenses: str
    netInterestIncome: str
    interestIncome: str
    interestExpense: str
    depreciationAndAmortization: str
    ebitda: str
    ebit: str
    nonOperatingIncomeExcludingInterest: str
    operatingIncome: str
    totalOtherIncomeExpensesNet: str
    incomeBeforeTax: str
    incomeTaxExpense: str
    netIncomeFromContinuingOperations: str
    netIncomeFromDiscontinuedOperations: str
    otherAdjustmentsToNetIncome: str
    netIncome: str
    netIncomeDeductions: str
    bottomLineNetIncome: str
    eps: str
    epsDiluted: str
    weightedAverageShsOut: str
    weightedAverageShsOutDil: str


class IncomeStatementGrowthBulkResult(TypedDict):
    """Income statement growth for every company, for one fiscal period. Returned by `income_statement_growth_bulk()`."""

    symbol: str
    date: str
    fiscalYear: str
    period: str
    reportedCurrency: str
    growthRevenue: str
    growthCostOfRevenue: str
    growthGrossProfit: str
    growthGrossProfitRatio: str
    growthResearchAndDevelopmentExpenses: str
    growthGeneralAndAdministrativeExpenses: str
    growthSellingAndMarketingExpenses: str
    growthOtherExpenses: str
    growthOperatingExpenses: str
    growthCostAndExpenses: str
    growthInterestIncome: str
    growthInterestExpense: str
    growthDepreciationAndAmortization: str
    growthEBITDA: str
    growthOperatingIncome: str
    growthIncomeBeforeTax: str
    growthIncomeTaxExpense: str
    growthNetIncome: str
    growthEPS: str
    growthEPSDiluted: str
    growthWeightedAverageShsOut: str
    growthWeightedAverageShsOutDil: str
    growthEBIT: str
    growthNonOperatingIncomeExcludingInterest: str
    growthNetInterestIncome: str
    growthTotalOtherIncomeExpensesNet: str
    growthNetIncomeFromContinuingOperations: str
    growthOtherAdjustmentsToNetIncome: str
    growthNetIncomeDeductions: str


class BalanceSheetStatementBulkResult(TypedDict):
    """Balance sheet for every company, for one fiscal period. Returned by `balance_sheet_statement_bulk()`."""

    date: str
    symbol: str
    reportedCurrency: str
    cik: str
    filingDate: str
    acceptedDate: str
    fiscalYear: str
    period: str
    cashAndCashEquivalents: str
    shortTermInvestments: str
    cashAndShortTermInvestments: str
    netReceivables: str
    accountsReceivables: str
    otherReceivables: str
    inventory: str
    prepaids: str
    otherCurrentAssets: str
    totalCurrentAssets: str
    propertyPlantEquipmentNet: str
    goodwill: str
    intangibleAssets: str
    goodwillAndIntangibleAssets: str
    longTermInvestments: str
    taxAssets: str
    otherNonCurrentAssets: str
    totalNonCurrentAssets: str
    otherAssets: str
    totalAssets: str
    totalPayables: str
    accountPayables: str
    otherPayables: str
    accruedExpenses: str
    shortTermDebt: str
    capitalLeaseObligationsCurrent: str
    taxPayables: str
    deferredRevenue: str
    otherCurrentLiabilities: str
    totalCurrentLiabilities: str
    longTermDebt: str
    capitalLeaseObligationsNonCurrent: str
    deferredRevenueNonCurrent: str
    deferredTaxLiabilitiesNonCurrent: str
    otherNonCurrentLiabilities: str
    totalNonCurrentLiabilities: str
    otherLiabilities: str
    capitalLeaseObligations: str
    totalLiabilities: str
    treasuryStock: str
    preferredStock: str
    commonStock: str
    retainedEarnings: str
    additionalPaidInCapital: str
    accumulatedOtherComprehensiveIncomeLoss: str
    otherTotalStockholdersEquity: str
    totalStockholdersEquity: str
    totalEquity: str
    minorityInterest: str
    totalLiabilitiesAndTotalEquity: str
    totalInvestments: str
    totalDebt: str
    netDebt: str


class BalanceSheetStatementGrowthBulkResult(TypedDict):
    """Balance sheet growth for every company, for one fiscal period. Returned by `balance_sheet_statement_growth_bulk()`."""

    symbol: str
    date: str
    fiscalYear: str
    period: str
    reportedCurrency: str
    growthCashAndCashEquivalents: str
    growthShortTermInvestments: str
    growthCashAndShortTermInvestments: str
    growthNetReceivables: str
    growthInventory: str
    growthOtherCurrentAssets: str
    growthTotalCurrentAssets: str
    growthPropertyPlantEquipmentNet: str
    growthGoodwill: str
    growthIntangibleAssets: str
    growthGoodwillAndIntangibleAssets: str
    growthLongTermInvestments: str
    growthTaxAssets: str
    growthOtherNonCurrentAssets: str
    growthTotalNonCurrentAssets: str
    growthOtherAssets: str
    growthTotalAssets: str
    growthAccountPayables: str
    growthShortTermDebt: str
    growthTaxPayables: str
    growthDeferredRevenue: str
    growthOtherCurrentLiabilities: str
    growthTotalCurrentLiabilities: str
    growthLongTermDebt: str
    growthDeferredRevenueNonCurrent: str
    growthDeferredTaxLiabilitiesNonCurrent: str
    growthOtherNonCurrentLiabilities: str
    growthTotalNonCurrentLiabilities: str
    growthOtherLiabilities: str
    growthTotalLiabilities: str
    growthPreferredStock: str
    growthCommonStock: str
    growthRetainedEarnings: str
    growthAccumulatedOtherComprehensiveIncomeLoss: str
    growthOthertotalStockholdersEquity: str
    growthTotalStockholdersEquity: str
    growthMinorityInterest: str
    growthTotalEquity: str
    growthTotalLiabilitiesAndStockholdersEquity: str
    growthTotalInvestments: str
    growthTotalDebt: str
    growthNetDebt: str
    growthAccountsReceivables: str
    growthOtherReceivables: str
    growthPrepaids: str
    growthTotalPayables: str
    growthOtherPayables: str
    growthAccruedExpenses: str
    growthCapitalLeaseObligationsCurrent: str
    growthAdditionalPaidInCapital: str
    growthTreasuryStock: str


class CashFlowStatementBulkResult(TypedDict):
    """Cash flow statement for every company, for one fiscal period. Returned by `cash_flow_statement_bulk()`."""

    date: str
    symbol: str
    reportedCurrency: str
    cik: str
    filingDate: str
    acceptedDate: str
    fiscalYear: str
    period: str
    netIncome: str
    depreciationAndAmortization: str
    deferredIncomeTax: str
    stockBasedCompensation: str
    changeInWorkingCapital: str
    accountsReceivables: str
    inventory: str
    accountsPayables: str
    otherWorkingCapital: str
    otherNonCashItems: str
    netCashProvidedByOperatingActivities: str
    investmentsInPropertyPlantAndEquipment: str
    acquisitionsNet: str
    purchasesOfInvestments: str
    salesMaturitiesOfInvestments: str
    otherInvestingActivities: str
    netCashProvidedByInvestingActivities: str
    netDebtIssuance: str
    longTermNetDebtIssuance: str
    shortTermNetDebtIssuance: str
    netStockIssuance: str
    netCommonStockIssuance: str
    commonStockIssuance: str
    commonStockRepurchased: str
    netPreferredStockIssuance: str
    netDividendsPaid: str
    commonDividendsPaid: str
    preferredDividendsPaid: str
    otherFinancingActivities: str
    netCashProvidedByFinancingActivities: str
    effectOfForexChangesOnCash: str
    netChangeInCash: str
    cashAtEndOfPeriod: str
    cashAtBeginningOfPeriod: str
    operatingCashFlow: str
    capitalExpenditure: str
    freeCashFlow: str
    incomeTaxesPaid: str
    interestPaid: str


class CashFlowStatementGrowthBulkResult(TypedDict):
    """3 fields keep FMP's own typo verbatim — `...Activites`, missing
    the second `i` — matching the real documented response, not
    `cash_flow_statement_bulk`'s correctly-spelled
    `...ProvidedByOperatingActivities`/etc. Don't "fix" these; it would
    break the cast against real JSON."""

    symbol: str
    date: str
    fiscalYear: str
    period: str
    reportedCurrency: str
    growthNetIncome: str
    growthDepreciationAndAmortization: str
    growthDeferredIncomeTax: str
    growthStockBasedCompensation: str
    growthChangeInWorkingCapital: str
    growthAccountsReceivables: str
    growthInventory: str
    growthAccountsPayables: str
    growthOtherWorkingCapital: str
    growthOtherNonCashItems: str
    growthNetCashProvidedByOperatingActivites: str
    growthInvestmentsInPropertyPlantAndEquipment: str
    growthAcquisitionsNet: str
    growthPurchasesOfInvestments: str
    growthSalesMaturitiesOfInvestments: str
    growthOtherInvestingActivites: str
    growthNetCashUsedForInvestingActivites: str
    growthDebtRepayment: str
    growthCommonStockIssued: str
    growthCommonStockRepurchased: str
    growthDividendsPaid: str
    growthOtherFinancingActivites: str
    growthNetCashUsedProvidedByFinancingActivities: str
    growthEffectOfForexChangesOnCash: str
    growthNetChangeInCash: str
    growthCashAtEndOfPeriod: str
    growthCashAtBeginningOfPeriod: str
    growthOperatingCashFlow: str
    growthCapitalExpenditure: str
    growthFreeCashFlow: str
    growthNetDebtIssuance: str
    growthLongTermNetDebtIssuance: str
    growthShortTermNetDebtIssuance: str
    growthNetStockIssuance: str
    growthPreferredDividendsPaid: str
    growthIncomeTaxesPaid: str
    growthInterestPaid: str


class EodBulkResult(TypedDict):
    """End-of-day OHLCV price for every symbol, on one date. Returned by `eod_bulk()`."""

    symbol: str
    date: str
    open: str
    low: str
    high: str
    close: str
    adjClose: str
    volume: str
