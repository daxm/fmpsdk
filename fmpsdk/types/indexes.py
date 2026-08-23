"""TypedDicts for ``client.indexes`` response shapes (REWRITE_ARCHITECTURE.md §6, ``client.indexes``).

Split out of the former single ``types.py`` for size — see
``fmpsdk/types/__init__.py`` for the shared conventions (naming,
when shapes are/aren't reused, the functional-TypedDict-form cases)
and the re-export barrel that keeps ``from fmpsdk.types import X``
working unchanged for every caller.
"""

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
