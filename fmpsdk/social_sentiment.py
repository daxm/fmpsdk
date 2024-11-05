import typing
from .url_methods import __return_json_v4
from .data_compression import compress_json_to_tsv
import os

API_KEY = os.getenv('FMP_API_KEY')


def historical_social_sentiment(
    symbol: str,
    page: int = 0,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve historical social sentiment data for a company.

    Provides insights into public perception of a company over time, useful for:
    - Tracking sentiment trends
    - Identifying potential market reactions
    - Informing investment decisions

    Social sentiment is derived from analyzing social media, news, and online content.

    :param symbol: The stock symbol (e.g., 'AAPL')
    :param page: The page number for pagination (default: 0)
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with historical social sentiment data,
             or None if request fails
    """
    path = "historical/social-sentiment"
    query_vars = {"apikey": API_KEY, "symbol": symbol, "page": page}
    result = __return_json_v4(path=path, query_vars=query_vars)
    
    fields = ('date', 'symbol', 'stocktwitsPosts', 'twitterPosts', 'stocktwitsComments',
              'twitterComments', 'stocktwitsLikes', 'twitterLikes', 'stocktwitsImpressions',
              'twitterImpressions', 'stocktwitsSentiment', 'twitterSentiment')
    
    return compress_json_to_tsv(result, fields) if tsv else result


def trending_social_sentiment(
    sentiment_type: str = "bullish",
    source: str = "stocktwits",
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve trending social sentiment data for stocks.

    This function provides insights into current market sentiment trends, useful for:
    - Identifying popular stocks among social media users
    - Gauging overall market sentiment
    - Spotting potential trading opportunities

    :param sentiment_type: Type of sentiment to retrieve (default: 'bullish')
                           Options: 'bullish' or 'bearish'
    :param source: Source of sentiment data (default: 'stocktwits')
                   Options: 'stocktwits' or 'twitter'
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with trending social sentiment data,
             or None if request fails
    """
    path = "social-sentiments/trending"
    query_vars = {"apikey": API_KEY, "type": sentiment_type, "source": source}
    result = __return_json_v4(path=path, query_vars=query_vars)
    
    fields = ('symbol', 'name', 'stocktwitsPosts', 'twitterPosts', 'stocktwitsComments',
              'twitterComments', 'stocktwitsLikes', 'twitterLikes', 'stocktwitsImpressions',
              'twitterImpressions', 'stocktwitsSentiment', 'twitterSentiment')
    
    return compress_json_to_tsv(result, fields) if tsv else result


def social_sentiment_changes(
    sentiment_type: str = "bullish",
    source: str = "stocktwits",
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve changes in social sentiment data over time for various stocks.

    Useful for:
    - Identifying shifts in market sentiment
    - Spotting emerging trends
    - Comparing sentiment changes across different stocks

    :param sentiment_type: Type of sentiment to analyze (default: 'bullish')
                           Options: 'bullish' or 'bearish'
    :param source: Source of sentiment data (default: 'stocktwits')
                   Options: 'stocktwits' or 'twitter'
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with social sentiment changes data,
             or None if request fails
    """
    path = "social-sentiments/change"
    query_vars = {"apikey": API_KEY, "type": sentiment_type, "source": source}
    result = __return_json_v4(path=path, query_vars=query_vars)
    
    fields = ('symbol', 'name', 'change', 'stocktwitsPosts', 'twitterPosts',
              'stocktwitsComments', 'twitterComments', 'stocktwitsLikes',
              'twitterLikes', 'stocktwitsImpressions', 'twitterImpressions',
              'stocktwitsSentiment', 'twitterSentiment')
    
    return compress_json_to_tsv(result, fields) if tsv else result