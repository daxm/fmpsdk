import typing
import os
from .settings import DEFAULT_LIMIT
from .url_methods import __return_json_v3, __validate_sector, __validate_industry

API_KEY = os.getenv('FMP_API_KEY')

def stock_screener(
    market_cap_more_than: typing.Union[float, int] = None,
    market_cap_lower_than: typing.Union[float, int] = None,
    beta_more_than: typing.Union[float, int] = None,
    beta_lower_than: typing.Union[float, int] = None,
    volume_more_than: typing.Union[float, int] = None,
    volume_lower_than: typing.Union[float, int] = None,
    dividend_more_than: typing.Union[float, int] = None,
    dividend_lower_than: typing.Union[float, int] = None,
    price_more_than: typing.Union[float, int] = None,
    price_lower_than: typing.Union[float, int] = None,
    is_etf: bool = None,
    is_fund: bool = None,
    is_actively_trading: bool = None,
    sector: str = None,
    industry: str = None,
    country: str = None,
    exchange: typing.Union[str, typing.List[str]] = None,
    limit: int = DEFAULT_LIMIT,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Screen stocks based on financial and market criteria.

    Args:
        market_cap_more_than, market_cap_lower_than: Market cap range (USD)
        beta_more_than, beta_lower_than: Beta range
        volume_more_than, volume_lower_than: Volume range
        dividend_more_than, dividend_lower_than: Dividend yield range (%)
        price_more_than, price_lower_than: Price range (USD)
        is_etf: Include (True) or exclude (False) ETFs
        is_fund: Include (True) or exclude (False) funds
        is_actively_trading: Filter for actively traded stocks
        sector: Filter by sector (e.g., "Technology")
        industry: Filter by industry (e.g., "Software")
        country: Filter by country (e.g., "US")
        exchange: Filter by exchange(s) (str or list)
        limit: Max results (default: DEFAULT_LIMIT)

    Returns:
        List of dicts with stock data or None if request fails

    Example:
        stock_screener(market_cap_more_than=1e9, sector='Technology', limit=10)
    """
    path = "stock-screener"
    query_vars = {"apikey": API_KEY, "limit": limit}
    if market_cap_more_than:
        query_vars["marketCapMoreThan"] = market_cap_more_than
    if market_cap_lower_than:
        query_vars["marketCapLowerThan"] = market_cap_lower_than
    if beta_more_than:
        query_vars["betaMoreThan"] = beta_more_than
    if beta_lower_than:
        query_vars["betaLowerThan"] = beta_lower_than
    if volume_more_than:
        query_vars["volumeMoreThan"] = volume_more_than
    if volume_lower_than:
        query_vars["volumeLowerThan"] = volume_lower_than
    if dividend_more_than:
        query_vars["dividendMoreThan"] = dividend_more_than
    if dividend_lower_than:
        query_vars["dividendLowerThan"] = dividend_lower_than
    if price_more_than:
        query_vars["priceMoreThan"] = price_more_than
    if price_lower_than:
        query_vars["priceLowerThan"] = price_lower_than
    if is_etf is not None:
        query_vars["isEtf"] = is_etf
    if is_fund is not None:
        query_vars["isFund"] = is_fund
    if is_actively_trading is not None:
        query_vars["isActivelyTrading"] = is_actively_trading
    if sector:
        query_vars["sector"] = __validate_sector(sector)
    if industry:
        query_vars["industry"] = __validate_industry(industry)
    if country:
        query_vars["country"] = country
    if exchange:
        if isinstance(exchange, list):
            query_vars["exchange"] = ",".join(exchange)
        else:
            query_vars["exchange"] = exchange
    return __return_json_v3(path=path, query_vars=query_vars)