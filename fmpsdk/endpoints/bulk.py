"""client.bulk — Whole-universe bulk downloads: one call returns a
field set for every company FMP covers, instead of one call per symbol.
18 methods. Requires an FMP Ultimate-tier plan — 402s on free, Starter,
and Premium (confirmed working on Ultimate 2026-08-24).

Every response is real CSV (``text/csv``), not JSON, despite FMP's own
docs showing JSON-looking examples — confirmed live 2026-08-24,
including ``profile_bulk`` (previously assumed to be the one exception
returning real JSON; it doesn't). Every field on every method's result
comes back as a plain string — see ``types/bulk.py``'s module
docstring.
"""

from __future__ import annotations

from typing import cast

from ..types import (
    BalanceSheetStatementBulkResult,
    BalanceSheetStatementGrowthBulkResult,
    CashFlowStatementBulkResult,
    CashFlowStatementGrowthBulkResult,
    DcfBulkResult,
    EarningsSurprisesBulkResult,
    EodBulkResult,
    EtfHolderBulkResult,
    IncomeStatementBulkResult,
    IncomeStatementGrowthBulkResult,
    KeyMetricsTtmBulkResult,
    PeersBulkResult,
    PriceTargetSummaryBulkResult,
    ProfileBulkResult,
    RatingBulkResult,
    RatiosTtmBulkResult,
    ScoresBulkResult,
    UpgradesDowngradesConsensusBulkResult,
)


class BulkEndpoints:
    """Mixed into :class:`fmpsdk.client.Client`. Each method issues one GET
    against its ``stable/`` path via ``self._get_csv`` (defined on
    ``Client``) — every bulk response is real CSV, not JSON.
    """

    def profile_bulk(self, part: str) -> list[ProfileBulkResult]:
        """``GET profile-bulk`` — company profiles for a whole page
        ("part") of the universe at once. Same field set as
        `profile`/`profile_cik` (`ProfileResult`), but every value is a
        `str` — see `ProfileBulkResult`.

        :param part: which page of the universe to fetch, e.g. ``"0"``.
        """
        return cast(
            "list[ProfileBulkResult]", self._get_csv("profile-bulk", {"part": part})
        )

    def rating_bulk(self) -> list[RatingBulkResult]:
        """``GET rating-bulk`` — current overall rating and component
        scores for every company at once. No parameters."""
        return cast("list[RatingBulkResult]", self._get_csv("rating-bulk", {}))

    def dcf_bulk(self) -> list[DcfBulkResult]:
        """``GET dcf-bulk`` — discounted-cash-flow valuation for every
        company at once. No parameters."""
        return cast("list[DcfBulkResult]", self._get_csv("dcf-bulk", {}))

    def scores_bulk(self) -> list[ScoresBulkResult]:
        """``GET scores-bulk`` — Altman Z-Score, Piotroski score, and
        related financial-health metrics for every company at once. No
        parameters."""
        return cast("list[ScoresBulkResult]", self._get_csv("scores-bulk", {}))

    def price_target_summary_bulk(self) -> list[PriceTargetSummaryBulkResult]:
        """``GET price-target-summary-bulk`` — analyst price-target
        summary (last month/quarter/year/all-time) for every company at
        once. No parameters."""
        return cast(
            "list[PriceTargetSummaryBulkResult]",
            self._get_csv("price-target-summary-bulk", {}),
        )

    def etf_holder_bulk(self, part: str) -> list[EtfHolderBulkResult]:
        """``GET etf-holder-bulk`` — ETF holdings for a whole page
        ("part") of the universe at once.

        :param part: which page of the universe to fetch, e.g. ``"1"``.
        """
        return cast(
            "list[EtfHolderBulkResult]",
            self._get_csv("etf-holder-bulk", {"part": part}),
        )

    def upgrades_downgrades_consensus_bulk(
        self,
    ) -> list[UpgradesDowngradesConsensusBulkResult]:
        """``GET upgrades-downgrades-consensus-bulk`` — analyst
        upgrade/downgrade consensus for every company at once. No
        parameters."""
        return cast(
            "list[UpgradesDowngradesConsensusBulkResult]",
            self._get_csv("upgrades-downgrades-consensus-bulk", {}),
        )

    def key_metrics_ttm_bulk(self) -> list[KeyMetricsTtmBulkResult]:
        """``GET key-metrics-ttm-bulk`` — trailing-twelve-month key
        metrics for every company at once. No parameters — non-filterable,
        always the latest TTM data."""
        return cast(
            "list[KeyMetricsTtmBulkResult]", self._get_csv("key-metrics-ttm-bulk", {})
        )

    def ratios_ttm_bulk(self) -> list[RatiosTtmBulkResult]:
        """``GET ratios-ttm-bulk`` — trailing-twelve-month financial
        ratios for every company at once. No parameters."""
        return cast("list[RatiosTtmBulkResult]", self._get_csv("ratios-ttm-bulk", {}))

    def peers_bulk(self) -> list[PeersBulkResult]:
        """``GET peers-bulk`` — peer-company list for every company at
        once. No parameters."""
        return cast("list[PeersBulkResult]", self._get_csv("peers-bulk", {}))

    def earnings_surprises_bulk(self, year: str) -> list[EarningsSurprisesBulkResult]:
        """``GET earnings-surprises-bulk`` — actual vs. estimated EPS for
        every company, for one fiscal year.

        :param year: fiscal year, e.g. ``"2026"``.
        """
        return cast(
            "list[EarningsSurprisesBulkResult]",
            self._get_csv("earnings-surprises-bulk", {"year": year}),
        )

    def income_statement_bulk(
        self, year: str, period: str
    ) -> list[IncomeStatementBulkResult]:
        """``GET income-statement-bulk`` — income statement for every
        company, for one fiscal period.

        :param year: fiscal year, e.g. ``"2026"``.
        :param period: fiscal period, one of ``constants.PERIOD_FISCAL``
            (``"Q1"``/``"Q2"``/``"Q3"``/``"Q4"``/``"FY"``).
        """
        return cast(
            "list[IncomeStatementBulkResult]",
            self._get_csv("income-statement-bulk", {"year": year, "period": period}),
        )

    def income_statement_growth_bulk(
        self, year: str, period: str
    ) -> list[IncomeStatementGrowthBulkResult]:
        """``GET income-statement-growth-bulk`` — income statement
        growth for every company, for one fiscal period.

        :param year: fiscal year, e.g. ``"2026"``.
        :param period: fiscal period, one of ``constants.PERIOD_FISCAL``.
        """
        return cast(
            "list[IncomeStatementGrowthBulkResult]",
            self._get_csv(
                "income-statement-growth-bulk", {"year": year, "period": period}
            ),
        )

    def balance_sheet_statement_bulk(
        self, year: str, period: str
    ) -> list[BalanceSheetStatementBulkResult]:
        """``GET balance-sheet-statement-bulk`` — balance sheet for
        every company, for one fiscal period.

        :param year: fiscal year, e.g. ``"2026"``.
        :param period: fiscal period, one of ``constants.PERIOD_FISCAL``.
        """
        return cast(
            "list[BalanceSheetStatementBulkResult]",
            self._get_csv(
                "balance-sheet-statement-bulk", {"year": year, "period": period}
            ),
        )

    def balance_sheet_statement_growth_bulk(
        self, year: str, period: str
    ) -> list[BalanceSheetStatementGrowthBulkResult]:
        """``GET balance-sheet-statement-growth-bulk`` — balance sheet
        growth for every company, for one fiscal period.

        :param year: fiscal year, e.g. ``"2026"``.
        :param period: fiscal period, one of ``constants.PERIOD_FISCAL``.
        """
        return cast(
            "list[BalanceSheetStatementGrowthBulkResult]",
            self._get_csv(
                "balance-sheet-statement-growth-bulk",
                {"year": year, "period": period},
            ),
        )

    def cash_flow_statement_bulk(
        self, year: str, period: str
    ) -> list[CashFlowStatementBulkResult]:
        """``GET cash-flow-statement-bulk`` — cash flow statement for
        every company, for one fiscal period.

        :param year: fiscal year, e.g. ``"2026"``.
        :param period: fiscal period, one of ``constants.PERIOD_FISCAL``.
        """
        return cast(
            "list[CashFlowStatementBulkResult]",
            self._get_csv("cash-flow-statement-bulk", {"year": year, "period": period}),
        )

    def cash_flow_statement_growth_bulk(
        self, year: str, period: str
    ) -> list[CashFlowStatementGrowthBulkResult]:
        """``GET cash-flow-statement-growth-bulk`` — cash flow statement
        growth for every company, for one fiscal period.

        :param year: fiscal year, e.g. ``"2026"``.
        :param period: fiscal period, one of ``constants.PERIOD_FISCAL``.
        """
        return cast(
            "list[CashFlowStatementGrowthBulkResult]",
            self._get_csv(
                "cash-flow-statement-growth-bulk", {"year": year, "period": period}
            ),
        )

    def eod_bulk(self, date: str) -> list[EodBulkResult]:
        """``GET eod-bulk`` — end-of-day OHLCV price for every symbol, on
        one date.

        :param date: date, ``YYYY-MM-DD``.
        """
        return cast("list[EodBulkResult]", self._get_csv("eod-bulk", {"date": date}))
