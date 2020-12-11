from .url_methods import __return_json, __validate_exchange
from .general_methods import __quotes, __historical_chart, __historical_price_full
import typing


def quote_short(apikey: str, symbol: str) -> typing.List[typing.Dict]:
    """
    Query FMP /quote-short/ API.

    :param apikey: Your API key
    :param symbol: Company ticker.
    :return: A list of dictionaries.
    """
    path = f"quote-short/{symbol}"
    query_vars = {
        "apikey": apikey,
    }
    return __return_json(path=path, query_vars=query_vars)


def exchange_realtime(apikey: str, exchange: str) -> typing.List[typing.Dict]:
    """
    Query FMP /quotes/ API.

    :param apikey: Your API key
    :param exchange: Exchange symbol.
    :return: A list of dictionaries.
    """
    return __quotes(apikey=apikey, value=__validate_exchange(exchange))


def historical_stock_price(
    apikey: str, symbol: str, time_delta: str
) -> typing.List[typing.Dict]:
    """
    Query FMP /historical-chart/ API.

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :param time_delta: The string value of time from now to go historical "1min" - "4hour".
    :return: A list of dictionaries.
    """
    return __historical_chart(apikey=apikey, value=symbol, time_delta=time_delta)


def historical_stock_price_full(
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


def historical_stock_dividend(apikey: str, symbol: str) -> typing.List[typing.Dict]:
    """
    Query FMP /historical-price-full/stock_divident/ API

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :return: A list of dictionaries.
    """
    return __historical_price_full(
        apikey=apikey, value=f"historical-price-full/stock_dividend/{symbol}",
    )


def historical_stock_split(apikey: str, symbol: str) -> typing.List[typing.Dict]:
    """
    Query FMP /historical-price-full/stock_divident/ API

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :return: A list of dictionaries.
    """
    return __historical_price_full(
        apikey=apikey, value=f"historical-price-full/stock_split/{symbol}",
    )
