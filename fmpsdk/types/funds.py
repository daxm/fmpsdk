"""TypedDicts for ``client.funds`` response shapes (REWRITE_ARCHITECTURE.md §6, ``client.funds``).

Split out of the former single ``types.py`` for size — see
``fmpsdk/types/__init__.py`` for the shared conventions (naming,
when shapes are/aren't reused, the functional-TypedDict-form cases)
and the re-export barrel that keeps ``from fmpsdk.types import X``
working unchanged for every caller.
"""

from __future__ import annotations

from typing import TypedDict

# --- client.funds ------------------------------------------------------------


class EtfHoldingsResult(TypedDict):
    symbol: str
    asset: str
    name: str
    isin: str
    securityCusip: str
    sharesNumber: int
    weightPercentage: float
    marketValue: float
    updatedAt: str


class EtfInfoSectorExposure(TypedDict):
    """Nested shape of `EtfInfoResult`'s `sectorsList`."""

    industry: str
    exposure: float


class EtfInfoResult(TypedDict):
    symbol: str
    name: str
    description: str
    isin: str
    assetClass: str
    securityCusip: str
    domicile: str
    website: str
    etfCompany: str
    expenseRatio: float
    assetsUnderManagement: float
    avgVolume: int
    inceptionDate: str
    nav: float
    navCurrency: str
    holdingsCount: int
    isActivelyTrading: bool
    updatedAt: str
    sectorsList: list[EtfInfoSectorExposure]


class EtfCountryWeightingsResult(TypedDict):
    country: str
    # Verbatim from FMP's documented example: sent as a "97.26%"-style
    # string, not a float, unlike EtfSectorWeightingsResult below.
    weightPercentage: str


class EtfAssetExposureResult(TypedDict):
    """Different shape from `EtfHoldingsResult` despite the overlapping
    field names: this answers "which ETFs hold this asset" (one row per
    ETF), not "what does this ETF hold" (one row per asset) — no
    `name`/`isin`/`securityCusip` in the documented example."""

    symbol: str
    asset: str
    sharesNumber: int
    weightPercentage: float
    marketValue: float


class EtfSectorWeightingsResult(TypedDict):
    symbol: str
    sector: str
    weightPercentage: float


class FundsDisclosureHoldersLatestResult(TypedDict):
    cik: str
    holder: str
    securityCusip: str
    shares: int
    dateReported: str
    change: int
    weightPercent: float


class FundsDisclosureResult(TypedDict):
    cik: str
    date: str
    acceptedDate: str
    symbol: str
    name: str
    lei: str
    title: str
    cusip: str
    isin: str
    balance: float
    units: str
    cur_cd: str
    valUsd: float
    pctVal: float
    payoffProfile: str
    assetCat: str
    issuerCat: str
    invCountry: str
    isRestrictedSec: str
    fairValLevel: str
    isCashCollateral: str
    isNonCashCollateral: str
    isLoanByFund: str


class FundsDisclosureHoldersSearchResult(TypedDict):
    symbol: str
    cik: str
    classId: str
    seriesId: str
    entityName: str
    entityOrgType: str
    seriesName: str
    className: str
    reportingFileNumber: str
    address: str
    city: str
    zipCode: str
    state: str


class FundsDisclosureDatesResult(TypedDict):
    date: str
    year: int
    quarter: int
