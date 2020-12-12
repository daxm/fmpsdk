from .url_methods import __return_json
from .general_methods import __quotes
import typing


def available_efts(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /symbol/available-etfs/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"/symbol/available-etfs"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def etf_list(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /quotes/etf/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"quotes/etf"
    return __quotes(apikey=apikey, value=path)
