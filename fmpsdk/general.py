import typing
import os

from .settings import DEFAULT_LINE_PARAMETER
from .url_methods import __return_json_v3, __return_json_v4, __validate_series_type, __validate_time_delta

API_KEY = os.getenv('FMP_API_KEY')

def __quotes(value: str) -> typing.Optional[typing.List[typing.Dict]]: 
    """
    Query FMP /quotes/ API.

    :param value: The Ticker(s), Index(es), Commodity(ies), etc. symbol to query for.
    :return: A list of dictionaries containing quote data.
    :example: __quotes('AAPL')
    :endpoint: https://financialmodelingprep.com/api/v3/quotes/{value}
    """
    path = f"quotes/{value}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def quote(symbol: typing.Union[str, typing.List[str]]) -> typing.Optional[typing.List[typing.Dict]]: 
    """
    Query FMP Quote API.

    :param symbol: The Ticker(s), Index(es), Commodity(ies), etc. symbol to query for. Can be a single symbol or a list of symbols.
    :return: A list of dictionaries containing quote data.
    :example: quote('AAPL')
    :example: quote(['AAPL', 'GOOGL'])
    :endpoint: https://financialmodelingprep.com/api/v3/quote/{symbol}
    """
    if type(symbol) is list:
        symbol = ",".join(symbol)
    path = f"quote/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def historical_chart(symbol: str, time_delta: str, from_date: str, to_date: str, time_series: str = DEFAULT_LINE_PARAMETER) -> typing.Optional[typing.List[typing.Dict]]: 
    """
    Query FMP Historical Chart API.

    :param symbol: The Ticker, Index, Commodity, etc. symbol to query for (e.g., 'AAPL').
    :param time_delta: The string value of time from now to go historical (e.g., '1min', '5min', '15min', '30min', '1hour', '4hour').
    :param from_date: The starting date for the API query in 'yyyy-mm-dd' format.
    :param to_date: The ending date for the API query in 'yyyy-mm-dd' format.
    :param time_series: The time series parameter, default is 'line'.
    :return: A list of dictionaries containing historical stock data or None if the request fails.
    :example: historical_chart('AAPL', '5min', '2023-08-10', '2023-09-10')
    :endpoint: https://financialmodelingprep.com/api/v3/historical-chart/{time_delta}/{symbol}
    """
    path = f"historical-chart/{__validate_time_delta(time_delta)}/{symbol}"
    query_vars = {"apikey": API_KEY}
    if time_series:
        query_vars["timeseries"] = time_series
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    return __return_json_v3(path=path, query_vars=query_vars)


def historical_price_full(symbol: typing.Union[str, typing.List], from_date: str = None, to_date: str = None) -> typing.Optional[typing.List[typing.Dict]]: 
    """
    Query FMP Historical Price Full API.

    :param symbol: The Ticker, Index, Commodity, etc. symbol to query for. Can be a single symbol or a list of symbols (e.g., 'AAPL' or ['AAPL', 'GOOGL']).
    :param from_date: The starting date for the API query in 'yyyy-mm-dd' format (e.g., '2020-01-01').
    :param to_date: The ending date for the API query in 'yyyy-mm-dd' format (e.g., '2023-01-01').
    :return: A list of dictionaries containing historical stock data or None if the request fails.
    :example: historical_price_full('AAPL', '2020-01-01', '2023-01-01')
    :endpoint: https://financialmodelingprep.com/api/v3/historical-price-full/{symbol}
    """
    if type(symbol) is list:
        symbol = ",".join(symbol)
    path = f"historical-price-full/{symbol}"
    query_vars = {"apikey": API_KEY}
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date

    res = __return_json_v3(path=path, query_vars=query_vars)
    if res:
        return res.get("historicalStockList", res.get("historical", None))
    else:
        return res