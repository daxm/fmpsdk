import typing
import os
from .url_methods import __return_json_v4

API_KEY = os.getenv('FMP_API_KEY')

def price_targets(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /price-target/ API.

    Get the price target for a company, which is the price at which an analyst believes the company's stock is fairly valued. Price targets can be used to make investment decisions, such as whether to buy, sell, or hold a stock.

    :param symbol: The stock symbol (e.g., 'AAPL').
    :return: A list of dictionaries containing price target information or None if the request fails.

    Example:
    >>> price_targets('AAPL')
    [{'symbol': 'AAPL', 'priceTarget': 150.0, 'analyst': 'Goldman Sachs', 'date': '2023-10-01', ...}, ...]

    Users can get price targets for many different companies by providing the appropriate ticker symbol.

    Endpoint:
    https://financialmodelingprep.com/api/v4/price-target?symbol={symbol}

    API Documentation:
    https://site.financialmodelingprep.com/developer/docs/price-target-api
    """
    path = "price-target"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def price_target_summary(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /price-target-summary/ API.

    Get a summary of the price targets for a company from different analysts. This summary includes the average price target, the high price target, and the low price target. Investors can use this information to get a general idea of what analysts think about a company's stock.

    :param symbol: The stock symbol (e.g., 'AAPL').
    :return: A list of dictionaries containing price target summary information or None if the request fails.

    Example:
    >>> price_target_summary('AAPL')
    [{'symbol': 'AAPL', 'averagePriceTarget': 150.0, 'highPriceTarget': 160.0, 'lowPriceTarget': 140.0, 'numberOfAnalysts': 10, ...}, ...]

    Users can get price target summaries for many different companies by providing the appropriate ticker symbol.

    Endpoint:
    https://financialmodelingprep.com/api/v4/price-target-summary?symbol={symbol}

    API Documentation:
    https://site.financialmodelingprep.com/developer/docs/price-target-summary-api
    """
    path = "price-target-summary"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def price_target_by_analyst_name(name: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /price-target-analyst-name API for price targets from a specific analyst.

    :param name: The name of the analyst (e.g., 'Tim Anderson')
    :return: A list of dictionaries containing price target information for the specified analyst.
    """
    path = "price-target-analyst-name"
    query_vars = {"apikey": API_KEY, "name": name}
    return __return_json_v4(path=path, query_vars=query_vars)

def price_target_by_company(company: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /price-target-analyst-company/ API for price targets from a specific company.

    Get the price targets for all companies in a specific industry or sector. This can be useful if you want to compare the price targets of different companies in the same industry.

    :param company: The name of the company (e.g., 'Barclays').
    :return: A list of dictionaries containing price target information for the specified company.

    Example:
    >>> price_target_by_company('Barclays')
    [{'symbol': 'AAPL', 'priceTarget': 150.0, 'analyst': 'Barclays', 'date': '2023-10-01', ...}, ...]

    Users can get price targets for many different companies by providing the appropriate company name.

    Endpoint:
    https://financialmodelingprep.com/api/v4/price-target-analyst-company?company={company}

    API Documentation:
    https://site.financialmodelingprep.com/developer/docs/price-target-by-analyst-company-api
    """
    path = "price-target-analyst-company"
    query_vars = {"apikey": API_KEY, "company": company}
    return __return_json_v4(path=path, query_vars=query_vars)

def price_target_consensus(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /price-target-consensus/ API for consensus price targets of a specific symbol.

    Get the consensus price target for a company, which is the average of all price targets from different analysts. This can be useful if you want to get a general idea of what analysts think about a company's stock.

    :param symbol: The stock symbol (e.g., 'AAPL').
    :return: A list of dictionaries containing consensus price target information or None if the request fails.

    Example:
    >>> price_target_consensus('AAPL')
    [{'symbol': 'AAPL', 'priceTargetAverage': 150.0, 'priceTargetHigh': 160.0, 'priceTargetLow': 140.0, 'numberOfAnalysts': 10, ...}, ...]

    Users can get consensus price targets for many different companies by providing the appropriate ticker symbol.

    Endpoint:
    https://financialmodelingprep.com/api/v4/price-target-consensus?symbol={symbol}

    API Documentation:
    https://site.financialmodelingprep.com/developer/docs/price-target-consensus-api
    """
    path = "price-target-consensus"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def price_target_rss_feed(page: int = 0) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /price-target-rss-feed/ API for the latest price target updates.

    Get an RSS feed of price target updates for a company. This way, you can stay up-to-date on the latest price targets from analysts.

    :param page: The page number for pagination (default is 0).
    :return: A list of dictionaries containing the latest price target updates.

    Example:
    >>> price_target_rss_feed(page=1)
    [{'symbol': 'AAPL', 'analyst': 'Goldman Sachs', 'priceTarget': 150.0, 'date': '2023-10-01', ...}, ...]

    Users can get the latest price target updates for many different companies by providing the appropriate page number for pagination.

    Endpoint:
    https://financialmodelingprep.com/api/v4/price-target-rss-feed?page={page}

    API Documentation:
    https://site.financialmodelingprep.com/developer/docs/price-target-rss-feed-api
    """
    path = "price-target-rss-feed"
    query_vars = {"apikey": API_KEY, "page": page}
    return __return_json_v4(path=path, query_vars=query_vars)