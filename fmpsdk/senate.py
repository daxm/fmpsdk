"""
   https://site.financialmodelingprep.com/developer/docs/#Senate-trading
"""
import typing

from .url_methods import __return_json_v4


def senate_trading_rss(
    apikey: str, page: int = 0
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP API for recently reported Senate trades.

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"senate-trading-rss-feed"
    query_vars = {"apikey": apikey, "page": page}
    return __return_json_v4(path=path, query_vars=query_vars)


def senate_trading_symbol(
    apikey: str,
    symbol: str,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP API for recently reported Senate trades filtered by symbol.

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"senate-trading"
    query_vars = {"apikey": apikey, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)


def senate_disclosure_rss(
    apikey: str, page: int = 0
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP API for recently filed Senate disclosures.

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"senate-disclosure-rss-feed"
    query_vars = {"apikey": apikey, "page": page}
    return __return_json_v4(path=path, query_vars=query_vars)


def senate_disclosure_symbol(
    apikey: str,
    symbol: str,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP API for recently filed Senate disclosures filtered by symbol.

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"senate-disclosure"
    query_vars = {"apikey": apikey, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)
