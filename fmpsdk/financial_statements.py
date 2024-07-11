import typing
import os
import requests
import logging
from .settings import (
    FINANCIAL_STATEMENT_FILENAME,
    INCOME_STATEMENT_FILENAME,
    BALANCE_SHEET_STATEMENT_FILENAME,
    CASH_FLOW_STATEMENT_FILENAME,
    INCOME_STATEMENT_AS_REPORTED_FILENAME,
    BALANCE_SHEET_STATEMENT_AS_REPORTED_FILENAME,
    CASH_FLOW_STATEMENT_AS_REPORTED_FILENAME,
    DEFAULT_LIMIT,
    BASE_URL_v3,
)
from .url_methods import __return_json_v3, __validate_period

API_KEY = os.getenv('FMP_API_KEY')

def financial_statement(symbol: str, filename: str = FINANCIAL_STATEMENT_FILENAME) -> None:
    """
    Query FMP /financial-statements/ API for company's financial statement.

    :param symbol: Company ticker.
    :param filename: Name of saved file. Default is FINANCIAL_STATEMENT_FILENAME.
    :return: None
    :example: financial_statement('AAPL', 'AAPL_financial_statement.zip')
    :endpoint: https://financialmodelingprep.com/api/v3/financial-statements/{symbol}
    """
    path = f"financial-statements/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "datatype": "zip",  # Only ZIP format is supported.
    }
    response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
    open(filename, "wb").write(response.content)
    logging.info(f"Saving {symbol} financial statement as {filename}.")


def income_statement(
    symbol: str,
    period: str = "annual",
    limit: int = DEFAULT_LIMIT,
    download: bool = False,
    filename: str = INCOME_STATEMENT_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP /income-statement/ API for company's income statement.

    :param symbol: Company ticker.
    :param period: 'quarter' or 'annual'. Default is 'annual'.
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :param download: If True, download data as CSV. Default is False.
    :param filename: Name of saved file. Default is INCOME_STATEMENT_FILENAME.
    :return: List of dictionaries with income statement data or None if download is True.
    :example: income_statement('AAPL', period='quarter', limit=5, download=True)
    :endpoint: https://financialmodelingprep.com/api/v3/income-statement/{symbol}
    """
    path = f"income-statement/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit, "period": __validate_period(period)}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving {symbol} financial statement as {filename}.")
    else:
        return __return_json_v3(path=path, query_vars=query_vars)


def balance_sheet_statement(
    symbol: str,
    period: str = "annual",
    limit: int = DEFAULT_LIMIT,
    download: bool = False,
    filename: str = BALANCE_SHEET_STATEMENT_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP /balance-sheet-statement/ API for company's balance sheet statement.

    :param symbol: Company ticker.
    :param period: 'quarter' or 'annual'. Default is 'annual'.
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :param download: If True, download data as CSV. Default is False.
    :param filename: Name of saved file. Default is BALANCE_SHEET_STATEMENT_FILENAME.
    :return: List of dictionaries with balance sheet data or None if download is True.
    :example: balance_sheet_statement('AAPL', period='quarter', limit=5, download=True)
    :endpoint: https://financialmodelingprep.com/api/v3/balance-sheet-statement/{symbol}
    """
    path = f"balance-sheet-statement/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit, "period": __validate_period(period)}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving {symbol} balance sheet statement as {filename}.")
    else:
        return __return_json_v3(path=path, query_vars=query_vars)


def cash_flow_statement(
    symbol: str,
    period: str = "annual",
    limit: int = DEFAULT_LIMIT,
    download: bool = False,
    filename: str = CASH_FLOW_STATEMENT_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP /cash-flow-statement/ API for company's cash flow statement.

    :param symbol: Company ticker.
    :param period: 'quarter' or 'annual'. Default is 'annual'.
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :param download: If True, download data as CSV. Default is False.
    :param filename: Name of saved file. Default is CASH_FLOW_STATEMENT_FILENAME.
    :return: List of dictionaries with cash flow data or None if download is True.
    :example: cash_flow_statement('AAPL', period='quarter', limit=5, download=True)
    :endpoint: https://financialmodelingprep.com/api/v3/cash-flow-statement/{symbol}
    """
    path = f"cash-flow-statement/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit, "period": __validate_period(period)}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving {symbol} financial statement as {filename}.")
    else:
        return __return_json_v3(path=path, query_vars=query_vars)

def income_statement_as_reported(
    symbol: str,
    period: str = "annual",
    limit: int = DEFAULT_LIMIT,
    download: bool = False,
    filename: str = INCOME_STATEMENT_AS_REPORTED_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP /income-statement-as-reported/ API for company's as-reported income statement.

    :param symbol: Company ticker.
    :param period: 'quarter' or 'annual'. Default is 'annual'.
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :param download: If True, download data as CSV. Default is False.
    :param filename: Name of saved file. Default is INCOME_STATEMENT_AS_REPORTED_FILENAME.
    :return: List of dictionaries with as-reported income statement data or None if download is True.
    :example: income_statement_as_reported('AAPL', period='quarter', limit=5, download=True)
    :endpoint: https://financialmodelingprep.com/api/v3/income-statement-as-reported/{symbol}
    """
    path = f"income-statement-as-reported/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "limit": limit,
        "period": __validate_period(value=period),
    }
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving {symbol} financial statement as {filename}.")
    else:
        return __return_json_v3(path=path, query_vars=query_vars)


def balance_sheet_statement_as_reported(
    symbol: str,
    period: str = "annual",
    limit: int = DEFAULT_LIMIT,
    download: bool = False,
    filename: str = BALANCE_SHEET_STATEMENT_AS_REPORTED_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP /balance-sheet-statement-as-reported/ API for company's as-reported balance sheet.

    :param symbol: Company ticker.
    :param period: 'quarter' or 'annual'. Default is 'annual'.
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :param download: If True, download data as CSV. Default is False.
    :param filename: Name of saved file. Default is BALANCE_SHEET_STATEMENT_AS_REPORTED_FILENAME.
    :return: List of dictionaries with as-reported balance sheet data or None if download is True.
    :example: balance_sheet_statement_as_reported('AAPL', period='quarter', limit=5, download=True)
    :endpoint: https://financialmodelingprep.com/api/v3/balance-sheet-statement-as-reported/{symbol}
    """
    path = f"balance-sheet-statement-as-reported/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "limit": limit,
        "period": __validate_period(value=period),
    }
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving {symbol} financial statement as {filename}.")
    else:
        return __return_json_v3(path=path, query_vars=query_vars)


def cash_flow_statement_as_reported(
    symbol: str,
    period: str = "annual",
    limit: int = DEFAULT_LIMIT,
    download: bool = False,
    filename: str = CASH_FLOW_STATEMENT_AS_REPORTED_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP /cash-flow-statement-as-reported/ API for company's as-reported cash flow statement.

    :param symbol: Company ticker.
    :param period: 'quarter' or 'annual'. Default is 'annual'.
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :param download: If True, download data as CSV. Default is False.
    :param filename: Name of saved file. Default is CASH_FLOW_STATEMENT_AS_REPORTED_FILENAME.
    :return: List of dictionaries with as-reported cash flow data or None if download is True.
    :example: cash_flow_statement_as_reported('AAPL', period='quarter', limit=5, download=True)
    :endpoint: https://financialmodelingprep.com/api/v3/cash-flow-statement-as-reported/{symbol}
    """
    path = f"cash-flow-statement-as-reported/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "limit": limit,
        "period": __validate_period(value=period),
    }
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving {symbol} financial statement as {filename}.")
    else:
        return __return_json_v3(path=path, query_vars=query_vars)


def financial_statement_full_as_reported(symbol: str, period: str = "annual") -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /financial-statement-full-as-reported/ API for company's full as-reported financial statement.

    :param symbol: Company ticker.
    :param period: 'quarter' or 'annual'. Default is 'annual'.
    :return: List of dictionaries with full as-reported financial statement data.
    :example: financial_statement_full_as_reported('AAPL', period='quarter')
    :endpoint: https://financialmodelingprep.com/api/v3/financial-statement-full-as-reported/{symbol}
    """
    path = f"financial-statement-full-as-reported/{symbol}"
    query_vars = {"apikey": API_KEY, "period": __validate_period(value=period)}
    return __return_json_v3(path=path, query_vars=query_vars)