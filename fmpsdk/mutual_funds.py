import typing

from .general import __quotes
from .url_methods import __return_json_v3


def available_mutual_funds(apikey: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /symbol/available-mutual-funds/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"symbol/available-mutual-funds"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def mutual_fund_list(apikey: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /quotes/mutual_fund/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"mutual_fund"
    return __quotes(apikey=apikey, value=path)
