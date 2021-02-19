from .settings import (
    BASE_URL,
    DEFAULT_LIMIT,
    FINANCIAL_STATEMENT_FILENAME,
    CASH_FLOW_STATEMENT_FILENAME,
    INCOME_STATEMENT_FILENAME,
    BALANCE_SHEET_STATEMENT_FILENAME,
    INCOME_STATEMENT_AS_REPORTED_FILENAME,
    BALANCE_SHEET_STATEMENT_AS_REPORTED_FILENAME,
    CASH_FLOW_STATEMENT_AS_REPORTED_FILENAME,
    SEC_RSS_FEEDS_FILENAME,
    SP500_CONSTITUENTS_FILENAME,
    NASDAQ_CONSTITUENTS_FILENAME,
    DOWJONES_CONSTITUENTS_FILENAME,
)
from .url_methods import (
    __return_json,
    __validate_sector,
    __validate_period,
    __validate_industry,
    __validate_exchange,
    __validate_statistics_type,
    __validate_technical_indicators_time_delta,
    __validate_time_delta,
    __validate_series_type,
)
import requests
import typing
import logging

attribution: str = "Data provided by Financial Modeling Prep"
logging.info(attribution)


# # # # # # # # # # # # # # # # # General Functions # # # # # # # # # # # # # # # # #
def __quotes(apikey: str, value: str) -> typing.List[typing.Dict]:
    """
    Query FMP /quotes/ API.

    This API endpoint is a multifunction tool!
    :param apikey: Your API key
    :param value: The Ticker(s), Index(es), Commodity(ies), etc. symbol to query for.
    :return: A list of dictionaries.
    """
    path = f"quotes/{value}"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def quote(
    apikey: str, symbol: typing.Union[str, typing.List[str]]
) -> typing.List[typing.Dict]:
    """
    Query FMP Quote API.

    This API endpoint is a multifunction tool!

    :param apikey: Your API key
    :param symbol: The Ticker(s), Index(es), Commodity(ies), etc. symbol to query for.
    :return: A list of dictionaries.
    """
    if type(symbol) is list:
        symbol = ",".join(symbol)
    path = f"quote/{symbol}"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def historical_chart(
    apikey: str, symbol: str, time_delta: str
) -> typing.List[typing.Dict]:
    """
    Query FMP Historical Chart API.

    This API endpoint is a multifunction tool!

    :param apikey: Your API key
    :param symbol: The Ticker, Index, Commodity, etc. symbol to query for.
    :param time_delta: The string value of time from now to go historical "1min" - "4hour".
    :return: A list of dictionaries.
    """
    path = f"historical-chart/{__validate_time_delta(time_delta)}/{symbol}"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def historical_price_full(
    apikey: str,
    symbol: typing.Union[str, typing.List],
    time_series: int = None,
    series_type: str = None,
    from_date: str = None,
    to_date: str = None,
) -> typing.List[typing.Dict]:
    """
    Query FMP Historical Price Full API.

    This API endpoint is a multifunction tool!

    :param apikey: Your API Key
    :param symbol: The Ticker, Index, Commodity, etc. symbol to query for.
    :param time_series: Not sure what this is.  5 is the only value I've seen used.
    :param series_type: Not sure what this is.  "line" is the only option I've seen used.
    :param from_date: 'YYYY-MM-DD' format
    :param to_date: 'YYYY-MM-DD' format
    :return: A list of dictionaries.
    """
    if type(symbol) is list:
        symbol = ",".join(symbol)
    path = f"historical-price-full/{symbol}"
    query_vars = {
        "apikey": apikey,
    }
    if time_series:
        query_vars["timeseries"] = time_series
    if series_type:
        query_vars["serietype"] = __validate_series_type(series_type)
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    return __return_json(path=path, query_vars=query_vars)


# # # # # # # # # # # # # # # # # Company Valuation Functions # # # # # # # # # # # # # # # # #
def company_profile(apikey: str, symbol: str) -> typing.List[typing.Dict]:
    """
    Query FMP /profile/ API.

    Gather this company's information.
    :param apikey: Your API key.
    :param symbol: Ticker of Company.
    """
    path = f"profile/{symbol}"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def key_executives(apikey: str, symbol: str) -> typing.List[typing.Dict]:
    """
    Query FMP /key-executives/ API.

    Gather info about company's key executives.
    :param apikey: Your API Key.
    :param symbol: Ticker of company.
    :return: A list of dictionaries.
    """
    path = f"key-executives/{symbol}"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def search(
    apikey: str, query: str = "", limit: int = DEFAULT_LIMIT, exchange: str = ""
) -> typing.List[typing.Dict]:
    """
    Query FMP /search/ API.

    Search via ticker and company name.
    :param apikey: Your API key.
    :param query: Whole or fragment of Ticker or Name of company.
    :param limit: Number of rows to return.
    :param exchange: Stock exchange to search.
    :return: A list of dictionaries.
    """
    path = f"search/"
    query_vars = {
        "apikey": apikey,
        "limit": limit,
        "query": query,
        "exchange": __validate_exchange(value=exchange),
    }
    return __return_json(path=path, query_vars=query_vars)


def search_ticker(
    apikey: str, query: str = "", limit: int = DEFAULT_LIMIT, exchange: str = ""
) -> typing.List[typing.Dict]:
    """
    Query FMP /search-ticker/ API.

    Search only via ticker.
    :param apikey: Your API key.
    :param query: Whole or fragment of Ticker.
    :param limit: Number of rows to return.
    :param exchange:Stock exchange to search.
    :return: A list of dictionaries.
    """
    path = f"search-ticker/"
    query_vars = {
        "apikey": apikey,
        "limit": limit,
        "query": query,
        "exchange": __validate_exchange(value=exchange),
    }
    return __return_json(path=path, query_vars=query_vars)


def financial_statement(
    apikey: str, symbol: str, filename: str = FINANCIAL_STATEMENT_FILENAME
) -> None:
    """
    Query FMP /financial-statements/ API.

    Download company's financial statement.
    :param apikey: Your API key.
    :param symbol: Ticker of company.
    :param filename: Name of saved file.
    :return: A list of dictionaries.
    """
    path = f"financial-statements/{symbol}"
    query_vars = {
        "apikey": apikey,
        "datatype": "zip",  # Only ZIP format is supported.
    }
    response = requests.get(f"{BASE_URL}{path}", params=query_vars)
    open(filename, "wb").write(response.content)
    logging.info(f"Saving {symbol} financial statement as {filename}.")


def income_statement(
    apikey: str,
    symbol: str,
    period: str = "annual",
    limit: int = DEFAULT_LIMIT,
    download: bool = False,
    filename: str = INCOME_STATEMENT_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP /income-statement/ API.

    Display or download company's income statement.
    :param apikey: Your API key.
    :param symbol: Company ticker.
    :param period: 'quarter' or 'annual'.
    :param limit: Number of rows to return.
    :param download: True/False
    :param filename: Name of saved file.
    :return: A list of dictionaries.
    """
    path = f"income-statement/{symbol}"
    query_vars = {"apikey": apikey, "limit": limit, "period": __validate_period(period)}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving {symbol} financial statement as {filename}.")
    else:
        return __return_json(path=path, query_vars=query_vars)


def balance_sheet_statement(
    apikey: str,
    symbol: str,
    period: str = "annual",
    limit: int = DEFAULT_LIMIT,
    download: bool = False,
    filename: str = BALANCE_SHEET_STATEMENT_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP /balance-sheet-statement/ API.

    Display or download company's balance sheet statement.
    :param apikey: Your API key.
    :param symbol: Company ticker.
    :param period: 'quarter' or 'annual'.
    :param limit: Number of rows to return.
    :param download: True/False
    :param filename: Name of saved file.
    :return: A list of dictionaries.
    """
    path = f"balance-sheet-statement/{symbol}"
    query_vars = {"apikey": apikey, "limit": limit, "period": __validate_period(period)}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving {symbol} financial statement as {filename}.")
    else:
        return __return_json(path=path, query_vars=query_vars)


def cash_flow_statement(
    apikey: str,
    symbol: str,
    period: str = "annual",
    limit: int = DEFAULT_LIMIT,
    download: bool = False,
    filename: str = CASH_FLOW_STATEMENT_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP /cash-flow-statement/ API.

    Display or download company's cash flow statement.
    :param apikey: Your API key.
    :param symbol: Company ticker.
    :param period: 'quarter' or 'annual'.
    :param limit: Number of rows to return.
    :param download: True/False
    :param filename: Name of saved file.
    :return: A list of dictionaries.
    """
    path = f"cash-flow-statement/{symbol}"
    query_vars = {"apikey": apikey, "limit": limit, "period": __validate_period(period)}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving {symbol} financial statement as {filename}.")
    else:
        return __return_json(path=path, query_vars=query_vars)


def financial_statement_symbol_lists(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /financial-statement-symbol-lists/ API.

    List of symbols that have financial statements.
    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"financial-statement-symbol-lists"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def income_statement_growth(
    apikey: str,
    symbol: str,
    limit: int = DEFAULT_LIMIT,
) -> typing.List[typing.Dict]:
    """
    Query FMP /income-statement-growth/ API.

    Growth stats for company's income statement.
    :param apikey: Your API key.
    :param symbol: Company ticker.
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    """
    path = f"income-statement-growth/{symbol}"
    query_vars = {
        "apikey": apikey,
        "limit": limit,
    }
    return __return_json(path=path, query_vars=query_vars)


def balance_sheet_statement_growth(
    apikey: str, symbol: str, limit: int = DEFAULT_LIMIT
) -> typing.List[typing.Dict]:
    """
    Query FMP /balance-sheet-statement-growth/ API.

    Growth stats for company's balance sheet statement.
    :param apikey: Your API key.
    :param symbol: Company ticker.
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    """
    path = f"balance-sheet-statement-growth/{symbol}"
    query_vars = {
        "apikey": apikey,
        "limit": limit,
    }
    return __return_json(path=path, query_vars=query_vars)


def cash_flow_statement_growth(
    apikey: str, symbol: str, limit: int = DEFAULT_LIMIT
) -> typing.List[typing.Dict]:
    """
    Query FMP /cash-flow-statement-growth/ API.

    Growth stats for company's cash flow statement.
    :param apikey: Your API key.
    :param symbol: Company ticker.
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    """
    path = f"cash-flow-statement-growth/{symbol}"
    query_vars = {
        "apikey": apikey,
        "limit": limit,
    }
    return __return_json(path=path, query_vars=query_vars)


def income_statement_as_reported(
    apikey: str,
    symbol: str,
    period: str = "annual",
    limit: int = DEFAULT_LIMIT,
    download: bool = False,
    filename: str = INCOME_STATEMENT_AS_REPORTED_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP /income-statement-as-reported/ API.

    Company's "as reported" income statement.
    :param apikey: Your API key.
    :param symbol: Company ticker.
    :param period: 'annual' or 'quarter'
    :param limit: Number of rows to return.
    :param download: True/False
    :param filename: Name of saved file.
    :return: A list of dictionaries.
    """
    path = f"income-statement-as-reported/{symbol}"
    query_vars = {
        "apikey": apikey,
        "limit": limit,
        "period": __validate_period(value=period),
    }
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving {symbol} financial statement as {filename}.")
    else:
        return __return_json(path=path, query_vars=query_vars)


def balance_sheet_statement_as_reported(
    apikey: str,
    symbol: str,
    period: str = "annual",
    limit: int = DEFAULT_LIMIT,
    download: bool = False,
    filename: str = BALANCE_SHEET_STATEMENT_AS_REPORTED_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP /balance-sheet-statement-as-reported/ API.

    Company's "as reported" balance sheet statement.
    :param apikey: Your API key.
    :param symbol: Company ticker.
    :param period: 'annual' or 'quarter'
    :param limit: Number of rows to return.
    :param download: True/False
    :param filename: Name of saved file.
    :return: A list of dictionaries.
    """
    path = f"balance-sheet-statement-as-reported/{symbol}"
    query_vars = {
        "apikey": apikey,
        "limit": limit,
        "period": __validate_period(value=period),
    }
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving {symbol} financial statement as {filename}.")
    else:
        return __return_json(path=path, query_vars=query_vars)


def cash_flow_statement_as_reported(
    apikey: str,
    symbol: str,
    period: str = "annual",
    limit: int = DEFAULT_LIMIT,
    download: bool = False,
    filename: str = CASH_FLOW_STATEMENT_AS_REPORTED_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP /cash-flow-statement-as-reported/ API.

    Company's "as reported" cash flow statement.
    :param apikey: Your API key.
    :param symbol: Company ticker.
    :param period: 'annual' or 'quarter'
    :param limit: Number of rows to return.
    :param download: True/False
    :param filename: Name of saved file.
    :return: A list of dictionaries.
    """
    path = f"cash-flow-statement-as-reported/{symbol}"
    query_vars = {
        "apikey": apikey,
        "limit": limit,
        "period": __validate_period(value=period),
    }
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving {symbol} financial statement as {filename}.")
    else:
        return __return_json(path=path, query_vars=query_vars)


def financial_statement_full_as_reported(
    apikey: str,
    symbol: str,
    period: str = "annual",
) -> typing.List[typing.Dict]:
    """
    Query FMP /financial-statement-full-as-reported/ API.

    Company's "as reported" full income statement.
    :param apikey: Your API key.
    :param symbol: Company ticker.
    :param period: 'annual' or 'quarter'
    :return: A list of dictionaries.
    """
    path = f"financial-statement-full-as-reported/{symbol}"
    query_vars = {"apikey": apikey, "period": __validate_period(value=period)}
    return __return_json(path=path, query_vars=query_vars)


def financial_ratios_ttm(apikey: str, symbol: str) -> typing.List[typing.Dict]:
    """
    Query FmP /ratios-ttm/ API.

    :param apikey: Your API key
    :param symbol: Company ticker
    :return: A list of dictionaries.
    """
    path = f"ratios-ttm/{symbol}"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def financial_ratios(
    apikey: str,
    symbol: str,
    period: str = "annual",
    limit: int = DEFAULT_LIMIT,
) -> typing.List[typing.Dict]:
    """
    Query FmP /ratios/ API.

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :param period: 'annual' or 'quarter'
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    """
    path = f"ratios/{symbol}"
    query_vars = {
        "apikey": apikey,
        "limit": limit,
        "period": __validate_period(value=period),
    }
    return __return_json(path=path, query_vars=query_vars)


def enterprise_values(
    apikey: str,
    symbol: str,
    period: str = "annual",
    limit: int = DEFAULT_LIMIT,
) -> typing.List[typing.Dict]:
    """
    Query FMP /enterprise-values/ API.

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :param period: 'annual' or 'quarter'
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    """
    path = f"enterprise-values/{symbol}"
    query_vars = {
        "apikey": apikey,
        "limit": limit,
        "period": __validate_period(value=period),
    }
    return __return_json(path=path, query_vars=query_vars)


def key_metrics_ttm(
    apikey: str,
    symbol: str,
    limit: int = DEFAULT_LIMIT,
) -> typing.List[typing.Dict]:
    """
    Query FMP /key-metrics-ttm/ API

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    """
    path = f"key-metrics-ttm/{symbol}"
    query_vars = {"apikey": apikey, "limit": limit}
    return __return_json(path=path, query_vars=query_vars)


def key_metrics(
    apikey: str,
    symbol: str,
    period: str = "annual",
    limit: int = DEFAULT_LIMIT,
) -> typing.List[typing.Dict]:
    """
    Query FMP /key-metrics/ API

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :param period: 'annual' or 'quarter'
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    """
    path = f"key-metrics/{symbol}"
    query_vars = {
        "apikey": apikey,
        "limit": limit,
        "period": __validate_period(value=period),
    }
    return __return_json(path=path, query_vars=query_vars)


def financial_growth(
    apikey: str,
    symbol: str,
    period: str = "annual",
    limit: int = DEFAULT_LIMIT,
) -> typing.List[typing.Dict]:
    """
    Query FMP /financial-growth/ API.

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :param period: 'annual' or 'quarter'
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    """
    path = f"financial-growth/{symbol}"
    query_vars = {
        "apikey": apikey,
        "limit": limit,
        "period": __validate_period(value=period),
    }
    return __return_json(path=path, query_vars=query_vars)


def rating(apikey: str, symbol: str) -> typing.List[typing.Dict]:
    """
    Query FMP /rating/ API.

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :return: A list of dictionaries.
    """
    path = f"rating/{symbol}"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def historical_rating(
    apikey: str,
    symbol: str,
    limit: int = DEFAULT_LIMIT,
) -> typing.List[typing.Dict]:
    """
    Query FMP /financial-growth/ API.

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    """
    path = f"financial-growth/{symbol}"
    query_vars = {"apikey": apikey, "limit": limit}
    return __return_json(path=path, query_vars=query_vars)


def discounted_cash_flow(apikey: str, symbol: str) -> typing.List[typing.Dict]:
    """
    Query FMP /discounted-cash-flow/ API.

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :return: A list of dictionaries.
    """
    path = f"discounted-cash-flow/{symbol}"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def historical_discounted_cash_flow(
    apikey: str,
    symbol: str,
    period: str = "annual",
    limit: int = DEFAULT_LIMIT,
) -> typing.List[typing.Dict]:
    """
    Query FMP /historical-discounted-cash-flow/ API.

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :param period: 'annual' or 'quarter'
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    """
    path = f"historical-discounted-cash-flow/{symbol}"
    query_vars = {
        "apikey": apikey,
        "limit": limit,
        "period": __validate_period(value=period),
    }
    return __return_json(path=path, query_vars=query_vars)


def historical_daily_discounted_cash_flow(
    apikey: str, symbol: str, limit: int = DEFAULT_LIMIT
) -> typing.List[typing.Dict]:
    """
    Query FMP /historical-daily-discounted-cash-flow/ API.

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    """
    path = f"historical-daily-discounted-cash-flow/{symbol}"
    query_vars = {"apikey": apikey, "limit": limit}
    return __return_json(path=path, query_vars=query_vars)


def market_capitalization(apikey: str, symbol: str) -> typing.List[typing.Dict]:
    """
    Query FMP /market-capitalization/ API.

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :return: A list of dictionaries.
    """
    path = f"market-capitalization/{symbol}"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def historical_market_capitalization(
    apikey: str, symbol: str, limit: int = DEFAULT_LIMIT
) -> typing.List[typing.Dict]:
    """
    Query FMP /historical-market-capitalization/ API.

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    """
    path = f"historical-market-capitalization/{symbol}"
    query_vars = {"apikey": apikey, "limit": limit}
    return __return_json(path=path, query_vars=query_vars)


def symbols_list(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /stock/list/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"stock/list"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def stock_screener(
    apikey: str,
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
    is_ETF: bool = None,
    is_actively_trading: bool = None,
    sector: str = None,
    industry: str = None,
    exchange: typing.Union[str, typing.List[str]] = None,
    limit: int = DEFAULT_LIMIT,
) -> typing.List[typing.Dict]:
    """
    Query FMP /stock-screener/ API.

    :param apikey: Your API key.
    :param market_cap_more_than: Numeric Value
    :param market_cap_lower_than: Numeric Value
    :param beta_more_than:  Numeric Value
    :param beta_lower_than:  Numeric Value
    :param volume_more_than:  Numeric Value
    :param volume_lower_than:  Numeric Value
    :param dividend_more_than:  Numeric Value
    :param dividend_lower_than:  Numeric Value
    :price_more_than: Numeric Value
    :price_lower_than: Numeric Value
    :is_ETF: bool
    :is_actively_trading: bool
    :param sector: Valid sector name.
    :param industry: Valid industry name.
    :param exchange: Stock exchange symbol.
    :param limit: Number of rows to return.
    :return: A list of dicitonaries.
    """
    path = f"stock-screener"
    query_vars = {"apikey": apikey, "limit": limit}
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
    if is_ETF:
        query_vars["isEtf"] = is_ETF
    if is_actively_trading:
        query_vars["isActivelyTrading"] = is_actively_trading
    if sector:
        query_vars["sector"] = __validate_sector(sector)
    if industry:
        query_vars["industry"] = __validate_industry(industry)
    if exchange:
        if type(exchange) is list:
            for item in exchange:
                if item != __validate_exchange(item):
                    logging.error(f"Invalid Exchange value: {exchange}.")
                    exit(1)
            query_vars["exchange"] = ",".join(exchange)
        else:
            query_vars["exchange"] = __validate_exchange(exchange)
    return __return_json(path=path, query_vars=query_vars)


def delisted_companies(
    apikey: str, limit: int = DEFAULT_LIMIT
) -> typing.List[typing.Dict]:
    """
    Query FMP /delisted-companies/ API.

    :param apikey: Your API key.
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    """
    path = f"delisted-companies"
    query_vars = {"apikey": apikey, "limt": limit}
    return __return_json(path=path, query_vars=query_vars)


def stock_news(
    apikey: str,
    tickers: typing.Union[str, typing.List] = "",
    limit: int = DEFAULT_LIMIT,
) -> typing.List[typing.Dict]:
    """
    Query FMP /stock_news/ API.

    :param apikey: Your API key.
    :param tickers: List of ticker symbols.
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    """
    path = f"stock_news"
    query_vars = {"apikey": apikey, "limt": limit}
    if tickers:
        if type(tickers) is list:
            tickers = ",".join(tickers)
        query_vars["tickers"] = tickers
    return __return_json(path=path, query_vars=query_vars)


def earnings_surprises(apikey: str, symbol: str) -> typing.List[typing.Dict]:
    """
    Query FMP /earnings-surprises/ API.

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :return: A list of dictionaries.
    """
    path = f"earnings-surprises/{symbol}"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def sec_filings(
    apikey: str, symbol: str, filing_type: str = "", limit: int = DEFAULT_LIMIT
) -> typing.List[typing.Dict]:
    """
    Query FMP /sec_filings/ API.

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :param filing_type: Name of filing.
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    """
    path = f"sec_filings/{symbol}"
    query_vars = {"apikey": apikey, "type": filing_type, "limit": limit}
    return __return_json(path=path, query_vars=query_vars)


def press_releases(
    apikey: str, symbol: str, limit: int = DEFAULT_LIMIT
) -> typing.List[typing.Dict]:
    """
    Query FMP /press-releases/ API.

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    """
    path = f"press-releases/{symbol}"
    query_vars = {"apikey": apikey, "limit": limit}
    return __return_json(path=path, query_vars=query_vars)


# # # # # # # # # # # # # # # # # Calendar Functions # # # # # # # # # # # # # # # # #
def earning_calendar(
    apikey: str, from_date: str = None, to_date: str = None
) -> typing.List[typing.Dict]:
    """
    Query FMP /earning_calendar/ API.

    Note: Between the "from" and "to" parameters the maximum time interval can be 3 months.
    :param apikey: Your API key.
    :param from_date: 'YYYY:MM:DD'
    :param to_date: 'YYYY:MM:DD'
    :return: A list of dictionaries.
    """
    path = f"earning_calendar"
    query_vars = {
        "apikey": apikey,
    }
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    return __return_json(path=path, query_vars=query_vars)


def historical_earning_calendar(
    apikey: str, symbol: str, limit: int = DEFAULT_LIMIT
) -> typing.List[typing.Dict]:
    """
    Query FMP /historical/earning_calendar/ API.

    Note: Between the "from" and "to" parameters the maximum time interval can be 3 months.
    :param apikey: Your API key.
    :param symbol: Company ticker.
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    """
    path = f"historical/earning_calendar/{symbol}"
    query_vars = {
        "apikey": apikey,
        "symbol": symbol,
        "limit": limit,
    }
    return __return_json(path=path, query_vars=query_vars)


def ipo_calendar(
    apikey: str, from_date: str = None, to_date: str = None
) -> typing.List[typing.Dict]:
    """
    Query FMP /ipo_calendar/ API.

    Note: Between the "from" and "to" parameters the maximum time interval can be 3 months.
    :param apikey: Your API key.
    :param from_date: 'YYYY:MM:DD'
    :param to_date: 'YYYY:MM:DD'
    :return: A list of dictionaries.
    """
    path = f"ipo_calendar"
    query_vars = {
        "apikey": apikey,
    }
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    return __return_json(path=path, query_vars=query_vars)


def stock_split_calendar(
    apikey: str, from_date: str = None, to_date: str = None
) -> typing.List[typing.Dict]:
    """
    Query FMP /stock_split_calendar/ API.

    Note: Between the "from" and "to" parameters the maximum time interval can be 3 months.
    :param apikey: Your API key.
    :param from_date: 'YYYY:MM:DD'
    :param to_date: 'YYYY:MM:DD'
    :return: A list of dictionaries.
    """
    path = f"stock_split_calendar"
    query_vars = {
        "apikey": apikey,
    }
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    return __return_json(path=path, query_vars=query_vars)


def dividend_calendar(
    apikey: str, from_date: str = None, to_date: str = None
) -> typing.List[typing.Dict]:
    """
    Query FMP /stock_dividend_calendar/ API.

    Note: Between the "from" and "to" parameters the maximum time interval can be 3 months.
    :param apikey: Your API key.
    :param from_date: 'YYYY:MM:DD'
    :param to_date: 'YYYY:MM:DD'
    :return: A list of dictionaries.
    """
    path = f"stock_dividend_calendar"
    query_vars = {
        "apikey": apikey,
    }
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    return __return_json(path=path, query_vars=query_vars)


def economic_calendar(
    apikey: str, from_date: str = None, to_date: str = None
) -> typing.List[typing.Dict]:
    """
    Query FMP /economic_calendar/ API.

    Note: Between the "from" and "to" parameters the maximum time interval can be 3 months.
    :param apikey: Your API key.
    :param from_date: 'YYYY:MM:DD'
    :param to_date: 'YYYY:MM:DD'
    :return: A list of dictionaries.
    """
    path = f"economic_calendar"
    query_vars = {
        "apikey": apikey,
    }
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    return __return_json(path=path, query_vars=query_vars)


# # # # # # # # # # # # # # # # # Institutional Fund Functions # # # # # # # # # # # # # # # # #
def institutional_holders(apikey: str, symbol: str) -> typing.List[typing.Dict]:
    """
    Query FMP /institutional-holder/ API.

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :return: A list of dictionaries.
    """
    path = f"institutional-holder/{symbol}"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def mutual_fund_holders(apikey: str, symbol: str) -> typing.List[typing.Dict]:
    """
    Query FMP /mutual-fund-holder/ API.

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :return: A list of dictionaries.
    """
    path = f"mutual-fund-holder/{symbol}"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def etf_holders(apikey: str, symbol: str) -> typing.List[typing.Dict]:
    """
    Query FMP /etf-holder/ API.

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :return: A list of dictionaries.
    """
    path = f"etf-holder/{symbol}"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def etf_sector_weightings(apikey: str, symbol: str) -> typing.List[typing.Dict]:
    """
    Query FMP /etf-sector-weightings/ API.

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :return: A list of dictionaries.
    """
    path = f"etf-sector-weightings/{symbol}"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def etf_country_weightings(apikey: str, symbol: str) -> typing.List[typing.Dict]:
    """
    Query FMP /etf-country-weightings/ API.

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :return: A list of dictionaries.
    """
    path = f"etf-country-weightings/{symbol}"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def sec_rss_feeds(
    apikey: str,
    limit: int = DEFAULT_LIMIT,
    download: bool = False,
    filename: str = SEC_RSS_FEEDS_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP /rss_feed/ API.

    :param apikey: Your API key.
    :param limit: Number of rows to return.
    :param download: True/False
    :param filename: Name of saved file.
    :return: A list of dictionaries.
    """
    path = f"rss_feed"
    query_vars = {"apikey": apikey}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving SEC RSS Feeds as {filename}.")
    else:
        query_vars["limit"] = limit
        return __return_json(path=path, query_vars=query_vars)


def cik_list(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /cik_list/ API.

    Complete list of all institutional investment managers by cik
    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"cik_list"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def cik_search(apikey: str, name: str) -> typing.List[typing.Dict]:
    """
    Query FMP /cik-search/ API.

    FORM 13F cik search by name
    :param apikey: Your API key.
    :param name: Name
    :return: A list of dictionaries.
    """
    path = f"cik-search/{name}"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def cik(apikey: str, cik_id: str) -> typing.List[typing.Dict]:
    """
    Query FMP /cik/ API.

    FORM 13F get company name by cik
    :param apikey: Your API key.
    :param cik_id: CIK value
    :return: A list of dictionaries.
    """
    path = f"cik/{cik_id}"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def form_13f(apikey: str, cik_id: str, date: str = None) -> typing.List[typing.Dict]:
    """
    Query FMP /form-thirteen/ API.

    FORM 13F statements provides position-level report of all institutional investment managers with more than $100m
    in assets under management.
    :param apikey: Your API key.
    :param cik_id: CIK value
    :param date: 'YYYY-MM-DD'
    :return: A list of dictionaries.
    """
    path = f"form-thirteen/{cik_id}"
    query_vars = {"apikey": apikey}
    if date:
        query_vars["date"] = date
    return __return_json(path=path, query_vars=query_vars)


def cusip(apikey: str, cik_id: str) -> typing.List[typing.Dict]:
    """
    Query FMP /cusip/ API.

    Cusip mapper
    :param apikey: Your API key.
    :param cik_id: CIK value
    :return: A list of dictionaries.
    """
    path = f"cusip/{cik_id}"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


# # # # # # # # # # # # # # # # # Stock Time Series Functions # # # # # # # # # # # # # # # # #
def quote_short(apikey: str, symbol: str) -> typing.List[typing.Dict]:
    """
    Query FMP /quote-short/ API.

    :param apikey: Your API key
    :param symbol: Company ticker.
    :return: A list of dictionaries.
    """
    path = f"quote-short/{symbol}"
    query_vars = {
        "apikey": apikey,
    }
    return __return_json(path=path, query_vars=query_vars)


def exchange_realtime(apikey: str, exchange: str) -> typing.List[typing.Dict]:
    """
    Query FMP /quotes/ API.

    :param apikey: Your API key
    :param exchange: Exchange symbol.
    :return: A list of dictionaries.
    """
    return __quotes(apikey=apikey, value=__validate_exchange(exchange))


def historical_stock_dividend(apikey: str, symbol: str) -> typing.List[typing.Dict]:
    """
    Query FMP /historical-price-full/stock_divident/ API

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :return: A list of dictionaries.
    """
    path = f"historical-price-full/stock_dividend/{symbol}"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def historical_stock_split(apikey: str, symbol: str) -> typing.List[typing.Dict]:
    """
    Query FMP /historical-price-full/stock_divident/ API

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :return: A list of dictionaries.
    """
    path = f"historical-price-full/stock_split/{symbol}"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


# # # # # # # # # # # # # # # # # Technical Indicators Functions # # # # # # # # # # # # # # # # #
def technical_indicators(
    apikey: str,
    symbol: str,
    period: int = 10,
    statistics_type: str = "SMA",
    time_delta: str = "daily",
) -> typing.List[typing.Dict]:
    """
    Query FMP /technical_indicator/ API.

    :param apikey: Your API key
    :param symbol: Company ticker
    :param period: I don't know.  10 is my only example.
    :param statistics_type: Not sure what this is.
    :param time_delta: 'daily' or intraday: '1min' - '4hour'
    :return:
    """
    path = f"technical_indicator/{__validate_technical_indicators_time_delta(time_delta)}/{symbol}"
    query_vars = {
        "apikey": apikey,
        "period": period,
        "type": __validate_statistics_type(statistics_type),
    }
    return __return_json(path=path, query_vars=query_vars)


# # # # # # # # # # # # # # # # # Market Indexes Functions # # # # # # # # # # # # # # # # #
def indexes(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /quotes/index/ API.

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"index"
    return __quotes(apikey=apikey, value=path)


def sp500_constituent(
    apikey: str,
    download: bool = False,
    filename: str = SP500_CONSTITUENTS_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP /sp500_constituent/ API

    :param apikey: Your API key.
    :param download: True/False
    :param filename: Name of saved file.
    :return: A list of dictionaries.
    """
    path = f"sp500_constituent"
    query_vars = {"apikey": apikey}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving SP500 Constituents as {filename}.")
    else:
        return __return_json(path=path, query_vars=query_vars)


def historical_sp500_constituent(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /historical/sp500_constitnuet/ API.

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"historical/sp500_constituent"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def nasdaq_constituent(
    apikey: str,
    download: bool = False,
    filename: str = NASDAQ_CONSTITUENTS_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP /nasdaq_constituent/ API

    :param apikey: Your API key.
    :param download: True/False
    :param filename: Name of saved file.
    :return: A list of dictionaries.
    """
    path = f"nasdaq_constituent"
    query_vars = {"apikey": apikey}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving NASDAQ Constituents as {filename}.")
    else:
        return __return_json(path=path, query_vars=query_vars)


def historical_nasdaq_constituent(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /historical/nasdaq_constitnuet/ API.

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"historical/nasdaq_constituent"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def dowjones_constituent(
    apikey: str,
    download: bool = False,
    filename: str = DOWJONES_CONSTITUENTS_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP /dowjones_constituent/ API

    :param apikey: Your API key.
    :param download: True/False
    :param filename: Name of saved file.
    :return: A list of dictionaries.
    """
    path = f"dowjones_constituent"
    query_vars = {"apikey": apikey}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving DOWJONES Constituents as {filename}.")
    else:
        return __return_json(path=path, query_vars=query_vars)


def historical_dowjones_constituent(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /historical/dowjones_constitnuet/ API.

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"historical/dowjones_constituent"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def available_indexes(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /symbol/available-indexes/ API

    :param apikey: Your API key
    :return: A list of dictionaries.
    """
    path = f"symbol/available-indexes"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


# # # # # # # # # # # # # # # # # Commodities Functions # # # # # # # # # # # # # # # # #
def available_commodities(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /symbol/available-commodities/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"symbol/available-commodities"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def commodities_list(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /quotes/commodity/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"commodity"
    return __quotes(apikey=apikey, value=path)


# # # # # # # # # # # # # # # # # ETF Functions # # # # # # # # # # # # # # # # #
def available_efts(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /symbol/available-etfs/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"symbol/available-etfs"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def etf_list(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /quotes/etf/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"etf"
    return __quotes(apikey=apikey, value=path)


# # # # # # # # # # # # # # # # # Mutual Funds Functions # # # # # # # # # # # # # # # # #
def available_mutual_funds(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /symbol/available-mutual-funds/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"symbol/available-mutual-funds"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def mutual_fund_list(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /quotes/mutual_fund/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"mutual_fund"
    return __quotes(apikey=apikey, value=path)


# # # # # # # # # # # # # # # # # EuroNext Functions # # # # # # # # # # # # # # # # #
def available_euronext(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /symbol/available-euronext/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"symbol/available-euronext"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def euronext_list(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /quotes/euronext/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"euronext"
    return __quotes(apikey=apikey, value=path)


# # # # # # # # # # # # # # # # # TSX Functions # # # # # # # # # # # # # # # # #
def available_tsx(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /symbol/available-tsx/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"symbol/available-tsx"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def tsx_list(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /quotes/tsx/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"tsx"
    return __quotes(apikey=apikey, value=path)


# # # # # # # # # # # # # # # # # Stock Market Functions # # # # # # # # # # # # # # # # #
def actives(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /actives/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"actives"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def gainers(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /gainers/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"gainers"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def losers(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /losers/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"losers"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def market_hours(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /market-hours/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"market-hours"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def sectors_performance(
    apikey: str, limit: int = DEFAULT_LIMIT
) -> typing.List[typing.Dict]:
    """
    Query FMP /sectors_performance/ API

    :param apikey: Your API key.
    :param limit: Number of rows to return
    :return: A list of dictionaries.
    """
    path = f"sectors-performance"
    query_vars = {"apikey": apikey, "limit": limit}
    return __return_json(path=path, query_vars=query_vars)


# # # # # # # # # # # # # # # # # Cryptocurrencies Functions # # # # # # # # # # # # # # # # #
def available_cryptocurrencies(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /symbol/available-cryptocurrencies/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"symbol/available-cryptocurrencies"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def cryptocurrencies_list(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /quotes/crypto/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"crypto"
    return __quotes(apikey=apikey, value=path)


# # # # # # # # # # # # # # # # # FOREX (FX) Functions # # # # # # # # # # # # # # # # #
def forex(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /fx/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"fx"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def forex_list(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /quotes/forex/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"forex"
    return __quotes(apikey=apikey, value=path)


def available_forex(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /symbol/available-forex-currency-pairs/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"symbol/available-forex-currency-pairs"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)
