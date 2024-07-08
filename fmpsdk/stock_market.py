import typing
import os
from .settings import DEFAULT_LIMIT
from .url_methods import __return_json_v3

API_KEY = os.getenv('FMP_API_KEY')

def actives() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /actives/ API

    :return: A list of dictionaries.
    """
    path = f"actives"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def gainers() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /gainers/ API

    :return: A list of dictionaries.
    """
    path = f"gainers"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def losers() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /losers/ API

    :return: A list of dictionaries.
    """
    path = f"losers"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def market_hours() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /market-hours/ API

    :return: A list of dictionaries.
    """
    path = f"market-hours"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def sectors_performance(
    limit: int = DEFAULT_LIMIT
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /sectors_performance/ API

    :param limit: Number of rows to return
    :return: A list of dictionaries.
    """
    path = f"sectors-performance"
    query_vars = {"apikey": API_KEY, "limit": limit}
    return __return_json_v3(path=path, query_vars=query_vars)