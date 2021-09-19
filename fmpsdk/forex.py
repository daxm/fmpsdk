import typing

from .general import __quotes
from .url_methods import __return_json_v3


def forex(apikey: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /fx/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"fx"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def forex_list(apikey: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /quotes/forex/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"forex"
    return __quotes(apikey=apikey, value=path)


def available_forex(apikey: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /symbol/available-forex-currency-pairs/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"symbol/available-forex-currency-pairs"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)
