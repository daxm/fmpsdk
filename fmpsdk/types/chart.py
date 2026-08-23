"""TypedDicts for ``client.chart`` response shapes (REWRITE_ARCHITECTURE.md §6, ``client.chart``).

Split out of the former single ``types.py`` for size — see
``fmpsdk/types/__init__.py`` for the shared conventions (naming,
when shapes are/aren't reused, the functional-TypedDict-form cases)
and the re-export barrel that keeps ``from fmpsdk.types import X``
working unchanged for every caller.
"""

from __future__ import annotations

from typing import TypedDict


class HistoricalChartResult(TypedDict):
    """Response for the 6 `historical_chart` intraday timeframes (§5.3
    collapse: `1min`/`5min`/`15min`/`30min`/`1hour`/`4hour` share one
    method and one shape). No `symbol` field in any documented example —
    unlike every other chart shape, the caller already knows which symbol
    they asked for."""

    date: str
    open: float
    low: float
    high: float
    close: float
    volume: int


class HistoricalPriceEodLightResult(TypedDict):
    symbol: str
    date: str
    price: float
    volume: int


class HistoricalPriceEodFullResult(TypedDict):
    symbol: str
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    change: float
    changePercent: float
    vwap: float


class HistoricalPriceEodNonSplitAdjustedResult(TypedDict):
    """Same field set as `HistoricalPriceEodDividendAdjustedResult`, but
    kept separate: split-adjustment and dividend-adjustment are different
    questions about "true" price, not the same query at different scope
    (contrast `DividendResult`/`SplitResult` above, §7.8's `profile`
    precedent)."""

    symbol: str
    date: str
    adjOpen: float
    adjHigh: float
    adjLow: float
    adjClose: float
    volume: int


class HistoricalPriceEodDividendAdjustedResult(TypedDict):
    """See `HistoricalPriceEodNonSplitAdjustedResult` — same shape,
    deliberately separate type."""

    symbol: str
    date: str
    adjOpen: float
    adjHigh: float
    adjLow: float
    adjClose: float
    volume: int
