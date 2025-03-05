import typing
import logging

from .general import __quotes
from .url_methods import __return_json_v3, __return_json_v4


def quote_short(apikey: str, symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /quote-short/ API.

    :param apikey: Your API key
    :param symbol: Company ticker.
    :return: A list of dictionaries.
    """
    path = f"quote-short/{symbol}"
    query_vars = {
        "apikey": apikey,
    }
    return __return_json_v3(path=path, query_vars=query_vars)


def exchange_realtime(
    apikey: str, exchange: str
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /quotes/ API.

    :param apikey: Your API key
    :param exchange: Exchange symbol.
    :return: A list of dictionaries.
    """
    return __quotes(apikey=apikey, value=exchange)


def historical_stock_dividend(
    apikey: str, symbol: str
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical-price-full/stock_divident/ API

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :return: A list of dictionaries.
    """
    path = f"historical-price-full/stock_dividend/{symbol}"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def historical_stock_split(
    apikey: str, symbol: str
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical-price-full/stock_divident/ API

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :return: A list of dictionaries.
    """
    path = f"historical-price-full/stock_split/{symbol}"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def historical_survivorship_bias_free_eod(
    apikey: str, symbol: str, date: str
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical-price-full/<ticker>/<date> API

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :param date: str YYYY-MM-DD
    :return: A list of dictionaries.
    """
    path = f"historical-price-full/{symbol}/{date}"
    query_vars = {"apikey": apikey}
    return __return_json_v4(path=path, query_vars=query_vars)


def live_full_price(apikey: str, symbol: str) -> typing.Optional[typing.Dict]:
    """
    Query FMP /live-full-price/ API.

    Get real-time bid/ask prices, volume, and last trade price for a stock.

    https://site.financialmodelingprep.com/developer/docs#live-full-price

    Endpoint:
        https://financialmodelingprep.com/api/v3/live-full-price/{symbol}

    :param apikey: Your API key.
    :param symbol: Company ticker symbol.
    :return: A dictionary containing real-time price data with fields:
             - symbol: The stock symbol
             - ask: The current ask price
             - askSize: The size of the ask order
             - bid: The current bid price
             - bidSize: The size of the bid order
             - price: The last trade price
             - volume: The trading volume
             - timestamp: The timestamp of the data
    """
    if not symbol:
        logging.warning("No symbol provided for live full price request.")
        return None
    
    path = f"live-full-price/{symbol}"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def full_real_time_price(apikey: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /stock/full/real-time-price API.

    Get real-time bid/ask prices, volume, and last trade price for all stocks.

    https://site.financialmodelingprep.com/developer/docs#all-live-full-price

    Endpoint:
        https://financialmodelingprep.com/api/v3/stock/full/real-time-price

    :param apikey: Your API key.
    :return: A list of dictionaries containing real-time price data for all stocks, each with fields:
             - symbol: The stock symbol
             - ask: The current ask price
             - askSize: The size of the ask order
             - bid: The current bid price
             - bidSize: The size of the bid order
             - price: The last trade price
             - volume: The trading volume
             - timestamp: The timestamp of the data
    """
    path = "stock/full/real-time-price"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)
