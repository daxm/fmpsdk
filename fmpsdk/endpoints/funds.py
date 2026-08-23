"""client.funds — ETF composition/info and fund N-PORT-style holdings
disclosures. 9 methods. ``etf_info``, ``etf_country_weightings``, and
``etf_sector_weightings`` require an FMP Starter-tier plan or higher.
The other 6 (``etf_holdings``, ``etf_asset_exposure``, and all 4
``funds_disclosure*`` methods) still 402 on both the free and Starter
tiers as of 2026-08-23 — they require FMP Premium or Ultimate (not yet
confirmed which).
"""

from __future__ import annotations

from typing import cast

from ..types import (
    EtfAssetExposureResult,
    EtfCountryWeightingsResult,
    EtfHoldingsResult,
    EtfInfoResult,
    EtfSectorWeightingsResult,
    FundsDisclosureDatesResult,
    FundsDisclosureHoldersLatestResult,
    FundsDisclosureHoldersSearchResult,
    FundsDisclosureResult,
)


class FundsEndpoints:
    """Mixed into :class:`fmpsdk.client.Client`. Each method issues one GET
    against its ``stable/`` path via ``self._get`` (defined on ``Client``).
    """

    def etf_holdings(self, symbol: str) -> list[EtfHoldingsResult]:
        """``GET etf/holdings`` — the assets an ETF holds, one row per
        holding, with market value and portfolio weight.

        :param symbol: ETF ticker symbol, e.g. ``"SPY"``.
        """
        return cast(
            "list[EtfHoldingsResult]", self._get("etf/holdings", {"symbol": symbol})
        )

    def etf_info(self, symbol: str) -> list[EtfInfoResult]:
        """``GET etf/info`` — fund-level metadata: expense ratio, AUM,
        NAV, inception date, and sector exposure breakdown.

        :param symbol: ETF ticker symbol, e.g. ``"SPY"``.
        """
        return cast("list[EtfInfoResult]", self._get("etf/info", {"symbol": symbol}))

    def etf_country_weightings(self, symbol: str) -> list[EtfCountryWeightingsResult]:
        """``GET etf/country-weightings`` — portfolio weight by country of
        the underlying holdings.

        :param symbol: ETF ticker symbol, e.g. ``"SPY"``.
        """
        return cast(
            "list[EtfCountryWeightingsResult]",
            self._get("etf/country-weightings", {"symbol": symbol}),
        )

    def etf_asset_exposure(self, symbol: str) -> list[EtfAssetExposureResult]:
        """``GET etf/asset-exposure`` — every ETF that holds a given
        asset, with each ETF's weight and market value for it. The
        inverse lookup of :meth:`etf_holdings`.

        :param symbol: asset ticker symbol, e.g. ``"AAPL"``.
        """
        return cast(
            "list[EtfAssetExposureResult]",
            self._get("etf/asset-exposure", {"symbol": symbol}),
        )

    def etf_sector_weightings(self, symbol: str) -> list[EtfSectorWeightingsResult]:
        """``GET etf/sector-weightings`` — portfolio weight by sector of
        the underlying holdings.

        :param symbol: ETF ticker symbol, e.g. ``"SPY"``.
        """
        return cast(
            "list[EtfSectorWeightingsResult]",
            self._get("etf/sector-weightings", {"symbol": symbol}),
        )

    def funds_disclosure(
        self, symbol: str, year: str, quarter: str, cik: str | None = None
    ) -> list[FundsDisclosureResult]:
        """``GET funds/disclosure`` — N-PORT-style per-holding disclosure
        for one fund, one filing period: balance, market value, issuer
        category, fair-value level.

        :param symbol: fund ticker symbol, e.g. ``"VWO"``.
        :param year: filing year, e.g. ``"2023"``.
        :param quarter: filing quarter, e.g. ``"4"``.
        :param cik: restrict to one filer's CIK.
        """
        return cast(
            "list[FundsDisclosureResult]",
            self._get(
                "funds/disclosure",
                {"symbol": symbol, "year": year, "quarter": quarter, "cik": cik},
            ),
        )

    def funds_disclosure_dates(
        self, symbol: str, cik: str | None = None
    ) -> list[FundsDisclosureDatesResult]:
        """``GET funds/disclosure-dates`` — every filing period available
        for :meth:`funds_disclosure`, for one fund.

        :param symbol: fund ticker symbol, e.g. ``"VWO"``.
        :param cik: restrict to one filer's CIK.
        """
        return cast(
            "list[FundsDisclosureDatesResult]",
            self._get("funds/disclosure-dates", {"symbol": symbol, "cik": cik}),
        )

    def funds_disclosure_holders_latest(
        self, symbol: str
    ) -> list[FundsDisclosureHoldersLatestResult]:
        """``GET funds/disclosure-holders-latest`` — the most recent
        disclosed holders of one security, across all filing funds, with
        share count and change since the prior filing.

        :param symbol: security ticker symbol, e.g. ``"AAPL"``.
        """
        return cast(
            "list[FundsDisclosureHoldersLatestResult]",
            self._get("funds/disclosure-holders-latest", {"symbol": symbol}),
        )

    def funds_disclosure_holders_search(
        self, name: str
    ) -> list[FundsDisclosureHoldersSearchResult]:
        """``GET funds/disclosure-holders-search`` — resolve a fund/entity
        name to its CIK, series/class IDs, and filer address.

        :param name: fund or entity name (fragment or full), e.g.
            ``"Federated Hermes Government Income Securities, Inc."``.
        """
        return cast(
            "list[FundsDisclosureHoldersSearchResult]",
            self._get("funds/disclosure-holders-search", {"name": name}),
        )
