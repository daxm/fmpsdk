import typing
import os
from .settings import DEFAULT_LIMIT
from .url_methods import __return_json_v3, __return_json_v4, __validate_period

API_KEY = os.getenv('FMP_API_KEY')

def discounted_cash_flow(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /discounted-cash-flow/ API for DCF valuation.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: List of dictionaries with DCF valuation data or None if request fails.
    :example: discounted_cash_flow('AAPL')
    :endpoint: https://financialmodelingprep.com/api/v3/discounted-cash-flow/{symbol}
    """
    path = f"discounted-cash-flow/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def advanced_discounted_cash_flow(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /advanced_discounted_cash_flow/ API for advanced DCF valuation.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: List of dictionaries with advanced DCF valuation data or None if request fails.
    :example: advanced_discounted_cash_flow('AAPL')
    :endpoint: https://financialmodelingprep.com/api/v4/advanced_discounted_cash_flow?symbol={symbol}
    """
    path = f"advanced_discounted_cash_flow"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def historical_discounted_cash_flow(symbol: str, period: str = "annual", limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical-discounted-cash-flow/ API for historical DCF valuation.

    :param symbol: Company ticker.
    :param period: 'annual' or 'quarter'. Default is 'annual'.
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :return: List of dictionaries with historical DCF valuation data or None if request fails.
    :example: historical_discounted_cash_flow('AAPL', period='quarter', limit=5)
    :endpoint: https://financialmodelingprep.com/api/v3/historical-discounted-cash-flow/{symbol}
    """
    path = f"historical-discounted-cash-flow/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "limit": limit,
        "period": __validate_period(value=period),
    }
    return __return_json_v3(path=path, query_vars=query_vars)

def historical_daily_discounted_cash_flow(symbol: str, limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical-daily-discounted-cash-flow/ API for daily historical DCF valuation.

    :param symbol: Company ticker.
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :return: List of dictionaries with daily historical DCF valuation data or None if request fails.
    :example: historical_daily_discounted_cash_flow('AAPL', limit=5)
    :endpoint: https://financialmodelingprep.com/api/v3/historical-daily-discounted-cash-flow/{symbol}
    """
    path = f"historical-daily-discounted-cash-flow/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit}
    return __return_json_v3(path=path, query_vars=query_vars)

def market_capitalization(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /market-capitalization/ API for company's market capitalization.

    :param symbol: Company ticker.
    :return: List of dictionaries with market capitalization data or None if request fails.
    :example: market_capitalization('AAPL')
    :endpoint: https://financialmodelingprep.com/api/v3/market-capitalization/{symbol}
    """
    path = f"market-capitalization/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def historical_market_capitalization(symbol: str, limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical-market-capitalization/ API for historical market capitalization.

    :param symbol: Company ticker.
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :return: List of dictionaries with historical market capitalization data or None if request fails.
    :example: historical_market_capitalization('AAPL', limit=5)
    :endpoint: https://financialmodelingprep.com/api/v3/historical-market-capitalization/{symbol}
    """
    path = f"historical-market-capitalization/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit}
    return __return_json_v3(path=path, query_vars=query_vars)