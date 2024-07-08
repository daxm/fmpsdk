import typing
import os
from .settings import DEFAULT_LIMIT
from .url_methods import __return_json_v3

API_KEY = os.getenv('FMP_API_KEY')

def actives(apikey: str = None) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /actives/ API

    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    path = f"actives"
    query_vars = {"apikey": apikey} if apikey else {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def gainers(apikey: str = None) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /gainers/ API

    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    path = f"gainers"
    query_vars = {"apikey": apikey} if apikey else {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def losers(apikey: str = None) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /losers/ API

    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    path = f"losers"
    query_vars = {"apikey": apikey} if apikey else {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def market_hours(apikey: str = None) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /market-hours/ API

    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    path = f"market-hours"
    query_vars = {"apikey": apikey} if apikey else {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def sectors_performance(
    apikey: str = None,
    limit: int = DEFAULT_LIMIT
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /sectors_performance/ API

    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :param limit: Number of rows to return
    :return: A list of dictionaries.
    """
    path = f"sectors-performance"
    query_vars = {"apikey": apikey, "limit": limit} if apikey else {"apikey": API_KEY, "limit": limit}
    return __return_json_v3(path=path, query_vars=query_vars)