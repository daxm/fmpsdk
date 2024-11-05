import logging
import typing
import os

from .settings import DEFAULT_LIMIT
from .url_methods import __return_json_v4
from .data_compression import compress_json_to_tsv

API_KEY = os.getenv('FMP_API_KEY')


def insider_trading(
    symbol: str = None,
    reporting_cik: int = None,
    company_cik: int = None,
    limit: int = DEFAULT_LIMIT,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve insider trading data for a company or individual.

    Provides information on insider trades, including transaction date, insider name,
    transaction type, shares traded, and price. Useful for tracking insider activity,
    identifying potential investment opportunities, and assessing company sentiment.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param reporting_cik: CIK of the reporting insider.
    :param company_cik: CIK of the company.
    :param limit: Number of records to return. Default is DEFAULT_LIMIT.
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with insider trading data.
    :note: Provide only one of symbol, reporting_cik, or company_cik.
    :example: insider_trading(symbol='AAPL', limit=10)
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
    result = __return_json_v4(path=path, query_vars=query_vars)
    return compress_json_to_tsv(result) if tsv else result


def mapper_cik_name(
    name: str,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Query FMP /mapper-cik-name/ API.

    List with names and their CIK

    :param name: String of name.
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with CIK mapping data.
    """
    path = f"mapper-cik-name/"
    query_vars = {"apikey": API_KEY}
    if name:
        query_vars["name"] = name
    result = __return_json_v4(path=path, query_vars=query_vars)
    return compress_json_to_tsv(result) if tsv else result


def mapper_cik_company(
    ticker: str,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Query FMP /mapper-cik-company/ API.

    Company CIK mapper

    :param ticker: String of name.
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with company CIK mapping data.
    """
    path = f"mapper-cik-company/{ticker}"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v4(path=path, query_vars=query_vars)
    return compress_json_to_tsv(result) if tsv else result


def insider_trading_rss_feed(
    limit: int = DEFAULT_LIMIT,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve real-time RSS feed of insider trades.

    Provides up-to-date information on insider trading activity, allowing users to
    track changes in insider ownership of stocks. Useful for identifying companies
    with high insider activity, monitoring large insider transactions, and spotting
    potential investment opportunities based on insider behavior.

    :param limit: Number of records to return. Default is DEFAULT_LIMIT.
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with insider trading RSS feed data.
    :example: insider_trading_rss_feed(limit=20)
    """
    path = f"insider-trading-rss-feed"
    query_vars = {"apikey": API_KEY, "limit": limit}
    result = __return_json_v4(path=path, query_vars=query_vars)
    return compress_json_to_tsv(result) if tsv else result