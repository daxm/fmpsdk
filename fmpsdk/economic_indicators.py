import typing

from .url_methods import __return_json_v4, __validate_economic_indicator


def economic_indicator(
    apikey: str,
    name: str,
    from_date: str = None,
    to_date: str = None,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /economic/ API for economic indicators.

    :param apikey: Your API key
    :param name: Name of the economic indicator (e.g., 'GDP', 'CPI', 'inflationRate', etc.)
    :param from_date: From date in 'YYYY-MM-DD' format
    :param to_date: To date in 'YYYY-MM-DD' format
    :return: A list of dictionaries containing the economic indicator data
    """
    path = "economic"
    name = __validate_economic_indicator(name)
    
    query_vars = {
        "apikey": apikey,
        "name": name,
    }
    
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
        
    return __return_json_v4(path=path, query_vars=query_vars)


def treasury_rates(
    apikey: str,
    from_date: str,
    to_date: str,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /treasury/ API.

    Provides real-time and historical Treasury rates for all maturities.

    :param apikey: Your API key
    :param from_date: The starting date in 'YYYY-MM-DD' format
    :param to_date: The ending date in 'YYYY-MM-DD' format
    :return: A list of dictionaries containing Treasury rates data
    """
    path = "treasury"
    query_vars = {
        "apikey": apikey,
        "from": from_date,
        "to": to_date,
    }
    return __return_json_v4(path=path, query_vars=query_vars) 