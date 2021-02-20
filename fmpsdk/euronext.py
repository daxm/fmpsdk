from .general import __quotes
from .url_methods import __return_json_v3

import typing


def available_euronext(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /symbol/available-euronext/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"symbol/available-euronext"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def euronext_list(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /quotes/euronext/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"euronext"
    return __quotes(apikey=apikey, value=path)
