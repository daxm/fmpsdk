"""
   https://site.financialmodelingprep.com/developer/docs#share-float
"""
import typing

from .url_methods import __return_json_v4


def shares_float(
    apikey: str, symbol: str
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /shares_float/ API.

    Provides the total number of shares that are publicly traded for a given company.
    :param apikey: Your API key.
    :param symbol: Ticker of Company.
    :return: A list of dictionaries.
    """
    path = f"shares_float?symbol={symbol}"
    query_vars = {"apikey": apikey}
    return __return_json_v4(path=path, query_vars=query_vars)


def shares_float_all(
    apikey: str
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /shares_float/all/ API.

    The number of shares available for trading, this includes Restricted Stock Units (RSUs)
    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = "shares_float/all"
    query_vars = {"apikey": apikey}
    return __return_json_v4(path=path, query_vars=query_vars)
