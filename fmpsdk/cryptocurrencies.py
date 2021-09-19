import typing

from .general import __quotes
from .url_methods import __return_json_v3


def available_cryptocurrencies(
    apikey: str,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /symbol/available-cryptocurrencies/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"symbol/available-cryptocurrencies"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def cryptocurrencies_list(apikey: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /quotes/crypto/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"crypto"
    return __quotes(apikey=apikey, value=path)
