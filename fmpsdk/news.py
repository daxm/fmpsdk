import typing
from .url_methods import __return_json_v3, __return_json_v4
import os
from .settings import DEFAULT_LIMIT
from .data_compression import compress_json_to_tsv

API_KEY = os.getenv('FMP_API_KEY')


def fmp_articles(
    page: int = 0,
    size: int = 25,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve the latest articles from Financial Modeling Prep.

    Provides access to FMP's latest financial news and analysis articles.
    Useful for staying updated on market trends, company news, and financial insights.

    :param page: Page number for pagination (default: 0).
    :param size: Number of articles per page (default: 25).
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with article data.
    :example: fmp_articles(page=1, size=5)
    """
    path = "fmp/articles"
    query_vars = {"apikey": API_KEY, "page": page, "size": size}
    result = __return_json_v3(path=path, query_vars=query_vars)
    result = result["content"]
    return compress_json_to_tsv(result) if tsv else result


def general_news(
    pages: int = 20,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve the latest general news articles from a variety of sources.

    Provides access to a daily-updated list of general news articles.
    Useful for staying informed on current events and market trends.
    Each article includes headline, snippet, and publication URL.

    :param pages: Number of pages to retrieve. Default is 20 which will 
    typically cover 24 hours of news.
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with general news data.
    :example: general_news(pages=5)
    """
    path = "general_news"
    all_results = []

    for page in range(pages):
        query_vars = {"apikey": API_KEY, "page": page}
        result = __return_json_v4(path=path, query_vars=query_vars)
        all_results.extend(result)

    return compress_json_to_tsv(all_results) if tsv else all_results


def stock_news(
    tickers: typing.Union[str, typing.List] = "",
    limit: int = 25,
    page: int = 0,
    from_date: str = "",
    to_date: str = "",
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve the latest stock-specific news articles from various sources.

    Provides news articles related to specific stocks or companies, including
    headline, snippet, publication URL, and ticker symbol. Updated daily to
    offer the most current stock market news.

    :param tickers: Ticker symbol(s) (e.g., 'AAPL' or ['AAPL', 'FB']).
    :param limit: Number of results per page (default: 25).
    :param page: Page number for pagination (default: 0).
    :param from_date: Start date for news articles (format: YYYY-MM-DD).
    :param to_date: End date for news articles (format: YYYY-MM-DD).
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with stock news data.
    :example: stock_news(['AAPL', 'FB'], limit=10, page=3, from_date='2024-01-01', to_date='2024-03-01')
    """
    path = "stock_news"
    query_vars = {"apikey": API_KEY, "limit": limit, "page": page}
    if tickers:
        query_vars["tickers"] = ",".join(tickers) if isinstance(tickers, list) else tickers
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tsv(result) if tsv else result


def mergers_acquisitions_rss_feed(
    page: int = 0,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve the latest M&A news RSS feed.

    Provides insights into mergers, acquisitions, and other corporate transactions.

    :param page: Page number for pagination. Default is 0.
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with latest M&A news RSS feed data.
    :example: mergers_acquisitions_rss_feed(page=1)
    """
    path = "mergers-acquisitions-rss-feed"
    query_vars = {"apikey": API_KEY, "page": page}
    result = __return_json_v4(path=path, query_vars=query_vars)
    return compress_json_to_tsv(result) if tsv else result


def upgrades_downgrades_rss_feed(
    page: int = 0,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve daily-updated RSS feed of stock upgrades and downgrades from various analysts.

    Provides the latest analyst ratings to help investors stay informed about
    changing market sentiments and potential investment opportunities.

    :param page: Page number for pagination. Default is 0.
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with latest stock upgrades and downgrades data.
    :example: upgrades_downgrades_rss_feed(page=1)
    """
    path = "upgrades-downgrades-rss-feed"
    query_vars = {"apikey": API_KEY, "page": page}
    result = __return_json_v4(path=path, query_vars=query_vars)
    return compress_json_to_tsv(result) if tsv else result


def upgrades_downgrades(
    symbol: str,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve a comprehensive list of stock upgrades and downgrades for a company.

    Provides insights into analysts' changing expectations for a stock's performance.
    Updated daily to offer the most current analyst ratings.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with upgrade/downgrade data.
    :example: upgrades_downgrades('AAPL')
    """
    path = "upgrades-downgrades"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    result = __return_json_v4(path=path, query_vars=query_vars)
    return compress_json_to_tsv(result) if tsv else result


def press_releases(
    symbol: str = None,
    limit: int = DEFAULT_LIMIT,
    page: int = 0,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve the latest press releases, optionally filtered by company.

    Provides detailed information about company announcements, including
    release date, title, and content. Useful for staying updated on important
    developments and news from organizations.

    :param symbol: Company ticker (e.g., 'AAPL'). If None, returns releases for all companies.
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :param page: Page number for pagination. Default is 0.
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with press releases data.
    :example: press_releases(symbol='AAPL', limit=10, page=0)
              press_releases(limit=20, page=1)
    """
    path = f"press-releases/{symbol}" if symbol else "press-releases"
    query_vars = {"apikey": API_KEY, "limit": limit, "page": page}
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tsv(result) if tsv else result