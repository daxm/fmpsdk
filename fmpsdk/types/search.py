"""Response shapes returned by ``client.search`` methods."""

from __future__ import annotations

from typing import TypedDict

# --- client.search ---------------------------------------------------------


class SearchSymbolResult(TypedDict):
    """Shape shared by `search_symbol` and `search_name` (identical in both
    documented examples)."""

    symbol: str
    name: str
    currency: str
    exchangeFullName: str
    exchange: str


class SearchCikResult(TypedDict):
    """One identity record resolved from a CIK search. Returned by `search_cik()`."""

    symbol: str
    companyName: str
    cik: str
    exchangeFullName: str
    exchange: str
    currency: str


class SearchCusipResult(TypedDict):
    """One identity record resolved from a CUSIP search. Returned by `search_cusip()`."""

    symbol: str
    companyName: str
    cusip: str
    marketCap: float


class SearchIsinResult(TypedDict):
    """One identity record resolved from an ISIN search. Returned by `search_isin()`."""

    symbol: str
    name: str
    isin: str
    marketCap: float


class CompanyScreenerResult(TypedDict):
    """One company matching the screener's filter criteria. Returned by `company_screener()`."""

    symbol: str
    companyName: str
    marketCap: float
    sector: str
    industry: str
    beta: float
    price: float
    lastAnnualDividend: float
    volume: int
    exchange: str
    exchangeShortName: str
    country: str
    isEtf: bool
    isFund: bool
    isActivelyTrading: bool


class SearchExchangeVariantsResult(TypedDict):
    """One exchange listing of a symbol, with a full profile record for that listing. Returned by `search_exchange_variants()`."""

    symbol: str
    price: float
    beta: float
    volAvg: int
    mktCap: float
    lastDiv: float
    range: str
    changes: float
    companyName: str
    currency: str
    cik: str
    isin: str
    cusip: str
    exchange: str
    exchangeShortName: str
    industry: str
    website: str
    description: str
    ceo: str
    sector: str
    country: str
    fullTimeEmployees: str
    phone: str
    address: str
    city: str
    state: str
    zip: str
    dcfDiff: float
    dcf: float
    image: str
    ipoDate: str
    defaultImage: bool
    isEtf: bool
    isActivelyTrading: bool
    isAdr: bool
    isFund: bool
