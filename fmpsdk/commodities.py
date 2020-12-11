from .url_methods import __return_json
from .general_methods import (
    __quotes,
    __quote,
    __historical_chart,
    __historical_price_full,
)
import typing


def available_commodities(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /available-commodities/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"available-commodities"
    query_vars = {"apikey": apikey}
    return __return_json(path=path, query_vars=query_vars)


def commodities_list(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP /quotes/commodity/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"quotes/commodity"
    return __quotes(apikey=apikey, value=path)


def commodity_quote(
    apikey: str, symbol: typing.Union[str, typing.List]
) -> typing.List[typing.Dict]:
    """
    Query FMP /quote/ API

    :param apikey: Your API key.
    :param symbol: Commodity ticker
    :return: A list of dictionaries.
    """
    return __quote(apikey=apikey, value=symbol)


def historical_commodity_price(
    apikey: str, symbol: str, time_delta: str
) -> typing.List[typing.Dict]:
    """
    Query FMP /historical-chart/ API.

    :param apikey: Your API key.
    :param symbol: Commodity ticker.
    :param time_delta: The string value of time from now to go historical "1min" - "4hour".
    :return: A list of dictionaries.
    """
    return __historical_chart(apikey=apikey, value=symbol, time_delta=time_delta)


def historical_commodity_price_full(
    apikey: str,
    symbol: typing.Union[str, typing.List],
    time_series: int = None,
    series_type: str = None,
    from_date: str = None,
    to_date: str = None,
) -> typing.List[typing.Dict]:
    """
    Query FMP /historical-price-full/ API.

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :param time_series: Not sure what this is.  5 is my only example.
    :param series_type: Not sure what this is.  'line' is my only example.
    :param from_date: 'YYYY-MM-DD'
    :param to_date: 'YYYY-MM-DD'
    :return: A list of dictionaries.
    """
    return __historical_price_full(
        apikey=apikey,
        value=symbol,
        time_series=time_series,
        series_type=series_type,
        from_date=from_date,
        to_date=to_date,
    )
