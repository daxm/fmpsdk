"""TypedDicts for ``client.technical_indicators`` response shapes (REWRITE_ARCHITECTURE.md §6, ``client.technical_indicators``).

Split out of the former single ``types.py`` for size — see
``fmpsdk/types/__init__.py`` for the shared conventions (naming,
when shapes are/aren't reused, the functional-TypedDict-form cases)
and the re-export barrel that keeps ``from fmpsdk.types import X``
working unchanged for every caller.
"""

from __future__ import annotations

from typing import TypedDict

# --- client.technical_indicators -------------------------------------------------
# One TypedDict per indicator, not shared: the indicator's own value lives
# under a key literally named after the indicator (`sma`, `rsi`, ...), so
# the shapes differ in key name, not just semantics — can't be the same
# TypedDict. All 9 share the same 6 OHLCV+date base fields otherwise.


class SmaResult(TypedDict):
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    sma: float


class EmaResult(TypedDict):
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    ema: float


class WmaResult(TypedDict):
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    wma: float


class DemaResult(TypedDict):
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    dema: float


class TemaResult(TypedDict):
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    tema: float


class RsiResult(TypedDict):
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    rsi: float


class StandardDeviationResult(TypedDict):
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    standardDeviation: float


class WilliamsResult(TypedDict):
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    williams: float


class AdxResult(TypedDict):
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    adx: float
