import typing

from .general import __quotes
from .url_methods import __return_json_v3


def available_efts(apikey: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /symbol/available-etfs/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"symbol/available-etfs"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def etf_price_realtime(apikey: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /quotes/etf/ API

    All Real-time ETF Prices.

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"etf"
    return __quotes(apikey=apikey, value=path)
