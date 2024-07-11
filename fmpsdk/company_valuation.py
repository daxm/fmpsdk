import logging
import typing
import os
import requests

from .settings import (
    BALANCE_SHEET_STATEMENT_AS_REPORTED_FILENAME,
    BALANCE_SHEET_STATEMENT_FILENAME,
    CASH_FLOW_STATEMENT_AS_REPORTED_FILENAME,
    CASH_FLOW_STATEMENT_FILENAME,
    DEFAULT_LIMIT,
    FINANCIAL_STATEMENT_FILENAME,
    INCOME_STATEMENT_AS_REPORTED_FILENAME,
    INCOME_STATEMENT_FILENAME,
    BASE_URL_v3,
    BASE_URL_v4,
)
from .url_methods import (
    __return_json_v3,
    __return_json_v4,
    __validate_industry,
    __validate_period,
    __validate_sector,
)

API_KEY = os.getenv('FMP_API_KEY')

def company_profile(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /profile/ API.

    Get a comprehensive overview of a company, including key information such as price, beta, market capitalization, description, headquarters, and more.

    :param symbol: Ticker symbol of the company (e.g., 'AAPL').
    :return: A list of dictionaries containing company profile data or None if the request fails.

    Example:
    >>> company_profile('AAPL')
    [{'symbol': 'AAPL', 'price': 150.0, 'beta': 1.2, 'marketCap': 2000000000000, 'description': 'Apple Inc. designs, manufactures, and markets smartphones, personal computers, tablets, wearables, and accessories worldwide.', 'sector': 'Technology', 'industry': 'Consumer Electronics', 'ceo': 'Tim Cook', 'website': 'https://www.apple.com', 'image': 'https://financialmodelingprep.com/image.png', ...}, ...]

    Users can get a detailed profile for many different companies by providing the appropriate ticker symbol.

    Endpoint:
    https://financialmodelingprep.com/api/v3/profile/{symbol}

    API Documentation:
    https://site.financialmodelingprep.com/developer/docs/companies-key-stats-free-api
    """
    path = f"profile/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def key_executives(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /key-executives/ API.

    Gather info about company's key executives.
    :param symbol: Ticker of company.
    :return: A list of dictionaries.
    :example: key_executives('AAPL')
    :endpoint: https://financialmodelingprep.com/api/v3/key-executives/{symbol}
    :docs: https://site.financialmodelingprep.com/developer/docs/key-executives-api
    """
    path = f"key-executives/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def search(query: str = "", limit: int = DEFAULT_LIMIT, exchange: str = "") -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /search/ API.

    Search for ticker symbols and companies by name or ticker symbol. This API supports over 70,000 symbols, including cryptocurrencies, forex, stocks, ETFs, and other financial instruments.

    :param query: Whole or fragment of Ticker or Name of company (e.g., 'Apple' or 'AAPL').
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :param exchange: Stock exchange to search (e.g., 'NASDAQ', 'NYSE'). If empty, searches across all exchanges.
    :return: A list of dictionaries containing search results or None if the request fails.

    Example:
    >>> search('Apple', limit=10, exchange='NASDAQ')
    [{'symbol': 'AAPL', 'name': 'Apple Inc.', 'exchange': 'NASDAQ', ...}, ...]

    Users can search for many different markets including stocks, indices, commodities, and more by providing the appropriate query and exchange.

    Endpoint:
    https://financialmodelingprep.com/api/v3/search?query={query}&limit={limit}&exchange={exchange}

    API Documentation:
    https://site.financialmodelingprep.com/developer/docs/stock-ticker-symbol-lookup-api
    """
    path = f"search/"
    query_vars = {
        "apikey": API_KEY,
        "limit": limit,
        "query": query,
        "exchange": exchange,
    }
    return __return_json_v3(path=path, query_vars=query_vars)


def search_ticker(query: str = "", limit: int = DEFAULT_LIMIT, exchange: str = "") -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /search-ticker/ API.

    Search for ticker symbols by company name or ticker symbol. This API supports searching for equity securities and exchange-traded funds (ETFs) across various exchanges.

    :param query: Whole or fragment of Ticker or Name of company (e.g., 'AAPL' or 'Apple').
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :param exchange: Stock exchange to search (e.g., 'NASDAQ', 'NYSE'). If empty, searches across all exchanges.
    :return: A list of dictionaries containing search results or None if the request fails.

    Example:
    >>> search_ticker('AAPL', limit=10, exchange='NASDAQ')
    [{'symbol': 'AAPL', 'name': 'Apple Inc.', 'exchange': 'NASDAQ', ...}, ...]

    Users can search for ticker symbols and companies by providing the appropriate query and exchange.

    Endpoint:
    https://financialmodelingprep.com/api/v3/search-ticker?query={query}&limit={limit}&exchange={exchange}

    API Documentation:
    https://site.financialmodelingprep.com/developer/docs#ticker-search-company-search
    """
    path = f"search-ticker/"
    query_vars = {
        "apikey": API_KEY,
        "limit": limit,
        "query": query,
        "exchange": exchange,
    }
    return __return_json_v3(path=path, query_vars=query_vars)


def financial_statement(symbol: str, filename: str = FINANCIAL_STATEMENT_FILENAME) -> None:
    """
    Query FMP /financial-statements/ API.

    Download company's financial statement.
    :param symbol: Ticker of company.
    :param filename: Name of saved file.
    :example: financial_statement('AAPL', 'AAPL_financial_statement.zip')
    :endpoint: https://financialmodelingprep.com/api/v3/financial-statements/{symbol}
    :docs: https://site.financialmodelingprep.com/developer/docs/financial-statements-api
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
    Query FMP /income-statement/ API.

    Display or download a company's income statement. The income statement, also known as the profit and loss statement, shows a company's revenue, expenses, and net income over a period of time.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param period: 'quarter' or 'annual'. Default is 'annual'.
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :param download: If True, download data as a CSV file. Default is False.
    :param filename: Name of the file to save the downloaded data. Default is INCOME_STATEMENT_FILENAME.
    :return: A list of dictionaries containing income statement data or None if download is True.

    Example:
    >>> income_statement('AAPL', period='quarter', limit=5, download=True, filename='AAPL_income_statement.csv')
    [{'date': '2023-01-01', 'symbol': 'AAPL', 'revenue': 100000000, 'netIncome': 20000000, 'eps': 1.5, ...}, ...]

    Users can get income statements for many different companies by providing the appropriate ticker symbol and period.

    Endpoint:
    https://financialmodelingprep.com/api/v3/income-statement/{symbol}?period={period}&limit={limit}

    API Documentation:
    https://site.financialmodelingprep.com/developer/docs/financial-statement-free-api
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
    Query FMP /balance-sheet-statement/ API.

    Get a company's balance sheet statement data. The balance sheet displays a company's total assets, liabilities, and shareholder equity over a specific timeframe (quarterly or yearly).

    :param symbol: Ticker symbol of the company (e.g., 'AAPL').
    :param period: Reporting period ('annual' or 'quarter'). Default is 'annual'.
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :param download: If True, download data as a file. Default is False.
    :param filename: Name of the file to save the downloaded data. Default is BALANCE_SHEET_STATEMENT_FILENAME.
    :return: A list of dictionaries with balance sheet data or None if the request fails.

    Example:
    >>> balance_sheet_statement('AAPL', period='quarter', limit=5)
    [{'date': '2023-01-01', 'symbol': 'AAPL', 'totalAssets': 300000000, 'totalLiabilities': 150000000, 'shareholderEquity': 150000000, ...}, ...]

    Users can get balance sheet statements for many different companies by providing the appropriate ticker symbol and period.

    Endpoint:
    https://financialmodelingprep.com/api/v3/balance-sheet-statement/{symbol}?period={period}&limit={limit}

    API Documentation:
    https://site.financialmodelingprep.com/developer/docs/balance-sheet-statements-financial-statements
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
    Query FMP /cash-flow-statement/ API.

    Display or download a company's cash flow statement. The cash flow statement highlights how cash moves through the company, including both cash inflows and outflows, categorized into operating, investing, and financing activities.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param period: 'quarter' or 'annual'. Default is 'annual'.
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :param download: If True, download data as a CSV file. Default is False.
    :param filename: Name of the file to save the downloaded data. Default is CASH_FLOW_STATEMENT_FILENAME.
    :return: A list of dictionaries containing cash flow statement data or None if download is True.

    Example:
    >>> cash_flow_statement('AAPL', period='quarter', limit=5, download=True, filename='AAPL_cash_flow_statement.csv')
    [{'date': '2023-01-01', 'symbol': 'AAPL', 'operatingCashFlow': 50000000, 'investingCashFlow': -20000000, 'financingCashFlow': 10000000, ...}, ...]

    Users can get cash flow statements for many different companies by providing the appropriate ticker symbol and period.

    Endpoint:
    https://financialmodelingprep.com/api/v3/cash-flow-statement/{symbol}?period={period}&limit={limit}

    API Documentation:
    https://site.financialmodelingprep.com/developer/docs/cashflow-statements-financial-statements
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


def financial_statement_symbol_lists() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /financial-statement-symbol-lists/ API.

    List of symbols that have financial statements.
    :return: A list of dictionaries.
    :example: financial_statement_symbol_lists()
    :endpoint: https://financialmodelingprep.com/api/v3/financial-statement-symbol-lists
    :docs: https://site.financialmodelingprep.com/developer/docs/financial-statement-symbol-lists-api
    """
    path = f"financial-statement-symbol-lists"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def income_statement_growth(symbol: str, limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /income-statement-growth/ API.

    Growth stats for company's income statement.
    :param symbol: Company ticker.
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    :example: income_statement_growth('AAPL', limit=5)
    :endpoint: https://financialmodelingprep.com/api/v3/income-statement-growth/{symbol}
    :docs: https://site.financialmodelingprep.com/developer/docs/income-statement-growth-api
    """
    path = f"income-statement-growth/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "limit": limit,
    }
    return __return_json_v3(path=path, query_vars=query_vars)


def balance_sheet_statement_growth(symbol: str, limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /balance-sheet-statement-growth/ API.

    Growth stats for company's balance sheet statement.
    :param symbol: Company ticker.
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    :example: balance_sheet_statement_growth('AAPL', limit=5)
    :endpoint: https://financialmodelingprep.com/api/v3/balance-sheet-statement-growth/{symbol}
    :docs: https://site.financialmodelingprep.com/developer/docs/balance-sheet-statement-growth-api
    """
    path = f"balance-sheet-statement-growth/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "limit": limit,
    }
    return __return_json_v3(path=path, query_vars=query_vars)


def cash_flow_statement_growth(symbol: str, limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /cash-flow-statement-growth/ API.

    Growth stats for company's cash flow statement.
    :param symbol: Company ticker.
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    :example: cash_flow_statement_growth('AAPL', limit=5)
    :endpoint: https://financialmodelingprep.com/api/v3/cash-flow-statement-growth/{symbol}
    :docs: https://site.financialmodelingprep.com/developer/docs/cash-flow-statement-growth-api
    """
    path = f"cash-flow-statement-growth/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "limit": limit,
    }
    return __return_json_v3(path=path, query_vars=query_vars)


def income_statement_as_reported(
    symbol: str,
    period: str = "annual",
    limit: int = DEFAULT_LIMIT,
    download: bool = False,
    filename: str = INCOME_STATEMENT_AS_REPORTED_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP /income-statement-as-reported/ API.

    Company's "as reported" income statement.
    :param symbol: Company ticker.
    :param period: 'annual' or 'quarter'
    :param limit: Number of rows to return.
    :param download: True/False
    :param filename: Name of saved file.
    :return: A list of dictionaries or None if download is True.
    :example: income_statement_as_reported('AAPL', period='quarter', limit=5, download=True, filename='AAPL_income_statement_as_reported.csv')
    :endpoint: https://financialmodelingprep.com/api/v3/income-statement-as-reported/{symbol}
    :docs: https://site.financialmodelingprep.com/developer/docs/income-statement-as-reported-api
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
    Query FMP /balance-sheet-statement-as-reported/ API.

    Company's "as reported" balance sheet statement.
    :param symbol: Company ticker.
    :param period: 'annual' or 'quarter'
    :param limit: Number of rows to return.
    :param download: True/False
    :param filename: Name of saved file.
    :return: A list of dictionaries or None if download is True.
    :example: balance_sheet_statement_as_reported('AAPL', period='quarter', limit=5, download=True, filename='AAPL_balance_sheet_statement_as_reported.csv')
    :endpoint: https://financialmodelingprep.com/api/v3/balance-sheet-statement-as-reported/{symbol}
    :docs: https://site.financialmodelingprep.com/developer/docs/balance-sheet-statement-as-reported-api
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
    Query FMP /cash-flow-statement-as-reported/ API.

    Company's "as reported" cash flow statement.
    :param symbol: Company ticker.
    :param period: 'annual' or 'quarter'
    :param limit: Number of rows to return.
    :param download: True/False
    :param filename: Name of saved file.
    :return: A list of dictionaries or None if download is True.
    :example: cash_flow_statement_as_reported('AAPL', period='quarter', limit=5, download=True, filename='AAPL_cash_flow_statement_as_reported.csv')
    :endpoint: https://financialmodelingprep.com/api/v3/cash-flow-statement-as-reported/{symbol}
    :docs: https://site.financialmodelingprep.com/developer/docs/cash-flow-statement-as-reported-api
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
    Query FMP /financial-statement-full-as-reported/ API.

    Company's "as reported" full income statement.
    :param symbol: Company ticker.
    :param period: 'annual' or 'quarter'
    :return: A list of dictionaries.
    :example: financial_statement_full_as_reported('AAPL', period='quarter')
    :endpoint: https://financialmodelingprep.com/api/v3/financial-statement-full-as-reported/{symbol}
    :docs: https://site.financialmodelingprep.com/developer/docs/financial-statement-full-as-reported-api
    """
    path = f"financial-statement-full-as-reported/{symbol}"
    query_vars = {"apikey": API_KEY, "period": __validate_period(value=period)}
    return __return_json_v3(path=path, query_vars=query_vars)


def financial_ratios_ttm(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FmP /ratios-ttm/ API.

    :param symbol: Company ticker
    :return: A list of dictionaries.
    :example: financial_ratios_ttm('AAPL')
    :endpoint: https://financialmodelingprep.com/api/v3/ratios-ttm/{symbol}
    :docs: https://site.financialmodelingprep.com/developer/docs/ratios-ttm-api
    """
    path = f"ratios-ttm/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def financial_ratios(
    symbol: str, period: str = "annual", limit: int = DEFAULT_LIMIT
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /ratios/ API.

    Get financial ratios for a company, such as the P/B ratio and the ROE. These ratios help assess a company's financial health and compare it to its competitors.

    :param symbol: Ticker symbol of the company (e.g., 'AAPL').
    :param period: Reporting period ('annual' or 'quarter'). Default is 'annual'.
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :return: A list of dictionaries containing financial ratios data or None if the request fails.

    Example:
    >>> financial_ratios('AAPL', period='quarter', limit=5)
    [{'date': '2023-01-01', 'symbol': 'AAPL', 'priceToBookRatio': 15.0, 'returnOnEquity': 25.0, ...}, ...]

    Users can get financial ratios for many different companies by providing the appropriate ticker symbol and period.

    Endpoint:
    https://financialmodelingprep.com/api/v3/ratios/{symbol}?period={period}&limit={limit}

    API Documentation:
    https://site.financialmodelingprep.com/developer/docs/financial-ratio-free-api
    """
    path = f"ratios/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "period": __validate_period(value=period),
        "limit": limit,
    }
    return __return_json_v3(path=path, query_vars=query_vars)


def enterprise_values(symbol: str, period: str = "annual", limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /enterprise-values/ API.

    Get the enterprise value of a company, which is the total value of a company, including its equity and debt. This metric helps assess a company's overall value and compare it to its peers.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param period: Reporting period ('annual' or 'quarter'). Default is 'annual'.
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :return: A list of dictionaries containing enterprise value data or None if the request fails.

    Example:
    >>> enterprise_values('AAPL', period='quarter', limit=5)
    [{'date': '2023-01-01', 'symbol': 'AAPL', 'enterpriseValue': 2500000000000, 'marketCap': 2000000000000, 'totalDebt': 500000000000, 'cashAndCashEquivalents': 100000000000, ...}, ...]

    Users can get enterprise values for many different companies by providing the appropriate ticker symbol and period.

    Endpoint:
    https://financialmodelingprep.com/api/v3/enterprise-values/{symbol}?period={period}&limit={limit}

    API Documentation:
    https://site.financialmodelingprep.com/developer/docs/company-enterprise-value-api
    """
    path = f"enterprise-values/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "period": __validate_period(value=period),
        "limit": limit,
    }
    return __return_json_v3(path=path, query_vars=query_vars)


def key_metrics_ttm(symbol: str, limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /key-metrics-ttm/ API

    :param symbol: Company ticker.
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    :example: key_metrics_ttm('AAPL', limit=5)
    :endpoint: https://financialmodelingprep.com/api/v3/key-metrics-ttm/{symbol}
    :docs: https://site.financialmodelingprep.com/developer/docs/key-metrics-ttm-api
    """
    path = f"key-metrics-ttm/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit}
    return __return_json_v3(path=path, query_vars=query_vars)


def key_metrics(
    symbol: str, period: str = "annual", limit: int = DEFAULT_LIMIT
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /key-metrics/ API.

    Get key financial metrics for a company, including revenue, net income, earnings per share (EPS), and price-to-earnings ratio (P/E ratio). These metrics help assess a company's financial performance and compare it to its competitors.

    :param symbol: Ticker symbol of the company (e.g., 'AAPL').
    :param period: Reporting period ('annual' or 'quarter'). Default is 'annual'.
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :return: A list of dictionaries containing key financial metrics data or None if the request fails.

    Example:
    >>> key_metrics('AAPL', period='quarter', limit=5)
    [{'date': '2023-01-01', 'symbol': 'AAPL', 'revenue': 100000000, 'netIncome': 20000000, 'eps': 1.5, 'peRatio': 25.0, ...}, ...]

    Users can get key financial metrics for many different companies by providing the appropriate ticker symbol and period.

    Endpoint:
    https://financialmodelingprep.com/api/v3/key-metrics/{symbol}?period={period}&limit={limit}

    API Documentation:
    https://site.financialmodelingprep.com/developer/docs/company-key-metrics-api
    """
    path = f"key-metrics/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "period": __validate_period(value=period),
        "limit": limit,
    }
    return __return_json_v3(path=path, query_vars=query_vars)


def financial_growth(symbol: str, period: str = "annual", limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /financial-growth/ API.

    :param symbol: Company ticker.
    :param period: 'annual' or 'quarter'
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    :example: financial_growth('AAPL', period='quarter', limit=5)
    :endpoint: https://financialmodelingprep.com/api/v3/financial-growth/{symbol}
    :docs: https://site.financialmodelingprep.com/developer/docs/financial-growth-api
    """
    path = f"financial-growth/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "limit": limit,
        "period": __validate_period(value=period),
    }
    return __return_json_v3(path=path, query_vars=query_vars)


def rating(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /rating/ API.

    :param symbol: Company ticker.
    :return: A list of dictionaries.
    :example: rating('AAPL')
    :endpoint: https://financialmodelingprep.com/api/v3/rating/{symbol}
    :docs: https://site.financialmodelingprep.com/developer/docs/rating-api
    """
    path = f"rating/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def historical_rating(symbol: str, limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical-rating/ API.

    :param symbol: Company ticker.
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    :example: historical_rating('AAPL', limit=5)
    :endpoint: https://financialmodelingprep.com/api/v3/historical-rating/{symbol}
    :docs: https://site.financialmodelingprep.com/developer/docs/historical-rating-api
    """
    path = f"historical-rating/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit}
    return __return_json_v3(path=path, query_vars=query_vars)


def discounted_cash_flow(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /discounted-cash-flow/ API.

    Get the discounted cash flow (DCF) valuation for a company. DCF is a valuation method that estimates the value of an investment based on its expected future cash flows. The DCF valuation is calculated by discounting the expected future cash flows to their present value.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: A list of dictionaries containing DCF valuation data or None if the request fails.

    Example:
    >>> discounted_cash_flow('AAPL')
    [{'symbol': 'AAPL', 'date': '2023-01-01', 'dcf': 150.0, 'stockPrice': 145.0, ...}, ...]

    Users can get DCF valuations for many different companies by providing the appropriate ticker symbol.

    Endpoint:
    https://financialmodelingprep.com/api/v3/discounted-cash-flow/{symbol}

    API Documentation:
    https://site.financialmodelingprep.com/developer/docs/companies-dcf-reports-free-api
    """
    path = f"discounted-cash-flow/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def advanced_discounted_cash_flow(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /advanced_discounted_cash_flow/ API.

    Calculate the DCF valuation for a company with advanced features like modeling multiple scenarios and using different valuation methods. This endpoint allows investors to model different scenarios, such as different revenue growth rates or different cost structures, and to use different valuation methods, such as the weighted average cost of capital (WACC) method or the free cash flow to equity (FCFE) method.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: A list of dictionaries containing advanced DCF valuation data or None if the request fails.

    Example:
    >>> advanced_discounted_cash_flow('AAPL')
    [{'symbol': 'AAPL', 'date': '2023-01-01', 'dcf': 160.0, 'stockPrice': 150.0, 'valuationMethod': 'WACC', ...}, ...]

    Users can get advanced DCF valuations for many different companies by providing the appropriate ticker symbol.

    Endpoint:
    https://financialmodelingprep.com/api/v4/advanced_discounted_cash_flow?symbol={symbol}

    API Documentation:
    https://site.financialmodelingprep.com/developer/docs/advanced-dcf-discounted-cash-flow
    """
    path = f"advanced_discounted_cash_flow"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def historical_discounted_cash_flow(symbol: str, period: str = "annual", limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical-discounted-cash-flow/ API.

    :param symbol: Company ticker.
    :param period: 'annual' or 'quarter'
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    :example: historical_discounted_cash_flow('AAPL', period='quarter', limit=5)
    :endpoint: https://financialmodelingprep.com/api/v3/historical-discounted-cash-flow/{symbol}
    :docs: https://site.financialmodelingprep.com/developer/docs/historical-discounted-cash-flow-api
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
    Query FMP /historical-daily-discounted-cash-flow/ API.

    :param symbol: Company ticker.
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    :example: historical_daily_discounted_cash_flow('AAPL', limit=5)
    :endpoint: https://financialmodelingprep.com/api/v3/historical-daily-discounted-cash-flow/{symbol}
    :docs: https://site.financialmodelingprep.com/developer/docs/historical-daily-discounted-cash-flow-api
    """
    path = f"historical-daily-discounted-cash-flow/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit}
    return __return_json_v3(path=path, query_vars=query_vars)


def market_capitalization(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /market-capitalization/ API.

    :param symbol: Company ticker.
    :return: A list of dictionaries.
    :example: market_capitalization('AAPL')
    :endpoint: https://financialmodelingprep.com/api/v3/market-capitalization/{symbol}
    :docs: https://site.financialmodelingprep.com/developer/docs/market-capitalization-api
    """
    path = f"market-capitalization/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def historical_market_capitalization(symbol: str, limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical-market-capitalization/ API.

    :param symbol: Company ticker.
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    :example: historical_market_capitalization('AAPL', limit=5)
    :endpoint: https://financialmodelingprep.com/api/v3/historical-market-capitalization/{symbol}
    :docs: https://site.financialmodelingprep.com/developer/docs/historical-market-capitalization-api
    """
    path = f"historical-market-capitalization/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit}
    return __return_json_v3(path=path, query_vars=query_vars)


def symbols_list() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /stock/list/ API

    :return: A list of dictionaries.
    :example: symbols_list()
    :endpoint: https://financialmodelingprep.com/api/v3/stock/list
    :docs: https://site.financialmodelingprep.com/developer/docs/stock-list-api
    """
    path = f"stock/list"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def etf_list() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /etf/list/ API

    All ETF symbols

    :return: A list of dictionaries.
    :example: etf_list()
    :endpoint: https://financialmodelingprep.com/api/v3/etf/list
    :docs: https://site.financialmodelingprep.com/developer/docs/etf-list-api
    """
    path = f"etf/list"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def available_traded_list() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /available-traded/list/ API

    All tradable symbols

    :return: A list of dictionaries.
    :example: available_traded_list()
    :endpoint: https://financialmodelingprep.com/api/v3/available-traded/list
    :docs: https://site.financialmodelingprep.com/developer/docs/available-traded-list-api
    """
    path = f"available-traded/list"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def stock_screener(
    market_cap_more_than: typing.Union[float, int] = None,
    market_cap_lower_than: typing.Union[float, int] = None,
    beta_more_than: typing.Union[float, int] = None,
    beta_lower_than: typing.Union[float, int] = None,
    volume_more_than: typing.Union[float, int] = None,
    volume_lower_than: typing.Union[float, int] = None,
    dividend_more_than: typing.Union[float, int] = None,
    dividend_lower_than: typing.Union[float, int] = None,
    price_more_than: typing.Union[float, int] = None,
    price_lower_than: typing.Union[float, int] = None,
    is_etf: bool = None,
    is_fund: bool = None,
    is_actively_trading: bool = None,
    sector: str = None,
    industry: str = None,
    country: str = None,
    exchange: typing.Union[str, typing.List[str]] = None,
    limit: int = DEFAULT_LIMIT,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /stock-screener/ API.

    Find stocks that meet your investment criteria based on various filters such as market cap, price, volume, beta, sector, and country.

    :param market_cap_more_than: Filter stocks with market cap greater than this value (e.g., 1000000000).
    :param market_cap_lower_than: Filter stocks with market cap lower than this value (e.g., 5000000000).
    :param beta_more_than: Filter stocks with beta greater than this value (e.g., 1.5).
    :param beta_lower_than: Filter stocks with beta lower than this value (e.g., 1.0).
    :param volume_more_than: Filter stocks with volume greater than this value (e.g., 1000000).
    :param volume_lower_than: Filter stocks with volume lower than this value (e.g., 5000000).
    :param dividend_more_than: Filter stocks with dividend yield greater than this value (e.g., 2.0).
    :param dividend_lower_than: Filter stocks with dividend yield lower than this value (e.g., 5.0).
    :param price_more_than: Filter stocks with price greater than this value (e.g., 50).
    :param price_lower_than: Filter stocks with price lower than this value (e.g., 200).
    :param is_etf: Filter for ETFs if True.
    :param is_fund: Filter for mutual funds if True.
    :param is_actively_trading: Filter for actively trading stocks if True.
    :param sector: Filter stocks by sector (e.g., 'Technology').
    :param industry: Filter stocks by industry (e.g., 'Software').
    :param country: Filter stocks by country (e.g., 'US').
    :param exchange: Filter stocks by exchange(s) (e.g., 'NASDAQ' or ['NASDAQ', 'NYSE']).
    :param limit: Number of results to return. Default is DEFAULT_LIMIT.
    :return: A list of dictionaries containing stock data or None if the request fails.
    :example: stock_screener(market_cap_more_than=1000000000, limit=10)
    :endpoint: https://financialmodelingprep.com/api/v3/stock-screener
    :docs: https://site.financialmodelingprep.com/developer/docs/stock-screener-api
    """
    path = "stock-screener"
    query_vars = {"apikey": API_KEY, "limit": limit}
    if market_cap_more_than:
        query_vars["marketCapMoreThan"] = market_cap_more_than
    if market_cap_lower_than:
        query_vars["marketCapLowerThan"] = market_cap_lower_than
    if beta_more_than:
        query_vars["betaMoreThan"] = beta_more_than
    if beta_lower_than:
        query_vars["betaLowerThan"] = beta_lower_than
    if volume_more_than:
        query_vars["volumeMoreThan"] = volume_more_than
    if volume_lower_than:
        query_vars["volumeLowerThan"] = volume_lower_than
    if dividend_more_than:
        query_vars["dividendMoreThan"] = dividend_more_than
    if dividend_lower_than:
        query_vars["dividendLowerThan"] = dividend_lower_than
    if price_more_than:
        query_vars["priceMoreThan"] = price_more_than
    if price_lower_than:
        query_vars["priceLowerThan"] = price_lower_than
    if is_etf is not None:
        query_vars["isEtf"] = is_etf
    if is_fund is not None:
        query_vars["isFund"] = is_fund
    if is_actively_trading is not None:
        query_vars["isActivelyTrading"] = is_actively_trading
    if sector:
        query_vars["sector"] = __validate_sector(sector)
    if industry:
        query_vars["industry"] = __validate_industry(industry)
    if country:
        query_vars["country"] = country
    if exchange:
        if type(exchange) is list:
            query_vars["exchange"] = ",".join(exchange)
        else:
            query_vars["exchange"] = exchange
    return __return_json_v3(path=path, query_vars=query_vars)


def delisted_companies(limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /delisted-companies/ API.

    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    :example: delisted_companies(limit=10)
    :endpoint: https://financialmodelingprep.com/api/v3/delisted-companies
    :docs: https://site.financialmodelingprep.com/developer/docs/delisted-companies-api
    """
    path = f"delisted-companies"
    query_vars = {"apikey": API_KEY, "limit": limit}
    return __return_json_v3(path=path, query_vars=query_vars)


def earnings_surprises(
    symbol: str
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /earnings-surprises/ API.

    :param symbol: Company ticker.
    :return: A list of dictionaries.
    :example: earnings_surprises('AAPL')
    :endpoint: https://financialmodelingprep.com/api/v3/earnings-surprises/{symbol}
    :docs: https://site.financialmodelingprep.com/developer/docs/earnings-surprises-api
    """
    path = f"earnings-surprises/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def earning_call_transcript(
    symbol: str, year: int, quarter: int
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /earning_call_transcript/ API.

    :param symbol: Company ticker.
    :param year: Year of the transcripts
    :param quarter: Quarter of the transcripts
    :return: A list of dictionaries.
    :example: earning_call_transcript('AAPL', 2023, 1)
    :endpoint: https://financialmodelingprep.com/api/v3/earning_call_transcript/{symbol}
    :docs: https://site.financialmodelingprep.com/developer/docs/earning-call-transcript-api
    """
    path = f"earning_call_transcript/{symbol}"
    query_vars = {"apikey": API_KEY, "year": year, "quarter": quarter}
    return __return_json_v3(path=path, query_vars=query_vars)


def batch_earning_call_transcript(
    symbol: str, year: int
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /batch_earning_call_transcript/ API.

    :param symbol: Company ticker.
    :param year: Year of the transcripts
    :return: A list of dictionaries.
    :example: batch_earning_call_transcript('AAPL', 2023)
    :endpoint: https://financialmodelingprep.com/api/v4/batch_earning_call_transcript/{symbol}
    :docs: https://site.financialmodelingprep.com/developer/docs/batch-earning-call-transcript-api
    """
    path = f"batch_earning_call_transcript/{symbol}"
    query_vars = {"apikey": API_KEY, "year": year}
    return __return_json_v4(path=path, query_vars=query_vars)


def earning_call_transcripts_available_dates(
    symbol: str
) -> typing.Optional[typing.List[typing.List]]:
    """
    Query FMP /earning_call_transcript/ API.

    :param symbol: Company ticker.
    :return: A list of lists.
    :example: earning_call_transcripts_available_dates('AAPL')
    :endpoint: https://financialmodelingprep.com/api/v4/earning_call_transcript
    :docs: https://site.financialmodelingprep.com/developer/docs/earning-call-transcript-api
    """
    path = f"earning_call_transcript"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)


def sec_filings(
    symbol: str, filing_type: str = "", limit: int = DEFAULT_LIMIT
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /sec_filings/ API.

    :param symbol: Company ticker.
    :param filing_type: Name of filing.
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    :example: sec_filings('AAPL', filing_type='10-K', limit=10)
    :endpoint: https://financialmodelingprep.com/api/v3/sec_filings/{symbol}
    :docs: https://site.financialmodelingprep.com/developer/docs/sec-filings-api
    """
    path = f"sec_filings/{symbol}"
    query_vars = {"apikey": API_KEY, "type": filing_type, "limit": limit}
    return __return_json_v3(path=path, query_vars=query_vars)


def press_releases(
    symbol: str, limit: int = DEFAULT_LIMIT
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /press-releases/ API.

    :param symbol: Company ticker.
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    """
    path = f"press-releases/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit}
    return __return_json_v3(path=path, query_vars=query_vars)


def stock_peers(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /stock_peers/ API.

    Get a list of companies that trade on the same exchange, are in the same sector, and have a similar market capitalization as the specified company.

    :param symbol: Ticker symbol of the company (e.g., 'AAPL').
    :return: A list of dictionaries containing stock peers data or None if the request fails.

    Example:
    >>> stock_peers('AAPL')
    [{'symbol': 'MSFT', 'companyName': 'Microsoft Corporation', 'marketCap': 2000000000000, 'sector': 'Technology', 'industry': 'Software'}, ...]

    Users can compare a company to its competitors and identify companies that are performing well by providing the appropriate ticker symbol.

    Endpoint:
    https://financialmodelingprep.com/api/v4/stock_peers?symbol={symbol}

    API Documentation:
    https://site.financialmodelingprep.com/developer/docs/stock-peers-api
    """
    path = f"stock_peers"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)


def analyst_estimates(
    symbol: str, period: str = "annual", limit: int = DEFAULT_LIMIT
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /analyst-estimates/ API.

    Get analyst estimates for a company's future earnings and revenue. This information helps investors understand what analysts expect from a company and identify potential investment opportunities.

    :param symbol: Ticker symbol of the company (e.g., 'AAPL').
    :param period: Reporting period ('annual' or 'quarter'). Default is 'annual'.
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :return: A list of dictionaries containing analyst estimates data or None if the request fails.

    Example:
    >>> analyst_estimates('AAPL', period='quarter', limit=5)
    [{'date': '2023-01-01', 'symbol': 'AAPL', 'estimatedRevenue': 100000000, 'estimatedEps': 1.5, ...}, ...]

    Users can get analyst estimates for many different companies by providing the appropriate ticker symbol and period.

    Endpoint:
    https://financialmodelingprep.com/api/v3/analyst-estimates/{symbol}?period={period}&limit={limit}

    API Documentation:
    https://site.financialmodelingprep.com/developer/docs/analyst-estimates-api
    """
    path = f"/analyst-estimates/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "symbol": symbol,
        "period": __validate_period(value=period),
        "limit": limit,
    }
    return __return_json_v3(path=path, query_vars=query_vars)

def sales_revenue_by_segments(
    symbol: str,
    structure: str = "flat",
    period: str = "annual"
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /revenue-product-segmentation API.

    Get a breakdown of a company's revenue by product category. This endpoint helps identify a company's most profitable products, track the performance of different product categories over time, and identify new product opportunities.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param structure: 'flat' or 'segment' (default is 'flat').
    :param period: 'annual' or 'quarter' (default is 'annual').
    :return: A list of dictionaries containing revenue by product segments data or None if the request fails.

    Example:
    >>> sales_revenue_by_segments('AAPL', structure='segment', period='quarter')
    [{'date': '2023-01-01', 'symbol': 'AAPL', 'productCategory': 'iPhone', 'revenue': 50000000000, ...}, ...]

    Users can get sales revenue by segments for many different companies by providing the appropriate ticker symbol, structure, and period.

    Endpoint:
    https://financialmodelingprep.com/api/v4/revenue-product-segmentation?symbol={symbol}&structure={structure}&period={period}

    API Documentation:
    https://site.financialmodelingprep.com/developer/docs/sales-revenue-by-segments-api
    """
    path = "revenue-product-segmentation"
    query_vars = {
        "apikey": API_KEY,
        "symbol": symbol,
        "structure": structure,
        "period": period
    }
    return __return_json_v4(path=path, query_vars=query_vars)

def revenue_geographic_segmentation(
    symbol: str,
    structure: str = "flat",
    period: str = "annual"
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /revenue-geographic-segmentation API.

    Get a breakdown of a company's revenue by geographic regions. This endpoint helps identify a company's most profitable regions, track the performance of different regions over time, and identify new market opportunities.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param structure: 'flat' or 'segment' (default is 'flat').
    :param period: 'annual' or 'quarter' (default is 'annual').
    :return: A list of dictionaries containing revenue by geographic segments data or None if the request fails.

    Example:
    >>> revenue_geographic_segmentation('AAPL', structure='segment', period='quarter')
    [{'date': '2023-01-01', 'symbol': 'AAPL', 'region': 'Americas', 'revenue': 50000000000, ...}, ...]

    Users can get revenue by geographic segments for many different companies by providing the appropriate ticker symbol, structure, and period.

    Endpoint:
    https://financialmodelingprep.com/api/v4/revenue-geographic-segmentation?symbol={symbol}&structure={structure}&period={period}

    API Documentation:
    https://site.financialmodelingprep.com/developer/docs/revenue-geographic-by-segments-api
    """
    path = "revenue-geographic-segmentation"
    query_vars = {
        "apikey": API_KEY,
        "symbol": symbol,
        "structure": structure,
        "period": period
    }
    return __return_json_v4(path=path, query_vars=query_vars)

def esg_score(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /esg-environmental-social-governance-data API for ESG scores.

    :param symbol: Company ticker symbol
    :return: A list of dictionaries containing ESG data
    """
    path = f"esg-environmental-social-governance-data"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def stock_grade(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /grade/ API for stock grades.

    :param symbol: Company ticker.
    :return: A list of dictionaries containing stock grades.
    """
    path = f"grade/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def financial_score(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /score/ API for financial score information.

    This endpoint provides financial scores for a company, including the Altman Z-Score and Piotroski Score, which are measures of the company's overall financial health. The Altman Z-Score is used to determine the possibility of bankruptcy for publicly traded manufacturing companies, while the Piotroski Score assesses the financial strength of a company.

    :param symbol: The stock symbol (e.g., 'AAPL').
    :return: A list of dictionaries containing financial score information or None if the request fails.

    Example:
    >>> financial_score('AAPL')
    [{'symbol': 'AAPL', 'altmanZScore': 3.5, 'piotroskiScore': 7, ...}, ...]

    Users can get financial scores for many different companies by providing the appropriate ticker symbol.

    Endpoint:
    https://financialmodelingprep.com/api/v4/score?symbol={symbol}

    API Documentation:
    https://site.financialmodelingprep.com/developer/docs/stock-financial-scores
    """
    path = "score"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def owner_earnings(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /owner_earnings API for owner earnings information.

    This endpoint provides owner earnings for a company, which is a measure of its profitability
    after accounting for all expenses, including taxes and debt payments. It helps assess a
    company's true profitability and compare it to its competitors.

    :param symbol: The stock symbol (e.g., 'AAPL')
    :return: A list of dictionaries containing owner earnings information.
    """
    path = "owner_earnings"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def upgrades_downgrades(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Get a comprehensive list of all stock upgrades and downgrades for a specific symbol.

    This endpoint provides information on stock upgrades and downgrades from different analysts, including the rating change, the analyst firm, and the date of the rating change. This information can be used to identify potential investment opportunities and assess the risk of current investments.

    :param symbol: The stock symbol (e.g., 'AAPL').
    :return: A list of dictionaries containing upgrades and downgrades information or None if the request fails.

    Example:
    >>> upgrades_downgrades('AAPL')
    [{'symbol': 'AAPL', 'analyst': 'Goldman Sachs', 'rating': 'Buy', 'date': '2023-01-01', ...}, ...]

    Users can get upgrades and downgrades for many different companies by providing the appropriate ticker symbol.

    Endpoint:
    https://financialmodelingprep.com/api/v4/upgrades-downgrades?symbol={symbol}

    API Documentation:
    https://site.financialmodelingprep.com/developer/docs#upgrades-downgrades-search
    """
    path = "upgrades-downgrades"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def upgrades_downgrades_rss_feed(page: int = 0) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /upgrades-downgrades-rss-feed/ API for the latest stock upgrades and downgrades.

    Get an RSS feed of all stock upgrades and downgrades from different analysts. This RSS feed is updated on a daily basis, so you can always stay up-to-date on the latest analyst ratings without having to manually check for updates.

    :param page: The page number for pagination (default is 0).
    :return: A list of dictionaries containing the latest stock upgrades and downgrades.

    Example:
    >>> upgrades_downgrades_rss_feed(page=1)
    [{'symbol': 'AAPL', 'analyst': 'Goldman Sachs', 'rating': 'Buy', 'date': '2023-10-01', ...}, ...]

    Users can get the latest stock upgrades and downgrades for many different companies by providing the appropriate page number for pagination.

    Endpoint:
    https://financialmodelingprep.com/api/v4/upgrades-downgrades-rss-feed?page={page}

    API Documentation:
    https://site.financialmodelingprep.com/developer/docs/upgrades-and-downgrades-rss-feed-api
    """
    path = "upgrades-downgrades-rss-feed"
    query_vars = {"apikey": API_KEY, "page": page}
    return __return_json_v4(path=path, query_vars=query_vars)

def upgrades_downgrades_consensus(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /upgrades-downgrades-consensus/ API.

    Get the consensus rating for a company, which is the average rating from different analysts. This information can be used to get a general idea of what analysts think about a company's stock and to make more informed investment decisions.

    :param symbol: The stock symbol (e.g., 'AAPL').
    :return: A list of dictionaries containing consensus rating information or None if the request fails.

    Example:
    >>> upgrades_downgrades_consensus('AAPL')
    [{'symbol': 'AAPL', 'consensusRating': 'Buy', 'numberOfAnalysts': 25, 'date': '2023-10-01', ...}, ...]

    Users can get consensus ratings for many different companies by providing the appropriate ticker symbol.

    Endpoint:
    https://financialmodelingprep.com/api/v4/upgrades-downgrades-consensus?symbol={symbol}

    API Documentation:
    https://site.financialmodelingprep.com/developer/docs/upgrades-and-downgrades-consensus-api
    """
    path = "upgrades-downgrades-consensus"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def upgrades_downgrades_by_company(company: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /upgrades-downgrades-grading-company/ API.

    Get a comprehensive list of all stock upgrades and downgrades for a specific company. This information includes the rating change, the analyst firm, and the date of the rating change. It can be used to track analyst sentiment for a company and to identify potential investment opportunities or risks.

    :param company: The name of the company (e.g., 'Barclays').
    :return: A list of dictionaries containing upgrades and downgrades information for the company.

    Example:
    >>> upgrades_downgrades_by_company('Barclays')
    [{'symbol': 'AAPL', 'analyst': 'Goldman Sachs', 'rating': 'Buy', 'date': '2023-10-01', ...}, ...]

    Users can get upgrades and downgrades for many different companies by providing the appropriate company name.

    Endpoint:
    https://financialmodelingprep.com/api/v4/upgrades-downgrades-grading-company?company={company}

    API Documentation:
    https://site.financialmodelingprep.com/developer/docs/upgrades-and-downgrades-by-company-api
    """
    path = "upgrades-downgrades-grading-company"
    query_vars = {"apikey": API_KEY, "company": company}
    return __return_json_v4(path=path, query_vars=query_vars)

def mergers_acquisitions_rss_feed(page: int = 0) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /mergers-acquisitions-rss-feed/ API for the latest M&A news and announcements.

    Get a real-time feed of mergers and acquisitions (M&A) news and announcements. This RSS feed is updated on a daily basis, so you can always stay up-to-date on the latest M&A deals and identify potential investment opportunities.

    :param page: The page number for pagination (default is 0).
    :return: A list of dictionaries containing M&A RSS feed data.

    Example:
    >>> mergers_acquisitions_rss_feed(page=1)
    [{'symbol': 'AAPL', 'company': 'Apple Inc.', 'headline': 'Apple Acquires AI Startup', 'date': '2023-10-01', 'url': 'https://example.com/article1', ...}, ...]

    Users can get the latest M&A news and announcements for many different companies by providing the appropriate page number for pagination.

    Endpoint:
    https://financialmodelingprep.com/api/v4/mergers-acquisitions-rss-feed?page={page}

    API Documentation:
    https://site.financialmodelingprep.com/developer/docs/merger-and-acquisition-api
    """
    path = "mergers-acquisitions-rss-feed"
    query_vars = {"apikey": API_KEY, "page": page}
    return __return_json_v4(path=path, query_vars=query_vars)

def search_mergers_acquisitions(name: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /mergers-acquisitions/search/ API.

    Search for M&A deals based on a company name. This endpoint allows users to search for M&A deals that involve a specific company, helping investors and analysts to identify potential investment opportunities and track market consolidations.

    :param name: The name of the company to search for.
    :return: A list of dictionaries containing M&A deal information or None if the request fails.

    Example:
    >>> search_mergers_acquisitions('Apple')
    [{'symbol': 'AAPL', 'company': 'Apple Inc.', 'headline': 'Apple Acquires AI Startup', 'date': '2023-10-01', 'url': 'https://example.com/article1', ...}, ...]

    Users can search for M&A deals involving many different companies by providing the appropriate company name.

    Endpoint:
    https://financialmodelingprep.com/api/v4/mergers-acquisitions/search?name={name}

    API Documentation:
    https://site.financialmodelingprep.com/developer/docs/merger-and-acquisition-api
    """
    path = "mergers-acquisitions/search"
    query_vars = {"apikey": API_KEY, "name": name}
    return __return_json_v4(path=path, query_vars=query_vars)

def executive_compensation(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /governance/executive_compensation API.

    Get detailed information about executive compensation for a specific company.
    
    :param symbol: Ticker symbol of the company.
    :return: A list of dictionaries containing executive compensation data.
    """
    return __return_json_v4("governance/executive_compensation", {"symbol": symbol})

def compensation_benchmark(year: int) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /executive-compensation-benchmark API.

    Compare a company's executive compensation to other companies in the same industry.
    
    :param year: The year for which to retrieve compensation benchmark data.
    :return: A list of dictionaries containing compensation benchmark data.
    """
    return __return_json_v4("executive-compensation-benchmark", {"year": year})

def company_notes(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /company-notes/ API.

    Get information about notes reported by a company in their financial statements. Notes can provide additional information about a company's financial condition, operations, and risks. For example, notes may provide information about a company's accounting policies, legal proceedings, or off-balance sheet items.

    :param symbol: Ticker symbol of the company (e.g., 'AAPL').
    :return: A list of dictionaries containing company notes data or None if the request fails.

    Example:
    >>> company_notes('AAPL')
    [{'date': '2023-01-01', 'symbol': 'AAPL', 'note': 'Apple Inc. reported a legal proceeding...', ...}, ...]

    Users can get detailed notes for many different companies by providing the appropriate ticker symbol.

    Endpoint:
    https://financialmodelingprep.com/api/v4/company-notes?symbol={symbol}

    API Documentation:
    https://site.financialmodelingprep.com/developer/docs/company-notes-due-api
    """
    path = "company-notes"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def historical_employee_count(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical/employee_count API.

    Track how a company's workforce has grown or shrunk over time. This endpoint provides historical data about the number of employees in a company, which can be used to identify trends in a company's growth and efficiency.

    :param symbol: Ticker symbol of the company (e.g., 'AAPL').
    :return: A list of dictionaries containing historical employee count data or None if the request fails.

    Example:
    >>> historical_employee_count('AAPL')
    [{'date': '2023-01-01', 'symbol': 'AAPL', 'employeeCount': 147000, ...}, ...]

    Users can get historical employee data for many different companies by providing the appropriate ticker symbol.

    Endpoint:
    https://financialmodelingprep.com/api/v4/historical/employee_count?symbol={symbol}

    API Documentation:
    https://site.financialmodelingprep.com/developer/docs/historical-numer-of-employees-api
    """
    path = "historical/employee_count"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def employee_count(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /employee_count API.

    Get the current number of employees in a company.
    
    :param symbol: Ticker symbol of the company.
    :return: A list of dictionaries containing current employee count data.
    """
    return __return_json_v4("employee_count", {"symbol": symbol})

def company_core_information(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /company-core-information/ API.

    Get core information about a company, such as CIK, exchange, and address. This information can be used to verify a company's identity or to find additional information about a company.

    :param symbol: Ticker symbol of the company (e.g., 'AAPL').
    :return: A list of dictionaries containing company core information or None if the request fails.

    Example:
    >>> company_core_information('AAPL')
    [{'symbol': 'AAPL', 'cik': '0000320193', 'exchange': 'NASDAQ', 'address': 'One Apple Park Way, Cupertino, CA 95014, United States', ...}, ...]

    Users can get core information for many different companies by providing the appropriate ticker symbol.

    Endpoint:
    https://financialmodelingprep.com/api/v4/company-core-information?symbol={symbol}

    API Documentation:
    https://site.financialmodelingprep.com/developer/docs/company-core-information-api
    """
    path = "company-core-information"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def all_countries() -> typing.Optional[typing.List[str]]:
    """
    Query FMP /get-all-countries API.

    Get a list of all countries where stocks are traded.
    
    :return: A list of country names.
    """
    return __return_json_v3("get-all-countries")

def analyst_recommendation(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /analyst-stock-recommendations/ API.

    Get analyst recommendations for buying, selling, or holding a company's stock. This information helps investors understand what analysts think about a company's stock and make informed investment decisions.

    :param symbol: Ticker symbol of the company (e.g., 'AAPL').
    :return: A list of dictionaries containing analyst recommendations or None if the request fails.

    Example:
    >>> analyst_recommendation('AAPL')
    [{'symbol': 'AAPL', 'analyst': 'Goldman Sachs', 'rating': 'Buy', 'date': '2023-10-01', ...}, ...]

    Users can get analyst recommendations for many different companies by providing the appropriate ticker symbol.

    Endpoint:
    https://financialmodelingprep.com/api/v3/analyst-stock-recommendations/{symbol}

    API Documentation:
    https://site.financialmodelingprep.com/developer/docs/analyst-stock-recommendations-api
    """
    path = f"analyst-stock-recommendations/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def is_market_open(exchange: str = "NASDAQ") -> typing.Optional[typing.Dict]:
    """
    Query FMP /is-the-market-open API.

    Check if a specific market is currently open or closed.
    
    :param exchange: The exchange to check (default is "NASDAQ").
    :return: A dictionary containing market open/close status.
    """
    return __return_json_v3("is-the-market-open", {"exchange": exchange})

def available_sectors() -> typing.Optional[typing.List[str]]:
    """
    Query FMP /sectors-list API.

    Get a list of all sectors available in the FMP database.
    
    :return: A list of sector names.
    """
    return __return_json_v3("sectors-list")

def available_industries() -> typing.Optional[typing.List[str]]:
    """
    Query FMP /industries-list API.

    Get a list of all industries available in the FMP database.
    
    :return: A list of industry names.
    """
    return __return_json_v3("industries-list")

def available_exchanges() -> typing.Optional[typing.List[str]]:
    """
    Query FMP /exchanges-list API.

    Get a list of all exchanges available in the FMP database.
    
    :return: A list of exchange names.
    """
    return __return_json_v3("exchanges-list")

def company_outlook(symbol: str) -> typing.Optional[typing.Dict]:
    """
    Query FMP /company-outlook/ API.

    Get comprehensive company information, including profile, insider trading, and financial statements. This endpoint provides an overview of a company, helping investors to get a comprehensive understanding of a company and to make informed investment decisions.

    :param symbol: Ticker symbol of the company (e.g., 'AAPL').
    :return: A dictionary with company outlook data or None if the request fails.

    Example:
    >>> company_outlook('AAPL')
    {'symbol': 'AAPL', 'profile': {'companyName': 'Apple Inc.', 'industry': 'Technology', 'sector': 'Consumer Electronics', ...}, 'insiderTrading': [...], 'financialStatements': [...], ...}

    Users can get comprehensive company information for many different companies by providing the appropriate ticker symbol.

    Endpoint:
    https://financialmodelingprep.com/api/v4/company-outlook?symbol={symbol}

    API Documentation:
    https://site.financialmodelingprep.com/developer/docs/company-outlook-api
    """
    path = "company-outlook"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

