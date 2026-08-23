"""Response shapes returned by ``client.indexes`` methods."""

from __future__ import annotations

from typing import TypedDict

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
