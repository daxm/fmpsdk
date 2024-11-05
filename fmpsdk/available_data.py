import typing
import os
from .settings import DEFAULT_LIMIT
from .url_methods import __return_json_v3
from .data_compression import compress_json_to_tsv

API_KEY = os.getenv('FMP_API_KEY')

def financial_statement_symbol_lists() -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve a list of symbols with available financial statements.

    Useful for identifying companies with accessible financial data for analysis.

    :return: List of dicts or TSV string with symbols and their available financial statements.
    :example: financial_statement_symbol_lists()
    """
    path = "financial-statement-symbol-lists"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def symbols_list(tsv: bool = True) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve a list of all available stock symbols.

    Useful for exploring and analyzing a wide range of stocks.

    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with stock symbols data.
    :example: symbols_list()
    """
    path = f"stock/list"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tsv(result) if tsv else result

def etf_list(tsv: bool = True) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve a list of all available ETF symbols.

    Useful for exploring and analyzing a wide range of ETFs.

    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with ETF symbols data.
    :example: etf_list()
    """
    path = "etf/list"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tsv(result) if tsv else result

def available_traded_list(
) -> typing.List[str]:
    """
    Retrieve a list of all available tradable symbols.

    Useful for exploring and analyzing a wide range of tradable securities.

    :return: List of dicts or tuple of tuples with tradable symbols data.
    :example: available_traded_list()
    """
    path = "available-traded/list"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def delisted_companies(
    limit: int = DEFAULT_LIMIT,
) -> typing.List[str]:
    """
    Retrieve a list of delisted companies.

    Useful for tracking and analyzing companies that have been delisted from exchanges.

    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :return: List of dicts or tuple of tuples with delisted companies data.
    :example: delisted_companies(limit=10)
    """
    path = "delisted-companies"
    query_vars = {"apikey": API_KEY, "limit": limit}
    return __return_json_v3(path=path, query_vars=query_vars)

def available_mutual_funds(
) -> typing.List[str]:
    """
    Query FMP /symbol/available-mutual-funds/ API

    :return: List of dicts or tuple of tuples with available mutual funds data.
    """
    path = f"symbol/available-mutual-funds"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def available_tsx(
) -> typing.List[str]:
    """
    Query FMP /symbol/available-tsx/ API

    :return: List of dicts or tuple of tuples with available TSX symbols data.
    """
    path = f"symbol/available-tsx"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def available_forex(
) -> typing.List[str]:
    """
    Get a list of all available forex currency pairs.

    Retrieves a comprehensive list of all currency pairs traded on the
    forex market. Useful for identifying available trading options.

    :return: List of dicts or tuple of tuples with available forex pairs data.
    :example: available_forex()
    """
    path = "symbol/available-forex-currency-pairs"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def cryptocurrencies_list(tsv: bool = True) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Query FMP /quotes/crypto API

    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string containing full quotes for all cryptocurrencies.
    :example: cryptocurrencies_list()
    :endpoint: https://financialmodelingprep.com/api/v3/quotes/crypto
    """
    path = "quotes/crypto"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tsv(result) if tsv else result

def all_countries(
) -> typing.List[str]:
    """
    Retrieve a list of all available countries.

    Useful for exploring and analyzing data from various countries.

    :return: List of country names or tuple of tuples with country names.
    :example: all_countries()
    """
    path = "get-all-countries"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def available_etfs(
) -> typing.List[str]:
    """
    Query FMP /symbol/available-etfs/ API.

    :return: List of dicts or tuple of tuples containing available ETFs.
    :example: available_etfs()
    :endpoint: https://financialmodelingprep.com/api/v3/symbol/available-etfs
    """
    path = f"symbol/available-etfs"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def available_commodities(
) -> typing.List[str]:
    """
    Query FMP /symbol/available-commodities API

    :return: List of dicts or tuple of tuples containing available commodities.
    :example: available_commodities()
    """
    path = "symbol/available-commodities"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def available_sectors(
) -> typing.List[str]:
    """
    Retrieve a list of available sectors.

    Useful for exploring and analyzing data across various sectors.

    :return: List of sector names or tuple of tuples with sector names.
    :example: available_sectors()
    """
    path = "sectors-list"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def available_industries(
) -> typing.List[str]:
    """
    Retrieve a list of available industries.

    Useful for exploring and analyzing data across various industries.

    :return: List of industry names or tuple of tuples with industry names.
    :example: available_industries()
    """
    path = "industries-list"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def available_exchanges(
) -> typing.List[str]:
    """
    Retrieve a list of available exchanges.

    Useful for exploring and analyzing data from various exchanges.

    :return: List of exchange names or tuple of tuples with exchange names.
    :example: available_exchanges()
    """
    path = "exchanges-list"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def available_cryptocurrencies(tsv: bool = True) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Query FMP /symbol/available-cryptocurrencies API

    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string containing available cryptocurrencies.
    :example: available_cryptocurrencies()
    :endpoint: https://financialmodelingprep.com/api/v3/symbol/available-cryptocurrencies
    """
    path = "symbol/available-cryptocurrencies"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tsv(result) if tsv else result

def available_euronext(tsv: bool = True) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Query FMP /symbol/available-euronext API

    Get a list of available Euronext stocks.

    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string containing available Euronext stocks.
    :example: available_euronext()
    """
    path = "symbol/available-euronext"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tsv(result) if tsv else result

def available_indexes(tsv: bool = True) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Query FMP /symbol/available-indexes/ API

    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string containing available indexes.
    :example: available_indexes()
    """
    path = "symbol/available-indexes"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tsv(result) if tsv else result