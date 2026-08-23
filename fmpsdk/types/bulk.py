"""TypedDicts for ``client.bulk`` response shapes
(REWRITE_ARCHITECTURE.md §6, ``client.bulk``).

**Every bulk endpoint except `profile_bulk` returns every field as a JSON
string, including fields that are semantically numeric or boolean** (e.g.
`rating_bulk`'s `"discountedCashFlowScore": "5"`,
`earnings_surprises_bulk`'s `"epsActual": "0.3631"`). This isn't a
transcription choice — it's what FMP's own documented example responses
literally show, verbatim, for 17 of the 18 methods. `profile_bulk` is the
lone exception: its example response has real JSON numbers/booleans, and
its shape is identical field-for-field to `ProfileResult`
(`types/company.py`) — reused directly rather than duplicated, since it
answers the same question (`profile`/`profile_cik`) at bulk scope. Typing
the other 17 as `str` throughout matches the doc evidence; verify live
before assuming otherwise.

`etf_holder_bulk`'s documented example has a garbled key/value pair —
`"lastUpdated\"": "2024-09-06\""` (embedded stray quote characters in
both the key and the value) — almost certainly a doc-generation artifact,
not a real wire field name containing a literal `"`. Modeled here as the
sane `lastUpdated: str`; flagged for live confirmation like `sec_profile`'s
`cik-A` parameter oddity in `types/sec_filings.py`.

`cash_flow_statement_growth_bulk`'s field names preserve FMP's own typos
verbatim (`...Activites`, missing the second `i`, on 3 of its fields) —
same policy as `commitment_of_traders`'s `Spead`/`netPostion`: "fixing"
it would break the cast against real JSON.

Split out of the former single ``types.py`` for size — see
``fmpsdk/types/__init__.py`` for the shared conventions and the
re-export barrel that keeps ``from fmpsdk.types import X`` working
unchanged for every caller.
"""

from __future__ import annotations

from typing import TypedDict


class RatingBulkResult(TypedDict):
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
    symbol: str
    strongBuy: str
    buy: str
    hold: str
    sell: str
    strongSell: str
    consensus: str


class KeyMetricsTtmBulkResult(TypedDict):
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
    symbol: str
    peers: str


class EarningsSurprisesBulkResult(TypedDict):
    symbol: str
    date: str
    epsActual: str
    epsEstimated: str
    lastUpdated: str


class IncomeStatementBulkResult(TypedDict):
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
    symbol: str
    date: str
    open: str
    low: str
    high: str
    close: str
    adjClose: str
    volume: str
