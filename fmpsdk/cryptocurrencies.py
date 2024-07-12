import typing
import os

from .general import __quotes
from .url_methods import __return_json_v3

API_KEY = os.getenv('FMP_API_KEY')

def available_cryptocurrencies() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /symbol/available-cryptocurrencies API

    :return: A list of dictionaries containing available cryptocurrencies.
    :example: available_cryptocurrencies()
    :endpoint: https://financialmodelingprep.com/api/v3/symbol/available-cryptocurrencies
    """
    path = "symbol/available-cryptocurrencies"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def cryptocurrencies_list() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /quotes/crypto API

    :return: A list of dictionaries containing full quotes for all cryptocurrencies.
    :example: cryptocurrencies_list()
    :endpoint: https://financialmodelingprep.com/api/v3/quotes/crypto
    """
    path = "quotes/crypto"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def cryptocurrency_quote(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /quote/{symbol} API for cryptocurrency quote

    :param symbol: The symbol of the cryptocurrency (e.g., 'BTCUSD')
    :return: A list containing a dictionary with the full quote for the specified cryptocurrency.
    :example: cryptocurrency_quote('BTCUSD')
    :endpoint: https://financialmodelingprep.com/api/v3/quote/BTCUSD
    """
    path = f"quote/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)