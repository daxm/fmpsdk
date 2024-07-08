import typing
import os

from .settings import DEFAULT_LINE_PARAMETER
from .url_methods import __return_json_v3, __validate_series_type, __validate_time_delta

API_KEY = os.getenv('FMP_API_KEY')

def __quotes(value: str, apikey: str = None) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /quotes/ API.

    This API endpoint is a multifunction tool!
    :param value: The Ticker(s), Index(es), Commodity(ies), etc. symbol to query for.
    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    path = f"quotes/{value}"
    query_vars = {"apikey": apikey} if apikey else {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def quote(
    symbol: typing.Union[str, typing.List[str]],
    apikey: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP Quote API.

    This API endpoint is a multifunction tool!

    :param symbol: The Ticker(s), Index(es), Commodity(ies), etc. symbol to query for.
    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    if type(symbol) is list:
        symbol = ",".join(symbol)
    path = f"quote/{symbol}"
    query_vars = {"apikey": apikey} if apikey else {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def historical_chart(
    symbol: str,
    time_delta: str,
    from_date: str,
    to_date: str,
    time_series: str = DEFAULT_LINE_PARAMETER,
    apikey: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP Historical Chart API.

    This API endpoint is a multifunction tool!

    :param symbol: The Ticker, Index, Commodity, etc. symbol to query for.
    :param time_delta: The string value of time from now to go historical "1min" - "4hour".
    :param from_date: The starting time for the API ("yyyy-mm-dd")
    :param to_date: The starting time for the API ("yyyy-mm-dd")
    :param time_series: line as default
    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.

    :return: A list of dictionaries.
    """
    path = f"historical-chart/{__validate_time_delta(time_delta)}/{symbol}"
    query_vars = {"apikey": apikey} if apikey else {"apikey": API_KEY}
    if time_series:
        query_vars["timeseries"] = time_series
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    return __return_json_v3(path=path, query_vars=query_vars)


def historical_price_full(
    symbol: typing.Union[str, typing.List],
    from_date: str = None,
    to_date: str = None,
    apikey: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP Historical Price Full API.

    This API endpoint is a multifunction tool!

    :param symbol: The Ticker, Index, Commodity, etc. symbol to query for.
    :param from_date: 'YYYY-MM-DD' format
    :param to_date: 'YYYY-MM-DD' format
    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    if type(symbol) is list:
        symbol = ",".join(symbol)
    path = f"historical-price-full/{symbol}"
    query_vars = {"apikey": apikey} if apikey else {"apikey": API_KEY}

    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date

    res = __return_json_v3(path=path, query_vars=query_vars)

    if res:
        return res.get("historicalStockList", res.get("historical", None))
    else:
        return res