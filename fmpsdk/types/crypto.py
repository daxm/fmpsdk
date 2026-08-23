"""TypedDicts for ``client.crypto`` response shapes (REWRITE_ARCHITECTURE.md §6, ``client.crypto``).

Split out of the former single ``types.py`` for size — see
``fmpsdk/types/__init__.py`` for the shared conventions (naming,
when shapes are/aren't reused, the functional-TypedDict-form cases)
and the re-export barrel that keeps ``from fmpsdk.types import X``
working unchanged for every caller.
"""

from __future__ import annotations

from typing import TypedDict

# --- client.crypto ------------------------------------------------------------


class CryptocurrencyListResult(TypedDict):
    symbol: str
    name: str
    exchange: str
    icoDate: str | None
    circulatingSupply: float
    totalSupply: float | None
