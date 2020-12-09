import typing
import json
from urllib import parse
from urllib.request import urlopen
import logging
from .settings import BASE_URL, INDUSTRY_VALUES, SECTOR_VALUES, PERIOD_VALUES, EXCHANGE_VALUES, TIME_DELTA_VALUES, \
    SERIES_TYPE_VALUES


def make_url(path: str, query_vars: typing.Dict):
    """
    Stitch component URL parts together.

    :param path: Path after TLD of URL
    :param query_vars: Dictionary of query values (after "?" of URL)
    :return: JSON response
    """
    tmp = parse.urlsplit(BASE_URL)
    url = parse.urlunsplit(
        (tmp.scheme, tmp.netloc, f"{tmp.path}{path}", parse.urlencode(query_vars), "",)
    )
    return url


def return_response(path: str, query_vars: typing.Dict):
    """
    Query URL for JSON response.

    :param path: Path after TLD of URL
    :param query_vars: Dictionary of query values (after "?" of URL)
    :return: JSON response
    """
    response = urlopen(make_url(path=path, query_vars=query_vars))
    data = response.read().decode("utf-8")
    return json.loads(data)


def set_exchange(value: str) -> str:
    valid_values = EXCHANGE_VALUES
    if value in valid_values:
        return value
    else:
        logging.error(f"Invalid exchange value.  Valid options: {valid_values}")


def set_period(value: str) -> str:
    valid_values = PERIOD_VALUES
    if value in valid_values:
        return value
    else:
        logging.error(f"Invalid period value.  Valid options: {valid_values}")


def set_sector(value: str) -> str:
    valid_values = SECTOR_VALUES
    if value in valid_values:
        return value
    else:
        logging.error(f"Invalid sector value.  Valid options: {valid_values}")


def set_industry(value: str) -> str:
    valid_values = INDUSTRY_VALUES
    if value in valid_values:
        return value
    else:
        logging.error(f"Invalid industry value.  Valid options: {valid_values}")


def set_time_delta(value: str) -> str:
    valid_values = TIME_DELTA_VALUES
    if value in valid_values:
        return value
    else:
        logging.error(f"Invalid time_delta value.  Valid options: {valid_values}")


def set_symbol(value: str) -> str:
    if type(value) is list:
        return ','.join(value)
    else:
        return value


def set_series_type(value: str) -> str:
    valid_values = SERIES_TYPE_VALUES
    if value in valid_values:
        return value
    else:
        logging.error(f"Invalid series_type value.  Valid options: {valid_values}")
