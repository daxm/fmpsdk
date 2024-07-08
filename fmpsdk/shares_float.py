"""
   https://site.financialmodelingprep.com/developer/docs#share-float
"""

import typing
import os
from .url_methods import __return_json_v4

API_KEY = os.getenv('FMP_API_KEY')

def shares_float(
    symbol: str, all: bool = False, apikey: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /shares_float/ API.

    Provides the total number of shares that are publicly traded for a given company.
    :param symbol: Ticker of Company.
    :param all: Optional boolean attribute. If True, changes the API url to the "all" endpoint.
    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    if all:
        path = "shares_float/all"
    else:
        path = f"shares_float?symbol={symbol}"
    query_vars = {"apikey": apikey} if apikey else {"apikey": API_KEY}
    return __return_json_v4(path=path, query_vars=query_vars)