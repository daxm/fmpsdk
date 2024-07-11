import typing
import os

from .general import __quotes
from .url_methods import __return_json_v3

API_KEY = os.getenv('FMP_API_KEY')

def forex() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /fx/ API

    :return: A list of dictionaries.
    """
    path = f"fx"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def forex_list() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /quotes/forex/ API

    :return: A list of dictionaries.
    """
    path = f"forex"
    return __quotes(apikey=API_KEY, value=path)


def available_forex() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /symbol/available-forex-currency-pairs/ API

    :return: A list of dictionaries.
    """
    path = f"symbol/available-forex-currency-pairs"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def fx_price_quote(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /fx/{symbol} API for the latest bid and ask prices of a currency pair.

    :param symbol: Currency pair symbol (e.g., 'EURUSD')
    :return: A list containing a dictionary with bid and ask prices.
    """
    path = f"fx/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)