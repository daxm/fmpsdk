import typing
import os
from .settings import DEFAULT_LIMIT
from .url_methods import __return_json_v3, __validate_period

API_KEY = os.getenv('FMP_API_KEY')

def income_statement_growth(symbol: str, limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /income-statement-growth/ API for company's income statement growth.

    :param symbol: Company ticker.
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :return: List of dictionaries with income statement growth data.
    :example: income_statement_growth('AAPL', limit=5)
    :endpoint: https://financialmodelingprep.com/api/v3/income-statement-growth/{symbol}
    """
    path = f"income-statement-growth/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "limit": limit,
    }
    return __return_json_v3(path=path, query_vars=query_vars)


def balance_sheet_statement_growth(symbol: str, limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /balance-sheet-statement-growth/ API for company's balance sheet statement growth.

    :param symbol: Company ticker.
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :return: List of dictionaries with balance sheet statement growth data.
    :example: balance_sheet_statement_growth('AAPL', limit=5)
    :endpoint: https://financialmodelingprep.com/api/v3/balance-sheet-statement-growth/{symbol}
    """
    path = f"balance-sheet-statement-growth/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "limit": limit,
    }
    return __return_json_v3(path=path, query_vars=query_vars)


def cash_flow_statement_growth(symbol: str, limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /cash-flow-statement-growth/ API for company's cash flow statement growth.

    :param symbol: Company ticker.
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :return: List of dictionaries with cash flow statement growth data.
    :example: cash_flow_statement_growth('AAPL', limit=5)
    :endpoint: https://financialmodelingprep.com/api/v3/cash-flow-statement-growth/{symbol}
    """
    path = f"cash-flow-statement-growth/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "limit": limit,
    }
    return __return_json_v3(path=path, query_vars=query_vars)


def financial_ratios_ttm(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /ratios-ttm/ API for company's trailing twelve months financial ratios.

    :param symbol: Company ticker.
    :return: List of dictionaries with TTM financial ratios data.
    :example: financial_ratios_ttm('AAPL')
    :endpoint: https://financialmodelingprep.com/api/v3/ratios-ttm/{symbol}
    """
    path = f"ratios-ttm/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def financial_ratios(
    symbol: str, period: str = "annual", limit: int = DEFAULT_LIMIT
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /ratios/ API for company's financial ratios.

    :param symbol: Company ticker.
    :param period: 'annual' or 'quarter'. Default is 'annual'.
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :return: List of dictionaries with financial ratios data.
    :example: financial_ratios('AAPL', period='quarter', limit=5)
    :endpoint: https://financialmodelingprep.com/api/v3/ratios/{symbol}
    """
    path = f"ratios/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "period": __validate_period(value=period),
        "limit": limit,
    }
    return __return_json_v3(path=path, query_vars=query_vars)


def financial_growth(symbol: str, period: str = "annual", limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /financial-growth/ API for company's financial growth metrics.

    :param symbol: Company ticker.
    :param period: 'annual' or 'quarter'. Default is 'annual'.
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :return: List of dictionaries with financial growth data.
    :example: financial_growth('AAPL', period='quarter', limit=5)
    :endpoint: https://financialmodelingprep.com/api/v3/financial-growth/{symbol}
    """
    path = f"financial-growth/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "limit": limit,
        "period": __validate_period(value=period),
    }
    return __return_json_v3(path=path, query_vars=query_vars)