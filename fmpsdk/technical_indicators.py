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

    :param symbol: Company ticker.
    :param period: Number of data points used to calculate the technical indicator.
    :param statistics_type: Type of technical indicator. Available options:
        - sma (simple moving average)
        - ema (exponential moving average)
        - wma (weighted moving average)
        - dema (double exponential moving average)
        - tema (triple exponential moving average)
        - williams (williams %r)
        - rsi (relative strength index)
        - adx (average directional index)
        - standarddeviation
    :param time_delta: Time interval for data points. Options:
        - 'daily' for daily data
        - Intraday options: '1min', '5min', '15min', '30min', '1hour', '4hour'
    :return: List of dictionaries containing technical indicator data or None if the request fails.
    :example: technical_indicators('AAPL', period=10, statistics_type='SMA', time_delta='daily')
    :endpoint: https://financialmodelingprep.com/api/v3/technical_indicator/{time_delta}/{symbol}
    """
    path = f"technical_indicator/{__validate_technical_indicators_time_delta(time_delta)}/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "period": period,
        "type": __validate_statistics_type(statistics_type),
    }
    return __return_json_v3(path=path, query_vars=query_vars)