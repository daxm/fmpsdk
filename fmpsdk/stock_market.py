import typing

from .settings import DEFAULT_LIMIT
from .url_methods import __return_json_v3


def actives(apikey: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /actives/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"actives"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def gainers(apikey: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /gainers/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"gainers"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def losers(apikey: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /losers/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"losers"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def market_hours(apikey: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /market-hours/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"market-hours"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def sectors_performance(
    apikey: str, limit: int = DEFAULT_LIMIT
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /sectors_performance/ API

    :param apikey: Your API key.
    :param limit: Number of rows to return
    :return: A list of dictionaries.
    """
    path = f"sectors-performance"
    query_vars = {"apikey": apikey, "limit": limit}
    return __return_json_v3(path=path, query_vars=query_vars)
