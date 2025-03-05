import logging
import typing

import requests

from .general import __quotes
from .settings import (
    DOWJONES_CONSTITUENTS_FILENAME,
    NASDAQ_CONSTITUENTS_FILENAME,
    SP500_CONSTITUENTS_FILENAME,
    BASE_URL_v3,
    DEFAULT_LIMIT,
)
from .url_methods import __return_json_v3, __return_json_v4


def indexes(apikey: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /quotes/index/ API.

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"quotes/index"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def sp500_constituent(
    apikey: str,
    download: bool = False,
    filename: str = SP500_CONSTITUENTS_FILENAME,
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
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving SP500 Constituents as {filename}.")
    else:
        return __return_json_v3(path=path, query_vars=query_vars)


def historical_sp500_constituent(
    apikey: str,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical/sp500_constitnuet/ API.

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"historical/sp500_constituent"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def nasdaq_constituent(
    apikey: str,
    download: bool = False,
    filename: str = NASDAQ_CONSTITUENTS_FILENAME,
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
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving NASDAQ Constituents as {filename}.")
    else:
        return __return_json_v3(path=path, query_vars=query_vars)


def historical_nasdaq_constituent(
    apikey: str,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical/nasdaq_constitnuet/ API.

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"historical/nasdaq_constituent"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def dowjones_constituent(
    apikey: str,
    download: bool = False,
    filename: str = DOWJONES_CONSTITUENTS_FILENAME,
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
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving DOWJONES Constituents as {filename}.")
    else:
        return __return_json_v3(path=path, query_vars=query_vars)


def historical_dowjones_constituent(
    apikey: str,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical/dowjones_constitnuet/ API.

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"historical/dowjones_constituent"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def available_indexes(apikey: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /symbol/available-indexes/ API

    :param apikey: Your API key
    :return: A list of dictionaries.
    """
    path = f"symbol/available-indexes"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def available_sectors(apikey: str) -> typing.Optional[typing.List[str]]:
    """
    Query FMP /sectors-list API to get all available sectors.

    :param apikey: Your API key
    :return: A list of sector names.
    """
    path = f"sectors-list"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def historical_sectors_performance(
    apikey: str,
    from_date: str,
    to_date: str,
    limit: int = DEFAULT_LIMIT,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical-sectors-performance API.

    Get historical performance data for different market sectors.

    https://site.financialmodelingprep.com/developer/docs#sector-historical

    Endpoint:
        https://financialmodelingprep.com/api/v3/historical-sectors-performance

    :param apikey: Your API key.
    :param from_date: The start date in "YYYY-MM-DD" format.
    :param to_date: The end date in "YYYY-MM-DD" format.
    :param limit: Number of records to return.
    :return: A list of dictionaries containing sector performance data with fields:
             - date: The date of the performance data
             - utilitiesChangesPercentage: Utilities sector performance
             - basicMaterialsChangesPercentage: Basic Materials sector performance
             - communicationServicesChangesPercentage: Communication Services sector performance
             - conglomeratesChangesPercentage: Conglomerates sector performance
             - consumerCyclicalChangesPercentage: Consumer Cyclical sector performance
             - consumerDefensiveChangesPercentage: Consumer Defensive sector performance
             - energyChangesPercentage: Energy sector performance
             - financialChangesPercentage: Financial sector performance
             - financialServicesChangesPercentage: Financial Services sector performance
             - healthcareChangesPercentage: Healthcare sector performance
             - industrialGoodsChangesPercentage: Industrial Goods sector performance
             - industrialsChangesPercentage: Industrials sector performance
             - realEstateChangesPercentage: Real Estate sector performance
             - servicesChangesPercentage: Services sector performance
             - technologyChangesPercentage: Technology sector performance
    """
    if not from_date or not to_date:
        logging.warning("Both from_date and to_date are required for historical sectors performance request.")
        return None
    
    path = "historical-sectors-performance"
    query_vars = {
        "apikey": apikey,
        "from": from_date,
        "to": to_date,
        "limit": limit
    }
    return __return_json_v3(path=path, query_vars=query_vars)


def all_exchange_market_hours(apikey: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /all-exchange-market-hours API to get market hours for all exchanges.

    :param apikey: Your API key.
    :return: A list of dictionaries containing market hours information for all exchanges.
    """
    path = "all-exchange-market-hours"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)
