"""client.calendar — Date-driven corporate events: dividends, earnings,
IPOs, splits (REWRITE_ARCHITECTURE.md §6, ``client.calendar``). 9 canonical
methods, no cross-listings. Each event type has a paired "one company's
history" method (``symbol*``) and a "market-wide, one date range" method
(``from``/``to``) — both share a response type per ``types.py`` where the
documented shapes are identical, since they answer the same question at
different scope.
"""

from __future__ import annotations

from typing import cast

from ..types import (
    DividendResult,
    EarningsResult,
    IposCalendarResult,
    IposDisclosureResult,
    IposProspectusResult,
    SplitResult,
)


class CalendarEndpoints:
    """Mixed into :class:`fmpsdk.client.Client`. Each method issues one GET
    against its ``stable/`` path via ``self._get`` (defined on ``Client``).
    """

    def dividends(self, symbol: str, limit: int | None = None) -> list[DividendResult]:
        """``GET dividends`` — one company's dividend history.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param limit: max results to return.
        """
        return cast(
            "list[DividendResult]", self._get("dividends", {"symbol": symbol, "limit": limit})
        )

    def dividends_calendar(
        self, from_: str | None = None, to: str | None = None, page: int | None = None
    ) -> list[DividendResult]:
        """``GET dividends-calendar`` — market-wide dividend events in a
        date range.

        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        :param page: zero-indexed page number.
        """
        return cast(
            "list[DividendResult]",
            self._get("dividends-calendar", {"from": from_, "to": to, "page": page}),
        )

    def earnings(
        self, symbol: str, limit: int | None = None, include_report_times: bool | None = None
    ) -> list[EarningsResult]:
        """``GET earnings`` — one company's earnings report history.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param limit: max results to return.
        :param include_report_times: include the before-market/after-market
            timing flag.
        """
        return cast(
            "list[EarningsResult]",
            self._get(
                "earnings",
                {"symbol": symbol, "limit": limit, "includeReportTimes": include_report_times},
            ),
        )

    def earnings_calendar(
        self,
        from_: str | None = None,
        to: str | None = None,
        page: int | None = None,
        include_report_times: bool | None = None,
    ) -> list[EarningsResult]:
        """``GET earnings-calendar`` — market-wide earnings reports in a
        date range.

        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        :param page: zero-indexed page number.
        :param include_report_times: include the before-market/after-market
            timing flag.
        """
        return cast(
            "list[EarningsResult]",
            self._get(
                "earnings-calendar",
                {
                    "from": from_,
                    "to": to,
                    "page": page,
                    "includeReportTimes": include_report_times,
                },
            ),
        )

    def ipos_calendar(
        self, from_: str | None = None, to: str | None = None
    ) -> list[IposCalendarResult]:
        """``GET ipos-calendar`` — upcoming and recent IPOs in a date range.

        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        """
        return cast(
            "list[IposCalendarResult]", self._get("ipos-calendar", {"from": from_, "to": to})
        )

    def ipos_disclosure(
        self, from_: str | None = None, to: str | None = None
    ) -> list[IposDisclosureResult]:
        """``GET ipos-disclosure`` — SEC IPO disclosure filings in a date
        range.

        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        """
        return cast(
            "list[IposDisclosureResult]",
            self._get("ipos-disclosure", {"from": from_, "to": to}),
        )

    def ipos_prospectus(
        self, from_: str | None = None, to: str | None = None
    ) -> list[IposProspectusResult]:
        """``GET ipos-prospectus`` — SEC IPO prospectus filings in a date
        range, with offering-price detail.

        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        """
        return cast(
            "list[IposProspectusResult]",
            self._get("ipos-prospectus", {"from": from_, "to": to}),
        )

    def splits(self, symbol: str, limit: int | None = None) -> list[SplitResult]:
        """``GET splits`` — one company's stock split history.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param limit: max results to return.
        """
        return cast(
            "list[SplitResult]", self._get("splits", {"symbol": symbol, "limit": limit})
        )

    def splits_calendar(
        self, from_: str | None = None, to: str | None = None, page: int | None = None
    ) -> list[SplitResult]:
        """``GET splits-calendar`` — market-wide stock splits in a date
        range.

        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        :param page: zero-indexed page number.
        """
        return cast(
            "list[SplitResult]",
            self._get("splits-calendar", {"from": from_, "to": to, "page": page}),
        )
