import typing
from .url_methods import __return_json_v3, __return_json_v4
import os

API_KEY = os.getenv('FMP_API_KEY')

def treasury_rates(from_date: str = None, to_date: str = None) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /treasury API for Treasury rates data.

    Provides real-time and historical Treasury rates for all maturities.

    :param from_date: Optional start date in YYYY-MM-DD format
    :param to_date: Optional end date in YYYY-MM-DD format
    :return: A list of dictionaries containing Treasury rates data
    :example: treasury_rates()
    :example: treasury_rates('2023-01-01', '2023-12-31')
    :endpoint: https://financialmodelingprep.com/api/v4/treasury
    """
    path = "treasury"
    query_vars = {"apikey": API_KEY}
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    return __return_json_v4(path=path, query_vars=query_vars)

def economic_indicators(name: str, from_date: str = None, to_date: str = None) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /economic API for economic indicator data.

    Provides real-time and historical economic data for various economic indicators. This endpoint allows tracking the performance of the economy over time, identifying trends in economic growth, and making informed investment decisions based on economic data.

    :param name: Name of the economic indicator (e.g., 'GDP', 'CPI', 'unemploymentRate')
    :param from_date: Optional start date in YYYY-MM-DD format
    :param to_date: Optional end date in YYYY-MM-DD format
    :return: A list of dictionaries containing economic indicator data
    :example: economic_indicators('GDP')
    :example: economic_indicators('CPI', '2023-01-01', '2023-12-31')
    :note: For a full list of available indicators, refer to the FMP documentation
    :endpoint: https://financialmodelingprep.com/api/v4/economic
    """
    path = "economic"
    query_vars = {"apikey": API_KEY, "name": name}
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    return __return_json_v4(path=path, query_vars=query_vars)

def market_risk_premium(country: str = None) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /market_risk_premium API for market risk premium data.

    :param country: Optional country name
    :return: A list of dictionaries containing market risk premium data
    :example: market_risk_premium()
    :example: market_risk_premium('United States')
    :endpoint: https://financialmodelingprep.com/api/v4/market_risk_premium
    """
    path = "market_risk_premium"
    query_vars = {"apikey": API_KEY}
    if country:
        query_vars["country"] = country
    return __return_json_v4(path=path, query_vars=query_vars)