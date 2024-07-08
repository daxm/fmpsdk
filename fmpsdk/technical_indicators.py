import typing
import os

from .url_methods import (
    __return_json_v3,
    __validate_statistics_type,
    __validate_technical_indicators_time_delta,
)

API_KEY = os.getenv('FMP_API_KEY')

def technical_indicators(
    symbol: str,
    period: int = 10,
    statistics_type: str = "SMA",
    time_delta: str = "daily",
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /technical_indicator/ API.

    :param symbol: Company ticker
    :param period: I don't know.  10 is my only example.
    :param statistics_type: Not sure what this is.
    :param time_delta: 'daily' or intraday: '1min' - '4hour'
    :return:
    """
    path = f"technical_indicator/{__validate_technical_indicators_time_delta(time_delta)}/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "period": period,
        "type": __validate_statistics_type(statistics_type),
    }
    return __return_json_v3(path=path, query_vars=query_vars)