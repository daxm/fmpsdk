import typing
import os
from decimal import Decimal, ROUND_HALF_UP
from .settings import DEFAULT_LIMIT
from .url_methods import __return_json_v3, __validate_period
from .data_compression import compress_json_to_tsv, apply_precision

API_KEY = os.getenv('FMP_API_KEY')

def income_statement_growth(
    symbol: str,
    limit: int = DEFAULT_LIMIT,
    tsv: bool = True,
    precision: typing.Optional[int] = 5
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve income statement growth metrics for a company.

    Provides insights into revenue and profit growth trends, useful for assessing
    financial performance and identifying growth patterns.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :param tsv: If True, return data in TSV format. Defaults to True.
    :param precision: Decimal places for rounding. None for full precision.
    :return: Income statement growth data or None if request fails.
    :example: income_statement_growth('AAPL', limit=5, precision=3)
    """
    path = f"income-statement-growth/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit}
    result = __return_json_v3(path=path, query_vars=query_vars)
    
    if result:
        result = apply_precision(result, precision)
    
    fields = tuple(result[0].keys()) if result else None
    return compress_json_to_tsv(result, fields) if tsv else result

def balance_sheet_statement_growth(
    symbol: str,
    limit: int = DEFAULT_LIMIT,
    tsv: bool = True,
    precision: typing.Optional[int] = 5
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve balance sheet statement growth metrics for a company.

    Provides insights into assets, liabilities, and equity growth, useful for
    assessing financial health and long-term stability.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :param tsv: If True, return data in TSV format. Defaults to True.
    :param precision: Decimal places for rounding. None for full precision.
    :return: Balance sheet growth data or None if request fails.
    :example: balance_sheet_statement_growth('AAPL', limit=5, precision=3)
    """
    path = f"balance-sheet-statement-growth/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit}
    result = __return_json_v3(path=path, query_vars=query_vars)
    
    if result:
        result = apply_precision(result, precision)
    
    fields = tuple(result[0].keys()) if result else None
    return compress_json_to_tsv(result, fields) if tsv else result

def cash_flow_statement_growth(
    symbol: str,
    limit: int = DEFAULT_LIMIT,
    tsv: bool = True,
    precision: typing.Optional[int] = 5
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve cash flow statement growth metrics for a company.

    Provides insights into cash inflows and outflows growth, useful for
    assessing liquidity and financial flexibility.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :param tsv: If True, return data in TSV format. Defaults to True.
    :param precision: Decimal places for rounding. None for full precision.
    :return: Cash flow statement growth data or None if request fails.
    :example: cash_flow_statement_growth('AAPL', limit=5, precision=3)
    """
    path = f"cash-flow-statement-growth/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit}
    result = __return_json_v3(path=path, query_vars=query_vars)
    
    if result:
        result = apply_precision(result, precision)
    
    fields = tuple(result[0].keys()) if result else None
    return compress_json_to_tsv(result, fields) if tsv else result

def financial_ratios_ttm(
    symbol: str,
    tsv: bool = True,
    precision: typing.Optional[int] = 5
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve trailing twelve months (TTM) financial ratios for a company.

    Provides insights into current financial performance and efficiency, useful
    for comparing with industry averages and identifying areas for improvement.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param tsv: If True, return data in TSV format. Defaults to True.
    :param precision: Decimal places for rounding. None for full precision.
    :return: TTM financial ratios data or None if request fails.
    :example: financial_ratios_ttm('AAPL', precision=3)
    """
    path = f"ratios-ttm/{symbol}"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v3(path=path, query_vars=query_vars)

    if result:
        result = apply_precision(result, precision)
    
    fields = tuple(result[0].keys()) if result else None
    return compress_json_to_tsv(result, fields) if tsv else result

def financial_ratios(
    symbol: str,
    period: str = "annual",
    limit: int = DEFAULT_LIMIT,
    tsv: bool = True,
    precision: typing.Optional[int] = 5
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve financial ratios for a company.

    This function provides various financial ratios calculated from a company's
    financial statements, useful for analyzing the company's financial health
    and performance.

    :param symbol: Company ticker (e.g., 'AAPL' for Apple Inc.)
    :param period: The period of the data. Can be 'annual' or 'quarter' (default is 'annual')
    :param limit: The number of results to return (default is DEFAULT_LIMIT)
    :param tsv: If True, return data in TSV format. Defaults to True.
    :param precision: The number of decimal places to round numeric values to (default is 5).
                      If None, returns full precision.
    :return: Financial ratios data or None if request fails.
    :example: financial_ratios('AAPL', period='quarter', limit=4, precision=5)
    """
    path = f"ratios/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "period": __validate_period(period),
        "limit": limit
    }
    result = __return_json_v3(path=path, query_vars=query_vars)
    
    if result:
        result = apply_precision(result, precision)
    
    fields = tuple(result[0].keys()) if result else None
    return compress_json_to_tsv(result, fields) if tsv else result

def financial_growth(
    symbol: str,
    period: str = "annual",
    limit: int = DEFAULT_LIMIT,
    tsv: bool = True,
    precision: typing.Optional[int] = 5
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve financial growth metrics for a company.

    Provides insights into overall financial performance improvement, useful for
    assessing growth trends, comparing performance over time, and identifying
    potential investment opportunities.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param period: Reporting period ('annual' or 'quarter'). Default is 'annual'.
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :param tsv: If True, return data in TSV format. Defaults to True.
    :param precision: Decimal places for rounding. None for full precision.
    :return: Financial growth data or None if request fails.
    :example: financial_growth('AAPL', period='quarter', limit=5, precision=3)
    """
    path = f"financial-growth/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "limit": limit,
        "period": __validate_period(value=period),
    }
    result = __return_json_v3(path=path, query_vars=query_vars)
    
    if result:
        result = apply_precision(result, precision)
    
    fields = tuple(result[0].keys()) if result else None
    return compress_json_to_tsv(result, fields) if tsv else result