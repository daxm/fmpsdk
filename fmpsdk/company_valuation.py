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

    Gather this company's information.
    :param symbol: Ticker of Company.
    :return: A list of dictionaries.
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
    """
    path = f"key-executives/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def search(query: str = "", limit: int = DEFAULT_LIMIT, exchange: str = "") -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /search/ API.

    Search via ticker and company name.
    :param query: Whole or fragment of Ticker or Name of company.
    :param limit: Number of rows to return.
    :param exchange: Stock exchange to search.
    :return: A list of dictionaries.
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

    Search only via ticker.
    :param query: Whole or fragment of Ticker.
    :param limit: Number of rows to return.
    :param exchange:Stock exchange to search.
    :return: A list of dictionaries.
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
    :return: A list of dictionaries.
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

    Display or download company's income statement.
    :param symbol: Company ticker.
    :param period: 'quarter' or 'annual'.
    :param limit: Number of rows to return.
    :param download: True/False
    :param filename: Name of saved file.
    :return: A list of dictionaries.
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

    Display or download company's balance sheet statement.
    :param symbol: Company ticker.
    :param period: 'quarter' or 'annual'.
    :param limit: Number of rows to return.
    :param download: True/False
    :param filename: Name of saved file.
    :return: A list of dictionaries.
    """
    path = f"balance-sheet-statement/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit, "period": __validate_period(period)}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving {symbol} financial statement as {filename}.")
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

    Display or download company's cash flow statement.
    :param symbol: Company ticker.
    :param period: 'quarter' or 'annual'.
    :param limit: Number of rows to return.
    :param download: True/False
    :param filename: Name of saved file.
    :return: A list of dictionaries.
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
    :return: A list of dictionaries.
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
    :return: A list of dictionaries.
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
    :return: A list of dictionaries.
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
    """
    path = f"financial-statement-full-as-reported/{symbol}"
    query_vars = {"apikey": API_KEY, "period": __validate_period(value=period)}
    return __return_json_v3(path=path, query_vars=query_vars)


def financial_ratios_ttm(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FmP /ratios-ttm/ API.

    :param symbol: Company ticker
    :return: A list of dictionaries.
    """
    path = f"ratios-ttm/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def financial_ratios(symbol: str, period: str = "annual", limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FmP /ratios/ API.

    :param symbol: Company ticker.
    :param period: 'annual' or 'quarter'
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    """
    path = f"ratios/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "limit": limit,
        "period": __validate_period(value=period),
    }
    return __return_json_v3(path=path, query_vars=query_vars)


def enterprise_values(symbol: str, period: str = "annual", limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /enterprise-values/ API.

    :param symbol: Company ticker.
    :param period: 'annual' or 'quarter'
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    """
    path = f"enterprise-values/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "limit": limit,
        "period": __validate_period(value=period),
    }
    return __return_json_v3(path=path, query_vars=query_vars)


def key_metrics_ttm(symbol: str, limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /key-metrics-ttm/ API

    :param symbol: Company ticker.
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    """
    path = f"key-metrics-ttm/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit}
    return __return_json_v3(path=path, query_vars=query_vars)


def key_metrics(symbol: str, period: str = "annual", limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /key-metrics/ API

    :param symbol: Company ticker.
    :param period: 'annual' or 'quarter'
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    """
    path = f"key-metrics/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "limit": limit,
        "period": __validate_period(value=period),
    }
    return __return_json_v3(path=path, query_vars=query_vars)


def financial_growth(symbol: str, period: str = "annual", limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /financial-growth/ API.

    :param symbol: Company ticker.
    :param period: 'annual' or 'quarter'
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
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
    """
    path = f"historical-rating/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit}
    return __return_json_v3(path=path, query_vars=query_vars)


def discounted_cash_flow(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /discounted-cash-flow/ API.

    :param symbol: Company ticker.
    :return: A list of dictionaries.
    """
    path = f"discounted-cash-flow/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def historical_discounted_cash_flow(symbol: str, period: str = "annual", limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical-discounted-cash-flow/ API.

    :param symbol: Company ticker.
    :param period: 'annual' or 'quarter'
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
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
    """
    path = f"historical-daily-discounted-cash-flow/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit}
    return __return_json_v3(path=path, query_vars=query_vars)


def market_capitalization(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /market-capitalization/ API.

    :param symbol: Company ticker.
    :return: A list of dictionaries.
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
    """
    path = f"historical-market-capitalization/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit}
    return __return_json_v3(path=path, query_vars=query_vars)


def symbols_list() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /stock/list/ API

    :return: A list of dictionaries.
    """
    path = f"stock/list"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def etf_list() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /etf/list/ API

    All ETF symbols

    :return: A list of dictionaries.
    """
    path = f"etf/list"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def available_traded_list() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /available-traded/list/ API

    All tradable symbols

    :return: A list of dictionaries.
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

    :param market_cap_more_than: Numeric Value
    :param market_cap_lower_than: Numeric Value
    :param beta_more_than:  Numeric Value
    :param beta_lower_than:  Numeric Value
    :param volume_more_than:  Numeric Value
    :param volume_lower_than:  Numeric Value
    :param dividend_more_than:  Numeric Value
    :param dividend_lower_than:  Numeric Value
    :param price_more_than: Numeric Value
    :param price_lower_than: Numeric Value
    :param price_more_than: Numeric Value
    :param price_lower_than: Numeric Value
    :param is_etf: bool
    :param is_fund: bool
    :param is_actively_trading: bool
    :param sector: Valid sector name.
    :param industry: Valid industry name.
    :param country: 2 digit country code as string.
    :param exchange: Stock exchange symbol.
    :param limit: Number of rows to return.
    :return: A list of dicitonaries.
    """
    path = f"stock-screener"
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
    """
    path = f"delisted-companies"
    query_vars = {"apikey": API_KEY, "limit": limit}
    return __return_json_v3(path=path, query_vars=query_vars)


def stock_news(
    tickers: typing.Union[str, typing.List] = "", limit: int = DEFAULT_LIMIT
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /stock_news/ API.

    :param tickers: List of ticker symbols.
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    """
    path = f"stock_news"
    query_vars = {"apikey": API_KEY, "limit": limit}
    if tickers:
        if type(tickers) is list:
            tickers = ",".join(tickers)
        query_vars["tickers"] = tickers
    return __return_json_v3(path=path, query_vars=query_vars)


def earnings_surprises(
    symbol: str
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /earnings-surprises/ API.

    :param symbol: Company ticker.
    :return: A list of dictionaries.
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
    Query FMP /stock_peers/ API
    :param symbol: Company ticker
    :return: A list of dictionaries
    """
    path = f"stock_peers"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)


def analyst_estimates(
    symbol: str, period: str = "annual", limit: int = DEFAULT_LIMIT
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /analyst-estimates/ API.

    :param symbol: Company ticker.
    :param period: 'annual' or 'quarter'
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    """
    path = f"/analyst-estimates/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "symbol": symbol,
        "period": __validate_period(value=period),
        "limit": limit,
    }
    return __return_json_v3(path=path, query_vars=query_vars)
