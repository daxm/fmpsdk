"""client.company — Company-level reference and profile data, incl. market
cap, float, executives, M&A (REWRITE_ARCHITECTURE.md §6, ``client.company``).
17 canonical methods, no cross-listings.
"""

from __future__ import annotations

from typing import cast

from ..types import (
    CompanyNotesResult,
    DelistedCompanyResult,
    EmployeeCountResult,
    ExecutiveCompensationBenchmarkResult,
    ExecutiveCompensationResult,
    KeyExecutiveResult,
    MarketCapResult,
    MergersAcquisitionsResult,
    ProfileResult,
    SharesFloatAllResult,
    SharesFloatResult,
    StockPeersResult,
)


class CompanyEndpoints:
    """Mixed into :class:`fmpsdk.client.Client`. Each method issues one GET
    against its ``stable/`` path via ``self._get`` (defined on ``Client``).
    """

    def profile(self, symbol: str) -> list[ProfileResult]:
        """``GET profile`` — the full company profile record: price,
        market cap, identifiers (CIK/ISIN/CUSIP), sector/industry,
        leadership, contact info.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        """
        return cast("list[ProfileResult]", self._get("profile", {"symbol": symbol}))

    def profile_cik(self, cik: str) -> list[ProfileResult]:
        """``GET profile-cik`` — the same company profile record as
        :meth:`profile`, looked up by CIK instead of ticker symbol.

        :param cik: SEC Central Index Key, e.g. ``"320193"``.
        """
        return cast("list[ProfileResult]", self._get("profile-cik", {"cik": cik}))

    def company_notes(self, symbol: str) -> list[CompanyNotesResult]:
        """``GET company-notes`` — corporate debt notes issued by the
        company, with exchange listing.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        """
        return cast("list[CompanyNotesResult]", self._get("company-notes", {"symbol": symbol}))

    def stock_peers(self, symbol: str) -> list[StockPeersResult]:
        """``GET stock-peers`` — companies on the same exchange, sector,
        and market-cap range.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        """
        return cast("list[StockPeersResult]", self._get("stock-peers", {"symbol": symbol}))

    def delisted_companies(
        self, page: int | None = None, limit: int | None = None
    ) -> list[DelistedCompanyResult]:
        """``GET delisted-companies`` — companies removed from public
        exchanges, paginated.

        :param page: zero-indexed page number.
        :param limit: max results per page.
        """
        return cast(
            "list[DelistedCompanyResult]",
            self._get("delisted-companies", {"page": page, "limit": limit}),
        )

    def employee_count(
        self, symbol: str, limit: int | None = None
    ) -> list[EmployeeCountResult]:
        """``GET employee-count`` — workforce size from the most recent
        SEC filing.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param limit: max results to return.
        """
        return cast(
            "list[EmployeeCountResult]",
            self._get("employee-count", {"symbol": symbol, "limit": limit}),
        )

    def historical_employee_count(
        self, symbol: str, limit: int | None = None
    ) -> list[EmployeeCountResult]:
        """``GET historical-employee-count`` — the same workforce data as
        :meth:`employee_count`, across every filed reporting period.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param limit: max results to return.
        """
        return cast(
            "list[EmployeeCountResult]",
            self._get("historical-employee-count", {"symbol": symbol, "limit": limit}),
        )

    def market_capitalization(self, symbol: str) -> list[MarketCapResult]:
        """``GET market-capitalization`` — current market cap for one
        symbol.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        """
        return cast(
            "list[MarketCapResult]", self._get("market-capitalization", {"symbol": symbol})
        )

    def market_capitalization_batch(self, symbols: str) -> list[MarketCapResult]:
        """``GET market-capitalization-batch`` — current market cap for
        several symbols in one call.

        :param symbols: comma-separated ticker symbols, e.g. ``"AAPL,MSFT,GOOG"``.
        """
        return cast(
            "list[MarketCapResult]",
            self._get("market-capitalization-batch", {"symbols": symbols}),
        )

    def historical_market_capitalization(
        self,
        symbol: str,
        limit: int | None = None,
        from_: str | None = None,
        to: str | None = None,
    ) -> list[MarketCapResult]:
        """``GET historical-market-capitalization`` — market cap for one
        symbol over a date range.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param limit: max results to return.
        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        """
        return cast(
            "list[MarketCapResult]",
            self._get(
                "historical-market-capitalization",
                {"symbol": symbol, "limit": limit, "from": from_, "to": to},
            ),
        )

    def shares_float(self, symbol: str) -> list[SharesFloatResult]:
        """``GET shares-float`` — publicly tradable share count and free
        float percentage for one company.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        """
        return cast("list[SharesFloatResult]", self._get("shares-float", {"symbol": symbol}))

    def shares_float_all(
        self, limit: int | None = None, page: int | None = None
    ) -> list[SharesFloatAllResult]:
        """``GET shares-float-all`` — free float and outstanding shares
        across every company FMP tracks, paginated.

        :param limit: max results per page.
        :param page: zero-indexed page number.
        """
        return cast(
            "list[SharesFloatAllResult]",
            self._get("shares-float-all", {"limit": limit, "page": page}),
        )

    def mergers_acquisitions_latest(
        self, page: int | None = None, limit: int | None = None
    ) -> list[MergersAcquisitionsResult]:
        """``GET mergers-acquisitions-latest`` — recent M&A filings,
        unfiltered, paginated.

        :param page: zero-indexed page number.
        :param limit: max results per page.
        """
        return cast(
            "list[MergersAcquisitionsResult]",
            self._get("mergers-acquisitions-latest", {"page": page, "limit": limit}),
        )

    def mergers_acquisitions_search(self, name: str) -> list[MergersAcquisitionsResult]:
        """``GET mergers-acquisitions-search`` — the same M&A filing data
        as :meth:`mergers_acquisitions_latest`, filtered by company name.

        :param name: company name (acquirer or target) to search for, e.g. ``"Apple"``.
        """
        return cast(
            "list[MergersAcquisitionsResult]",
            self._get("mergers-acquisitions-search", {"name": name}),
        )

    def key_executives(self, symbol: str) -> list[KeyExecutiveResult]:
        """``GET key-executives`` — company leadership roster: name,
        title, pay, and demographic detail.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        """
        return cast("list[KeyExecutiveResult]", self._get("key-executives", {"symbol": symbol}))

    def governance_executive_compensation(
        self, symbol: str
    ) -> list[ExecutiveCompensationResult]:
        """``GET governance-executive-compensation`` — detailed per-executive
        compensation filings: salary, bonus, stock/option awards, total.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        """
        return cast(
            "list[ExecutiveCompensationResult]",
            self._get("governance-executive-compensation", {"symbol": symbol}),
        )

    def executive_compensation_benchmark(
        self, year: str | None = None
    ) -> list[ExecutiveCompensationBenchmarkResult]:
        """``GET executive-compensation-benchmark`` — average executive
        compensation by industry, for cross-company benchmarking.

        :param year: filing year, e.g. ``"2024"``.
        """
        return cast(
            "list[ExecutiveCompensationBenchmarkResult]",
            self._get("executive-compensation-benchmark", {"year": year}),
        )
