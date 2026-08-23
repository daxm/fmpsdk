"""Response shapes returned by ``client.economics`` methods."""

from __future__ import annotations

from typing import TypedDict

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
