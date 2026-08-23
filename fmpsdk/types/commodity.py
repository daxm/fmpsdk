"""Response shapes returned by ``client.commodity`` methods."""

from __future__ import annotations

from typing import TypedDict

# --- client.commodity --------------------------------------------------------


class CommoditiesListResult(TypedDict):
    symbol: str
    name: str
    exchange: str | None
    tradeMonth: str
    currency: str
