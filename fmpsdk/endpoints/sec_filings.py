"""client.sec_filings — SEC filing search, SEC company identity, and
SIC industry classification. 12 methods. Only
``industry_classification_search`` and ``all_industry_classification``
require an FMP Starter-tier plan or higher — the other 10 work on the
free tier.
"""

from __future__ import annotations

from typing import cast

from ..types import (
    IndustryClassificationResult,
    SecFilingResult,
    SecFilingSearchResult,
    SecFilingsCompanySearchResult,
    SecProfileResult,
    StandardIndustrialClassificationResult,
)


class SecFilingsEndpoints:
    """Mixed into :class:`fmpsdk.client.Client`. Each method issues one GET
    against its ``stable/`` path via ``self._get`` (defined on ``Client``).
    """

    def sec_filings_8k(
        self,
        from_: str,
        to: str,
        page: int | None = None,
        limit: int | None = None,
    ) -> list[SecFilingResult]:
        """``GET sec-filings-8k`` — most recent 8-K filings across all
        companies, in a date range.

        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        :param page: zero-indexed page number.
        :param limit: max results per page.
        """
        return cast(
            "list[SecFilingResult]",
            self._get(
                "sec-filings-8k",
                {"from": from_, "to": to, "page": page, "limit": limit},
            ),
        )

    def sec_filings_financials(
        self,
        from_: str,
        to: str,
        page: int | None = None,
        limit: int | None = None,
    ) -> list[SecFilingResult]:
        """``GET sec-filings-financials`` — most recent filings that
        carry financial statements (8-K, 10-K, 10-Q, ...), in a date range.

        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        :param page: zero-indexed page number.
        :param limit: max results per page.
        """
        return cast(
            "list[SecFilingResult]",
            self._get(
                "sec-filings-financials",
                {"from": from_, "to": to, "page": page, "limit": limit},
            ),
        )

    def sec_filings_search_form_type(
        self,
        form_type: str,
        from_: str,
        to: str,
        page: int | None = None,
        limit: int | None = None,
    ) -> list[SecFilingSearchResult]:
        """``GET sec-filings-search/form-type`` — filings of one form
        type (e.g. ``"8-K"``, ``"10-K"``) across all companies, in a date
        range.

        :param form_type: SEC form type, e.g. ``"8-K"``.
        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        :param page: zero-indexed page number.
        :param limit: max results per page.
        """
        return cast(
            "list[SecFilingSearchResult]",
            self._get(
                "sec-filings-search/form-type",
                {
                    "formType": form_type,
                    "from": from_,
                    "to": to,
                    "page": page,
                    "limit": limit,
                },
            ),
        )

    def sec_filings_search_symbol(
        self,
        symbol: str,
        from_: str,
        to: str,
        page: int | None = None,
        limit: int | None = None,
    ) -> list[SecFilingSearchResult]:
        """``GET sec-filings-search/symbol`` — one company's filings, in
        a date range.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        :param page: zero-indexed page number.
        :param limit: max results per page.
        """
        return cast(
            "list[SecFilingSearchResult]",
            self._get(
                "sec-filings-search/symbol",
                {
                    "symbol": symbol,
                    "from": from_,
                    "to": to,
                    "page": page,
                    "limit": limit,
                },
            ),
        )

    def sec_filings_search_cik(
        self,
        cik: str,
        from_: str,
        to: str,
        page: int | None = None,
        limit: int | None = None,
    ) -> list[SecFilingSearchResult]:
        """``GET sec-filings-search/cik`` — one entity's filings by CIK,
        in a date range.

        :param cik: SEC Central Index Key, e.g. ``"0000320193"``.
        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        :param page: zero-indexed page number.
        :param limit: max results per page.
        """
        return cast(
            "list[SecFilingSearchResult]",
            self._get(
                "sec-filings-search/cik",
                {"cik": cik, "from": from_, "to": to, "page": page, "limit": limit},
            ),
        )

    def sec_filings_company_search_name(
        self, company: str
    ) -> list[SecFilingsCompanySearchResult]:
        """``GET sec-filings-company-search/name`` — companies/entities
        whose registered name matches a search string, resolving to a CIK.

        :param company: company/entity name to search for, e.g. ``"Berkshire"``.
        """
        return cast(
            "list[SecFilingsCompanySearchResult]",
            self._get("sec-filings-company-search/name", {"company": company}),
        )

    def sec_filings_company_search_symbol(
        self, symbol: str
    ) -> list[SecFilingsCompanySearchResult]:
        """``GET sec-filings-company-search/symbol`` — one company's SEC
        identity (CIK, SIC code, business address) by ticker symbol.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        """
        return cast(
            "list[SecFilingsCompanySearchResult]",
            self._get("sec-filings-company-search/symbol", {"symbol": symbol}),
        )

    def sec_filings_company_search_cik(
        self, cik: str
    ) -> list[SecFilingsCompanySearchResult]:
        """``GET sec-filings-company-search/cik`` — one company's SEC
        identity (name, SIC code, business address) by CIK.

        :param cik: SEC Central Index Key, e.g. ``"0000320193"``.
        """
        return cast(
            "list[SecFilingsCompanySearchResult]",
            self._get("sec-filings-company-search/cik", {"cik": cik}),
        )

    def sec_profile(
        self, symbol: str, cik: str | None = None
    ) -> list[SecProfileResult]:
        """``GET sec-profile`` — full SEC-registrant profile: business/
        mailing address, SIC classification, CEO, fiscal year end, IPO
        date, and more.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param cik: optional CIK filter. FMP's own docs render this
            parameter's name as ``cik-A``, which looks like a table
            rendering artifact rather than a real wire name — exposed
            here as plain ``cik`` pending live confirmation either way.
        """
        return cast(
            "list[SecProfileResult]",
            self._get("sec-profile", {"symbol": symbol, "cik": cik}),
        )

    def standard_industrial_classification_list(
        self,
        industry_title: str | None = None,
        sic_code: str | None = None,
    ) -> list[StandardIndustrialClassificationResult]:
        """``GET standard-industrial-classification-list`` — every SIC
        code and its industry title FMP recognizes.

        :param industry_title: filter by industry title, e.g. ``"SERVICES"``.
        :param sic_code: filter by SIC code, e.g. ``"7371"``.
        """
        return cast(
            "list[StandardIndustrialClassificationResult]",
            self._get(
                "standard-industrial-classification-list",
                {"industryTitle": industry_title, "sicCode": sic_code},
            ),
        )

    def industry_classification_search(
        self,
        symbol: str | None = None,
        cik: str | None = None,
        sic_code: str | None = None,
    ) -> list[IndustryClassificationResult]:
        """``GET industry-classification-search`` — companies matching a
        symbol, CIK, and/or SIC code, with their industry classification.

        :param symbol: filter by ticker symbol, e.g. ``"AAPL"``.
        :param cik: filter by SEC Central Index Key.
        :param sic_code: filter by SIC code, e.g. ``"7371"``.
        """
        return cast(
            "list[IndustryClassificationResult]",
            self._get(
                "industry-classification-search",
                {"symbol": symbol, "cik": cik, "sicCode": sic_code},
            ),
        )

    def all_industry_classification(
        self, page: int | None = None, limit: int | None = None
    ) -> list[IndustryClassificationResult]:
        """``GET all-industry-classification`` — every company's industry
        classification, market-wide, paginated.

        :param page: zero-indexed page number.
        :param limit: max results per page.
        """
        return cast(
            "list[IndustryClassificationResult]",
            self._get("all-industry-classification", {"page": page, "limit": limit}),
        )
