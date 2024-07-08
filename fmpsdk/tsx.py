import typing
import os

from .general import __quotes
from .url_methods import __return_json_v3

API_KEY = os.getenv('FMP_API_KEY')

def available_tsx() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /symbol/available-tsx/ API

    :return: A list of dictionaries.
    """
    path = f"symbol/available-tsx"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def tsx_list() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /quotes/tsx/ API

    :return: A list of dictionaries.
    """
    path = f"tsx"
    return __quotes(apikey=API_KEY, value=path)