import typing

from .general import __quotes
from .url_methods import __return_json_v3


def available_tsx(apikey: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /symbol/available-tsx/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"symbol/available-tsx"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def tsx_list(apikey: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /quotes/tsx/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"tsx"
    return __quotes(apikey=apikey, value=path)
