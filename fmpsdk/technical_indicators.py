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
    :param period: Number of data points used to calculate the technical indicator
    :param statistics_type: Type of technical indicator. Available options:
        - SMA (Simple Moving Average)
        - EMA (Exponential Moving Average)
        - WMA (Weighted Moving Average)
        - DEMA (Double Exponential Moving Average)
        - TEMA (Triple Exponential Moving Average)
        - williams (Williams %R)
        - RSI (Relative Strength Index)
        - ADX (Average Directional Index)
        - standardDeviation
    :param time_delta: Time interval for data points. Options:
        - 'daily' for daily data
        - Intraday options: '1min', '5min', '15min', '30min', '1hour', '4hour'
    :return: List of dictionaries containing technical indicator data
    """
    path = f"technical_indicator/{__validate_technical_indicators_time_delta(time_delta)}/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "period": period,
        "type": __validate_statistics_type(statistics_type),
    }
    return __return_json_v3(path=path, query_vars=query_vars)