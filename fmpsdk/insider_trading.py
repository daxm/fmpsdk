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
    apikey: str = None,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /insider-trading/ API.

    The federal securities laws require certain individuals (such as officers, directors, and those that hold more
    than 10% of any class of a company's securities, together we'll call, "insiders") to report purchases, sales,
    and holdings of their company's securities by filing Forms 3, 4, and 5.

    This API can be queried with your choice of symbol, company_cik or reporting_cik. Only one of these parameters
    will be accepted.

    :param symbol: Company ticker.
    :param reporting_cik: String of CIK
    :param company_cik: String of CIK
    :param limit: Number of records to return.
    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    path = f"insider-trading/"
    query_vars = {"apikey": apikey} if apikey else {"apikey": API_KEY}
    query_vars["limit"] = limit
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
    apikey: str = None,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /mapper-cik-name/ API.

    List with names and their CIK

    :param name: String of name.
    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    path = f"mapper-cik-name/"
    query_vars = {"apikey": apikey} if apikey else {"apikey": API_KEY}
    if name:
        query_vars["name"] = name
    return __return_json_v4(path=path, query_vars=query_vars)


def mapper_cik_company(
    ticker: str,
    apikey: str = None,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /mapper-cik-company/ API.

    Company CIK mapper

    :param ticker: String of name.
    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    path = f"mapper-cik-company/{ticker}"
    query_vars = {"apikey": apikey} if apikey else {"apikey": API_KEY}
    return __return_json_v4(path=path, query_vars=query_vars)


def insider_trading_rss_feed(
    limit: int = DEFAULT_LIMIT,
    apikey: str = None,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /insider-trading-rss-feed/ API.

    Complete list of all institutional investment managers by cik
    :param limit: Number of records to return.
    :param apikey: Your API key. If not provided, the function will use the API_KEY from environment variables.
    :return: A list of dictionaries.
    """
    path = f"insider-trading-rss-feed"
    query_vars = {"apikey": apikey} if apikey else {"apikey": API_KEY}
    query_vars["limit"] = limit
    return __return_json_v4(path=path, query_vars=query_vars)