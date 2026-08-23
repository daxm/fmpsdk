"""TypedDicts for ``client.forex`` response shapes (REWRITE_ARCHITECTURE.md §6, ``client.forex``).

Split out of the former single ``types.py`` for size — see
``fmpsdk/types/__init__.py`` for the shared conventions (naming,
when shapes are/aren't reused, the functional-TypedDict-form cases)
and the re-export barrel that keeps ``from fmpsdk.types import X``
working unchanged for every caller.
"""

from __future__ import annotations

from typing import TypedDict

# --- client.forex --------------------------------------------------------------


class ForexListResult(TypedDict):
    symbol: str
    fromCurrency: str
    toCurrency: str
    fromName: str
    toName: str
