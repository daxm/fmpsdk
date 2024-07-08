import typing
import os
from .settings import DEFAULT_LIMIT
from .url_methods import __return_json_v3

API_KEY = os.getenv('FMP_API_KEY')

def earning_calendar(
    from_date: str = None, to_date: str = None, apikey: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /earning_calendar/ API.

    Note: Between the "from" and "to" parameters the maximum time interval can be 3 months.
    :param from_date: 'YYYY:MM:DD'
    :param to_date: 'YYYY:MM:DD'
    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    path = f"earning_calendar"
    query_vars = {"apikey": apikey} if apikey else {"apikey": API_KEY}
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    return __return_json_v3(path=path, query_vars=query_vars)


def historical_earning_calendar(
    symbol: str, limit: int = DEFAULT_LIMIT, apikey: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical/earning_calendar/ API.

    Note: Between the "from" and "to" parameters the maximum time interval can be 3 months.
    :param symbol: Company ticker.
    :param limit: Number of rows to return.
    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    path = f"historical/earning_calendar/{symbol}"
    query_vars = {"apikey": apikey} if apikey else {"apikey": API_KEY}
    query_vars["symbol"] = symbol
    query_vars["limit"] = limit
    return __return_json_v3(path=path, query_vars=query_vars)


def ipo_calendar(
    from_date: str = None, to_date: str = None, apikey: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /ipo_calendar/ API.

    Note: Between the "from" and "to" parameters the maximum time interval can be 3 months.
    :param from_date: 'YYYY:MM:DD'
    :param to_date: 'YYYY:MM:DD'
    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    path = f"ipo_calendar"
    query_vars = {"apikey": apikey} if apikey else {"apikey": API_KEY}
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    return __return_json_v3(path=path, query_vars=query_vars)


def stock_split_calendar(
    from_date: str = None, to_date: str = None, apikey: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /stock_split_calendar/ API.

    Note: Between the "from" and "to" parameters the maximum time interval can be 3 months.
    :param from_date: 'YYYY:MM:DD'
    :param to_date: 'YYYY:MM:DD'
    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    path = f"stock_split_calendar"
    query_vars = {"apikey": apikey} if apikey else {"apikey": API_KEY}
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    return __return_json_v3(path=path, query_vars=query_vars)


def dividend_calendar(
    from_date: str = None, to_date: str = None, apikey: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /stock_dividend_calendar/ API.

    Note: Between the "from" and "to" parameters the maximum time interval can be 3 months.
    :param from_date: 'YYYY:MM:DD'
    :param to_date: 'YYYY:MM:DD'
    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    path = f"stock_dividend_calendar"
    query_vars = {"apikey": apikey} if apikey else {"apikey": API_KEY}
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    return __return_json_v3(path=path, query_vars=query_vars)


def economic_calendar(
    from_date: str = None, to_date: str = None, apikey: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /economic_calendar/ API.

    Note: Between the "from" and "to" parameters the maximum time interval can be 3 months.
    :param from_date: 'YYYY:MM:DD'
    :param to_date: 'YYYY:MM:DD'
    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    path = f"economic_calendar"
    query_vars = {"apikey": apikey} if apikey else {"apikey": API_KEY}
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    return __return_json_v3(path=path, query_vars=query_vars)