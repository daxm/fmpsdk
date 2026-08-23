"""Response shapes returned by ``client.chart`` methods."""

from __future__ import annotations

from typing import TypedDict


class HistoricalChartResult(TypedDict):
    """Response for `historical_chart`'s intraday timeframes
    (`1min`/`5min`/`15min`/`30min`/`1hour`/`4hour`). No `symbol` field —
    unlike every other chart shape, since you already know which symbol
    you asked for."""

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
    kept as a separate type: split-adjustment and dividend-adjustment
    answer different questions about "true" price, so don't assume the
    two are interchangeable even though the shape matches."""

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
