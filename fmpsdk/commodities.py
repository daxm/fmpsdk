import typing

from .general import __quotes
from .url_methods import __return_json_v3


def available_commodities(apikey: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /symbol/available-commodities/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"symbol/available-commodities"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def commodities_list(apikey: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /quotes/commodity/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"commodity"
    return __quotes(apikey=apikey, value=path)
