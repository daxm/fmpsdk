import typing

from .settings import DEFAULT_LIMIT
from .url_methods import __return_json_v4, __return_json_v3


def social_sentiment(
    apikey: str,
    symbol: str,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /social-sentiment/ API.

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :return: A list of dictionaries.
    """
    path = f"historical/social-sentiment/"
    query_vars = {"apikey": apikey, "symbol": symbol}

    return __return_json_v4(path=path, query_vars=query_vars)


def trending_social_sentiment(
    apikey: str,
    type: str,
    source: str,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /social-sentiment/ API.

    :param apikey: Your API key.
    :param type: Type of trend. Either 'bullish' or 'bearish'.
    :param source: Source of information. Either "twitter" or "stocktwits".
    :return: A list of dictionaries.
    """
    path = f"social-sentiments/trending/"
    query_vars = {"apikey": apikey, "type": type, "source": source}

    return __return_json_v4(path=path, query_vars=query_vars)

def change_social_sentiment(
    apikey: str,
    type: str,
    source: str,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /social-sentiment/ API.

    :param apikey: Your API key.
    :param type: Type of change.
    :param source: Source of information
    :return: A list of dictionaries.
    """
    path = f"social-sentiments/change/"
    query_vars = {"apikey": apikey, "type": type.value, "source": source.value}

    return __return_json_v4(path=path, query_vars=query_vars)


def stock_grade(
    apikey: str,
    symbol: str,
    limit: int = DEFAULT_LIMIT,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /stock_grade/ API.

    :param apikey: Your API key.
    :param stock: Company ticker.
    :param limit: Number of records to return.
    :return: A list of dictionaries.
    """
    path = f"grade/{symbol}/"
    query_vars = {"apikey": apikey, "limit": limit}

    return __return_json_v3(path=path, query_vars=query_vars)





