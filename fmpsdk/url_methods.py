import typing
import json
import requests
import logging
from .settings import (
    BASE_URL,
    INDUSTRY_VALUES,
    SECTOR_VALUES,
    PERIOD_VALUES,
    EXCHANGE_VALUES,
    TIME_DELTA_VALUES,
    SERIES_TYPE_VALUES,
    STATISTICS_TYPE_VALUES,
    TECHNICAL_INDICATORS_TIME_DELTA_VALUES,
)


def __return_json(path: str, query_vars: typing.Dict):
    """
    Query URL for JSON response.

    :param path: Path after TLD of URL
    :param query_vars: Dictionary of query values (after "?" of URL)
    :return: JSON response
    """
    response = requests.get(f"{BASE_URL}{path}", params=query_vars)
    return json.loads(response.text)


def __validate_exchange(value: str) -> str:
    valid_values = EXCHANGE_VALUES
    if value in valid_values:
        return value
    else:
        logging.error(
            f"Invalid exchange value: {value}.  Valid options: {valid_values}"
        )


def __validate_period(value: str) -> str:
    valid_values = PERIOD_VALUES
    if value in valid_values:
        return value
    else:
        logging.error(f"Invalid period value: {value}.  Valid options: {valid_values}")


def __validate_sector(value: str) -> str:
    valid_values = SECTOR_VALUES
    if value in valid_values:
        return value
    else:
        logging.error(f"Invalid sector value: {value}.  Valid options: {valid_values}")


def __validate_industry(value: str) -> str:
    valid_values = INDUSTRY_VALUES
    if value in valid_values:
        return value
    else:
        logging.error(
            f"Invalid industry value: {value}.  Valid options: {valid_values}"
        )


def __validate_time_delta(value: str) -> str:
    valid_values = TIME_DELTA_VALUES
    if value in valid_values:
        return value
    else:
        logging.error(
            f"Invalid time_delta value: {value}.  Valid options: {valid_values}"
        )


def __validate_series_type(value: str) -> str:
    valid_values = SERIES_TYPE_VALUES
    if value in valid_values:
        return value
    else:
        logging.error(
            f"Invalid series_type value: {value}.  Valid options: {valid_values}"
        )


def __validate_statistics_type(value: str) -> str:
    valid_values = STATISTICS_TYPE_VALUES
    if value in valid_values:
        return value
    else:
        logging.error(
            f"Invalid statistics_type value: {value}.  Valid options: {valid_values}"
        )


def __validate_technical_indicators_time_delta(value: str) -> str:
    """Exactly like set_time_delta() method but adds 'daily' as an option"""
    valid_values = TECHNICAL_INDICATORS_TIME_DELTA_VALUES
    if value in valid_values:
        return value
    else:
        logging.error(
            f"Invalid time_delta value: {value}.  Valid options: {valid_values}"
        )
