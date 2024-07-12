import logging
import typing
import os

from .settings import DEFAULT_LIMIT
from .url_methods import __return_json_v4

API_KEY = os.getenv('FMP_API_KEY')

def insider_trading(
    symbol: str = None,
    reporting_cik: int = None,
    company_cik: int = None,
    limit: int = DEFAULT_LIMIT,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /insider-trading/ API.

    Get insider trading data for a company or individual. Only one of symbol, company_cik, or reporting_cik should be provided.

    :param symbol: Company ticker.
    :param reporting_cik: CIK of the reporting insider.
    :param company_cik: CIK of the company.
    :param limit: Number of records to return.
    :return: A list of dictionaries containing insider trading data.
    """
    path = f"insider-trading/"
    query_vars = {"apikey": API_KEY, "limit": limit}
    if not sum(i is not None for i in [reporting_cik, company_cik, symbol]) == 1:
        msg = "Do not combine symbol, reporting_cik or company_cik parameters. Only provide one."
        logging.error(msg)
        raise ValueError(msg)
    if reporting_cik:
        query_vars["reportingCik"] = reporting_cik
    if company_cik:
        query_vars["companyCik"] = company_cik
    if symbol:
        query_vars["symbol"] = symbol
    return __return_json_v4(path=path, query_vars=query_vars)


def mapper_cik_name(
    name: str,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /mapper-cik-name/ API.

    List with names and their CIK

    :param name: String of name.
    :return: A list of dictionaries.
    """
    path = f"mapper-cik-name/"
    query_vars = {"apikey": API_KEY}
    if name:
        query_vars["name"] = name
    return __return_json_v4(path=path, query_vars=query_vars)


def mapper_cik_company(
    ticker: str,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /mapper-cik-company/ API.

    Company CIK mapper

    :param ticker: String of name.
    :return: A list of dictionaries.
    """
    path = f"mapper-cik-company/{ticker}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v4(path=path, query_vars=query_vars)


def insider_trading_rss_feed(
    limit: int = DEFAULT_LIMIT
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /insider-trading-rss-feed/ API.

    Complete list of all institutional investment managers by cik
    :param limit: Number of records to return.
    :return: A list of dictionaries.
    """
    path = f"insider-trading-rss-feed"
    query_vars = {"apikey": API_KEY, "limit": limit}
    return __return_json_v4(path=path, query_vars=query_vars)