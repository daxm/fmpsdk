import typing
import os
from .settings import DEFAULT_LIMIT
from .url_methods import __return_json_v3

API_KEY = os.getenv('FMP_API_KEY')

def earning_calendar(
    from_date: str = None, to_date: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /earning_calendar/ API for upcoming and past earnings announcements.

    :param from_date: Start date in 'YYYY-MM-DD' format.
    :param to_date: End date in 'YYYY-MM-DD' format.
    :return: List of dictionaries with earnings calendar data.
    :example: earning_calendar('2023-01-01', '2023-12-31')
    :endpoint: https://financialmodelingprep.com/api/v3/earning_calendar
    """
    path = f"earning_calendar"
    query_vars = {"apikey": API_KEY}
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    return __return_json_v3(path=path, query_vars=query_vars)

def historical_earning_calendar(
    symbol: str, limit: int = DEFAULT_LIMIT
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical/earning_calendar/ API for historical earnings announcements.

    :param symbol: Ticker symbol of the company.
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :return: List of dictionaries with historical earnings data.
    :example: historical_earning_calendar('AAPL', limit=5)
    :endpoint: https://financialmodelingprep.com/api/v3/historical/earning_calendar/{symbol}
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
    Query FMP /ipo_calendar/ API for IPO calendar.

    :param from_date: Start date in 'YYYY-MM-DD' format.
    :param to_date: End date in 'YYYY-MM-DD' format.
    :return: List of dictionaries with IPO calendar data.
    :example: ipo_calendar('2023-01-01', '2023-03-31')
    :endpoint: https://financialmodelingprep.com/api/v3/ipo_calendar
    Note: Maximum time interval between from_date and to_date is 3 months.
    """
    path = f"ipo_calendar"
    query_vars = {"apikey": API_KEY}
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    return __return_json_v3(path=path, query_vars=query_vars)

def stock_split_calendar(
    from_date: str = None, to_date: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /stock_split_calendar/ API for stock split calendar.

    :param from_date: Start date in 'YYYY-MM-DD' format.
    :param to_date: End date in 'YYYY-MM-DD' format.
    :return: List of dictionaries with stock split calendar data.
    :example: stock_split_calendar('2023-01-01', '2023-03-31')
    :endpoint: https://financialmodelingprep.com/api/v3/stock_split_calendar
    Note: Maximum time interval between from_date and to_date is 3 months.
    """
    path = f"stock_split_calendar"
    query_vars = {"apikey": API_KEY}
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    return __return_json_v3(path=path, query_vars=query_vars)

def dividend_calendar(
    from_date: str = None, to_date: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /stock_dividend_calendar/ API for dividend calendar.

    :param from_date: Start date in 'YYYY-MM-DD' format.
    :param to_date: End date in 'YYYY-MM-DD' format.
    :return: List of dictionaries with dividend calendar data.
    :example: dividend_calendar('2023-01-01', '2023-03-31')
    :endpoint: https://financialmodelingprep.com/api/v3/stock_dividend_calendar
    Note: Maximum time interval between from_date and to_date is 3 months.
    """
    path = f"stock_dividend_calendar"
    query_vars = {"apikey": API_KEY}
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    return __return_json_v3(path=path, query_vars=query_vars)

def economic_calendar(
    from_date: str = None, to_date: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /economic_calendar/ API for economic data releases calendar.

    :param from_date: Start date in 'YYYY-MM-DD' format.
    :param to_date: End date in 'YYYY-MM-DD' format.
    :return: List of dictionaries with economic calendar data.
    :example: economic_calendar('2023-08-10', '2023-10-10')
    :endpoint: https://financialmodelingprep.com/api/v3/economic_calendar
    Note: Maximum time interval between from_date and to_date is 3 months.
    """
    path = f"economic_calendar"
    query_vars = {"apikey": API_KEY}
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    return __return_json_v3(path=path, query_vars=query_vars)