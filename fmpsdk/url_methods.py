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


def __return_json(path: str, query_vars: typing.Dict) -> typing.List:
    """
    Query URL for JSON response.

    :param path: Path after TLD of URL
    :param query_vars: Dictionary of query values (after "?" of URL)
    :return: JSON response
    """
    response = requests.get(f"{BASE_URL}{path}", params=query_vars)
    if response.text:
        return json.loads(response.text)
    else:
        logging.error("Response appears to have no data.  Returning empty List.")
        return []


def __validate_exchange(value: str) -> str:
    """
    Check to see if passed string is in the list of possible Exchanges.
    :param value: Exchange name.
    :return: Passed value or No Return
    """
    valid_values = EXCHANGE_VALUES
    if value in valid_values:
        return value
    else:
        logging.error(
            f"Invalid exchange value: {value}.  Valid options: {valid_values}"
        )


def __validate_period(value: str) -> str:
    """
    Check to see if passed string is in the list of possible time periods.
    :param value: Period name.
    :return: Passed value or No Return
    """
    valid_values = PERIOD_VALUES
    if value in valid_values:
        return value
    else:
        logging.error(f"Invalid period value: {value}.  Valid options: {valid_values}")


def __validate_sector(value: str) -> str:
    """
    Check to see if passed string is in the list of possible Sectors.
    :param value: Sector name.
    :return: Passed value or No Return
    """
    valid_values = SECTOR_VALUES
    if value in valid_values:
        return value
    else:
        logging.error(f"Invalid sector value: {value}.  Valid options: {valid_values}")


def __validate_industry(value: str) -> str:
    """
    Check to see if passed string is in the list of possible Industries.
    :param value: Industry name.
    :return: Passed value or No Return
    """
    valid_values = INDUSTRY_VALUES
    if value in valid_values:
        return value
    else:
        logging.error(
            f"Invalid industry value: {value}.  Valid options: {valid_values}"
        )


def __validate_time_delta(value: str) -> str:
    """
    Check to see if passed string is in the list of possible Time Deltas.
    :param value: Time Delta name.
    :return: Passed value or No Return
    """
    valid_values = TIME_DELTA_VALUES
    if value in valid_values:
        return value
    else:
        logging.error(
            f"Invalid time_delta value: {value}.  Valid options: {valid_values}"
        )


def __validate_series_type(value: str) -> str:
    """
    Check to see if passed string is in the list of possible Series Type.
    :param value: Series Type name.
    :return: Passed value or No Return
    """
    valid_values = SERIES_TYPE_VALUES
    if value in valid_values:
        return value
    else:
        logging.error(
            f"Invalid series_type value: {value}.  Valid options: {valid_values}"
        )


def __validate_statistics_type(value: str) -> str:
    """
    Check to see if passed string is in the list of possible Statistics Type.
    :param value: Statistics Type name.
    :return: Passed value or No Return
    """
    valid_values = STATISTICS_TYPE_VALUES
    if value in valid_values:
        return value
    else:
        logging.error(
            f"Invalid statistics_type value: {value}.  Valid options: {valid_values}"
        )


def __validate_technical_indicators_time_delta(value: str) -> str:
    """Exactly like set_time_delta() method but adds 'daily' as an option.
    :param value: Indicators Time Delta name.
    :return: Passed value or No Return
    """
    valid_values = TECHNICAL_INDICATORS_TIME_DELTA_VALUES
    if value in valid_values:
        return value
    else:
        logging.error(
            f"Invalid time_delta value: {value}.  Valid options: {valid_values}"
        )
