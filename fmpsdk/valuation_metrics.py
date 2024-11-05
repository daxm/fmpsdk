import typing
import os
from .settings import DEFAULT_LIMIT
from .url_methods import __return_json_v3, __return_json_v4
from .data_compression import compress_json_to_tsv

API_KEY = os.getenv('FMP_API_KEY')

def discounted_cash_flow(
    symbol: str,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve discounted cash flow (DCF) valuation data for a company.

    Provides a method to estimate a company's intrinsic value based on
    future cash flows. Useful for identifying potential undervalued or
    overvalued companies.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: DCF valuation data or TSV string.
    :example: discounted_cash_flow('AAPL')
    """
    path = f"discounted-cash-flow/{symbol}"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tsv(result) if tsv else result

def advanced_discounted_cash_flow(
    symbol: str,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve advanced discounted cash flow (DCF) valuation data for a company.

    Provides a more detailed method to estimate a company's intrinsic value
    based on future cash flows. Useful for identifying potential undervalued
    or overvalued companies.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: Advanced DCF valuation data or TSV string.
    :example: advanced_discounted_cash_flow('AAPL')
    """
    path = f"advanced_discounted_cash_flow"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    result = __return_json_v4(path=path, query_vars=query_vars)
    return compress_json_to_tsv(result) if tsv else result

def historical_daily_discounted_cash_flow(
    symbol: str,
    limit: int = DEFAULT_LIMIT,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve daily historical discounted cash flow (DCF) valuation data for a company.

    Provides a method to analyze a company's historical intrinsic value
    based on daily cash flows. Useful for identifying trends and patterns
    in a company's valuation over time.

    :param symbol: Company ticker.
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: Daily historical DCF valuation data or TSV string.
    :example: historical_daily_discounted_cash_flow('AAPL', limit=5)
    """
    path = f"historical-daily-discounted-cash-flow/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit}
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tsv(result) if tsv else result

def market_capitalization(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve a company's current market capitalization.

    Provides the total value of a company's outstanding shares. Useful for
    identifying large-cap, mid-cap, or small-cap companies.

    :param symbol: Company ticker.
    :return: List of dicts with market capitalization data or None if request fails.
    :example: market_capitalization('AAPL')
    """
    path = f"market-capitalization/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def historical_market_capitalization(
    symbol: str,
    limit: int = DEFAULT_LIMIT,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve historical market capitalization data for a company.

    Provides up to five years of data to analyze growth trajectory and
    performance trends. Useful for tracking company growth over time and
    identifying potential underperformance relative to the market.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts with historical market cap data, or TSV string if tsv is True.
             Returns None if request fails.
    :example: historical_market_capitalization('AAPL', limit=100)
    """
    path = f"historical-market-capitalization/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit}
    result = __return_json_v3(path=path, query_vars=query_vars)
    
    if result is not None:
        return compress_json_to_tsv(result) if tsv else result
    
    return None

def discounted_cash_flow(
    symbol: str,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve discounted cash flow (DCF) valuation data for a company.

    Provides a method to estimate a company's intrinsic value based on
    future cash flows. Useful for identifying potential undervalued or
    overvalued companies.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: DCF valuation data or TSV string.
    :example: discounted_cash_flow('AAPL')
    """
    path = f"discounted-cash-flow/{symbol}"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tsv(result) if tsv else result


def advanced_discounted_cash_flow(
    symbol: str,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve advanced discounted cash flow (DCF) valuation data for a company.

    Provides a more detailed method to estimate a company's intrinsic value
    based on future cash flows. Useful for identifying potential undervalued
    or overvalued companies.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: Advanced DCF valuation data or TSV string.
    :example: advanced_discounted_cash_flow('AAPL')
    """
    path = f"advanced_discounted_cash_flow"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    result = __return_json_v4(path=path, query_vars=query_vars)
    return compress_json_to_tsv(result) if tsv else result


def historical_daily_discounted_cash_flow(
    symbol: str,
    limit: int = DEFAULT_LIMIT,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve daily historical discounted cash flow (DCF) valuation data for a company.

    Provides a method to analyze a company's historical intrinsic value
    based on daily cash flows. Useful for identifying trends and patterns
    in a company's valuation over time.

    :param symbol: Company ticker.
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: Daily historical DCF valuation data or TSV string.
    :example: historical_daily_discounted_cash_flow('AAPL', limit=5)
    """
    path = f"historical-daily-discounted-cash-flow/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit}
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tsv(result) if tsv else result
