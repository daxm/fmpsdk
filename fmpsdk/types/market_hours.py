"""Response shapes returned by ``client.market_hours`` methods."""

from __future__ import annotations

from typing import TypedDict

# --- client.market_hours --------------------------------------------------------


class ExchangeMarketHoursResult(TypedDict):
    """Shape shared by `exchange_market_hours` (one exchange) and
    `all_exchange_market_hours` (every exchange) — identical fields."""

    exchange: str
    name: str
    openingHour: str
    closingHour: str
    timezone: str
    isMarketOpen: bool


class HolidaysByExchangeResult(TypedDict):
    exchange: str
    date: str
    name: str
    isClosed: bool
    adjOpenTime: str | None
    adjCloseTime: str | None
