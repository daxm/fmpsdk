"""client.fundraisers — Reg CF crowdfunding and Reg D/A equity offerings
(REWRITE_ARCHITECTURE.md §6, ``client.fundraisers``). 6 canonical methods,
no cross-listings.
"""

from __future__ import annotations

from typing import cast

from ..types import (
    CrowdfundingOfferingResult,
    CrowdfundingOfferingSearchResult,
    FundraisingResult,
    FundraisingSearchResult,
)


class FundraisersEndpoints:
    """Mixed into :class:`fmpsdk.client.Client`. Each method issues one GET
    against its ``stable/`` path via ``self._get`` (defined on ``Client``).
    """

    def crowdfunding_offerings(self, cik: str) -> list[CrowdfundingOfferingResult]:
        """``GET crowdfunding-offerings`` — one issuer's Reg CF campaign
        filings, identified by CIK.

        :param cik: issuer's SEC Central Index Key, e.g. ``"0001916078"``.
        """
        return cast(
            "list[CrowdfundingOfferingResult]",
            self._get("crowdfunding-offerings", {"cik": cik}),
        )

    def crowdfunding_offerings_latest(
        self, page: int | None = None, limit: int | None = None
    ) -> list[CrowdfundingOfferingResult]:
        """``GET crowdfunding-offerings-latest`` — most recent Reg CF
        campaign filings across all issuers, paginated.

        :param page: zero-indexed page number.
        :param limit: max results per page.
        """
        return cast(
            "list[CrowdfundingOfferingResult]",
            self._get("crowdfunding-offerings-latest", {"page": page, "limit": limit}),
        )

    def crowdfunding_offerings_search(
        self, name: str
    ) -> list[CrowdfundingOfferingSearchResult]:
        """``GET crowdfunding-offerings-search`` — issuers matching a
        company/campaign name, resolving to a CIK for use with
        :meth:`crowdfunding_offerings`.

        :param name: company or campaign name to search for, e.g. ``"enotap"``.
        """
        return cast(
            "list[CrowdfundingOfferingSearchResult]",
            self._get("crowdfunding-offerings-search", {"name": name}),
        )

    def fundraising(self, cik: str) -> list[FundraisingResult]:
        """``GET fundraising`` — one issuer's Reg D/A exempt equity
        offering filings, identified by CIK.

        :param cik: issuer's SEC Central Index Key, e.g. ``"0001547416"``.
        """
        return cast("list[FundraisingResult]", self._get("fundraising", {"cik": cik}))

    def fundraising_latest(
        self,
        page: int | None = None,
        limit: int | None = None,
        cik: str | None = None,
    ) -> list[FundraisingResult]:
        """``GET fundraising-latest`` — most recent Reg D/A exempt equity
        offering filings across all issuers, paginated.

        :param page: zero-indexed page number.
        :param limit: max results per page.
        :param cik: restrict to one issuer's SEC Central Index Key.
        """
        return cast(
            "list[FundraisingResult]",
            self._get("fundraising-latest", {"page": page, "limit": limit, "cik": cik}),
        )

    def fundraising_search(self, name: str) -> list[FundraisingSearchResult]:
        """``GET fundraising-search`` — issuers matching a company name,
        resolving to a CIK for use with :meth:`fundraising`.

        :param name: company name to search for, e.g. ``"NJOY"``.
        """
        return cast(
            "list[FundraisingSearchResult]",
            self._get("fundraising-search", {"name": name}),
        )
