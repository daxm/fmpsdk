"""Response shapes returned by ``client.forex`` methods."""

from __future__ import annotations

from typing import TypedDict

# --- client.forex --------------------------------------------------------------


class ForexListResult(TypedDict):
    """One currency pair FMP tracks, with symbol and base/counter currency names. Returned by `forex_list()`."""

    symbol: str
    fromCurrency: str
    toCurrency: str
    fromName: str
    toName: str
