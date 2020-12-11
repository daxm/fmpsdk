import typing
from .url_methods import __return_json, __validate_time_delta, __validate_series_type


def __quote(
    apikey: str, value: typing.Union[str, typing.List[str]]
) -> typing.List[typing.Dict]:
    """
    Query FMP Quote API.

    This API endpoint is a multifunction tool!

    :param apikey: Your API key
    :param value: The Ticker(s), Index(es), Commodity(ies), etc. symbol to query for.
    :return: A list of dictionaries.
    """
    if type(value) is list:
        value = ",".join(value)
    path = f"quote/{value}"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def __quotes(apikey: str, value: str) -> typing.List[typing.Dict]:
    """
    Query FMP /quotes/ API.

    This API endpoint is a multifunction tool!
    :param apikey: Your API key
    :param value: The Ticker(s), Index(es), Commodity(ies), etc. symbol to query for.
    :return: A list of dictionaries.
    """
    path = f"quotes/{value}"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def __historical_chart(
    apikey: str, value: str, time_delta: str
) -> typing.List[typing.Dict]:
    """
    Query FMP Historical Chart API.

    This API endpoint is a multifunction tool!

    :param apikey: Your API key
    :param value: The Ticker, Index, Commodity, etc. symbol to query for.
    :param time_delta: The string value of time from now to go historical "1min" - "4hour".
    :return: A list of dictionaries.
    """
    path = f"historical-chart/{__validate_time_delta(time_delta)}/{value}"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def __historical_price_full(
    apikey: str,
    value: typing.Union[str, typing.List],
    time_series: int = None,
    series_type: str = None,
    from_date: str = None,
    to_date: str = None,
) -> typing.List[typing.Dict]:
    """
    Query FMP Historical Price Full API.

    This API endpoint is a multifunction tool!

    :param apikey: Your API Key
    :param value: The Ticker, Index, Commodity, etc. symbol to query for.
    :param time_series: Not sure what this is.  5 is the only value I've seen used.
    :param series_type: Not sure what this is.  "line" is the only option I've seen used.
    :param from_date: 'YYYY-MM-DD' format
    :param to_date: 'YYYY-MM-DD' format
    :return: A list of dictionaries.
    """
    if type(value) is list:
        value = ",".join(value)
    path = f"historical-price-full/{value}"
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
    return __return_json(path=path, query_vars=query_vars)
