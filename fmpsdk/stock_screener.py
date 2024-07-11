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
    Query FMP /stock-screener/ API for stocks based on various filters.

    :param market_cap_more_than: Min market cap.
    :param market_cap_lower_than: Max market cap.
    :param beta_more_than: Min beta.
    :param beta_lower_than: Max beta.
    :param volume_more_than: Min volume.
    :param volume_lower_than: Max volume.
    :param dividend_more_than: Min dividend yield.
    :param dividend_lower_than: Max dividend yield.
    :param price_more_than: Min price.
    :param price_lower_than: Max price.
    :param is_etf: Filter ETFs.
    :param is_fund: Filter mutual funds.
    :param is_actively_trading: Filter active stocks.
    :param sector: Filter by sector.
    :param industry: Filter by industry.
    :param country: Filter by country.
    :param exchange: Filter by exchange(s).
    :param limit: Number of results. Default is DEFAULT_LIMIT.
    :return: List of dicts with stock data or None if request fails.
    :example: stock_screener(market_cap_more_than=1000000000, limit=10)
    :endpoint: https://financialmodelingprep.com/api/v3/stock-screener
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