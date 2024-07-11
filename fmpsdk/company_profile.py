import typing
import os
from .url_methods import __return_json_v3

API_KEY = os.getenv('FMP_API_KEY')

def company_profile(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /profile/ API for a comprehensive overview of a company.

    :param symbol: Ticker symbol of the company (e.g., 'AAPL').
    :return: List of dictionaries containing company profile data or None if request fails.
    :example: company_profile('AAPL')
    :endpoint: https://financialmodelingprep.com/api/v3/profile/{symbol}
    """
    path = f"profile/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def key_executives(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /key-executives/ API for company's key executives.

    :param symbol: Ticker symbol of the company.
    :return: List of dictionaries containing key executives data or None if request fails.
    :example: key_executives('AAPL')
    :endpoint: https://financialmodelingprep.com/api/v3/key-executives/{symbol}
    """
    path = f"key-executives/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)