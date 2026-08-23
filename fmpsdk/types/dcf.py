"""Response shapes returned by ``client.dcf`` methods."""

from __future__ import annotations

from typing import TypedDict

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
# valuation questions, so don't assume the two are interchangeable.
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
