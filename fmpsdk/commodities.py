import typing
import os
from .url_methods import __return_json_v3

API_KEY = os.getenv('FMP_API_KEY')

def available_commodities() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /symbol/available-commodities API

    :return: A list of dictionaries containing available commodities.
    :example: available_commodities()
    :endpoint: https://financialmodelingprep.com/api/v3/symbol/available-commodities
    """
    path = "symbol/available-commodities"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def commodities_list() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /quotes/commodity API

    :return: A list of dictionaries containing full quotes for all commodities.
    :example: commodities_list()
    :endpoint: https://financialmodelingprep.com/api/v3/quotes/commodity
    """
    path = "quotes/commodity"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def commodity_price(symbol: str, from_date: str = None, to_date: str = None) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical-price-full/{symbol} API for commodity price data

    :param symbol: The symbol of the commodity (e.g., 'ZGUSD')
    :param from_date: Start date in 'YYYY-MM-DD' format (optional)
    :param to_date: End date in 'YYYY-MM-DD' format (optional)
    :return: A list of dictionaries containing historical price data for the specified commodity.
    :example: commodity_price('ZGUSD', from_date='2023-01-01', to_date='2023-12-31')
    :endpoint: https://financialmodelingprep.com/api/v3/historical-price-full/{symbol}
    """
    path = f"historical-price-full/{symbol}"
    query_vars = {"apikey": API_KEY}
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    return __return_json_v3(path=path, query_vars=query_vars)