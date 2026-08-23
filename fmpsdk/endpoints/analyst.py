"""client.analyst — Sell-side estimates, ratings, price targets, grades
(REWRITE_ARCHITECTURE.md §6, ``client.analyst``). 8 canonical methods, no
cross-listings. Every method takes a required ``symbol``.
"""

from __future__ import annotations

from typing import cast

from ..types import (
    AnalystEstimatesResult,
    GradesConsensusResult,
    GradesHistoricalResult,
    GradesResult,
    PriceTargetConsensusResult,
    PriceTargetSummaryResult,
    RatingsHistoricalResult,
    RatingsSnapshotResult,
)


class AnalystEndpoints:
    """Mixed into :class:`fmpsdk.client.Client`. Each method issues one GET
    against its ``stable/`` path via ``self._get`` (defined on ``Client``).
    """

    def analyst_estimates(
        self,
        symbol: str,
        period: str,
        page: int | None = None,
        limit: int | None = None,
    ) -> list[AnalystEstimatesResult]:
        """``GET analyst-estimates`` — consensus revenue/EPS/margin forecasts.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param period: ``"annual"`` or ``"quarter"`` (``constants.PERIOD_ANNUAL_QUARTER``
            — one of the three incompatible ``period`` vocabularies in the
            catalog, §8.1; this endpoint does *not* accept ``Q1``-``Q4``/``FY``).
        :param page: zero-indexed page number.
        :param limit: max results to return.
        """
        return cast(
            "list[AnalystEstimatesResult]",
            self._get(
                "analyst-estimates",
                {"symbol": symbol, "period": period, "page": page, "limit": limit},
            ),
        )

    def ratings_snapshot(self, symbol: str) -> list[RatingsSnapshotResult]:
        """``GET ratings-snapshot`` — current overall rating and per-factor
        scores (DCF, ROE, ROA, debt/equity, P/E, P/B).

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        """
        return cast(
            "list[RatingsSnapshotResult]", self._get("ratings-snapshot", {"symbol": symbol})
        )

    def ratings_historical(
        self, symbol: str, limit: int | None = None
    ) -> list[RatingsHistoricalResult]:
        """``GET ratings-historical`` — dated history of the same rating and
        per-factor scores as :meth:`ratings_snapshot`.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param limit: max results to return.
        """
        return cast(
            "list[RatingsHistoricalResult]",
            self._get("ratings-historical", {"symbol": symbol, "limit": limit}),
        )

    def price_target_summary(self, symbol: str) -> list[PriceTargetSummaryResult]:
        """``GET price-target-summary`` — average analyst price targets
        over the last month/quarter/year/all-time, with publisher list.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        """
        return cast(
            "list[PriceTargetSummaryResult]",
            self._get("price-target-summary", {"symbol": symbol}),
        )

    def price_target_consensus(self, symbol: str) -> list[PriceTargetConsensusResult]:
        """``GET price-target-consensus`` — high/low/median/consensus
        analyst price targets.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        """
        return cast(
            "list[PriceTargetConsensusResult]",
            self._get("price-target-consensus", {"symbol": symbol}),
        )

    def grades(self, symbol: str) -> list[GradesResult]:
        """``GET grades`` — individual analyst grading actions (upgrade,
        downgrade, maintain), one row per action.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        """
        return cast("list[GradesResult]", self._get("grades", {"symbol": symbol}))

    def grades_historical(
        self, symbol: str, limit: int | None = None
    ) -> list[GradesHistoricalResult]:
        """``GET grades-historical`` — dated counts of strong-buy/buy/hold/
        sell/strong-sell ratings in force, one row per date.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param limit: max results to return.
        """
        return cast(
            "list[GradesHistoricalResult]",
            self._get("grades-historical", {"symbol": symbol, "limit": limit}),
        )

    def grades_consensus(self, symbol: str) -> list[GradesConsensusResult]:
        """``GET grades-consensus`` — current consensus grade counts and
        overall consensus label (e.g. ``"Buy"``).

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        """
        return cast(
            "list[GradesConsensusResult]", self._get("grades-consensus", {"symbol": symbol})
        )
