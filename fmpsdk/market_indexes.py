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

def indexes() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /quotes/index API for major stock market indices.

    Retrieves a list of all major stock market indices, such as the S&P 500, 
    the Dow Jones Industrial Average, and the Nasdaq Composite Index.

    :return: A list of dictionaries containing index data.
    :example: indexes()
    :endpoint: https://financialmodelingprep.com/api/v3/quotes/index
    """
    path = "quotes/index"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def sp500_constituent(
    download: bool = False,
    filename: str = SP500_CONSTITUENTS_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP /sp500_constituent/ API

    :param download: True/False
    :param filename: Name of saved file.
    :return: A list of dictionaries.
    """
    path = f"sp500_constituent"
    query_vars = {"apikey": API_KEY}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving SP500 Constituents as {filename}.")
    else:
        return __return_json_v3(path=path, query_vars=query_vars)


def historical_sp500_constituent() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical/sp500_constitnuet/ API.

    :return: A list of dictionaries.
    """
    path = f"historical/sp500_constituent"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def nasdaq_constituent(
    download: bool = False,
    filename: str = NASDAQ_CONSTITUENTS_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP /nasdaq_constituent/ API

    :param download: True/False
    :param filename: Name of saved file.
    :return: A list of dictionaries.
    """
    path = f"nasdaq_constituent"
    query_vars = {"apikey": API_KEY}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving NASDAQ Constituents as {filename}.")
    else:
        return __return_json_v3(path=path, query_vars=query_vars)


def historical_nasdaq_constituent() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical/nasdaq_constitnuet/ API.

    :return: A list of dictionaries.
    """
    path = f"historical/nasdaq_constituent"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def dowjones_constituent(
    download: bool = False,
    filename: str = DOWJONES_CONSTITUENTS_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP /dowjones_constituent/ API

    :param download: True/False
    :param filename: Name of saved file.
    :return: A list of dictionaries.
    """
    path = f"dowjones_constituent"
    query_vars = {"apikey": API_KEY}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving DOWJONES Constituents as {filename}.")
    else:
        return __return_json_v3(path=path, query_vars=query_vars)


def historical_dowjones_constituent() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical/dowjones_constitnuet/ API.

    :return: A list of dictionaries.
    """
    path = f"historical/dowjones_constituent"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def available_indexes() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /symbol/available-indexes/ API

    :return: A list of dictionaries.
    """
    path = f"symbol/available-indexes"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)