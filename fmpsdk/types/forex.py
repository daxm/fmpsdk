"""Response shapes returned by ``client.forex`` methods."""

from __future__ import annotations

from typing import TypedDict

# --- client.forex --------------------------------------------------------------


class ForexListResult(TypedDict):
    symbol: str
    fromCurrency: str
    toCurrency: str
    fromName: str
    toName: str
