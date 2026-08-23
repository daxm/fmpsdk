"""TypedDicts for ``client.market_hours`` response shapes (REWRITE_ARCHITECTURE.md §6, ``client.market_hours``).

Split out of the former single ``types.py`` for size — see
``fmpsdk/types/__init__.py`` for the shared conventions (naming,
when shapes are/aren't reused, the functional-TypedDict-form cases)
and the re-export barrel that keeps ``from fmpsdk.types import X``
working unchanged for every caller.
"""

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
