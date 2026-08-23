"""Response shapes returned by ``client.economics`` methods."""

from __future__ import annotations

from typing import TypedDict

# --- client.economics --------------------------------------------------------


class TreasuryRatesResult(TypedDict):
    """US Treasury yield curve (1-month through 30-year), one row per date. Returned by `treasury_rates()`."""

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
    """One macroeconomic series (GDP, CPI, unemployment, etc.) value at one date. Returned by `economic_indicators()`."""

    name: str
    date: str
    value: float


class EconomicCalendarResult(TypedDict):
    """One scheduled economic data release, with prior/estimate/actual values once reported. Requires an FMP Starter-tier plan or higher. Returned by `economic_calendar()`."""

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
    """Country risk premium and total equity risk premium for one country. Returned by `market_risk_premium()`."""

    country: str
    continent: str
    countryRiskPremium: float
    totalEquityRiskPremium: float
