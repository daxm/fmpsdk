import typing
import os

from .url_methods import __return_json_v4

# Read API key from environment variable
API_KEY = os.environ.get('FMP_API_KEY')

def commitment_of_traders_report_list() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /commitment_of_traders_report/list API.

    List of symbols for COT.
    :return: A list of dictionaries.
    """
    path = f"commitment_of_traders_report/list"
    query_vars = {"apikey": API_KEY}
    return __return_json_v4(path=path, query_vars=query_vars)

def commitment_of_traders_report(
    symbol: str,
    from_date: str = None,
    to_date: str = None,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /commitment_of_traders_report API.

    The Commodity Futures Trading Commission (Commission or CFTC) publishes the Commitments of Traders (COT)
    reports to help the public understand market dynamics. Specifically, the COT reports provide a breakdown of
    each Tuesday's open interest for futures and options on futures markets in which 20 or more traders hold
    positions equal to or above the reporting levels established by the CFTC.

    :param symbol: COT symbol (required).
    :param from_date: Optional. Start date in YYYY-MM-DD format.
    :param to_date: Optional. End date in YYYY-MM-DD format.
    :return: A list of dictionaries containing COT report data.
    """
    path = f"commitment_of_traders_report/{symbol}"
    query_vars = {"apikey": API_KEY}
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    return __return_json_v4(path=path, query_vars=query_vars)

def commitment_of_traders_report_analysis(
    symbol: str,
    from_date: str,
    to_date: str,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /commitment_of_traders_report_analysis API.

    Analysis of reports for time period or symbol.

    :param symbol: trading symbol.
    :param from_date: YYYY-MM-DD string.
    :param to_date: YYYY-MM-DD string.
    :return: A list of dictionaries.
    """
    path = f"commitment_of_traders_report_analysis"
    query_vars = {"apikey": API_KEY}
    if symbol:
        path = f"{path}/{symbol}"
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    return __return_json_v4(path=path, query_vars=query_vars)