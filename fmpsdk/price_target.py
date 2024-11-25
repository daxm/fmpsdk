import typing

from .url_methods import __return_json_v4


def price_target(
    apikey: str,
    symbol: str,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /price-target/ API.

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :return: A list of dictionaries.
    """
    path = f"price-target/"
    query_vars = {"apikey": apikey, "symbol": symbol}

    return __return_json_v4(path=path, query_vars=query_vars)


def price_target_summary(
    apikey: str,
    symbol: str,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /social-sentiment/ API.

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :return: A list of dictionaries.
    """
    path = f"price-target-summary/"
    query_vars = {"apikey": apikey, "symbol": symbol}

    return __return_json_v4(path=path, query_vars=query_vars)


def price_target_analyst_name(
    apikey: str,
    name: str,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /price-target-analyst-name/ API.

    :param apikey: Your API key.
    :param name: Analyst Name.
    :return: A list of dictionaries.
    """
    path = f"price-target-analyst-name/"
    query_vars = {"apikey": apikey, "name": name}

    return __return_json_v4(path=path, query_vars=query_vars)


def price_target_analyst_company(
    apikey: str,
    company: str,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /price-target-analyst-company/ API.

    :param apikey: Your API key.
    :param company: Analyst Company Name.
    :return: A list of dictionaries.
    """
    path = f"price-target-analyst-company/"
    query_vars = {"apikey": apikey, "company": company}

    return __return_json_v4(path=path, query_vars=query_vars)


def price_target_consensus(
    apikey: str,
    symbol: str,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /price-target-consensus/ API.

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :return: A list of dictionaries.
    """
    path = f"price-target-consensus/"
    query_vars = {"apikey": apikey, "symbol": symbol}

    return __return_json_v4(path=path, query_vars=query_vars)


