import typing
import logging

from .settings import DEFAULT_LIMIT
from .url_methods import __return_json_v3, __return_json_v4


def earning_calendar(
    apikey: str, from_date: str = None, to_date: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
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
    return __return_json_v3(path=path, query_vars=query_vars)


def historical_earning_calendar(
    apikey: str, symbol: str, limit: int = DEFAULT_LIMIT
) -> typing.Optional[typing.List[typing.Dict]]:
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
    return __return_json_v3(path=path, query_vars=query_vars)


def ipo_calendar(
    apikey: str, from_date: str = None, to_date: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
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
    return __return_json_v3(path=path, query_vars=query_vars)


def stock_split_calendar(
    apikey: str, from_date: str = None, to_date: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
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
    return __return_json_v3(path=path, query_vars=query_vars)


def dividend_calendar(
    apikey: str, from_date: str = None, to_date: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
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
    return __return_json_v3(path=path, query_vars=query_vars)


def economic_calendar(
    apikey: str, from_date: str = None, to_date: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
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
    return __return_json_v3(path=path, query_vars=query_vars)


def earning_calendar_confirmed(
    apikey: str,
    from_date: str = None,
    to_date: str = None,
    limit: int = DEFAULT_LIMIT,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /earning-calendar-confirmed API.

    Get confirmed earnings announcement dates for companies.

    https://site.financialmodelingprep.com/developer/docs#earnings-calendar-confirmed

    Endpoint:
        https://financialmodelingprep.com/api/v4/earning-calendar-confirmed

    :param apikey: Your API key.
    :param from_date: The start date in "YYYY-MM-DD" format.
    :param to_date: The end date in "YYYY-MM-DD" format.
    :param limit: Number of records to return.
    :return: A list of dictionaries containing confirmed earnings data with fields:
             - symbol: The stock symbol
             - date: The confirmed earnings date
             - time: The time of the earnings announcement
             - exchange: The stock exchange
             - beforeAfterMarket: Whether the announcement is before/after market
             - currency: The currency of the financials
             - reportedEPS: The reported earnings per share
             - estimatedEPS: The estimated earnings per share
             - revenueEstimated: The estimated revenue
             - numberOfEstimates: Number of analyst estimates
             - EPSAveragePrediction: Average EPS prediction
    """
    path = "earning-calendar-confirmed"
    query_vars = {"apikey": apikey, "limit": limit}
    
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    
    return __return_json_v4(path=path, query_vars=query_vars)


def ipo_calendar_confirmed(
    apikey: str,
    from_date: str,
    to_date: str,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /ipo-calendar-confirmed API.

    Get confirmed IPO dates for companies.

    https://site.financialmodelingprep.com/developer/docs#ipo-calendar-confirmed

    Endpoint:
        https://financialmodelingprep.com/api/v4/ipo-calendar-confirmed

    :param apikey: Your API key.
    :param from_date: The start date in "YYYY-MM-DD" format (required).
    :param to_date: The end date in "YYYY-MM-DD" format (required).
    :return: A list of dictionaries containing confirmed IPO data with fields:
             - symbol: The stock symbol
             - date: The confirmed IPO date
             - exchange: The stock exchange
             - name: The company name
             - currency: The currency of the IPO
             - price: The IPO price
             - shares: Number of shares offered
             - marketCap: Market capitalization at IPO
             - sector: Company sector
             - industry: Company industry
    """
    if not from_date or not to_date:
        logging.warning("Both from_date and to_date are required for IPO calendar confirmed request.")
        return None
    
    path = "ipo-calendar-confirmed"
    query_vars = {
        "apikey": apikey,
        "from": from_date,
        "to": to_date
    }
    return __return_json_v4(path=path, query_vars=query_vars)
