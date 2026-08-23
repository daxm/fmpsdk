"""TypedDicts for ``client.economics`` response shapes (REWRITE_ARCHITECTURE.md §6, ``client.economics``).

Split out of the former single ``types.py`` for size — see
``fmpsdk/types/__init__.py`` for the shared conventions (naming,
when shapes are/aren't reused, the functional-TypedDict-form cases)
and the re-export barrel that keeps ``from fmpsdk.types import X``
working unchanged for every caller.
"""

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
