import logging
import typing

from .settings import DEFAULT_LIMIT
from .url_methods import __return_json_v4


def insider_trading(
    apikey: str,
    symbol: str = None,
    reporting_cik: int = None,
    company_cik: int = None,
    limit: int = DEFAULT_LIMIT,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /insider-trading/ API.

    The federal securities laws require certain individuals (such as officers, directors, and those that hold more
    than 10% of any class of a company’s securities, together we’ll call, “insiders”) to report purchases, sales,
    and holdings of their company’s securities by filing Forms 3, 4, and 5.

    This API can be queried with your choice of symbol, company_cik or reporting_cik. Only one of these parameters
    will be accepted.

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :param reporting_cik: String of CIK
    :param company_cik: String of CIK
    :param limit: Number of records to return.
    :return: A list of dictionaries.
    """
    path = f"insider-trading/"
    query_vars = {"apikey": apikey, "limit": limit}
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
    apikey: str,
    name: str,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /mapper-cik-name/ API.

    List with names and their CIK

    :param apikey: Your API key.
    :param name: String of name.
    :return: A list of dictionaries.
    """
    path = f"mapper-cik-name/"
    query_vars = {"apikey": apikey}
    if name:
        query_vars["name"] = name
    return __return_json_v4(path=path, query_vars=query_vars)


def mapper_cik_company(
    apikey: str,
    ticker: str,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /mapper-cik-company/ API.

    Company CIK mapper

    :param apikey: Your API key.
    :param ticker: String of name.
    :return: A list of dictionaries.
    """
    path = f"mapper-cik-company/{ticker}"
    query_vars = {"apikey": apikey}
    return __return_json_v4(path=path, query_vars=query_vars)


def insider_trading_rss_feed(
    apikey: str, limit: int = DEFAULT_LIMIT
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /insider-trading-rss-feed/ API.

    Complete list of all institutional investment managers by cik
    :param apikey: Your API key.
    :param limit: Number of records to return.
    :return: A list of dictionaries.
    """
    path = f"insider-trading-rss-feed"
    query_vars = {"apikey": apikey, "limit": limit}
    return __return_json_v4(path=path, query_vars=query_vars)
