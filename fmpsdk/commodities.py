import typing
import os
from .general import __quotes
from .url_methods import __return_json_v3

API_KEY = os.getenv('FMP_API_KEY')

def available_commodities() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /symbol/available-commodities/ API

    :return: A list of dictionaries.
    """
    path = f"symbol/available-commodities"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def commodities_list() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /quotes/commodity/ API

    :return: A list of dictionaries.
    """
    path = f"commodity"
    return __quotes(apikey=API_KEY, value=path)