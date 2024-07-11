import typing
import os

from .settings import (
    DEFAULT_LIMIT,
)
from .url_methods import (
    __return_json_v3,
)

API_KEY = os.getenv('FMP_API_KEY')


def search(query: str = "", limit: int = DEFAULT_LIMIT, exchange: str = "") -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /search/ API for ticker symbols and companies by name or ticker symbol.

    :param query: Whole or fragment of Ticker or Name of company (e.g., 'Apple' or 'AAPL').
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :param exchange: Stock exchange to search (e.g., 'NASDAQ', 'NYSE'). If empty, searches across all exchanges.
    :return: List of dictionaries containing search results or None if the request fails.
    :example: search('Apple', limit=10, exchange='NASDAQ')
    :endpoint: https://financialmodelingprep.com/api/v3/search?query={query}&limit={limit}&exchange={exchange}
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
    Query FMP /search-ticker/ API for ticker symbols by company name or ticker symbol.

    :param query: Whole or fragment of Ticker or Name of company (e.g., 'AAPL' or 'Apple').
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :param exchange: Stock exchange to search (e.g., 'NASDAQ', 'NYSE'). If empty, searches across all exchanges.
    :return: List of dictionaries containing search results or None if the request fails.
    :example: search_ticker('AAPL', limit=10, exchange='NASDAQ')
    :endpoint: https://financialmodelingprep.com/api/v3/search-ticker?query={query}&limit={limit}&exchange={exchange}
    """
    path = f"search-ticker/"
    query_vars = {
        "apikey": API_KEY,
        "limit": limit,
        "query": query,
        "exchange": exchange,
    }
    return __return_json_v3(path=path, query_vars=query_vars)