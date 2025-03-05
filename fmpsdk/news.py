import typing
import logging

from .settings import DEFAULT_LIMIT
from .url_methods import __return_json_v3, __return_json_v4


def fmp_articles(
    apikey: str, page: int = 0, size: int = DEFAULT_LIMIT
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /fmp/articles/ API

    :param apikey: Your API key.
    :param page: Page number.
    :param size: Number of rows to return.
    :return: A list of dictionaries.
    """
    path = f"fmp/articles"
    query_vars = {"apikey": apikey, "page": page, "size": size}
    return __return_json_v3(path=path, query_vars=query_vars)


def general_news(
    apikey: str, page: int = 0
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /general_news/ API

    :param apikey: Your API key.
    :param page: Page number.
    :return: A list of dictionaries.
    """
    path = f"general_news"
    query_vars = {"apikey": apikey, "page": page}
    return __return_json_v4(path=path, query_vars=query_vars)


def news_sentiment_rss(
    apikey: str, page: int = 0
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /stock-news-sentiments-rss-feed/ API

    :param apikey: Your API key.
    :param page: Page number.
    :return: A list of dictionaries.
    """
    path = f"stock-news-sentiments-rss-feed"
    query_vars = {"apikey": apikey, "page": page}
    return __return_json_v4(path=path, query_vars=query_vars)


def trending_sentiment(
    apikey: str, type: str, source: str = "stocktwits"
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /social-sentiments/trending/ API

    :param apikey: Your API key.
    :param type: Sentiment type, 'bullish' or 'bearish'.
    :param source: Social media source (e.g. 'stocktwits' or 'twitter'). Default to 'stocktwits'.
    """
    path = "social-sentiments/trending"
    query_vars = {"apikey": apikey, "type": type, "source": source}
    return __return_json_v4(path=path, query_vars=query_vars)


def sentiment_change(
    apikey: str, type: str, source: str = "stocktwits"
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /social-sentiments/change/ API

    :param apikey: Your API key.
    :param type: Sentiment type, 'bullish' or 'bearish'.
    :param source: Social media source (e.g. 'stocktwits' or 'twitter'). Default to 'stocktwits'.
    """
    path = "social-sentiments/change"
    query_vars = {"apikey": apikey, "type": type, "source": source}
    return __return_json_v4(path=path, query_vars=query_vars)


def mergers_acquisitions_rss_feed(
    apikey: str,
    page: int = 0,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /mergers-acquisitions-rss-feed API.

    Get the latest mergers and acquisitions news and announcements.

    https://site.financialmodelingprep.com/developer/docs#mergers-acquisitions-rss-feed

    Endpoint:
        https://financialmodelingprep.com/api/v4/mergers-acquisitions-rss-feed

    :param apikey: Your API key.
    :param page: Page number (default: 0).
    :return: A list of dictionaries containing M&A news data with fields:
             - title: The title of the news article
             - link: URL to the full article
             - pubDate: Publication date
             - description: Article description/summary
             - guid: Unique identifier
             - symbol: Related stock symbol(s)
             - source: News source
             - sentiment: Sentiment analysis score
    """
    if page < 0:
        logging.warning("Page number must be non-negative.")
        return None
    
    path = "mergers-acquisitions-rss-feed"
    query_vars = {"apikey": apikey, "page": page}
    return __return_json_v4(path=path, query_vars=query_vars)
