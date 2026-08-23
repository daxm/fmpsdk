"""TypedDicts for ``client.market_performance`` response shapes (REWRITE_ARCHITECTURE.md §6, ``client.market_performance``).

Split out of the former single ``types.py`` for size — see
``fmpsdk/types/__init__.py`` for the shared conventions (naming,
when shapes are/aren't reused, the functional-TypedDict-form cases)
and the re-export barrel that keeps ``from fmpsdk.types import X``
working unchanged for every caller.
"""

from __future__ import annotations

from typing import TypedDict

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
