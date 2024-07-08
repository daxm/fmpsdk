import logging
import typing
import os

import requests

from .general import __quotes
from .settings import (
    DOWJONES_CONSTITUENTS_FILENAME,
    NASDAQ_CONSTITUENTS_FILENAME,
    SP500_CONSTITUENTS_FILENAME,
    BASE_URL_v3,
)
from .url_methods import __return_json_v3

API_KEY = os.getenv('FMP_API_KEY')

def indexes(apikey: str = None) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /quotes/index/ API.

    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    path = f"index"
    query_vars = {"apikey": apikey} if apikey else {"apikey": API_KEY}
    return __quotes(apikey=query_vars, value=path)


def sp500_constituent(
    download: bool = False,
    filename: str = SP500_CONSTITUENTS_FILENAME,
    apikey: str = None,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP /sp500_constituent/ API

    :param download: True/False
    :param filename: Name of saved file.
    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    path = f"sp500_constituent"
    query_vars = {"apikey": apikey} if apikey else {"apikey": API_KEY}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving SP500 Constituents as {filename}.")
    else:
        return __return_json_v3(path=path, query_vars=query_vars)


def historical_sp500_constituent(apikey: str = None) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical/sp500_constitnuet/ API.

    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    path = f"historical/sp500_constituent"
    query_vars = {"apikey": apikey} if apikey else {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def nasdaq_constituent(
    download: bool = False,
    filename: str = NASDAQ_CONSTITUENTS_FILENAME,
    apikey: str = None,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP /nasdaq_constituent/ API

    :param download: True/False
    :param filename: Name of saved file.
    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    path = f"nasdaq_constituent"
    query_vars = {"apikey": apikey} if apikey else {"apikey": API_KEY}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving NASDAQ Constituents as {filename}.")
    else:
        return __return_json_v3(path=path, query_vars=query_vars)


def historical_nasdaq_constituent(apikey: str = None) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical/nasdaq_constitnuet/ API.

    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    path = f"historical/nasdaq_constituent"
    query_vars = {"apikey": apikey} if apikey else {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def dowjones_constituent(
    download: bool = False,
    filename: str = DOWJONES_CONSTITUENTS_FILENAME,
    apikey: str = None,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP /dowjones_constituent/ API

    :param download: True/False
    :param filename: Name of saved file.
    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    path = f"dowjones_constituent"
    query_vars = {"apikey": apikey} if apikey else {"apikey": API_KEY}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving DOWJONES Constituents as {filename}.")
    else:
        return __return_json_v3(path=path, query_vars=query_vars)


def historical_dowjones_constituent(apikey: str = None) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical/dowjones_constitnuet/ API.

    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    path = f"historical/dowjones_constituent"
    query_vars = {"apikey": apikey} if apikey else {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def available_indexes(apikey: str = None) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /symbol/available-indexes/ API

    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    path = f"symbol/available-indexes"
    query_vars = {"apikey": apikey} if apikey else {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)