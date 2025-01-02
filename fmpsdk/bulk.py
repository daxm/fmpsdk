import logging
import typing

import requests

from .general import __quotes
from .settings import DEFAULT_LIMIT, BASE_URL_v3, BASE_URL_v4
from .url_methods import __return_json_v3, __return_json_v4


def bulk_historical_eod(
    apikey: str, date: str
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Batch request that contains all end of day prices for specific date

    https://site.financialmodelingprep.com/developer/docs#batch-eod-prices

    Endpoint:
        https://financialmodelingprep.com/api/v4/batch-historical-eod?date=2021-05-18

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"batch-historical-eod"
    query_vars = {"apikey": apikey, "date": date}
    return __return_json_v4(path=path, query_vars=query_vars)


def bulk_profiles(apikey: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    It contains all profiles from our API in one CSV file

    Endpoint:
        https://financialmodelingprep.com/api/v4/profile/all

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"profile/all"
    query_vars = {"apikey": apikey}
    return __return_json_v4(path=path, query_vars=query_vars)
