import typing
from .url_methods import __return_json_v3, __return_json_v4
import os

API_KEY = os.getenv('FMP_API_KEY')

def treasury_rates(from_date: str, to_date: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Get Treasury rates for a specified date range.

    :param from_date: Start date in YYYY-MM-DD format
    :param to_date: End date in YYYY-MM-DD format
    :return: A list of dictionaries containing Treasury rates data
    """
    path = "treasury"
    query_vars = {"apikey": API_KEY, "from": from_date, "to": to_date}
    return __return_json_v4(path=path, query_vars=query_vars)

def economic_indicators(name: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Get economic indicator data for a specific indicator.

    :param name: Name of the economic indicator (e.g., "GDP", "unemployment")
    :return: A list of dictionaries containing economic indicator data
    """
    path = "economic"
    query_vars = {"apikey": API_KEY, "name": name}
    return __return_json_v4(path=path, query_vars=query_vars)

def market_risk_premium(country: str = None) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /market_risk_premium API for market risk premium data.

    :param country: Optional country name
    :return: A list of dictionaries containing market risk premium data
    """
    path = "market_risk_premium"
    query_vars = {"apikey": API_KEY}
    if country:
        query_vars["country"] = country
    return __return_json_v4(path=path, query_vars=query_vars)