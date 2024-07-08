import typing
import os

from .general import __quotes
from .url_methods import __return_json_v3

API_KEY = os.getenv('FMP_API_KEY')

def available_mutual_funds() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /symbol/available-mutual-funds/ API

    :return: A list of dictionaries.
    """
    path = f"symbol/available-mutual-funds"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def mutual_fund_list() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /quotes/mutual_fund/ API

    :return: A list of dictionaries.
    """
    path = f"mutual_fund"
    return __quotes(apikey=API_KEY, value=path)