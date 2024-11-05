import typing
import os
from .settings import DEFAULT_LIMIT
from .url_methods import __return_json_v3
from .data_compression import compress_json_to_tsv

API_KEY = os.getenv('FMP_API_KEY')

def earning_calendar(
    from_date: str = None,
    to_date: str = None,
    estimate_required: bool = True,
    revenue_minimum: float = 1000000000,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve a list of upcoming and past earnings announcements.

    Provides valuable insights into companies' financial performance and outlook.

    :param from_date: Start date in 'YYYY-MM-DD' format.
    :param to_date: End date in 'YYYY-MM-DD' format.
    :param estimate_required: If True, exclude entries where either 'epsEstimated'
                              or 'revenueEstimated' is null. Defaults to True.
    :param revenue_minimum: Minimum 'revenueEstimated' value to include an entry.
                            Defaults to 1,000,000,000 (1 billion).
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts with earnings data, or TSV string if tsv is True.
             Returns None if request fails.
    :example: earning_calendar('2023-01-01', '2023-12-31', estimate_required=True, 
                                revenue_minimum=500000000, tsv=True)
    """
    path = "earning_calendar"
    query_vars = {"apikey": API_KEY}
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    
    result = __return_json_v3(path=path, query_vars=query_vars)
    
    if result is not None:
        if estimate_required:
            result = [
                entry for entry in result
                if entry.get('epsEstimated') is not None
                and entry.get('revenueEstimated') is not None
            ]
        
        result = [
            entry for entry in result
            if entry.get('revenueEstimated', 0) >= revenue_minimum
        ]
        
        fields = ('date', 'symbol', 'eps', 'epsEstimated', 'revenue', 'revenueEstimated', "fiscalDateEnding")
        
        return compress_json_to_tsv(result, fields) if tsv else result
    
    return None

def historical_earning_calendar(
    symbol: str,
    limit: int = DEFAULT_LIMIT,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve historical and upcoming earnings announcements for a specific company.

    Provides valuable insights into a company's past performance and future outlook.
    Useful for analyzing earnings trends, identifying surprises, and making
    informed investment decisions.

    :param symbol: Ticker symbol of the company (e.g., 'AAPL').
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts with earnings data, or TSV string if tsv is True.
    :example: historical_earning_calendar('AAPL', limit=10)
    """
    path = f"historical/earning_calendar/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "symbol": symbol,
        "limit": limit,
    }
    result = __return_json_v3(path=path, query_vars=query_vars)
    
    fields = ('date', 'symbol', 'eps', 'epsEstimated', 'revenue', 'revenueEstimated')
    return compress_json_to_tsv(result, fields) if tsv else result

def ipo_calendar(
    from_date: str = None,
    to_date: str = None,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve a list of confirmed upcoming IPOs.

    Provides information on scheduled Initial Public Offerings, including
    company name, symbol, IPO date, exchange, and pricing details. Useful
    for tracking new investment opportunities and market trends.

    :param from_date: Start date for IPO range (format: YYYY-MM-DD).
    :param to_date: End date for IPO range (format: YYYY-MM-DD).
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts with IPO calendar data, or TSV string if tsv is True.
    :example: ipo_calendar(from_date='2023-01-01', to_date='2023-12-31')
    """
    path = f"ipo_calendar"
    query_vars = {"apikey": API_KEY}
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    result = __return_json_v3(path=path, query_vars=query_vars)
    
    fields = ('date', 'symbol', 'exchange', 'name', 'ipoPrice', 'priceRange')
    return compress_json_to_tsv(result, fields) if tsv else result

def stock_split_calendar(
    from_date: str = None,
    to_date: str = None,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve upcoming stock split data for publicly traded companies.

    Provides information on scheduled stock splits, including split date,
    ratio, and type. Useful for identifying potential investment opportunities,
    tracking increased liquidity, and monitoring changes in share affordability.

    :param from_date: Start date for the split calendar (format: YYYY-MM-DD).
    :param to_date: End date for the split calendar (format: YYYY-MM-DD).
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts with stock split calendar data, or TSV string if tsv is True.
    :example: stock_split_calendar(from_date='2023-08-10', to_date='2023-10-10')
    """
    path = f"stock_split_calendar"
    query_vars = {"apikey": API_KEY}
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    result = __return_json_v3(path=path, query_vars=query_vars)
    
    fields = ('date', 'symbol', 'numerator', 'denominator', 'fromFactor', 'toFactor')
    return compress_json_to_tsv(result, fields) if tsv else result

def dividend_calendar(
    from_date: str = None,
    to_date: str = None,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve upcoming dividend payments for publicly traded companies.

    Provides a list of dividend payments within a specified date range,
    including payment date, ex-dividend date, and dividend per share.
    Useful for identifying high-yield stocks and tracking dividend trends.

    :param from_date: Start date for dividend calendar (format: YYYY-MM-DD).
    :param to_date: End date for dividend calendar (format: YYYY-MM-DD).
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts with dividend calendar data, or TSV string if tsv is True.
    Note: Maximum time interval between from_date and to_date is 3 months.
    :example: dividend_calendar(from_date='2023-10-01', to_date='2023-10-31')
    """
    path = f"stock_dividend_calendar"
    query_vars = {"apikey": API_KEY}
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    result = __return_json_v3(path=path, query_vars=query_vars)
    
    fields = ('date', 'symbol', 'dividend', 'recordDate', 'paymentDate', 'declarationDate')
    return compress_json_to_tsv(result, fields) if tsv else result

def economic_calendar(
    from_date: str = None,
    to_date: str = None,
    tsv: bool = True,
    impact_filter: typing.Union[str, typing.List[str]] = ['High'],
    country_filter: typing.Union[str, typing.List[str]] = None,
    currency_filter: typing.Union[str, typing.List[str]] = None
) -> typing.Optional[typing.Union[typing.List[typing.Dict], str]]:
    """
    Retrieve economic calendar events with flexible filtering options.

    Provides economic event data for analyzing market-moving events and trends.
    Returns a compact tuple structure for efficient data processing.

    :param from_date: Start date in 'YYYY-MM-DD' format.
    :param to_date: End date in 'YYYY-MM-DD' format.
    :param tsv: If True, return data in TSV format. Defaults to True.
    :param impact_filter: Filter by impact level ('Low', 'Medium', 'High' or list).
    :param country_filter: Filter by country code(s) (e.g., 'US', 'EU' or list).
    :param currency_filter: Filter by currency code(s) (e.g., 'USD', 'EUR' or list).
    :return: List of dicts with economic calendar data, or TSV string if tsv is True.
             Returns None if request fails.
    :example: economic_calendar('2024-08-20', '2024-08-21', impact_filter=['High', 'Medium'],
              country_filter=['US', 'EU'], currency_filter=['USD', 'EUR'])
    """
    path = "economic_calendar"
    query_vars = {"apikey": API_KEY}
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    
    result = __return_json_v3(path=path, query_vars=query_vars)
    
    if result is not None:
        if impact_filter:
            if isinstance(impact_filter, str):
                impact_filter = [impact_filter]
            result = [event for event in result if event.get('impact') in impact_filter]
        
        if country_filter:
            if isinstance(country_filter, str):
                country_filter = [country_filter]
            result = [event for event in result if event.get('country') in country_filter]
        
        if currency_filter:
            if isinstance(currency_filter, str):
                currency_filter = [currency_filter]
            result = [event for event in result if event.get('currency') in currency_filter]
        
        fields = ('date', 'event', 'country', 'actual', 'previous', 'change',
                  'changePercentage', 'estimate', 'impact')
        return compress_json_to_tsv(result, fields) if tsv else result
    
    return None