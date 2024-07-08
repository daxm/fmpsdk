import typing
import os

from .general import __quotes
from .url_methods import __return_json_v3, __return_json_v4

API_KEY = os.getenv('FMP_API_KEY')

def available_efts(apikey: str = None):
    """
    Trying to avoid a breaking change.
    This method is misspelled so moving to a correct spelling method and deprecating this one.
    Use available_etfs() instead.
    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return:
    """
    print(
        "WARNING!  This is a deprecated method.  Use available_etfs() instead.  This will go away 20240101."
    )
    available_etfs(apikey=apikey)


def available_etfs(apikey: str = None) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /symbol/available-etfs/ API

    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    path = f"symbol/available-etfs"
    query_vars = {"apikey": apikey} if apikey else {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def etf_price_realtime(apikey: str = None) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /quotes/etf/ API

    All Real-time ETF Prices.

    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    path = f"etf"
    return __quotes(apikey=apikey, value=path)


def etf_info(symbol: str, apikey: str = None) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /etf-info/ API

    All Real-time ETF Prices.

    :param symbol: ETF ticker.
    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    path = f"etf-info"
    query_vars = {"symbol": symbol, "apikey": apikey} if apikey else {"symbol": symbol, "apikey": API_KEY}
    return __return_json_v4(path=path, query_vars=query_vars)