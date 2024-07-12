import typing
import os

from .general import __quotes
from .url_methods import __return_json_v3, __return_json_v4

API_KEY = os.getenv('FMP_API_KEY')

def quote_short(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /quote-short/ API.

    :param symbol: Company ticker.
    :return: A list of dictionaries containing short quote data.
    :example: quote_short('AAPL')
    :endpoint: https://financialmodelingprep.com/api/v3/quote-short/{symbol}
    """
    path = f"quote-short/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def exchange_realtime(exchange: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /quotes/ API.

    :param exchange: Exchange symbol.
    :return: A list of dictionaries containing real-time quotes for the exchange.
    :example: exchange_realtime('NASDAQ')
    :endpoint: https://financialmodelingprep.com/api/v3/quotes/{exchange}
    """
    return __quotes(value=exchange)

def historical_stock_dividend(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical-price-full/stock_dividend/ API.

    :param symbol: Company ticker.
    :return: A list of dictionaries containing historical stock dividend data.
    :example: historical_stock_dividend('AAPL')
    :endpoint: https://financialmodelingprep.com/api/v3/historical-price-full/stock_dividend/{symbol}
    """
    path = f"historical-price-full/stock_dividend/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def historical_stock_split(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical-price-full/stock_split/ API.

    :param symbol: Company ticker.
    :return: A list of dictionaries containing historical stock split data.
    :example: historical_stock_split('AAPL')
    :endpoint: https://financialmodelingprep.com/api/v3/historical-price-full/stock_split/{symbol}
    """
    path = f"historical-price-full/stock_split/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def historical_survivorship_bias_free_eod(symbol: str, date: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical-price-full/<ticker>/<date> API.

    :param symbol: Company ticker.
    :param date: str YYYY-MM-DD
    :return: A list of dictionaries containing historical stock data.
    :example: historical_survivorship_bias_free_eod('AAPL', '2023-01-01')
    :endpoint: https://financialmodelingprep.com/api/v3/historical-price-full/{symbol}/{date}
    """
    path = f"historical-price-full/{symbol}/{date}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v4(path=path, query_vars=query_vars)