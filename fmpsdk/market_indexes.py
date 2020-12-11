from .settings import (
    BASE_URL,
    SP500_CONSTITUENTS_FILENAME,
    NASDAQ_CONSTITUENTS_FILENAME,
    DOWJONES_CONSTITUENTS_FILENAME,
)
from .url_methods import __return_json
from .general_methods import (
    __quotes,
    __quote,
    __historical_chart,
    __historical_price_full,
)
import requests
import logging
import typing


def indexes(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /quotes/index/ API.

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"quotes/index"
    return __quotes(apikey=apikey, value=path)


def index_quote(apikey: str, index: str) -> typing.List[typing.Dict]:
    """
    Query FMP /quote/ API.

    :param apikey: Your API key.
    :param index: Market Index.
    :return: A list of dictionaries.
    """
    path = f"quote/{index}"
    return __quote(apikey=apikey, value=path)


def sp500_constituent(
    apikey: str, download: bool = False, filename: str = SP500_CONSTITUENTS_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP /sp500_constituent/ API

    :param apikey: Your API key.
    :param download: True/False
    :param filename: Name of saved file.
    :return: A list of dictionaries.
    """
    path = f"sp500_constituent"
    query_vars = {"apikey": apikey}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving SP500 Constituents as {filename}.")
    else:
        return __return_json(path=path, query_vars=query_vars)


def historical_sp500_constituent(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /historical/sp500_constitnuet/ API.

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"historical/sp500_constituent"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def nasdaq_constituent(
    apikey: str, download: bool = False, filename: str = NASDAQ_CONSTITUENTS_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP /nasdaq_constituent/ API

    :param apikey: Your API key.
    :param download: True/False
    :param filename: Name of saved file.
    :return: A list of dictionaries.
    """
    path = f"nasdaq_constituent"
    query_vars = {"apikey": apikey}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving NASDAQ Constituents as {filename}.")
    else:
        return __return_json(path=path, query_vars=query_vars)


def historical_nasdaq_constituent(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /historical/nasdaq_constitnuet/ API.

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"historical/nasdaq_constituent"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def dowjones_constituent(
    apikey: str, download: bool = False, filename: str = DOWJONES_CONSTITUENTS_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP /dowjones_constituent/ API

    :param apikey: Your API key.
    :param download: True/False
    :param filename: Name of saved file.
    :return: A list of dictionaries.
    """
    path = f"dowjones_constituent"
    query_vars = {"apikey": apikey}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving DOWJONES Constituents as {filename}.")
    else:
        return __return_json(path=path, query_vars=query_vars)


def historical_dowjones_constituent(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /historical/dowjones_constitnuet/ API.

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"historical/dowjones_constituent"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def available_indexes(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /symbol/available-indexes/ API

    :param apikey: Your API key
    :return: A list of dictionaries.
    """
    path = f"symbol/available-indexes"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def historical_index(
    apikey: str, index: str, time_delta: str = "4hour",
) -> typing.List[typing.Dict]:
    """
    Query FMP /historical-chart/ API

    :param apikey: Your API key
    :param index: Market index
    :param time_delta: The string value of time from now to go historical "1min" - "4hour".
    :return: A list of dictionaries.
    """
    return __historical_chart(apikey=apikey, value=index, time_delta=time_delta)


def historical_index_full(apikey: str, index: str) -> typing.List[typing.Dict]:
    """
    Query FMP /historical-price-full/ API.

    :param apikey: Your API Key
    :param index: The Ticker, Index, Commodity, etc. symbol to query for.
    :param time_series: Not sure what this is.  5 is the only value I've seen used.
    :param series_type: Not sure what this is.  "line" is the only option I've seen used.
    :param from_date: 'YYYY-MM-DD' format
    :param to_date: 'YYYY-MM-DD' format
    :return: A list of dictionaries.
    """
    return __historical_price_full(apikey=apikey, value=index)
