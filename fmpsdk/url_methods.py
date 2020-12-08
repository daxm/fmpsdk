import typing
import json
from urllib import parse
from urllib.request import urlopen
import logging


def make_url(base: str, path: str, query_vars: typing.Dict):
    """
    Stitch component URL parts together.

    :param base: First part of the URL
    :param path: Path after TLD of URL
    :param query_vars: Dictionary of query values (after "?" of URL)
    :return: JSON response
    """
    tmp = parse.urlsplit(base)
    url = parse.urlunsplit(
        (tmp.scheme, tmp.netloc, f"{tmp.path}{path}", parse.urlencode(query_vars), "",)
    )
    return url


def return_response(base: str, path: str, query_vars: typing.Dict):
    """
    Query URL for JSON response.

    :param base: First part of the URL
    :param path: Path after TLD of URL
    :param query_vars: Dictionary of query values (after "?" of URL)
    :return: JSON response
    """
    response = urlopen(make_url(base=base, path=path, query_vars=query_vars))
    data = response.read().decode("utf-8")
    return json.loads(data)


def set_exchange(value: str) -> str:
    valid_values = [
        "ETF",
        "MUTUAL_FUND",
        "COMMODITY",
        "INDEX",
        "CRYPTO",
        "FOREX",
        "TSX",
        "AMEX",
        "NASDAQ",
        "NYSE",
        "EURONEXT",
    ]
    if value in valid_values:
        return value
    else:
        logging.error(f"Invalid exchange value.  Valid options: {valid_values}")


def set_period(value: str) -> str:
    valid_values = ["annual", "quarter"]
    if value in valid_values:
        return value
    else:
        logging.error(f"Invalid period value.  Valid options: {valid_values}")
