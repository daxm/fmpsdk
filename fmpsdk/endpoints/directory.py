"""client.directory — Whole-universe reference lists: symbols,
exchanges, sectors, industries, countries. 10 methods, each a flat,
mostly param-free list (no ``symbol``/``cik``-scoped lookups — those
live in other groups). Requires an FMP Starter-tier plan or higher —
every method here 402s on the free tier.
"""

from __future__ import annotations

from typing import cast

from ..types import (
    ActivelyTradingListResult,
    AvailableCountryResult,
    AvailableExchangeResult,
    AvailableIndustryResult,
    AvailableSectorResult,
    CikListResult,
    EtfListResult,
    FinancialStatementSymbolListResult,
    StockListResult,
    SymbolChangeResult,
)


class DirectoryEndpoints:
    """Mixed into :class:`fmpsdk.client.Client`. Each method issues one GET
    against its ``stable/`` path via ``self._get`` (defined on ``Client``).
    """

    def stock_list(self) -> list[StockListResult]:
        """``GET stock-list`` — every symbol FMP tracks, across all asset
        classes and exchanges. No parameters; this is the full universe."""
        return cast("list[StockListResult]", self._get("stock-list", {}))

    def financial_statement_symbol_list(
        self,
    ) -> list[FinancialStatementSymbolListResult]:
        """``GET financial-statement-symbol-list`` — symbols for which FMP
        has financial statements (income/balance/cash flow) available,
        distinct from :meth:`stock_list`'s full tradable universe."""
        return cast(
            "list[FinancialStatementSymbolListResult]",
            self._get("financial-statement-symbol-list", {}),
        )

    def cik_list(
        self, page: int | None = None, limit: int | None = None
    ) -> list[CikListResult]:
        """``GET cik-list`` — every SEC CIK on file, paginated.

        :param page: zero-indexed page number.
        :param limit: max results per page.
        """
        return cast(
            "list[CikListResult]", self._get("cik-list", {"page": page, "limit": limit})
        )

    def symbol_change(
        self, invalid: bool | None = None, limit: int | None = None
    ) -> list[SymbolChangeResult]:
        """``GET symbol-change`` — recent ticker symbol changes (mergers,
        renames, splits).

        :param invalid: include changes involving now-invalid symbols.
        :param limit: max results to return.
        """
        return cast(
            "list[SymbolChangeResult]",
            self._get("symbol-change", {"invalid": invalid, "limit": limit}),
        )

    def etf_list(self) -> list[EtfListResult]:
        """``GET etf-list`` — every ETF symbol FMP tracks. No parameters;
        the ETF subset of the full universe, distinct from
        :meth:`actively_trading_list`'s activity-based filter."""
        return cast("list[EtfListResult]", self._get("etf-list", {}))

    def actively_trading_list(self) -> list[ActivelyTradingListResult]:
        """``GET actively-trading-list`` — every symbol currently actively
        traded, across all asset classes. No parameters; the
        activity-based subset of the full universe, distinct from
        :meth:`etf_list`'s asset-class filter."""
        return cast(
            "list[ActivelyTradingListResult]", self._get("actively-trading-list", {})
        )

    def available_exchanges(
        self, extended: bool | None = None
    ) -> list[AvailableExchangeResult]:
        """``GET available-exchanges`` — every exchange FMP has data for.

        :param extended: include extended exchange metadata.
        """
        return cast(
            "list[AvailableExchangeResult]",
            self._get("available-exchanges", {"extended": extended}),
        )

    def available_sectors(self) -> list[AvailableSectorResult]:
        """``GET available-sectors`` — every sector value usable for
        filtering elsewhere in the API (e.g. ``company_screener``'s
        ``sector`` parameter). No parameters."""
        return cast("list[AvailableSectorResult]", self._get("available-sectors", {}))

    def available_industries(self) -> list[AvailableIndustryResult]:
        """``GET available-industries`` — every industry value usable for
        filtering elsewhere in the API. No parameters."""
        return cast(
            "list[AvailableIndustryResult]", self._get("available-industries", {})
        )

    def available_countries(self) -> list[AvailableCountryResult]:
        """``GET available-countries`` — every country code usable for
        filtering elsewhere in the API. No parameters."""
        return cast(
            "list[AvailableCountryResult]", self._get("available-countries", {})
        )
