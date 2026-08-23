"""Response shapes returned by ``client.directory`` methods."""

from __future__ import annotations

from typing import TypedDict

# --- client.directory --------------------------------------------------------

# `stock_list` and `actively_trading_list`/`etf_list` share the {symbol, name}
# field set in FMP's docs, but per the module docstring's "different question"
# rule they stay separate types: whole-universe listing vs. two distinct
# filtered subsets, not the same query with different inputs.


class StockListResult(TypedDict):
    symbol: str
    companyName: str


class FinancialStatementSymbolListResult(TypedDict):
    symbol: str
    companyName: str
    tradingCurrency: str
    reportingCurrency: str


class CikListResult(TypedDict):
    cik: str
    companyName: str


class SymbolChangeResult(TypedDict):
    date: str
    companyName: str
    oldSymbol: str
    newSymbol: str


class EtfListResult(TypedDict):
    symbol: str
    name: str


class ActivelyTradingListResult(TypedDict):
    symbol: str
    name: str


class AvailableExchangeResult(TypedDict):
    exchange: str
    name: str
    countryName: str
    countryCode: str
    symbolSuffix: str
    delay: str


class AvailableSectorResult(TypedDict):
    sector: str


class AvailableIndustryResult(TypedDict):
    industry: str


class AvailableCountryResult(TypedDict):
    country: str
