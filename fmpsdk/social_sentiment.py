import typing
from .url_methods import __return_json_v4
import os

API_KEY = os.getenv('FMP_API_KEY')

def historical_social_sentiment(symbol: str, page: int = 0) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Get historical social sentiment data for a given ticker or company name.

    :param symbol: The stock symbol (e.g., 'AAPL')
    :param page: The page number for pagination (default: 0)
    :return: A list of dictionaries containing historical social sentiment data
    """
    path = "historical/social-sentiment"
    query_vars = {"apikey": API_KEY, "symbol": symbol, "page": page}
    return __return_json_v4(path=path, query_vars=query_vars)

def trending_social_sentiment(sentiment_type: str = "bullish", source: str = "stocktwits") -> typing.Optional[typing.List[typing.Dict]]:
    """
    Get trending social sentiment data.

    :param sentiment_type: The type of sentiment (default: 'bullish')
    :param source: The source of sentiment data (default: 'stocktwits')
    :return: A list of dictionaries containing trending social sentiment data
    """
    path = "social-sentiments/trending"
    query_vars = {"apikey": API_KEY, "type": sentiment_type, "source": source}
    return __return_json_v4(path=path, query_vars=query_vars)

def social_sentiment_changes(sentiment_type: str = "bullish", source: str = "stocktwits") -> typing.Optional[typing.List[typing.Dict]]:
    """
    Get changes in social sentiment data over a period of time.

    :param sentiment_type: The type of sentiment (default: 'bullish')
    :param source: The source of sentiment data (default: 'stocktwits')
    :return: A list of dictionaries containing social sentiment changes data
    """
    path = "social-sentiments/change"
    query_vars = {"apikey": API_KEY, "type": sentiment_type, "source": source}
    return __return_json_v4(path=path, query_vars=query_vars)