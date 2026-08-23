"""client.search — Identifier lookup (symbol/name/CIK/CUSIP/ISIN) and the
screener. Primary group for these 7 canonical methods
(REWRITE_ARCHITECTURE.md §6, ``client.search``). No cross-listings.
"""

from __future__ import annotations

from typing import cast

from ..types import (
    CompanyScreenerResult,
    SearchCikResult,
    SearchCusipResult,
    SearchExchangeVariantsResult,
    SearchIsinResult,
    SearchSymbolResult,
)


class SearchEndpoints:
    """Mixed into :class:`fmpsdk.client.Client`. Each method issues one GET
    against its ``stable/`` path via ``self._get`` (defined on ``Client``).
    """

    def search_symbol(
        self, query: str, limit: int | None = None, exchange: str | None = None
    ) -> list[SearchSymbolResult]:
        """``GET search-symbol`` — resolve a ticker symbol from a query fragment.

        ``search-X`` (as opposed to ``X-search``) means *resolve an
        identifier*: input is a fragment, output is identity records (§7.3).

        :param query: symbol or partial symbol to search for, e.g. ``"AAPL"``.
        :param limit: max results to return.
        :param exchange: restrict to one exchange, e.g. ``"NASDAQ"``.
        """
        return cast(
            "list[SearchSymbolResult]",
            self._get("search-symbol", {"query": query, "limit": limit, "exchange": exchange}),
        )

    def search_name(
        self, query: str, limit: int | None = None, exchange: str | None = None
    ) -> list[SearchSymbolResult]:
        """``GET search-name`` — resolve a ticker symbol from a company/asset
        name fragment. Same response shape as :meth:`search_symbol`.

        :param query: company or asset name fragment, e.g. ``"Apple"``.
        :param limit: max results to return.
        :param exchange: restrict to one exchange, e.g. ``"NASDAQ"``.
        """
        return cast(
            "list[SearchSymbolResult]",
            self._get("search-name", {"query": query, "limit": limit, "exchange": exchange}),
        )

    def search_cik(self, cik: str, limit: int | None = None) -> list[SearchCikResult]:
        """``GET search-cik`` — resolve identity records from a CIK.

        :param cik: SEC Central Index Key, e.g. ``"320193"``.
        :param limit: max results to return.
        """
        return cast("list[SearchCikResult]", self._get("search-cik", {"cik": cik, "limit": limit}))

    def search_cusip(self, cusip: str) -> list[SearchCusipResult]:
        """``GET search-cusip`` — resolve identity records from a CUSIP.

        :param cusip: 9-character CUSIP, e.g. ``"037833100"``.
        """
        return cast("list[SearchCusipResult]", self._get("search-cusip", {"cusip": cusip}))

    def search_isin(self, isin: str) -> list[SearchIsinResult]:
        """``GET search-isin`` — resolve identity records from an ISIN.

        :param isin: 12-character ISIN, e.g. ``"US0378331005"``.
        """
        return cast("list[SearchIsinResult]", self._get("search-isin", {"isin": isin}))

    def search_exchange_variants(self, symbol: str) -> list[SearchExchangeVariantsResult]:
        """``GET search-exchange-variants`` — every exchange listing a symbol
        trades on, with a full profile record per listing.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        """
        return cast(
            "list[SearchExchangeVariantsResult]",
            self._get("search-exchange-variants", {"symbol": symbol}),
        )

    def company_screener(
        self,
        market_cap_more_than: float | None = None,
        market_cap_lower_than: float | None = None,
        sector: str | None = None,
        industry: str | None = None,
        beta_more_than: float | None = None,
        beta_lower_than: float | None = None,
        price_more_than: float | None = None,
        price_lower_than: float | None = None,
        dividend_more_than: float | None = None,
        dividend_lower_than: float | None = None,
        volume_more_than: float | None = None,
        volume_lower_than: float | None = None,
        exchange: str | None = None,
        country: str | None = None,
        is_etf: bool | None = None,
        is_fund: bool | None = None,
        is_actively_trading: bool | None = None,
        page: int | None = None,
        limit: int | None = None,
        include_all_share_classes: bool | None = None,
    ) -> list[CompanyScreenerResult]:
        """``GET company-screener`` — filter the whole equity universe by
        market cap, price, sector, and more.

        Unlike its siblings in this group, this is a dataset query (input is
        a filter, output is domain records) rather than an identifier
        lookup, even though its own path lacks the ``-search`` suffix that
        usually marks that distinction (§7.3).
        """
        return cast(
            "list[CompanyScreenerResult]",
            self._get(
                "company-screener",
                {
                    "marketCapMoreThan": market_cap_more_than,
                    "marketCapLowerThan": market_cap_lower_than,
                    "sector": sector,
                    "industry": industry,
                    "betaMoreThan": beta_more_than,
                    "betaLowerThan": beta_lower_than,
                    "priceMoreThan": price_more_than,
                    "priceLowerThan": price_lower_than,
                    "dividendMoreThan": dividend_more_than,
                    "dividendLowerThan": dividend_lower_than,
                    "volumeMoreThan": volume_more_than,
                    "volumeLowerThan": volume_lower_than,
                    "exchange": exchange,
                    "country": country,
                    "isEtf": is_etf,
                    "isFund": is_fund,
                    "isActivelyTrading": is_actively_trading,
                    "page": page,
                    "limit": limit,
                    "includeAllShareClasses": include_all_share_classes,
                },
            ),
        )
