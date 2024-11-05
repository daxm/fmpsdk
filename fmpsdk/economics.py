import typing
import os
from .url_methods import __return_json_v3, __return_json_v4
from .data_compression import compress_json_to_tsv

API_KEY = os.getenv('FMP_API_KEY')


def treasury_rates(
    from_date: str = None,
    to_date: str = None,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve real-time and historical Treasury rates for all maturities.

    Treasury rates are key benchmarks for interest rates across the economy.
    Use this data to track rate movements, identify trends, and make informed
    investment decisions based on interest rates.

    :param from_date: Optional start date in YYYY-MM-DD format
    :param to_date: Optional end date in YYYY-MM-DD format
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with Treasury rates data, including date and rates
             for various maturities (e.g., month1, month2, month3, etc.)
    :example: treasury_rates()
    :example: treasury_rates('2023-01-01', '2023-12-31')
    """
    path = "treasury"
    query_vars = {"apikey": API_KEY}
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    result = __return_json_v4(path=path, query_vars=query_vars)
    return compress_json_to_tsv(result) if tsv else result


def economic_indicators(
    name: str,
    from_date: str = None,
    to_date: str = None,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve real-time and historical data for various economic indicators.

    Provides insights on economic performance, growth trends, and market impacts.
    Useful for tracking economic trends, identifying growth patterns, and making
    informed investment decisions based on indicators like GDP, CPI, and unemployment.

    :param name: Name of the economic indicator (e.g., 'GDP', 'CPI', 'unemploymentRate').
    :param from_date: Optional start date in YYYY-MM-DD format.
    :param to_date: Optional end date in YYYY-MM-DD format.
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with economic indicator data.
    :example: economic_indicators('GDP')
    :example: economic_indicators('CPI', '2023-01-01', '2023-12-31')
    """
    path = "economic"
    query_vars = {"apikey": API_KEY, "name": name}
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    result = __return_json_v4(path=path, query_vars=query_vars)
    return compress_json_to_tsv(result) if tsv else result


def market_risk_premium(
    country: str = None,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve market risk premium data for a given date.

    The market risk premium is the difference between the expected return
    of the market and the risk-free rate. This data is crucial for
    financial modeling, asset pricing, and investment decision-making.

    :param country: Optional country name to filter results.
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with market risk premium data, including date
             and premium value.
    :example: market_risk_premium()
    :example: market_risk_premium('United States')
    """
    path = "market_risk_premium"
    query_vars = {"apikey": API_KEY}
    if country:
        query_vars["country"] = country
    result = __return_json_v4(path=path, query_vars=query_vars)
    return compress_json_to_tsv(result) if tsv else result