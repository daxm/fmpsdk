"""
   https://site.financialmodelingprep.com/developer/docs/#Senate-trading
"""

import typing
import os

from .url_methods import __return_json_v4

API_KEY = os.getenv('FMP_API_KEY')

def senate_trading_rss(
    page: int = 0,
    apikey: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP API for recently reported Senate trades.

    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    path = f"senate-trading-rss-feed"
    query_vars = {"apikey": apikey} if apikey else {"apikey": API_KEY, "page": page}
    return __return_json_v4(path=path, query_vars=query_vars)


def senate_trading_symbol(
    symbol: str,
    apikey: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP API for recently reported Senate trades filtered by symbol.

    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    path = f"senate-trading"
    query_vars = {"apikey": apikey} if apikey else {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)


def senate_disclosure_rss(
    page: int = 0,
    apikey: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP API for recently filed Senate disclosures.

    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    path = f"senate-disclosure-rss-feed"
    query_vars = {"apikey": apikey} if apikey else {"apikey": API_KEY, "page": page}
    return __return_json_v4(path=path, query_vars=query_vars)


def senate_disclosure_symbol(
    symbol: str,
    apikey: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP API for recently filed Senate disclosures filtered by symbol.

    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    path = f"senate-disclosure"
    query_vars = {"apikey": apikey} if apikey else {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)