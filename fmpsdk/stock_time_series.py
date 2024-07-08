import typing
import os

from .general import __quotes
from .url_methods import __return_json_v3, __return_json_v4

API_KEY = os.getenv('FMP_API_KEY')

def quote_short(symbol: str, apikey: str = None) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /quote-short/ API.

    :param symbol: Company ticker.
    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    path = f"quote-short/{symbol}"
    query_vars = {"apikey": apikey} if apikey else {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def exchange_realtime(
    exchange: str, apikey: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /quotes/ API.

    :param exchange: Exchange symbol.
    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    return __quotes(apikey=apikey, value=exchange)


def historical_stock_dividend(
    symbol: str, apikey: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical-price-full/stock_divident/ API

    :param symbol: Company ticker.
    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    path = f"historical-price-full/stock_dividend/{symbol}"
    query_vars = {"apikey": apikey} if apikey else {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def historical_stock_split(
    symbol: str, apikey: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical-price-full/stock_divident/ API

    :param symbol: Company ticker.
    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    path = f"historical-price-full/stock_split/{symbol}"
    query_vars = {"apikey": apikey} if apikey else {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def historical_survivorship_bias_free_eod(
    symbol: str, date: str, apikey: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical-price-full/<ticker>/<date> API

    :param symbol: Company ticker.
    :param date: str YYYY-MM-DD
    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    path = f"historical-price-full/{symbol}/{date}"
    query_vars = {"apikey": apikey} if apikey else {"apikey": API_KEY}
    return __return_json_v4(path=path, query_vars=query_vars)