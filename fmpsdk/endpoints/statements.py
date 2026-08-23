"""client.statements — Financial statements (income, balance sheet,
cash flow) and everything computed directly from them: ratios, key
metrics, growth rates, scores, and more. 27 methods, the largest group
in this package. ``period`` splits across three incompatible
vocabularies depending on the method — see each method's docstring for
which ``constants.PERIOD_*`` applies.
"""

from __future__ import annotations

from typing import cast

from ..types import (
    BalanceSheetStatementAsReportedResult,
    BalanceSheetStatementGrowthResult,
    BalanceSheetStatementResult,
    BalanceSheetStatementTtmResult,
    CashFlowStatementAsReportedResult,
    CashFlowStatementGrowthResult,
    CashFlowStatementResult,
    EnterpriseValuesResult,
    FinancialGrowthResult,
    FinancialReportsDatesResult,
    FinancialReportsJsonResult,
    FinancialScoresResult,
    FinancialStatementFullAsReportedResult,
    IncomeStatementAsReportedResult,
    IncomeStatementGrowthResult,
    IncomeStatementResult,
    KeyMetricsResult,
    KeyMetricsTtmResult,
    LatestFinancialStatementsResult,
    OwnerEarningsResult,
    RatiosResult,
    RatiosTtmResult,
    RevenueGeographicSegmentationResult,
    RevenueProductSegmentationResult,
)


class StatementsEndpoints:
    """Mixed into :class:`fmpsdk.client.Client`. Each method issues one GET
    against its ``stable/`` path via ``self._get`` (defined on ``Client``).
    """

    def income_statement(
        self, symbol: str, limit: int | None = None, period: str | None = None
    ) -> list[IncomeStatementResult]:
        """``GET income-statement`` — revenue, expenses, and net income
        for one company, periodic.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param limit: max results to return.
        :param period: one of ``constants.PERIOD_ANY`` (``"Q1"``-``"Q4"``,
            ``"FY"``, ``"annual"``, ``"quarter"``).
        """
        return cast(
            "list[IncomeStatementResult]",
            self._get(
                "income-statement", {"symbol": symbol, "limit": limit, "period": period}
            ),
        )

    def income_statement_ttm(
        self, symbol: str, limit: int | None = None
    ) -> list[IncomeStatementResult]:
        """``GET income-statement-ttm`` — the same shape as
        :meth:`income_statement`, trailing twelve months. Still 402s on
        both the free and Starter tiers as of 2026-08-23 — requires FMP
        Premium or Ultimate (not yet confirmed which).

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param limit: max results to return.
        """
        return cast(
            "list[IncomeStatementResult]",
            self._get("income-statement-ttm", {"symbol": symbol, "limit": limit}),
        )

    def income_statement_as_reported(
        self, symbol: str, limit: int | None = None, period: str | None = None
    ) -> list[IncomeStatementAsReportedResult]:
        """``GET income-statement-as-reported`` — income statement data
        exactly as filed, XBRL tag names as keys, no normalization.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param limit: max results to return.
        :param period: one of ``constants.PERIOD_ANNUAL_QUARTER``
            (``"annual"``, ``"quarter"`` — no fiscal-quarter tokens here).
        """
        return cast(
            "list[IncomeStatementAsReportedResult]",
            self._get(
                "income-statement-as-reported",
                {"symbol": symbol, "limit": limit, "period": period},
            ),
        )

    def income_statement_growth(
        self, symbol: str, limit: int | None = None, period: str | None = None
    ) -> list[IncomeStatementGrowthResult]:
        """``GET income-statement-growth`` — year-over-year growth rate
        for every income-statement line item.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param limit: max results to return.
        :param period: one of ``constants.PERIOD_ANY``.
        """
        return cast(
            "list[IncomeStatementGrowthResult]",
            self._get(
                "income-statement-growth",
                {"symbol": symbol, "limit": limit, "period": period},
            ),
        )

    def balance_sheet_statement(
        self, symbol: str, limit: int | None = None, period: str | None = None
    ) -> list[BalanceSheetStatementResult]:
        """``GET balance-sheet-statement`` — assets, liabilities, and
        equity for one company, periodic.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param limit: max results to return.
        :param period: one of ``constants.PERIOD_ANY``.
        """
        return cast(
            "list[BalanceSheetStatementResult]",
            self._get(
                "balance-sheet-statement",
                {"symbol": symbol, "limit": limit, "period": period},
            ),
        )

    def balance_sheet_statement_ttm(
        self, symbol: str, limit: int | None = None
    ) -> list[BalanceSheetStatementTtmResult]:
        """``GET balance-sheet-statement-ttm`` — near-identical shape to
        :meth:`balance_sheet_statement`, trailing twelve months (kept as
        its own type — see `BalanceSheetStatementTtmResult`). Still
        402s on both the free and Starter tiers as of 2026-08-23 —
        requires FMP Premium or Ultimate (not yet confirmed which).

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param limit: max results to return.
        """
        return cast(
            "list[BalanceSheetStatementTtmResult]",
            self._get(
                "balance-sheet-statement-ttm", {"symbol": symbol, "limit": limit}
            ),
        )

    def balance_sheet_statement_as_reported(
        self, symbol: str, limit: int | None = None, period: str | None = None
    ) -> list[BalanceSheetStatementAsReportedResult]:
        """``GET balance-sheet-statement-as-reported`` — balance sheet
        data exactly as filed, XBRL tag names as keys, no normalization.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param limit: max results to return.
        :param period: one of ``constants.PERIOD_ANNUAL_QUARTER``.
        """
        return cast(
            "list[BalanceSheetStatementAsReportedResult]",
            self._get(
                "balance-sheet-statement-as-reported",
                {"symbol": symbol, "limit": limit, "period": period},
            ),
        )

    def balance_sheet_statement_growth(
        self, symbol: str, limit: int | None = None, period: str | None = None
    ) -> list[BalanceSheetStatementGrowthResult]:
        """``GET balance-sheet-statement-growth`` — year-over-year growth
        rate for every balance-sheet line item.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param limit: max results to return.
        :param period: one of ``constants.PERIOD_ANY``.
        """
        return cast(
            "list[BalanceSheetStatementGrowthResult]",
            self._get(
                "balance-sheet-statement-growth",
                {"symbol": symbol, "limit": limit, "period": period},
            ),
        )

    def cash_flow_statement(
        self, symbol: str, limit: int | None = None, period: str | None = None
    ) -> list[CashFlowStatementResult]:
        """``GET cash-flow-statement`` — operating, investing, and
        financing cash flows for one company, periodic.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param limit: max results to return.
        :param period: one of ``constants.PERIOD_ANY``.
        """
        return cast(
            "list[CashFlowStatementResult]",
            self._get(
                "cash-flow-statement",
                {"symbol": symbol, "limit": limit, "period": period},
            ),
        )

    def cash_flow_statement_ttm(
        self, symbol: str, limit: int | None = None
    ) -> list[CashFlowStatementResult]:
        """``GET cash-flow-statement-ttm`` — the same shape as
        :meth:`cash_flow_statement`, trailing twelve months. Still 402s
        on both the free and Starter tiers as of 2026-08-23 — requires
        FMP Premium or Ultimate (not yet confirmed which).

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param limit: max results to return.
        """
        return cast(
            "list[CashFlowStatementResult]",
            self._get("cash-flow-statement-ttm", {"symbol": symbol, "limit": limit}),
        )

    def cash_flow_statement_as_reported(
        self, symbol: str, limit: int | None = None, period: str | None = None
    ) -> list[CashFlowStatementAsReportedResult]:
        """``GET cash-flow-statement-as-reported`` — cash flow data
        exactly as filed, XBRL tag names as keys, no normalization.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param limit: max results to return.
        :param period: one of ``constants.PERIOD_ANNUAL_QUARTER``.
        """
        return cast(
            "list[CashFlowStatementAsReportedResult]",
            self._get(
                "cash-flow-statement-as-reported",
                {"symbol": symbol, "limit": limit, "period": period},
            ),
        )

    def cash_flow_statement_growth(
        self, symbol: str, limit: int | None = None, period: str | None = None
    ) -> list[CashFlowStatementGrowthResult]:
        """``GET cash-flow-statement-growth`` — year-over-year growth rate
        for every cash-flow-statement line item.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param limit: max results to return.
        :param period: one of ``constants.PERIOD_ANY``.
        """
        return cast(
            "list[CashFlowStatementGrowthResult]",
            self._get(
                "cash-flow-statement-growth",
                {"symbol": symbol, "limit": limit, "period": period},
            ),
        )

    def financial_statement_full_as_reported(
        self, symbol: str, limit: int | None = None, period: str | None = None
    ) -> list[FinancialStatementFullAsReportedResult]:
        """``GET financial-statement-full-as-reported`` — the combined
        income + balance sheet + cash flow filing exactly as reported,
        XBRL tag names as keys.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param limit: max results to return.
        :param period: one of ``constants.PERIOD_ANNUAL_QUARTER``.
        """
        return cast(
            "list[FinancialStatementFullAsReportedResult]",
            self._get(
                "financial-statement-full-as-reported",
                {"symbol": symbol, "limit": limit, "period": period},
            ),
        )

    def latest_financial_statements(
        self, page: int | None = None, limit: int | None = None
    ) -> list[LatestFinancialStatementsResult]:
        """``GET latest-financial-statements`` — every company with a
        newly filed statement, paginated across the whole market.
        Still 402s on both the free and Starter tiers as of 2026-08-23
        — requires FMP Premium or Ultimate (not yet confirmed which).

        :param page: zero-indexed page number.
        :param limit: max results per page.
        """
        return cast(
            "list[LatestFinancialStatementsResult]",
            self._get("latest-financial-statements", {"page": page, "limit": limit}),
        )

    def key_metrics(
        self, symbol: str, limit: int | None = None, period: str | None = None
    ) -> list[KeyMetricsResult]:
        """``GET key-metrics`` — valuation and efficiency metrics (EV
        multiples, ROIC, cash conversion cycle, ...) for one company,
        periodic.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param limit: max results to return.
        :param period: one of ``constants.PERIOD_ANY``.
        """
        return cast(
            "list[KeyMetricsResult]",
            self._get(
                "key-metrics", {"symbol": symbol, "limit": limit, "period": period}
            ),
        )

    def key_metrics_ttm(self, symbol: str) -> list[KeyMetricsTtmResult]:
        """``GET key-metrics-ttm`` — the same family of metrics as
        :meth:`key_metrics`, trailing twelve months (own type — every
        field is ``*TTM``-suffixed and the periodic identity fields are
        dropped, see ``types.KeyMetricsTtmResult``).

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        """
        return cast(
            "list[KeyMetricsTtmResult]",
            self._get("key-metrics-ttm", {"symbol": symbol}),
        )

    def ratios(
        self, symbol: str, limit: int | None = None, period: str | None = None
    ) -> list[RatiosResult]:
        """``GET ratios`` — profitability, liquidity, efficiency, and
        leverage ratios for one company, periodic.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param limit: max results to return.
        :param period: one of ``constants.PERIOD_ANY``.
        """
        return cast(
            "list[RatiosResult]",
            self._get("ratios", {"symbol": symbol, "limit": limit, "period": period}),
        )

    def ratios_ttm(self, symbol: str) -> list[RatiosTtmResult]:
        """``GET ratios-ttm`` — the same family of ratios as
        :meth:`ratios`, trailing twelve months (own type — every field is
        ``*TTM``-suffixed and the periodic identity fields are dropped,
        see ``types.RatiosTtmResult``).

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        """
        return cast(
            "list[RatiosTtmResult]", self._get("ratios-ttm", {"symbol": symbol})
        )

    def financial_scores(self, symbol: str) -> list[FinancialScoresResult]:
        """``GET financial-scores`` — Altman Z-Score and Piotroski Score,
        for bankruptcy-risk and financial-strength assessment.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        """
        return cast(
            "list[FinancialScoresResult]",
            self._get("financial-scores", {"symbol": symbol}),
        )

    def owner_earnings(
        self, symbol: str, limit: int | None = None
    ) -> list[OwnerEarningsResult]:
        """``GET owner-earnings`` — Buffett-style owner earnings (net
        income adjusted for maintenance vs. growth capex).

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param limit: max results to return.
        """
        return cast(
            "list[OwnerEarningsResult]",
            self._get("owner-earnings", {"symbol": symbol, "limit": limit}),
        )

    def enterprise_values(
        self, symbol: str, limit: int | None = None, period: str | None = None
    ) -> list[EnterpriseValuesResult]:
        """``GET enterprise-values`` — market cap plus debt minus cash,
        one row per period.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param limit: max results to return.
        :param period: one of ``constants.PERIOD_ANY``.
        """
        return cast(
            "list[EnterpriseValuesResult]",
            self._get(
                "enterprise-values",
                {"symbol": symbol, "limit": limit, "period": period},
            ),
        )

    def financial_growth(
        self, symbol: str, limit: int | None = None, period: str | None = None
    ) -> list[FinancialGrowthResult]:
        """``GET financial-growth`` — cross-statement growth metrics
        (revenue, margins, per-share trends over 3/5/10 years).

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param limit: max results to return.
        :param period: one of ``constants.PERIOD_ANY``.
        """
        return cast(
            "list[FinancialGrowthResult]",
            self._get(
                "financial-growth", {"symbol": symbol, "limit": limit, "period": period}
            ),
        )

    def financial_reports_dates(self, symbol: str) -> list[FinancialReportsDatesResult]:
        """``GET financial-reports-dates`` — every fiscal year/period FMP
        has a 10-K report for, with direct links to the JSON and XLSX
        forms.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        """
        return cast(
            "list[FinancialReportsDatesResult]",
            self._get("financial-reports-dates", {"symbol": symbol}),
        )

    def financial_reports_json(
        self, symbol: str, year: str, period: str
    ) -> FinancialReportsJsonResult:
        """``GET financial-reports-json`` — the full annual report (Form
        10-K) broken into its filed sections (Cover Page, Auditor
        Information, ...). Section names and structure vary by filing,
        so the return type is a loosely typed dict rather than a fixed
        TypedDict.

        Unlike every other method in this package, **returns a single
        object, not a list** — despite FMP's own docs showing this
        endpoint's example response array-wrapped like everything else,
        the real response body is one bare JSON object
        (``{"symbol": ..., "Cover Page": [...], ...}``).

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param year: fiscal year, e.g. ``"2022"``.
        :param period: one of ``constants.PERIOD_FISCAL``
            (``"Q1"``-``"Q4"``, ``"FY"`` — no ``annual``/``quarter`` tokens
            here).
        """
        return cast(
            "FinancialReportsJsonResult",
            self._get(
                "financial-reports-json",
                {"symbol": symbol, "year": year, "period": period},
            ),
        )

    def financial_reports_xlsx(self, symbol: str, year: str, period: str) -> bytes:
        """``GET financial-reports-xlsx`` — the same annual report as
        :meth:`financial_reports_json`, as a downloadable XLSX workbook.

        Returns raw ``bytes``, not JSON — despite an
        ``application/json`` content-type header, the real response
        body is a binary XLSX file (a ZIP container). Write it straight
        to a ``.xlsx`` file rather than trying to parse it as JSON.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param year: fiscal year, e.g. ``"2022"``.
        :param period: one of ``constants.PERIOD_FISCAL``.
        """
        return self._get_bytes(
            "financial-reports-xlsx", {"symbol": symbol, "year": year, "period": period}
        )

    def revenue_product_segmentation(
        self, symbol: str, period: str | None = None, structure: str | None = None
    ) -> list[RevenueProductSegmentationResult]:
        """``GET revenue-product-segmentation`` — revenue broken down by
        product line, one row per fiscal period.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param period: one of ``constants.PERIOD_ANNUAL_QUARTER``.
        :param structure: response layout, e.g. ``"flat"``.
        """
        return cast(
            "list[RevenueProductSegmentationResult]",
            self._get(
                "revenue-product-segmentation",
                {"symbol": symbol, "period": period, "structure": structure},
            ),
        )

    def revenue_geographic_segmentation(
        self, symbol: str, period: str | None = None, structure: str | None = None
    ) -> list[RevenueGeographicSegmentationResult]:
        """``GET revenue-geographic-segmentation`` — revenue broken down
        by geographic region, one row per fiscal period.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param period: one of ``constants.PERIOD_ANNUAL_QUARTER``.
        :param structure: response layout, e.g. ``"flat"``.
        """
        return cast(
            "list[RevenueGeographicSegmentationResult]",
            self._get(
                "revenue-geographic-segmentation",
                {"symbol": symbol, "period": period, "structure": structure},
            ),
        )
