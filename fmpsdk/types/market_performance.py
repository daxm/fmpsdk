"""Response shapes returned by ``client.market_performance`` methods."""

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
