"""Response shapes returned by ``client.crypto`` methods."""

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
