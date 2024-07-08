import typing
import os

from .general import __quotes
from .url_methods import __return_json_v3

API_KEY = os.getenv('FMP_API_KEY')

def available_cryptocurrencies() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /symbol/available-cryptocurrencies/ API

    :return: A list of dictionaries.
    """
    path = f"symbol/available-cryptocurrencies"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def cryptocurrencies_list() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /quotes/crypto/ API

    :return: A list of dictionaries.
    """
    path = f"crypto"
    return __quotes(apikey=API_KEY, value=path)