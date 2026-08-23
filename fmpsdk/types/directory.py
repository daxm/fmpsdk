"""Response shapes returned by ``client.directory`` methods."""

from __future__ import annotations

from typing import TypedDict

# --- client.directory --------------------------------------------------------

# `stock_list` and `actively_trading_list`/`etf_list` share the {symbol, name}
# field set in FMP's docs, but per the module docstring's "different question"
# rule they stay separate types: whole-universe listing vs. two distinct
# filtered subsets, not the same query with different inputs.


class StockListResult(TypedDict):
    """One symbol in FMP's full tradable universe, across all asset classes and exchanges. Returned by `stock_list()`."""

    symbol: str
    companyName: str


class FinancialStatementSymbolListResult(TypedDict):
    """One symbol FMP has financial statements available for. Returned by `financial_statement_symbol_list()`."""

    symbol: str
    companyName: str
    tradingCurrency: str
    reportingCurrency: str


class CikListResult(TypedDict):
    """One SEC CIK on file. Returned by `cik_list()`."""

    cik: str
    companyName: str


class SymbolChangeResult(TypedDict):
    """One recent ticker symbol change (merger, rename, split). Returned by `symbol_change()`."""

    date: str
    companyName: str
    oldSymbol: str
    newSymbol: str


class EtfListResult(TypedDict):
    """One ETF symbol FMP tracks. Returned by `etf_list()`."""

    symbol: str
    name: str


class ActivelyTradingListResult(TypedDict):
    """One symbol currently actively traded, across all asset classes. Returned by `actively_trading_list()`."""

    symbol: str
    name: str


class AvailableExchangeResult(TypedDict):
    """One exchange FMP has data for. Returned by `available_exchanges()`."""

    exchange: str
    name: str
    countryName: str
    countryCode: str
    symbolSuffix: str
    delay: str


class AvailableSectorResult(TypedDict):
    """One sector value usable for filtering elsewhere in the API (e.g. `company_screener`'s `sector` parameter). Returned by `available_sectors()`."""

    sector: str


class AvailableIndustryResult(TypedDict):
    """One industry value usable for filtering elsewhere in the API. Returned by `available_industries()`."""

    industry: str


class AvailableCountryResult(TypedDict):
    """One country code usable for filtering elsewhere in the API. Returned by `available_countries()`."""

    country: str
