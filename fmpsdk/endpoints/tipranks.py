"""client.tipranks — TipRanks partner analyst ratings and coverage
data. 7 methods. Requires an FMP Ultimate-tier plan — every method here
402s on the free tier.
"""

from __future__ import annotations

from typing import cast

from ..types import (
    TipranksAnalystDirectoryResult,
    TipranksAnalystSummaryResult,
    TipranksFirmSummaryResult,
    TipranksPointInTimeResult,
    TipranksRatingResult,
    TipranksSymbolSummaryResult,
)


class TipranksEndpoints:
    """Mixed into :class:`fmpsdk.client.Client`. Each method issues one GET
    against its ``stable/`` path via ``self._get`` (defined on ``Client``).
    """

    def tipranks_search(
        self,
        expert_uid: str | None = None,
        symbol: str | None = None,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        page: int | None = None,
        nonadjusted: bool | None = None,
    ) -> list[TipranksRatingResult]:
        """``GET tipranks-search`` — every individual TipRanks analyst
        rating, newest first, filterable by symbol/analyst/date range.
        Ratings history only goes back 3 years per FMP's own docs.

        :param expert_uid: restrict to one analyst's stable TipRanks ID.
        :param symbol: restrict to one ticker symbol, e.g. ``"AAPL"``.
        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        :param limit: max results per page (FMP max 5000).
        :param page: zero-indexed page number.
        :param nonadjusted: return price targets in native currency
            instead of FX-converted.
        """
        return cast(
            "list[TipranksRatingResult]",
            self._get(
                "tipranks-search",
                {
                    "expertUID": expert_uid,
                    "symbol": symbol,
                    "from": from_,
                    "to": to,
                    "limit": limit,
                    "page": page,
                    "nonadjusted": nonadjusted,
                },
            ),
        )

    def tipranks_pit_symbol(
        self,
        symbol: str,
        date: str | None = None,
        limit: int | None = None,
        page: int | None = None,
        nonadjusted: bool | None = None,
    ) -> list[TipranksPointInTimeResult]:
        """``GET tipranks-pit-symbol`` — point-in-time coverage panel for
        one symbol: every analyst's latest active call as of a chosen
        date, one row per analyst.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param date: snapshot date, ``YYYY-MM-DD``; defaults to now.
        :param limit: max results per page (FMP default 100, max 5000).
        :param page: zero-indexed page number.
        :param nonadjusted: return price targets in native currency
            instead of FX-converted.
        """
        return cast(
            "list[TipranksPointInTimeResult]",
            self._get(
                "tipranks-pit-symbol",
                {
                    "symbol": symbol,
                    "date": date,
                    "limit": limit,
                    "page": page,
                    "nonadjusted": nonadjusted,
                },
            ),
        )

    def tipranks_pit_analyst(
        self,
        expert_uid: str | None = None,
        analyst_name: str | None = None,
        date: str | None = None,
        limit: int | None = None,
        page: int | None = None,
        nonadjusted: bool | None = None,
    ) -> list[TipranksPointInTimeResult]:
        """``GET tipranks-pit-analyst`` — point-in-time book for one
        analyst: every symbol they cover with their latest active call
        as of a chosen date, one row per symbol. Same response shape as
        `tipranks_pit_symbol`.

        :param expert_uid: the analyst's stable TipRanks ID.
        :param analyst_name: the analyst's name, exact match required.
        :param date: snapshot date, ``YYYY-MM-DD``; defaults to now.
        :param limit: max results per page (FMP default 100, max 5000).
        :param page: zero-indexed page number.
        :param nonadjusted: return price targets in native currency
            instead of FX-converted.
        """
        return cast(
            "list[TipranksPointInTimeResult]",
            self._get(
                "tipranks-pit-analyst",
                {
                    "expertUID": expert_uid,
                    "analystName": analyst_name,
                    "date": date,
                    "limit": limit,
                    "page": page,
                    "nonadjusted": nonadjusted,
                },
            ),
        )

    def tipranks_symbol_summary(
        self, symbol: str, from_: str | None = None, to: str | None = None
    ) -> list[TipranksSymbolSummaryResult]:
        """``GET tipranks-symbol-summary`` — aggregated rollup of every
        TipRanks rating on one ticker over a date window (default:
        trailing twelve months).

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        """
        return cast(
            "list[TipranksSymbolSummaryResult]",
            self._get(
                "tipranks-symbol-summary",
                {"symbol": symbol, "from": from_, "to": to},
            ),
        )

    def tipranks_analyst_summary(
        self, expert_uid: str, from_: str | None = None, to: str | None = None
    ) -> list[TipranksAnalystSummaryResult]:
        """``GET tipranks-analyst-summary`` — aggregated rollup of every
        rating one analyst has issued over a date window (default:
        trailing twelve months).

        :param expert_uid: the analyst's stable TipRanks ID.
        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        """
        return cast(
            "list[TipranksAnalystSummaryResult]",
            self._get(
                "tipranks-analyst-summary",
                {"expertUID": expert_uid, "from": from_, "to": to},
            ),
        )

    def tipranks_firm_summary(
        self, firm_name: str, from_: str | None = None, to: str | None = None
    ) -> list[TipranksFirmSummaryResult]:
        """``GET tipranks-firm-summary`` — aggregated rollup of every
        rating issued by analysts at one firm over a date window
        (default: trailing twelve months).

        :param firm_name: firm name, matched exactly, e.g. ``"Morgan Stanley"``.
        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        """
        return cast(
            "list[TipranksFirmSummaryResult]",
            self._get(
                "tipranks-firm-summary",
                {"firmName": firm_name, "from": from_, "to": to},
            ),
        )

    def tipranks_analysts(
        self,
        page: int | None = None,
        limit: int | None = None,
        firm_name: str | None = None,
    ) -> list[TipranksAnalystDirectoryResult]:
        """``GET tipranks-analysts`` — analyst directory lookup:
        resolves an analyst's stable TipRanks ID plus firm, star rating,
        and aggregate performance metrics.

        :param page: zero-indexed page number.
        :param limit: max results per page.
        :param firm_name: restrict to one firm, matched exactly.
        """
        return cast(
            "list[TipranksAnalystDirectoryResult]",
            self._get(
                "tipranks-analysts",
                {"page": page, "limit": limit, "firmName": firm_name},
            ),
        )
