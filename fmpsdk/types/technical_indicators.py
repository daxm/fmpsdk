"""Response shapes returned by ``client.technical_indicators`` methods."""

from __future__ import annotations

from typing import TypedDict

# --- client.technical_indicators -------------------------------------------------
# One TypedDict per indicator, not shared: the indicator's own value lives
# under a key literally named after the indicator (`sma`, `rsi`, ...), so
# the shapes differ in key name, not just semantics — can't be the same
# TypedDict. All 9 share the same 6 OHLCV+date base fields otherwise.


class SmaResult(TypedDict):
    """One bar of simple moving average, with its OHLCV base fields."""

    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    sma: float


class EmaResult(TypedDict):
    """One bar of exponential moving average, with its OHLCV base fields."""

    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    ema: float


class WmaResult(TypedDict):
    """One bar of weighted moving average, with its OHLCV base fields."""

    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    wma: float


class DemaResult(TypedDict):
    """One bar of double exponential moving average, with its OHLCV base fields."""

    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    dema: float


class TemaResult(TypedDict):
    """One bar of triple exponential moving average, with its OHLCV base fields."""

    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    tema: float


class RsiResult(TypedDict):
    """One bar of relative strength index, with its OHLCV base fields."""

    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    rsi: float


class StandardDeviationResult(TypedDict):
    """One bar of rolling standard deviation, with its OHLCV base fields."""

    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    standardDeviation: float


class WilliamsResult(TypedDict):
    """One bar of Williams %R, with its OHLCV base fields."""

    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    williams: float


class AdxResult(TypedDict):
    """One bar of average directional index, with its OHLCV base fields."""

    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    adx: float
