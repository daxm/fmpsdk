import typing
import os

from .general import __quotes
from .url_methods import __return_json_v3

API_KEY = os.getenv('FMP_API_KEY')

def available_cryptocurrencies(apikey: str = None) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /symbol/available-cryptocurrencies/ API

    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    path = f"symbol/available-cryptocurrencies"
    query_vars = {"apikey": apikey} if apikey else {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def cryptocurrencies_list(apikey: str = None) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /quotes/crypto/ API

    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    path = f"crypto"
    return __quotes(apikey=apikey, value=path)