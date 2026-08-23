"""client.market_hours — Exchange trading sessions and holiday calendars
(REWRITE_ARCHITECTURE.md §6, ``client.market_hours``). 3 canonical
methods, no cross-listings.
"""

from __future__ import annotations

from typing import cast

from ..types import ExchangeMarketHoursResult, HolidaysByExchangeResult


class MarketHoursEndpoints:
    """Mixed into :class:`fmpsdk.client.Client`. Each method issues one GET
    against its ``stable/`` path via ``self._get`` (defined on ``Client``).
    """

    def exchange_market_hours(
        self, exchange: str, timestamp: str | None = None
    ) -> list[ExchangeMarketHoursResult]:
        """``GET exchange-market-hours`` — one exchange's opening/closing
        hours, timezone, and whether it's currently open.

        :param exchange: exchange code, e.g. ``"NASDAQ"``.
        :param timestamp: Unix timestamp to check status as of, as a string.
        """
        return cast(
            "list[ExchangeMarketHoursResult]",
            self._get(
                "exchange-market-hours", {"exchange": exchange, "timestamp": timestamp}
            ),
        )

    def all_exchange_market_hours(
        self, timestamp: str | None = None
    ) -> list[ExchangeMarketHoursResult]:
        """``GET all-exchange-market-hours`` — every exchange's
        opening/closing hours, timezone, and current open/closed status.

        :param timestamp: Unix timestamp to check status as of, as a string.
        """
        return cast(
            "list[ExchangeMarketHoursResult]",
            self._get("all-exchange-market-hours", {"timestamp": timestamp}),
        )

    def holidays_by_exchange(
        self,
        exchange: str,
        from_: str | None = None,
        to: str | None = None,
    ) -> list[HolidaysByExchangeResult]:
        """``GET holidays-by-exchange`` — one exchange's non-trading
        holiday dates, with any adjusted open/close times.

        :param exchange: exchange code, e.g. ``"NASDAQ"``.
        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        """
        return cast(
            "list[HolidaysByExchangeResult]",
            self._get(
                "holidays-by-exchange", {"exchange": exchange, "from": from_, "to": to}
            ),
        )
