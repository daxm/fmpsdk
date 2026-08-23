"""client.congress — U.S. Senate and House financial disclosures, trades,
and member profiles. 12 methods. ``house_latest`` and ``senate_latest``
(the two parameterless listings) work on the free tier. The 6
symbol/id/name-scoped trade lookups (``house_trades``,
``house_trades_by_id``, ``house_trades_by_name``, ``senate_trades``,
``senate_trades_by_id``, ``senate_trades_by_name``) require an FMP
Starter-tier plan or higher. ``senate_profile``, ``senate_positions``,
``senate_net_worth``, and ``senate_net_worth_aggregated`` still 402 on
both the free and Starter tiers as of 2026-08-23 — they require FMP
Premium or Ultimate (not yet confirmed which).

Every method that takes a member ID names its parameter ``senate_id``,
including the House ones (``house_trades_by_id``) — that's FMP's own
wire parameter name (``senateID``) even on House endpoints, not a typo
introduced here.
"""

from __future__ import annotations

from typing import cast

from ..types import (
    CongressionalTradeResult,
    SenateNetWorthAggregatedResult,
    SenateNetWorthResult,
    SenatePositionResult,
    SenateProfileResult,
)


class CongressEndpoints:
    """Mixed into :class:`fmpsdk.client.Client`. Each method issues one GET
    against its ``stable/`` path via ``self._get`` (defined on ``Client``).
    """

    def house_latest(
        self, page: int | None = None, limit: int | None = None
    ) -> list[CongressionalTradeResult]:
        """``GET house-latest`` — most recent House member financial
        disclosures across all members, paginated.

        :param page: zero-indexed page number.
        :param limit: max results per page.
        """
        return cast(
            "list[CongressionalTradeResult]",
            self._get("house-latest", {"page": page, "limit": limit}),
        )

    def house_trades(
        self, symbol: str, page: int | None = None, limit: int | None = None
    ) -> list[CongressionalTradeResult]:
        """``GET house-trades`` — House member trades in one security.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param page: zero-indexed page number.
        :param limit: max results per page.
        """
        return cast(
            "list[CongressionalTradeResult]",
            self._get("house-trades", {"symbol": symbol, "page": page, "limit": limit}),
        )

    def house_trades_by_id(
        self,
        senate_id: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> list[CongressionalTradeResult]:
        """``GET house-trades-by-id`` — one House member's trades, looked
        up by member ID.

        :param senate_id: the House member's ID, e.g. ``"P000197"``. Yes,
            ``senate_id`` on a House method — FMP's own wire parameter
            for this endpoint really is named ``senateID``.
        :param page: zero-indexed page number.
        :param limit: max results per page.
        """
        return cast(
            "list[CongressionalTradeResult]",
            self._get(
                "house-trades-by-id",
                {"senateID": senate_id, "page": page, "limit": limit},
            ),
        )

    def house_trades_by_name(self, name: str) -> list[CongressionalTradeResult]:
        """``GET house-trades-by-name`` — House member trades, looked up
        by member name.

        :param name: House member's name to search for, e.g. ``"James"``.
        """
        return cast(
            "list[CongressionalTradeResult]",
            self._get("house-trades-by-name", {"name": name}),
        )

    def senate_latest(
        self, page: int | None = None, limit: int | None = None
    ) -> list[CongressionalTradeResult]:
        """``GET senate-latest`` — most recent Senate member financial
        disclosures across all members, paginated.

        :param page: zero-indexed page number.
        :param limit: max results per page.
        """
        return cast(
            "list[CongressionalTradeResult]",
            self._get("senate-latest", {"page": page, "limit": limit}),
        )

    def senate_trades(
        self, symbol: str, page: int | None = None, limit: int | None = None
    ) -> list[CongressionalTradeResult]:
        """``GET senate-trades`` — Senate member trades in one security.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param page: zero-indexed page number.
        :param limit: max results per page.
        """
        return cast(
            "list[CongressionalTradeResult]",
            self._get(
                "senate-trades", {"symbol": symbol, "page": page, "limit": limit}
            ),
        )

    def senate_trades_by_id(
        self,
        senate_id: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> list[CongressionalTradeResult]:
        """``GET senate-trades-by-id`` — one Senate member's trades,
        looked up by member ID.

        :param senate_id: the Senate member's ID, e.g. ``"S000033"``.
        :param page: zero-indexed page number.
        :param limit: max results per page.
        """
        return cast(
            "list[CongressionalTradeResult]",
            self._get(
                "senate-trades-by-id",
                {"senateID": senate_id, "page": page, "limit": limit},
            ),
        )

    def senate_trades_by_name(self, name: str) -> list[CongressionalTradeResult]:
        """``GET senate-trades-by-name`` — Senate member trades, looked
        up by member name.

        :param name: Senate member's name to search for, e.g. ``"Jerry"``.
        """
        return cast(
            "list[CongressionalTradeResult]",
            self._get("senate-trades-by-name", {"name": name}),
        )

    def senate_profile(
        self,
        active: bool | None = None,
        senate_id: str | None = None,
        latest_party: str | None = None,
        latest_position: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> list[SenateProfileResult]:
        """``GET senate-profile`` — member-of-Congress profiles: party,
        state, position, and years active. Despite the ``senate-`` path
        prefix, covers both chambers.

        :param active: filter to currently active members.
        :param senate_id: filter by one member's ID, e.g. ``"P000197"``.
        :param latest_party: filter by party, e.g. ``"Republican"``.
        :param latest_position: filter by position, e.g. ``"Representative"``.
        :param page: zero-indexed page number.
        :param limit: max results per page.
        """
        return cast(
            "list[SenateProfileResult]",
            self._get(
                "senate-profile",
                {
                    "active": active,
                    "senateID": senate_id,
                    "latestParty": latest_party,
                    "latestPosition": latest_position,
                    "page": page,
                    "limit": limit,
                },
            ),
        )

    def senate_positions(
        self,
        senate_id: str | None = None,
        party: str | None = None,
        position: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> list[SenatePositionResult]:
        """``GET senate-positions`` — congressional positions a member
        has held, with term dates, party, and state.

        :param senate_id: filter by one member's ID, e.g. ``"P000197"``.
        :param party: filter by party, e.g. ``"Republican"``.
        :param position: filter by position, e.g. ``"Representative"``.
        :param page: zero-indexed page number.
        :param limit: max results per page.
        """
        return cast(
            "list[SenatePositionResult]",
            self._get(
                "senate-positions",
                {
                    "senateID": senate_id,
                    "party": party,
                    "position": position,
                    "page": page,
                    "limit": limit,
                },
            ),
        )

    def senate_net_worth(
        self,
        senate_id: str,
        page: int | None = None,
        limit: int | None = None,
    ) -> list[SenateNetWorthResult]:
        """``GET senate-net-worth`` — itemized net-worth disclosures for
        one member: assets, liabilities, and income by filing year.

        :param senate_id: the member's ID, e.g. ``"P000197"``.
        :param page: zero-indexed page number.
        :param limit: max results per page.
        """
        return cast(
            "list[SenateNetWorthResult]",
            self._get(
                "senate-net-worth",
                {"senateID": senate_id, "page": page, "limit": limit},
            ),
        )

    def senate_net_worth_aggregated(
        self, senate_id: str, totals_col: str | None = None
    ) -> list[SenateNetWorthAggregatedResult]:
        """``GET senate-net-worth-aggregated`` — aggregated net-worth
        totals for one member by year, grouped by asset/liability type.

        :param senate_id: the member's ID, e.g. ``"P000197"``.
        :param totals_col: optional column to aggregate by (FMP-defined).
        """
        return cast(
            "list[SenateNetWorthAggregatedResult]",
            self._get(
                "senate-net-worth-aggregated",
                {"senateID": senate_id, "totalsCol": totals_col},
            ),
        )
