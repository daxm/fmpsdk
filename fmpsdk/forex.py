import typing
import os

from .general import __quotes
from .url_methods import __return_json_v3

API_KEY = os.getenv('FMP_API_KEY')

def forex() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /fx API

    Get real-time forex prices for all currency pairs.

    :return: A list of dictionaries containing forex prices.
    :example: forex()
    :endpoint: https://financialmodelingprep.com/api/v3/fx
    """
    path = "fx"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def forex_list() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /quotes/forex API

    Get a list of all quotes for all currency pairs traded on the forex market.

    :return: A list of dictionaries containing full forex quotes.
    :example: forex_list()
    :endpoint: https://financialmodelingprep.com/api/v3/quotes/forex
    """
    path = "quotes/forex"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def available_forex() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /symbol/available-forex-currency-pairs API

    Get a list of all currency pairs that are traded on the forex market.

    :return: A list of dictionaries containing available forex currency pairs.
    :example: available_forex()
    :endpoint: https://financialmodelingprep.com/api/v3/symbol/available-forex-currency-pairs
    """
    path = "symbol/available-forex-currency-pairs"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def forex_quote(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /quote/{symbol} API for a full quote of a specific currency pair.

    Get a full quote for a specific currency pair, including current exchange rate,
    daily high, low, open rates, spread, and trading volume for the day.

    :param symbol: Currency pair symbol (e.g., 'EURUSD')
    :return: A list containing a dictionary with full quote information.
    :example: forex_quote('EURUSD')
    :endpoint: https://financialmodelingprep.com/api/v3/quote/EURUSD
    """
    path = f"quote/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def forex_historical(symbol: str, from_date: str, to_date: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical-price-full/{symbol} API for historical forex data.

    Get daily price data for a specific currency pair within a date range.

    :param symbol: Currency pair symbol (e.g., 'EURUSD')
    :param from_date: Start date in 'YYYY-MM-DD' format
    :param to_date: End date in 'YYYY-MM-DD' format
    :return: A list of dictionaries containing historical forex data.
    :example: forex_historical('EURUSD', '2023-01-01', '2023-12-31')
    :endpoint: https://financialmodelingprep.com/api/v3/historical-price-full/EURUSD
    """
    path = f"historical-price-full/{symbol}"
    query_vars = {"apikey": API_KEY, "from": from_date, "to": to_date}
    return __return_json_v3(path=path, query_vars=query_vars)