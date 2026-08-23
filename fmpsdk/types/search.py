"""TypedDicts for ``client.search`` response shapes (REWRITE_ARCHITECTURE.md §6, ``client.search``).

Split out of the former single ``types.py`` for size — see
``fmpsdk/types/__init__.py`` for the shared conventions (naming,
when shapes are/aren't reused, the functional-TypedDict-form cases)
and the re-export barrel that keeps ``from fmpsdk.types import X``
working unchanged for every caller.
"""

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
    symbol: str
    companyName: str
    cik: str
    exchangeFullName: str
    exchange: str
    currency: str


class SearchCusipResult(TypedDict):
    symbol: str
    companyName: str
    cusip: str
    marketCap: float


class SearchIsinResult(TypedDict):
    symbol: str
    name: str
    isin: str
    marketCap: float


class CompanyScreenerResult(TypedDict):
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
