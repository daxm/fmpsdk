"""client.institutional_ownership — Form 13F institutional holdings,
holders, and derived analytics (REWRITE_ARCHITECTURE.md §6,
``client.institutional_ownership``). 8 canonical methods, no
cross-listings. Named by the workflow doc's original pricing-tier audit
as a likely Bucket 2 ("granular Form 13F") category — confirm live rather
than assume.
"""

from __future__ import annotations

from typing import cast

from ..types import (
    InstitutionalOwnershipDatesResult,
    InstitutionalOwnershipExtractAnalyticsHolderResult,
    InstitutionalOwnershipExtractResult,
    InstitutionalOwnershipHolderIndustryBreakdownResult,
    InstitutionalOwnershipHolderPerformanceSummaryResult,
    InstitutionalOwnershipIndustrySummaryResult,
    InstitutionalOwnershipLatestResult,
    InstitutionalOwnershipSymbolPositionsSummaryResult,
)


class InstitutionalOwnershipEndpoints:
    """Mixed into :class:`fmpsdk.client.Client`. Each method issues one GET
    against its ``stable/`` path via ``self._get`` (defined on ``Client``).
    """

    def institutional_ownership_latest(
        self, page: int | None = None, limit: int | None = None
    ) -> list[InstitutionalOwnershipLatestResult]:
        """``GET institutional-ownership/latest`` — most recent Form 13F
        filings across all institutional investors, paginated.

        :param page: zero-indexed page number.
        :param limit: max results per page.
        """
        return cast(
            "list[InstitutionalOwnershipLatestResult]",
            self._get("institutional-ownership/latest", {"page": page, "limit": limit}),
        )

    def institutional_ownership_extract(
        self, cik: str, year: str, quarter: str
    ) -> list[InstitutionalOwnershipExtractResult]:
        """``GET institutional-ownership/extract`` — one filer's Form 13F
        holdings for one quarter, one row per security.

        :param cik: filer's SEC Central Index Key, e.g. ``"0001388838"``.
        :param year: filing year, e.g. ``"2023"``.
        :param quarter: filing quarter, e.g. ``"3"``.
        """
        return cast(
            "list[InstitutionalOwnershipExtractResult]",
            self._get(
                "institutional-ownership/extract",
                {"cik": cik, "year": year, "quarter": quarter},
            ),
        )

    def institutional_ownership_dates(
        self, cik: str
    ) -> list[InstitutionalOwnershipDatesResult]:
        """``GET institutional-ownership/dates`` — every fiscal
        year/quarter one filer has a Form 13F on file for.

        :param cik: filer's SEC Central Index Key, e.g. ``"0001067983"``.
        """
        return cast(
            "list[InstitutionalOwnershipDatesResult]",
            self._get("institutional-ownership/dates", {"cik": cik}),
        )

    def institutional_ownership_extract_analytics_holder(
        self,
        symbol: str,
        year: str,
        quarter: str,
        page: int | None = None,
        limit: int | None = None,
    ) -> list[InstitutionalOwnershipExtractAnalyticsHolderResult]:
        """``GET institutional-ownership/extract-analytics/holder`` —
        per-holder analytics for one security: weight, market value, and
        share-count changes, ownership percentage, holding period.

        :param symbol: security ticker symbol, e.g. ``"AAPL"``.
        :param year: filing year, e.g. ``"2023"``.
        :param quarter: filing quarter, e.g. ``"3"``.
        :param page: zero-indexed page number.
        :param limit: max results per page.
        """
        return cast(
            "list[InstitutionalOwnershipExtractAnalyticsHolderResult]",
            self._get(
                "institutional-ownership/extract-analytics/holder",
                {
                    "symbol": symbol,
                    "year": year,
                    "quarter": quarter,
                    "page": page,
                    "limit": limit,
                },
            ),
        )

    def institutional_ownership_holder_performance_summary(
        self, cik: str, page: int | None = None
    ) -> list[InstitutionalOwnershipHolderPerformanceSummaryResult]:
        """``GET institutional-ownership/holder-performance-summary`` —
        one filer's portfolio performance, including S&P 500-relative
        returns over 1/3/5 years and since inception.

        :param cik: filer's SEC Central Index Key, e.g. ``"0001067983"``.
        :param page: zero-indexed page number.
        """
        return cast(
            "list[InstitutionalOwnershipHolderPerformanceSummaryResult]",
            self._get(
                "institutional-ownership/holder-performance-summary",
                {"cik": cik, "page": page},
            ),
        )

    def institutional_ownership_holder_industry_breakdown(
        self, cik: str, year: str, quarter: str
    ) -> list[InstitutionalOwnershipHolderIndustryBreakdownResult]:
        """``GET institutional-ownership/holder-industry-breakdown`` — one
        filer's portfolio weight and performance broken down by industry.

        :param cik: filer's SEC Central Index Key, e.g. ``"0001067983"``.
        :param year: filing year, e.g. ``"2023"``.
        :param quarter: filing quarter, e.g. ``"3"``.
        """
        return cast(
            "list[InstitutionalOwnershipHolderIndustryBreakdownResult]",
            self._get(
                "institutional-ownership/holder-industry-breakdown",
                {"cik": cik, "year": year, "quarter": quarter},
            ),
        )

    def institutional_ownership_symbol_positions_summary(
        self, symbol: str, year: str, quarter: str
    ) -> list[InstitutionalOwnershipSymbolPositionsSummaryResult]:
        """``GET institutional-ownership/symbol-positions-summary`` —
        aggregate institutional positioning in one security: investor
        count, share/value totals, new/increased/reduced/closed position
        counts, put/call ratio.

        :param symbol: security ticker symbol, e.g. ``"AAPL"``.
        :param year: filing year, e.g. ``"2023"``.
        :param quarter: filing quarter, e.g. ``"3"``.
        """
        return cast(
            "list[InstitutionalOwnershipSymbolPositionsSummaryResult]",
            self._get(
                "institutional-ownership/symbol-positions-summary",
                {"symbol": symbol, "year": year, "quarter": quarter},
            ),
        )

    def institutional_ownership_industry_summary(
        self, year: str, quarter: str
    ) -> list[InstitutionalOwnershipIndustrySummaryResult]:
        """``GET institutional-ownership/industry-summary`` — total
        institutional investment value by industry, market-wide.

        :param year: filing year, e.g. ``"2023"``.
        :param quarter: filing quarter, e.g. ``"3"``.
        """
        return cast(
            "list[InstitutionalOwnershipIndustrySummaryResult]",
            self._get(
                "institutional-ownership/industry-summary",
                {"year": year, "quarter": quarter},
            ),
        )
