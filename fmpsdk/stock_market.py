import typing
import os
from .settings import DEFAULT_LIMIT
from .url_methods import __return_json_v3, __return_json_v4
from datetime import date
from .url_methods import __return_json_v4

API_KEY = os.getenv('FMP_API_KEY')

def actives() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /actives/ API

    :return: A list of dictionaries.
    """
    path = f"actives"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def gainers() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /gainers/ API

    :return: A list of dictionaries.
    """
    path = f"gainers"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def losers() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /losers/ API

    :return: A list of dictionaries.
    """
    path = f"losers"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def market_hours() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /market-hours/ API

    :return: A list of dictionaries.
    """
    path = f"market-hours"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def sectors_performance(
    limit: int = DEFAULT_LIMIT
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /sectors-performance/ API.

    :param limit: Number of rows to return.
    :return: A list of dictionaries containing sector performance data.
    :example: sectors_performance(limit=5)
    :endpoint: https://financialmodelingprep.com/api/v3/sectors-performance
    """
    path = f"sectors-performance"
    query_vars = {"apikey": API_KEY, "limit": limit}
    return __return_json_v3(path=path, query_vars=query_vars)

def fail_to_deliver(symbol: str, page: int = 0) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /fail_to_deliver API for fail to deliver data.

    :param symbol: Company ticker symbol.
    :param page: Page number for pagination (default is 0).
    :return: A list of dictionaries containing fail to deliver data.
    :example: fail_to_deliver('AAPL', page=1)
    :endpoint: https://financialmodelingprep.com/api/v4/fail_to_deliver?symbol={symbol}&page={page}
    """
    path = "fail_to_deliver"
    query_vars = {
        "apikey": API_KEY,
        "symbol": symbol,
        "page": page
    }
    return __return_json_v4(path=path, query_vars=query_vars)

def sector_pe_ratio(date: date, exchange: str = "NYSE") -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /sector_price_earning_ratio API.

    :param date: The date for which to retrieve the sector PE ratios.
    :param exchange: The stock exchange (default is NYSE).
    :return: A list of dictionaries containing sector PE ratios.
    :example: sector_pe_ratio('2023-01-01', exchange='NASDAQ')
    :endpoint: https://financialmodelingprep.com/api/v4/sector_price_earning_ratio?date={date}&exchange={exchange}
    """
    path = f"sector_price_earning_ratio"
    query_vars = {
        "date": date.strftime("%Y-%m-%d"),
        "exchange": exchange,
        "apikey": API_KEY
    }
    return __return_json_v4(path=path, query_vars=query_vars)

def industry_pe_ratio(date: date, exchange: str = "NYSE") -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /industry_price_earning_ratio API

    :param date: The date for which to retrieve the industry PE ratios
    :param exchange: The stock exchange (default is NYSE)
    :return: A list of dictionaries containing industry PE ratios
    """
    path = f"industry_price_earning_ratio"
    query_vars = {
        "date": date.strftime("%Y-%m-%d"),
        "exchange": exchange,
        "apikey": API_KEY
    }
    return __return_json_v4(path=path, query_vars=query_vars)

def batch_eod_prices(date: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Get batch request that contains all end of day prices for a specific date.

    :param date: The date in format YYYY-MM-DD
    :return: A list of dictionaries containing EOD prices for multiple stocks
    """
    path = "batch-request-end-of-day-prices"
    query_vars = {"apikey": API_KEY, "date": date}
    return __return_json_v4(path=path, query_vars=query_vars)

def multiple_company_prices(symbols: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Get multiple company prices at once.

    :param symbols: Comma-separated list of stock symbols (e.g., "AAPL,MSFT")
    :return: A list of dictionaries containing price information for the requested symbols
    """
    path = f"quote/{symbols}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)