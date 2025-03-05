import typing
import logging

from .general import __quotes
from .settings import DEFAULT_LIMIT
from .url_methods import __return_json_v3, __return_json_v4


def available_cryptocurrencies(
    apikey: str,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /symbol/available-cryptocurrencies/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"symbol/available-cryptocurrencies"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def cryptocurrencies_list(apikey: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /quotes/crypto/ API

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"crypto"
    return __quotes(apikey=apikey, value=path)


def crypto_news(
    apikey: str,
    symbol: str = None,
    from_date: str = None,
    to_date: str = None,
    page: int = 0,
    limit: int = DEFAULT_LIMIT,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /crypto_news/ API.

    :param apikey: Your API key.
    :param symbol: A forex symbol.
    :param from_date: The starting time for the API ("yyyy-mm-dd").
    :param to_date: The ending time for the API ("yyyy-mm-dd")
    :param page: Page number.
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    """
    path = f"crypto_news"
    query_vars = {"apikey": apikey, "page": page, "limit": limit}
    if symbol:
        query_vars["symbol"] = symbol
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date

    return __return_json_v4(path=path, query_vars=query_vars)


def last_crypto_price(apikey: str, symbol: str) -> typing.Optional[typing.Dict]:
    """
    Query FMP /crypto/last/ API.

    Get the latest price for a cryptocurrency.

    https://site.financialmodelingprep.com/developer/docs#crypto-last-price

    Endpoint:
        https://financialmodelingprep.com/api/v4/crypto/last/{symbol}

    :param apikey: Your API key.
    :param symbol: Cryptocurrency symbol (e.g., BTCUSD).
    :return: A dictionary containing the latest price data with fields:
             - symbol: The cryptocurrency symbol
             - price: The current price
             - volume: The trading volume
             - timestamp: The timestamp of the price
    """
    if not symbol:
        logging.warning("No symbol provided for last crypto price request.")
        return None
    
    path = f"crypto/last/{symbol}"
    query_vars = {"apikey": apikey}
    return __return_json_v4(path=path, query_vars=query_vars)
