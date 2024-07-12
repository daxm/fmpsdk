import typing

import os
from .general import __quotes
from .url_methods import __return_json_v3

API_KEY = os.getenv('FMP_API_KEY')

def available_euronext() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /symbol/available-euronext API

    Get a list of available Euronext stocks.

    :return: A list of dictionaries containing available Euronext stocks.
    :example: available_euronext()
    :endpoint: https://financialmodelingprep.com/api/v3/symbol/available-euronext
    """
    path = "symbol/available-euronext"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)