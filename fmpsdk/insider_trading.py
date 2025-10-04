import logging
import typing

from .settings import DEFAULT_LIMIT
from .url_methods import __return_json_v3, __return_json_v4, __return_json_stable


def insider_trading(
    apikey: str,
    symbol: str = None,
    reportingCik: str = None,
    companyCik: str = None,
    transactionType: str = None,
    page: int = 0,
    limit: int = DEFAULT_LIMIT,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /insider-trading/search API.

    :param apikey: Your API key.
    :param symbol: Company ticker symbol.
    :param reportingCik: CIK of the reporting person.
    :param companyCik: CIK of the company.
    :param transactionType: Type of transaction (e.g., 'P-Purchase', 'S-Sale').
    :param page: Page number for pagination.
    :param limit: Number of rows to return.
    :return: A list of dictionaries containing insider trading data.
    """
    path = f"insider-trading/search"
    query_vars = {"apikey": apikey, "page": page, "limit": limit}
    if symbol:
        query_vars["symbol"] = symbol
    if reportingCik:
        query_vars["reportingCik"] = reportingCik
    if companyCik:
        query_vars["companyCik"] = companyCik
    if transactionType:
        query_vars["transactionType"] = transactionType
    return __return_json_stable(path=path, query_vars=query_vars)


def insider_trading_latest(
    apikey: str,
    page: int = 0,
    limit: int = DEFAULT_LIMIT,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /insider-trading/latest API.

    :param apikey: Your API key.
    :param page: Page number for pagination.
    :param limit: Number of rows to return.
    :return: A list of dictionaries containing latest insider trading data.
    """
    path = f"insider-trading/latest"
    query_vars = {"apikey": apikey, "page": page, "limit": limit}
    return __return_json_stable(path=path, query_vars=query_vars)


def insider_trading_by_reporting_name(
    apikey: str,
    name: str = None,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /insider-trading/reporting-name API.

    :param apikey: Your API key.
    :param name: name of the reporting person.
    :return: A list of dictionaries containing reporting ciks.
    """
    path = f"insider-trading/reporting-name"
    query_vars = {"apikey": apikey}
    if name:
        query_vars["name"] = name
    return __return_json_stable(path=path, query_vars=query_vars)


def insider_trading_transaction_types(
    apikey: str,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /insider-trading-transaction-type API.

    :param apikey: Your API key.
    :return: A list of dictionaries containing all transaction types.
    """
    path = f"insider-trading-transaction-type"
    query_vars = {"apikey": apikey}
    return __return_json_stable(path=path, query_vars=query_vars)


def insider_trading_statistics(
    apikey: str,
    symbol: str = None,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /insider-trading/statistics API.

    :param apikey: Your API key.
    :param symbol: Company ticker symbol.
    :return: A list of dictionaries containing insider trading statistics.
    """
    path = f"insider-trading/statistics"
    query_vars = {"apikey": apikey}
    if symbol:
        query_vars["symbol"] = symbol
    return __return_json_stable(path=path, query_vars=query_vars)


def acquisition_of_beneficial_ownership(
    apikey: str,
    symbol: str = None,
    limit: int = DEFAULT_LIMIT,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /acquisition-of-beneficial-ownership API.

    :param apikey: Your API key.
    :param symbol: Company ticker symbol.
    :param limit: Number of rows to return.
    :return: A list of dictionaries containing changes in stock ownership during acquisitions.
    """
    path = f"acquisition-of-beneficial-ownership"
    query_vars = {"apikey": apikey, "limit": limit}
    if symbol:
        query_vars["symbol"] = symbol
    return __return_json_stable(path=path, query_vars=query_vars)


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
