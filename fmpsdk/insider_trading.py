import logging
import typing

from .settings import DEFAULT_LIMIT
from .url_methods import __return_json_v3, __return_json_v4


def insider_trading(
    apikey: str,
    symbol: str = None,
    reporting_name: str = None,
    limit: int = DEFAULT_LIMIT,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /insider-trading/ API.

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :param reporting_name: Name of reporting person.
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    """
    path = f"insider-trading"
    query_vars = {"apikey": apikey, "limit": limit}
    if symbol:
        query_vars["symbol"] = symbol
    if reporting_name:
        query_vars["reportingName"] = reporting_name
    return __return_json_v3(path=path, query_vars=query_vars)


def insider_trade_statistics(
    apikey: str,
    symbol: str,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /insider-roaster-statistic API.

    Get insider trading statistics for a specific company.

    https://site.financialmodelingprep.com/developer/docs#insider-trade-statistics

    Endpoint:
        https://financialmodelingprep.com/api/v4/insider-roaster-statistic?symbol=AAPL

    :param apikey: Your API key.
    :param symbol: Company ticker symbol.
    :return: A list of dictionaries containing insider trading statistics with fields:
             - symbol: The stock symbol
             - name: Name of the insider
             - position: Position in the company
             - totalBuy: Total number of buy transactions
             - totalBuyAmount: Total amount spent on buys
             - totalSell: Total number of sell transactions
             - totalSellAmount: Total amount from sells
             - totalTransactions: Total number of transactions
             - lastDate: Date of last transaction
             - lastPrice: Price of last transaction
             - lastAmount: Amount of last transaction
             - lastType: Type of last transaction (buy/sell)
    """
    if not symbol:
        logging.warning("Symbol is required for insider trade statistics request.")
        return None
    
    path = "insider-roaster-statistic"
    query_vars = {"apikey": apikey, "symbol": symbol}
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
