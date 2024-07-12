import typing
from .url_methods import __return_json_v3, __return_json_v4
import os
from .settings import (
    DEFAULT_LIMIT,
)
API_KEY = os.getenv('FMP_API_KEY')

def fmp_articles(page: int = 0, size: int = 5) -> typing.Optional[typing.List[typing.Dict]]: 
    """
    Query FMP /fmp/articles/ API.

    Get a list of the latest articles from Financial Modeling Prep, including the headline, snippet, and publication URL.

    :param page: The page number for pagination (default: 0).
    :param size: The number of articles per page (default: 5).
    :return: A list of dictionaries containing FMP articles information or None if the request fails.
    :example: fmp_articles(page=1, size=5)
    :endpoint: https://financialmodelingprep.com/api/v3/fmp/articles?page={page}&size={size}
    """
    path = "fmp/articles"
    query_vars = {"apikey": API_KEY, "page": page, "size": size}
    return __return_json_v3(path=path, query_vars=query_vars)

def general_news(page: int = 0) -> typing.Optional[typing.List[typing.Dict]]: 
    """
    Query FMP /general_news/ API.

    Get a list of the latest general news articles from a variety of sources, including the headline, snippet, and publication URL.

    :param page: The page number for pagination (default: 0).
    :return: A list of dictionaries containing general news articles information or None if the request fails.
    :example: general_news(page=1)
    :endpoint: https://financialmodelingprep.com/api/v4/general_news?page={page}
    """
    path = "general_news"
    query_vars = {"apikey": API_KEY, "page": page}
    return __return_json_v4(path=path, query_vars=query_vars)

def stock_news(tickers: typing.Union[str, typing.List] = "", limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]: 
    """
    Query FMP /stock_news/ API.

    Get a list of the latest stock news articles from a variety of sources, including the headline, snippet, publication URL, and ticker symbol.

    :param tickers: List of ticker symbols or a single ticker symbol (e.g., 'AAPL' or ['AAPL', 'GOOGL']).
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :return: A list of dictionaries containing stock news articles or None if the request fails.
    :example: stock_news(['AAPL', 'GOOGL'], limit=10)
    :endpoint: https://financialmodelingprep.com/api/v3/stock_news?tickers={tickers}&limit={limit}
    """
    path = f"stock_news"
    query_vars = {"apikey": API_KEY, "limit": limit}
    if tickers:
        if type(tickers) is list:
            tickers = ",".join(tickers)
        query_vars["tickers"] = tickers
    return __return_json_v3(path=path, query_vars=query_vars)