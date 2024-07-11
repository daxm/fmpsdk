import typing
import os
from .settings import DEFAULT_LIMIT
from .url_methods import __return_json_v3

API_KEY = os.getenv('FMP_API_KEY')

def earning_calendar(
    from_date: str = None, to_date: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /earning_calendar/ API.

    Get a list of upcoming and past earnings announcements for publicly traded companies, including the date, estimated earnings per share (EPS), and actual EPS (if available).

    :param from_date: Start date for the earnings calendar in 'YYYY-MM-DD' format (e.g., '2023-01-01').
    :param to_date: End date for the earnings calendar in 'YYYY-MM-DD' format (e.g., '2023-12-31').
    :return: A list of dictionaries containing earnings calendar data or None if the request fails.

    Example:
    >>> earning_calendar('2023-01-01', '2023-12-31')
    [{'date': '2023-01-25', 'symbol': 'AAPL', 'eps': 1.68, 'epsEstimated': 1.65, 'time': 'amc'}, ...]

    Users can get earnings announcements for many different companies by providing the appropriate date range.

    Endpoint:
    https://financialmodelingprep.com/api/v3/earning_calendar?from={from_date}&to={to_date}

    API Documentation:
    https://site.financialmodelingprep.com/developer/docs/earnings-calendar-api
    """
    path = f"earning_calendar"
    query_vars = {
        "apikey": API_KEY,
    }
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    return __return_json_v3(path=path, query_vars=query_vars)


def historical_earning_calendar(
    symbol: str, limit: int = DEFAULT_LIMIT
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical/earning_calendar/ API.

    Get a list of historical earnings announcements for a specific company, including the date, estimated earnings per share (EPS), and actual EPS.

    :param symbol: Ticker symbol of the company (e.g., 'AAPL').
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :return: A list of dictionaries containing historical earnings data or None if the request fails.

    Example:
    >>> historical_earning_calendar('AAPL', limit=5)
    [{'date': '2023-01-25', 'symbol': 'AAPL', 'eps': 1.68, 'epsEstimated': 1.65, 'time': 'amc'}, ...]

    Users can analyze a company's past earnings performance and identify trends by providing the appropriate ticker symbol and date range.

    Endpoint:
    https://financialmodelingprep.com/api/v3/historical/earning_calendar/{symbol}?limit={limit}

    API Documentation:
    https://site.financialmodelingprep.com/developer/docs/earnings-historical-earnings
    """
    path = f"historical/earning_calendar/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "symbol": symbol,
        "limit": limit,
    }
    return __return_json_v3(path=path, query_vars=query_vars)


def ipo_calendar(
    from_date: str = None, to_date: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /ipo_calendar/ API.

    Note: Between the "from" and "to" parameters the maximum time interval can be 3 months.
    :param from_date: 'YYYY:MM:DD'
    :param to_date: 'YYYY:MM:DD'
    :return: A list of dictionaries.
    """
    path = f"ipo_calendar"
    query_vars = {
        "apikey": API_KEY,
    }
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    return __return_json_v3(path=path, query_vars=query_vars)


def stock_split_calendar(
    from_date: str = None, to_date: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /stock_split_calendar/ API.

    Note: Between the "from" and "to" parameters the maximum time interval can be 3 months.
    :param from_date: 'YYYY:MM:DD'
    :param to_date: 'YYYY:MM:DD'
    :return: A list of dictionaries.
    """
    path = f"stock_split_calendar"
    query_vars = {
        "apikey": API_KEY,
    }
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    return __return_json_v3(path=path, query_vars=query_vars)


def dividend_calendar(
    from_date: str = None, to_date: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /stock_dividend_calendar/ API.

    Note: Between the "from" and "to" parameters the maximum time interval can be 3 months.
    :param from_date: 'YYYY:MM:DD'
    :param to_date: 'YYYY:MM:DD'
    :return: A list of dictionaries.
    """
    path = f"stock_dividend_calendar"
    query_vars = {
        "apikey": API_KEY,
    }
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    return __return_json_v3(path=path, query_vars=query_vars)


def economic_calendar(
    from_date: str = None, to_date: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /economic_calendar/ API.

    Get a calendar of upcoming economic data releases, including dates, times, and descriptions of the events.

    :param from_date: Start date for the economic calendar in 'YYYY-MM-DD' format (e.g., '2023-08-10').
    :param to_date: End date for the economic calendar in 'YYYY-MM-DD' format (e.g., '2023-10-10').
    Note: Between the "from" and "to" parameters the maximum time interval can be 3 months.
    :return: A list of dictionaries containing economic calendar data or None if the request fails.

    Example:
    >>> economic_calendar('2023-08-10', '2023-10-10')
    [{'date': '2023-08-10', 'event': 'CPI', 'country': 'US', 'actual': 0.5, 'forecast': 0.4, 'previous': 0.3}, ...]

    Users can stay up-to-date on the latest economic data releases and prepare for their impact on the market by providing the appropriate date range.

    Endpoint:
    https://financialmodelingprep.com/api/v3/economic_calendar?from={from_date}&to={to_date}

    API Documentation:
    https://site.financialmodelingprep.com/developer/docs/economic-calendar-api
    """
    path = f"economic_calendar"
    query_vars = {
        "apikey": API_KEY,
    }
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    return __return_json_v3(path=path, query_vars=query_vars)