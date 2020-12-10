from .url_methods import return_json, set_statistics_type, set_technical_indicators_time_delta
import typing


def technical_indicators(
        apikey: str,
        symbol: str,
        period: int = 10,
        statistics_type: str = 'SMA',
        time_delta: str = 'daily',
) -> typing.List[typing.Dict]:
    """
    Query FMP API for Technical Indicators.

    Example:
    https://financialmodelingprep.com/api/v3/technical_indicator/daily/AAPL?period=10&type=ema&apikey=demo
    [ {
        "date" : "2020-09-18",
        "open" : 110.400002,
        "high" : 110.879997,
        "low" : 106.089996,
        "close" : 106.839996,
        "volume" : 2.866936E8,
        "ema" : 113.85965628298615
      }, {
        "date" : "2020-09-17",
        "open" : 109.720001,
        "high" : 112.199997,
        "low" : 108.709999,
        "close" : 110.339996,
        "volume" : 1.78011E8,
        "ema" : 115.41958079031642
      }, {
        "date" : "2020-09-16",
        "open" : 115.230003,
        "high" : 116.0,
        "low" : 112.040001,
        "close" : 112.129997,
        "volume" : 1.54679E8,
        "ema" : 116.54837741038672
      }, ...
    ]
   """
    path = f"technical_indicator/{set_technical_indicators_time_delta(time_delta)}/{symbol}"
    query_vars = {
        "apikey": apikey,
        "period": period,
        "type": set_statistics_type(statistics_type),
    }
    return return_json(path=path, query_vars=query_vars)
