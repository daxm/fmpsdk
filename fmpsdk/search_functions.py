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
    Search for companies, stocks, ETFs, and other financial instruments.
    NOTE: This is NOT a general search function. It is only for financial instruments.

    Supports over 85,000 symbols including stocks, ETFs, cryptocurrencies,
    forex, and indexes. Results include company name, ticker, and exchange.

    :param query: Full or partial name/ticker (e.g., 'Apple' or 'AAPL')
    :param limit: Number of results to return (default: DEFAULT_LIMIT)
    :param exchange: Filter by exchange (e.g., 'NASDAQ', 'NYSE')
    :return: List of dicts with search results or None if request fails
    :example: search('Apple', limit=10, exchange='NASDAQ')
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
    Search for ticker symbols, company names, and exchange details.

    Retrieves information for equity securities and ETFs listed on various
    exchanges. Useful for finding specific assets when the symbol or name
    is known.

    :param query: Full or partial ticker/company name (e.g., 'AAPL' or 'Apple')
    :param limit: Number of results to return (default: 10)
    :param exchange: Filter by exchange (e.g., 'NASDAQ', 'NYSE')
    :return: List of dicts with search results or None if request fails
    :example: search_ticker('AAPL', limit=10, exchange='NASDAQ')
    """
    path = f"search-ticker/"
    query_vars = {
        "apikey": API_KEY,
        "limit": limit,
        "query": query,
        "exchange": exchange,
    }
    return __return_json_v3(path=path, query_vars=query_vars)