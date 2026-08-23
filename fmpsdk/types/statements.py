"""TypedDicts for ``client.statements`` response shapes (REWRITE_ARCHITECTURE.md §6, ``client.statements``).

Split out of the former single ``types.py`` for size — see
``fmpsdk/types/__init__.py`` for the shared conventions (naming,
when shapes are/aren't reused, the functional-TypedDict-form cases)
and the re-export barrel that keeps ``from fmpsdk.types import X``
working unchanged for every caller.
"""

from __future__ import annotations

from typing import TypedDict

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
