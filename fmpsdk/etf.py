import typing
import os

from .general import __quotes
from .url_methods import __return_json_v3, __return_json_v4

API_KEY = os.getenv('FMP_API_KEY')

def available_etfs() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /symbol/available-etfs/ API.

    :return: A list of dictionaries containing available ETFs.
    :example: available_etfs()
    :endpoint: https://financialmodelingprep.com/api/v3/symbol/available-etfs
    """
    path = f"symbol/available-etfs"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def etf_info(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /etf-info/ API.

    :param symbol: ETF ticker.
    :return: A list of dictionaries containing ETF information.
    :example: etf_info('SPY')
    :endpoint: https://financialmodelingprep.com/api/v4/etf-info?symbol={symbol}
    """
    path = f"etf-info"
    query_vars = {"symbol": symbol, "apikey": API_KEY}
    return __return_json_v4(path=path, query_vars=query_vars)