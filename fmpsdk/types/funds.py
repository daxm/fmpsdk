"""Response shapes returned by ``client.funds`` methods."""

from __future__ import annotations

from typing import TypedDict

# --- client.funds ------------------------------------------------------------


class EtfHoldingsResult(TypedDict):
    """One asset an ETF holds, with market value and portfolio weight. Returned by `etf_holdings()`."""

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
    """Fund-level metadata: expense ratio, AUM, NAV, inception date, and sector exposure breakdown. Returned by `etf_info()`."""

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
    """Portfolio weight by country of an ETF's underlying holdings. Returned by `etf_country_weightings()`."""

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
    """Portfolio weight by sector of an ETF's underlying holdings. Returned by `etf_sector_weightings()`."""

    symbol: str
    sector: str
    weightPercentage: float


class FundsDisclosureHoldersLatestResult(TypedDict):
    """One fund's most recent disclosed holding of one security, with share count and change since the prior filing. Returned by `funds_disclosure_holders_latest()`."""

    cik: str
    holder: str
    securityCusip: str
    shares: int
    dateReported: str
    change: int
    weightPercent: float


class FundsDisclosureResult(TypedDict):
    """One N-PORT-style per-holding disclosure line for one fund, one filing period. Returned by `funds_disclosure()`."""

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
    """One fund/entity matching a name search, with CIK, series/class IDs, and filer address. Returned by `funds_disclosure_holders_search()`."""

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
    """One filing period available for `funds_disclosure()`, for one fund. Returned by `funds_disclosure_dates()`."""

    date: str
    year: int
    quarter: int
