import logging
import typing

import requests

from .general import __quotes
from .settings import DEFAULT_LIMIT, BASE_URL_v3, BASE_URL_v4
from .url_methods import __return_json_v3, __return_json_v4, __return_json_stable


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


def bulk_profiles(apikey: str, part: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    It contains all profiles from our API in one CSV file

    Endpoint:
        https://site.financialmodelingprep.com/developer/docs/bulk-profiles

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"profile-bulk"
    query_vars = {"apikey": apikey, "part": part}
    return __return_json_stable(path=path, query_vars=query_vars)


def batch_quote(
    apikey: str, symbols: typing.List[str]
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Get real-time quotes for multiple symbols in a single request.

    https://site.financialmodelingprep.com/developer/docs#batch-pre-post-market

    Endpoint:
        https://financialmodelingprep.com/api/v4/batch-pre-post-market/{symbol}

    :param apikey: Your API key.
    :param symbols: List of stock symbols to get quotes for.
    :return: A list of dictionaries containing quote data for each symbol.
    """
    if not symbols:
        logging.warning("No symbols provided for batch quote request.")
        return []
    
    path = f"batch-pre-post-market/{','.join(symbols)}"
    query_vars = {"apikey": apikey}
    return __return_json_v4(path=path, query_vars=query_vars)


def batch_pre_post_market_trade(
    apikey: str, symbol: str
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Get real-time trade data for a specific symbol.

    https://site.financialmodelingprep.com/developer/docs#batch-pre-post-market-trade

    Endpoint:
        https://financialmodelingprep.com/api/v4/batch-pre-post-market-trade/{symbol}

    :param apikey: Your API key.
    :param symbol: The stock symbol to get trade data for.
    :return: A list of dictionaries containing trade data with fields:
             - symbol: The stock symbol
             - price: The trade price
             - size: The trade size
             - timestamp: The trade timestamp in milliseconds
    """
    if not symbol:
        logging.warning("No symbol provided for batch trade request.")
        return []
    
    path = f"batch-pre-post-market-trade/{symbol}"
    query_vars = {"apikey": apikey}
    return __return_json_v4(path=path, query_vars=query_vars)


def scores_bulk(
    apikey: str, symbols: typing.List[str]
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Get financial scores and metrics for multiple symbols in a single request.

    Endpoint:
        https://financialmodelingprep.com/stable/scores-bulk

    :param apikey: Your API key.
    :param symbols: List of stock symbols to get scores for.
    :return: A list of dictionaries containing financial scores and metrics for each symbol.
             Each dictionary contains various financial metrics and scores for the corresponding symbol.
    """
    if not symbols:
        logging.warning("No symbols provided for scores bulk request.")
        return []
    
    path = "scores-bulk"
    query_vars = {"apikey": apikey, "symbol": ','.join(symbols)}
    return __return_json_stable(path=path, query_vars=query_vars)


def upgrades_downgrades_consensus_bulk(
    apikey: str,
    limit: typing.Optional[int] = None,
    download: bool = False,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Get bulk data for upgrades and downgrades consensus.

    Endpoint:
        https://financialmodelingprep.com/stable/upgrades-downgrades-consensus-bulk

    :param apikey: Your API key.
    :param limit: Number of rows to return (optional).
    :param download: If True, returns data in CSV format (optional).
    :return: A list of dictionaries containing upgrades and downgrades consensus data.
             Each dictionary contains fields such as:
             - symbol
             - gradeDate
             - newGrade
             - oldGrade
             - company
             - action
             - analystsCount
             And more...
    """
    path = "upgrades-downgrades-consensus-bulk"
    query_vars = {"apikey": apikey}
    
    if limit is not None:
        query_vars["limit"] = limit
    
    if download:
        query_vars["datatype"] = "csv"
        
    return __return_json_stable(path=path, query_vars=query_vars)
