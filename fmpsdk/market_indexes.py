import logging
import typing
import os
import requests

from .settings import (
    DOWJONES_CONSTITUENTS_FILENAME,
    NASDAQ_CONSTITUENTS_FILENAME,
    SP500_CONSTITUENTS_FILENAME,
    BASE_URL_v3,
)
from .url_methods import __return_json_v3
from .data_compression import compress_json_to_tsv

API_KEY = os.getenv('FMP_API_KEY')

def indexes(tsv: bool = True) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Query FMP /quotes/index API for major stock market indices.
 
    Retrieves a list of all major stock market indices, such as the S&P 500, 
    the Dow Jones Industrial Average, and the Nasdaq Composite Index and 
    returns their performance.

    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: If tsv, TSV string. Otherwise, list of dictionaries containing index data.
             None if request fails.
    :example: indexes(tsv=True)
    """
    path = "quotes/index"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v3(path=path, query_vars=query_vars)
    
    return compress_json_to_tsv(result) if tsv else result

def sp500_constituent(
    download: bool = False,
    filename: str = SP500_CONSTITUENTS_FILENAME,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str, None]:
    """
    Query FMP /sp500_constituent/ API

    :param download: True/False
    :param filename: Name of saved file.
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: A list of dictionaries or TSV string if tsv is True.
    """
    path = f"sp500_constituent"
    query_vars = {"apikey": API_KEY}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving SP500 Constituents as {filename}.")
        return None
    else:
        result = __return_json_v3(path=path, query_vars=query_vars)
        return compress_json_to_tsv(result) if tsv else result

def historical_sp500_constituent(tsv: bool = True) -> typing.Union[typing.List[typing.Dict], 
                                                                   str, None]:
    """
    Query FMP /historical/sp500_constituent/ API.

    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: A list of dictionaries or TSV string if tsv is True.
    """
    path = f"historical/sp500_constituent"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tsv(result) if tsv else result

def nasdaq_constituent(
    download: bool = False,
    filename: str = NASDAQ_CONSTITUENTS_FILENAME,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str, None]:
    """
    Query FMP /nasdaq_constituent/ API

    :param download: True/False
    :param filename: Name of saved file.
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: A list of dictionaries or TSV string if tsv is True.
    """
    path = f"nasdaq_constituent"
    query_vars = {"apikey": API_KEY}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving NASDAQ Constituents as {filename}.")
        return None
    else:
        result = __return_json_v3(path=path, query_vars=query_vars)
        return compress_json_to_tsv(result) if tsv else result

def historical_nasdaq_constituent(tsv: bool = True) -> typing.Union[typing.List[typing.Dict], str, None]:
    """
    Query FMP /historical/nasdaq_constituent/ API.

    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: A list of dictionaries or TSV string if tsv is True.
    """
    path = f"historical/nasdaq_constituent"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tsv(result) if tsv else result

def dowjones_constituent(
    download: bool = False,
    filename: str = DOWJONES_CONSTITUENTS_FILENAME,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str, None]:
    """
    Query FMP /dowjones_constituent/ API

    :param download: True/False
    :param filename: Name of saved file.
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: A list of dictionaries or TSV string if tsv is True.
    """
    path = f"dowjones_constituent"
    query_vars = {"apikey": API_KEY}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving DOWJONES Constituents as {filename}.")
        return None
    else:
        result = __return_json_v3(path=path, query_vars=query_vars)
        return compress_json_to_tsv(result) if tsv else result

def historical_dowjones_constituent(tsv: bool = True) -> typing.Union[typing.List[typing.Dict], 
                                                                      str, None]:
    """
    Query FMP /historical/dowjones_constituent/ API.

    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: A list of dictionaries or TSV string if tsv is True.
    """
    path = f"historical/dowjones_constituent"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tsv(result) if tsv else result