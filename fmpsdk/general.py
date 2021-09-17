import typing

from .url_methods import __return_json_v3, __validate_series_type, __validate_time_delta


def __quotes(apikey: str, value: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /quotes/ API.

    This API endpoint is a multifunction tool!
    :param apikey: Your API key
    :param value: The Ticker(s), Index(es), Commodity(ies), etc. symbol to query for.
    :return: A list of dictionaries.
    """
    path = f"quotes/{value}"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def quote(
    apikey: str, symbol: typing.Union[str, typing.List[str]]
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP Quote API.

    This API endpoint is a multifunction tool!

    :param apikey: Your API key
    :param symbol: The Ticker(s), Index(es), Commodity(ies), etc. symbol to query for.
    :return: A list of dictionaries.
    """
    if type(symbol) is list:
        symbol = ",".join(symbol)
    path = f"quote/{symbol}"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def historical_chart(
    apikey: str, symbol: str, time_delta: str
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP Historical Chart API.

    This API endpoint is a multifunction tool!

    :param apikey: Your API key
    :param symbol: The Ticker, Index, Commodity, etc. symbol to query for.
    :param time_delta: The string value of time from now to go historical "1min" - "4hour".
    :return: A list of dictionaries.
    """
    path = f"historical-chart/{__validate_time_delta(time_delta)}/{symbol}"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def historical_price_full(
    apikey: str,
    symbol: typing.Union[str, typing.List],
    time_series: int = None,
    series_type: str = None,
    from_date: str = None,
    to_date: str = None,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP Historical Price Full API.

    This API endpoint is a multifunction tool!

    :param apikey: Your API Key
    :param symbol: The Ticker, Index, Commodity, etc. symbol to query for.
    :param time_series: Not sure what this is.  5 is the only value I've seen used.
    :param series_type: Not sure what this is.  "line" is the only option I've seen used.
    :param from_date: 'YYYY-MM-DD' format
    :param to_date: 'YYYY-MM-DD' format
    :return: A list of dictionaries.
    """
    if type(symbol) is list:
        symbol = ",".join(symbol)
    path = f"historical-price-full/{symbol}"
    query_vars = {
        "apikey": apikey,
    }
    if time_series:
        query_vars["timeseries"] = time_series
    if series_type:
        query_vars["serietype"] = __validate_series_type(series_type)
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date

    res = __return_json_v3(path=path, query_vars=query_vars)
    if res is None or len(res) == 0:
        return res
    return res["historical"]
