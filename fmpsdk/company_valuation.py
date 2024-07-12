import logging
import typing
import os
import requests

from .settings import DEFAULT_LIMIT
from .url_methods import (
    __return_json_v3,
    __return_json_v4,
    __validate_industry,
    __validate_period,
    __validate_sector,
)

API_KEY = os.getenv('FMP_API_KEY')

def financial_statement_symbol_lists() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /financial-statement-symbol-lists/ API for symbols with financial statements.

    :return: A list of dictionaries containing symbols.
    :example: financial_statement_symbol_lists()
    :endpoint: https://financialmodelingprep.com/api/v3/financial-statement-symbol-lists
    """
    path = "financial-statement-symbol-lists"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def enterprise_values(symbol: str, period: str = "annual", limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /enterprise-values/ API for company's enterprise value.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param period: Reporting period ('annual' or 'quarter'). Default is 'annual'.
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :return: A list of dictionaries with enterprise value data.
    :example: enterprise_values('AAPL', period='quarter', limit=5)
    :endpoint: https://financialmodelingprep.com/api/v3/enterprise-values/{symbol}
    """
    path = f"enterprise-values/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "period": __validate_period(value=period),
        "limit": limit,
    }
    return __return_json_v3(path=path, query_vars=query_vars)

def key_metrics_ttm(symbol: str, limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /key-metrics-ttm/ API for trailing twelve months key metrics.

    :param symbol: Company ticker.
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :return: A list of dictionaries with key metrics data.
    :example: key_metrics_ttm('AAPL', limit=5)
    :endpoint: https://financialmodelingprep.com/api/v3/key-metrics-ttm/{symbol}
    """
    path = f"key-metrics-ttm/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit}
    return __return_json_v3(path=path, query_vars=query_vars)

def key_metrics(symbol: str, period: str = "annual", limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /key-metrics/ API for company's key financial metrics.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param period: Reporting period ('annual' or 'quarter'). Default is 'annual'.
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :return: A list of dictionaries with key financial metrics data.
    :example: key_metrics('AAPL', period='quarter', limit=5)
    :endpoint: https://financialmodelingprep.com/api/v3/key-metrics/{symbol}
    """
    path = f"key-metrics/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "period": __validate_period(value=period),
        "limit": limit,
    }
    return __return_json_v3(path=path, query_vars=query_vars)

def rating(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /rating/ API for company rating.

    :param symbol: Company ticker.
    :return: A list of dictionaries with rating data.
    :example: rating('AAPL')
    :endpoint: https://financialmodelingprep.com/api/v3/rating/{symbol}
    """
    path = f"rating/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def historical_rating(symbol: str, limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical-rating/ API for historical company ratings.

    :param symbol: Company ticker.
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :return: A list of dictionaries with historical rating data.
    :example: historical_rating('AAPL', limit=5)
    :endpoint: https://financialmodelingprep.com/api/v3/historical-rating/{symbol}
    """
    path = f"historical-rating/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit}
    return __return_json_v3(path=path, query_vars=query_vars)

def discounted_cash_flow(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /discounted-cash-flow/ API for company's discounted cash flow.

    :param symbol: Company ticker.
    :return: A list of dictionaries with discounted cash flow data.
    :example: discounted_cash_flow('AAPL')
    :endpoint: https://financialmodelingprep.com/api/v3/discounted-cash-flow/{symbol}
    """
    path = f"discounted-cash-flow/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def advanced_discounted_cash_flow(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /advanced_discounted_cash_flow/ API for advanced DCF valuation.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: A list of dictionaries with advanced DCF valuation data.
    :example: advanced_discounted_cash_flow('AAPL')
    :endpoint: https://financialmodelingprep.com/api/v4/advanced_discounted_cash_flow?symbol={symbol}
    """
    path = f"advanced_discounted_cash_flow"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def historical_discounted_cash_flow(symbol: str, period: str = "annual", limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical-discounted-cash-flow/ API for historical DCF.

    :param symbol: Company ticker.
    :param period: 'annual' or 'quarter'. Default is 'annual'.
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :return: A list of dictionaries with historical DCF data.
    :example: historical_discounted_cash_flow('AAPL', period='quarter', limit=5)
    :endpoint: https://financialmodelingprep.com/api/v3/historical-discounted-cash-flow/{symbol}
    """
    path = f"historical-discounted-cash-flow/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "limit": limit,
        "period": __validate_period(value=period),
    }
    return __return_json_v3(path=path, query_vars=query_vars)

def historical_daily_discounted_cash_flow(symbol: str, limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical-daily-discounted-cash-flow/ API for daily historical DCF.

    :param symbol: Company ticker.
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :return: A list of dictionaries with daily historical DCF data.
    :example: historical_daily_discounted_cash_flow('AAPL', limit=5)
    :endpoint: https://financialmodelingprep.com/api/v3/historical-daily-discounted-cash-flow/{symbol}
    """
    path = f"historical-daily-discounted-cash-flow/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit}
    return __return_json_v3(path=path, query_vars=query_vars)

def symbols_list() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /stock/list/ API for list of all stock symbols.

    :return: A list of dictionaries with stock symbols data.
    :example: symbols_list()
    :endpoint: https://financialmodelingprep.com/api/v3/stock/list
    """
    path = f"stock/list"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def etf_list() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /etf/list/ API for list of all ETF symbols.

    :return: A list of dictionaries with ETF symbols data.
    :example: etf_list()
    :endpoint: https://financialmodelingprep.com/api/v3/etf/list
    """
    path = "etf/list"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def available_traded_list() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /available-traded/list/ API for list of all tradable symbols.

    :return: A list of dictionaries with tradable symbols data.
    :example: available_traded_list()
    :endpoint: https://financialmodelingprep.com/api/v3/available-traded/list
    """
    path = "available-traded/list"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def delisted_companies(limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /delisted-companies/ API for list of delisted companies.

    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :return: A list of dictionaries with delisted companies data.
    :example: delisted_companies(limit=10)
    :endpoint: https://financialmodelingprep.com/api/v3/delisted-companies
    """
    path = "delisted-companies"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def earnings_surprises(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /earnings-surprises/ API for company's earnings surprises.

    :param symbol: Company ticker.
    :return: A list of dictionaries with earnings surprises data.
    :example: earnings_surprises('AAPL')
    :endpoint: https://financialmodelingprep.com/api/v3/earnings-surprises/{symbol}
    """
    path = f"earnings-surprises/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def earning_call_transcript(symbol: str, year: int, quarter: int) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /earning_call_transcript/ API for company's earning call transcript.

    :param symbol: Company ticker.
    :param year: Year of the transcript.
    :param quarter: Quarter of the transcript.
    :return: A list of dictionaries with earning call transcript data.
    :example: earning_call_transcript('AAPL', 2023, 1)
    :endpoint: https://financialmodelingprep.com/api/v3/earning_call_transcript/{symbol}
    """
    path = f"earning_call_transcript/{symbol}"
    query_vars = {"apikey": API_KEY, "year": year, "quarter": quarter}
    return __return_json_v3(path=path, query_vars=query_vars)

def batch_earning_call_transcript(symbol: str, year: int) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /batch_earning_call_transcript/ API for company's batch earning call transcripts.

    :param symbol: Company ticker.
    :param year: Year of the transcripts.
    :return: A list of dictionaries with batch earning call transcript data.
    :example: batch_earning_call_transcript('AAPL', 2023)
    :endpoint: https://financialmodelingprep.com/api/v4/batch_earning_call_transcript/{symbol}
    """
    path = f"batch_earning_call_transcript/{symbol}"
    query_vars = {"apikey": API_KEY, "year": year}
    return __return_json_v4(path=path, query_vars=query_vars)

def earning_call_transcripts_available_dates(symbol: str) -> typing.Optional[typing.List[typing.List]]:
    """
    Query FMP /earning_call_transcript/ API for available dates of earning call transcripts.

    :param symbol: Company ticker.
    :return: A list of lists with available dates for earning call transcripts.
    :example: earning_call_transcripts_available_dates('AAPL')
    :endpoint: https://financialmodelingprep.com/api/v4/earning_call_transcript
    """
    path = f"earning_call_transcript"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def sec_filings(symbol: str, filing_type: str = "", limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /sec_filings/ API for company's SEC filings.

    :param symbol: Company ticker.
    :param filing_type: Name of filing. Default is empty string.
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :return: A list of dictionaries with SEC filings data.
    :example: sec_filings('AAPL', filing_type='10-K', limit=10)
    :endpoint: https://financialmodelingprep.com/api/v3/sec_filings/{symbol}
    """
    path = f"sec_filings/{symbol}"
    query_vars = {"apikey": API_KEY, "type": filing_type, "limit": limit}
    return __return_json_v3(path=path, query_vars=query_vars)

def press_releases(symbol: str, limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /press-releases/ API for company's press releases.

    :param symbol: Company ticker.
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :return: A list of dictionaries with press releases data.
    :example: press_releases('AAPL', limit=10)
    :endpoint: https://financialmodelingprep.com/api/v3/press-releases/{symbol}
    """
    path = f"press-releases/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit}
    return __return_json_v3(path=path, query_vars=query_vars)

def stock_peers(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /stock_peers/ API for company's stock peers.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: A list of dictionaries with stock peers data.
    :example: stock_peers('AAPL')
    :endpoint: https://financialmodelingprep.com/api/v4/stock_peers?symbol={symbol}
    """
    path = f"stock_peers"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def analyst_estimates(symbol: str, period: str = "annual", limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /analyst-estimates/ API for company's analyst estimates.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param period: Reporting period ('annual' or 'quarter'). Default is 'annual'.
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :return: A list of dictionaries with analyst estimates data.
    :example: analyst_estimates('AAPL', period='quarter', limit=5)
    :endpoint: https://financialmodelingprep.com/api/v3/analyst-estimates/{symbol}?period={period}&limit={limit}
    """
    path = f"/analyst-estimates/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "symbol": symbol,
        "period": __validate_period(value=period),
        "limit": limit,
    }
    return __return_json_v3(path=path, query_vars=query_vars)

def sales_revenue_by_segments(symbol: str, structure: str = "flat", period: str = "annual") -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /revenue-product-segmentation API for company's sales revenue by segments.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param structure: 'flat' or 'segment'. Default is 'flat'.
    :param period: 'annual' or 'quarter'. Default is 'annual'.
    :return: A list of dictionaries with sales revenue by segments data.
    :example: sales_revenue_by_segments('AAPL', structure='segment', period='quarter')
    :endpoint: https://financialmodelingprep.com/api/v4/revenue-product-segmentation?symbol={symbol}&structure={structure}&period={period}
    """
    path = "revenue-product-segmentation"
    query_vars = {
        "apikey": API_KEY,
        "symbol": symbol,
        "structure": structure,
        "period": period
    }
    return __return_json_v4(path=path, query_vars=query_vars)

def revenue_geographic_segmentation(symbol: str, structure: str = "flat", period: str = "annual") -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /revenue-geographic-segmentation API for company's revenue by geographic segments.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param structure: 'flat' or 'segment'. Default is 'flat'.
    :param period: 'annual' or 'quarter'. Default is 'annual'.
    :return: A list of dictionaries with revenue by geographic segments data.
    :example: revenue_geographic_segmentation('AAPL', structure='segment', period='quarter')
    :endpoint: https://financialmodelingprep.com/api/v4/revenue-geographic-segmentation?symbol={symbol}&structure={structure}&period={period}
    """
    path = "revenue-geographic-segmentation"
    query_vars = {
        "apikey": API_KEY,
        "symbol": symbol,
        "structure": structure,
        "period": period
    }
    return __return_json_v4(path=path, query_vars=query_vars)

def esg_score(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /esg-environmental-social-governance-data API for company's ESG score.

    :param symbol: Company ticker.
    :return: A list of dictionaries with ESG score data.
    :example: esg_score('AAPL')
    :endpoint: https://financialmodelingprep.com/api/v4/esg-environmental-social-governance-data?symbol={symbol}
    """
    path = f"esg-environmental-social-governance-data"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def stock_grade(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /grade/ API for company's stock grade.

    :param symbol: Company ticker.
    :return: A list of dictionaries with stock grade data.
    :example: stock_grade('AAPL')
    :endpoint: https://financialmodelingprep.com/api/v3/grade/{symbol}
    """
    path = f"grade/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def financial_score(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /score/ API for company's financial score.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: A list of dictionaries with financial score data.
    :example: financial_score('AAPL')
    :endpoint: https://financialmodelingprep.com/api/v4/score?symbol={symbol}
    """
    path = "score"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def owner_earnings(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /owner_earnings API for company's owner earnings.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: A list of dictionaries with owner earnings data.
    :example: owner_earnings('AAPL')
    :endpoint: https://financialmodelingprep.com/api/v4/owner_earnings?symbol={symbol}
    """
    path = "owner_earnings"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def upgrades_downgrades(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /upgrades-downgrades/ API for company's stock upgrades and downgrades.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: A list of dictionaries with stock upgrades and downgrades data.
    :example: upgrades_downgrades('AAPL')
    :endpoint: https://financialmodelingprep.com/api/v4/upgrades-downgrades?symbol={symbol}
    """
    path = "upgrades-downgrades"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def upgrades_downgrades_rss_feed(page: int = 0) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /upgrades-downgrades-rss-feed/ API for latest stock upgrades and downgrades RSS feed.

    :param page: Page number for pagination. Default is 0.
    :return: A list of dictionaries with latest stock upgrades and downgrades RSS feed data.
    :example: upgrades_downgrades_rss_feed(page=1)
    :endpoint: https://financialmodelingprep.com/api/v4/upgrades-downgrades-rss-feed?page={page}
    """
    path = "upgrades-downgrades-rss-feed"
    query_vars = {"apikey": API_KEY, "page": page}
    return __return_json_v4(path=path, query_vars=query_vars)

def upgrades_downgrades_consensus(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /upgrades-downgrades-consensus/ API for company's consensus rating.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: A list of dictionaries with consensus rating data.
    :example: upgrades_downgrades_consensus('AAPL')
    :endpoint: https://financialmodelingprep.com/api/v4/upgrades-downgrades-consensus?symbol={symbol}
    """
    path = "upgrades-downgrades-consensus"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def upgrades_downgrades_by_company(company: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /upgrades-downgrades-grading-company/ API for company's stock upgrades and downgrades.

    :param company: Company name (e.g., 'Barclays').
    :return: A list of dictionaries with stock upgrades and downgrades data for the company.
    :example: upgrades_downgrades_by_company('Barclays')
    :endpoint: https://financialmodelingprep.com/api/v4/upgrades-downgrades-grading-company?company={company}
    """
    path = "upgrades-downgrades-grading-company"
    query_vars = {"apikey": API_KEY, "company": company}
    return __return_json_v4(path=path, query_vars=query_vars)

def mergers_acquisitions_rss_feed(page: int = 0) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /mergers-acquisitions-rss-feed/ API for latest M&A news RSS feed.

    :param page: Page number for pagination. Default is 0.
    :return: A list of dictionaries with latest M&A news RSS feed data.
    :example: mergers_acquisitions_rss_feed(page=1)
    :endpoint: https://financialmodelingprep.com/api/v4/mergers-acquisitions-rss-feed?page={page}
    """
    path = "mergers-acquisitions-rss-feed"
    query_vars = {"apikey": API_KEY, "page": page}
    return __return_json_v4(path=path, query_vars=query_vars)

def search_mergers_acquisitions(name: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /mergers-acquisitions/search/ API for M&A deals based on company name.

    :param name: Company name (e.g., 'Apple').
    :return: A list of dictionaries with M&A deal data for the company.
    :example: search_mergers_acquisitions('Apple')
    :endpoint: https://financialmodelingprep.com/api/v4/mergers-acquisitions/search?name={name}
    """
    path = "mergers-acquisitions/search"
    query_vars = {"apikey": API_KEY, "name": name}
    return __return_json_v4(path=path, query_vars=query_vars)

def executive_compensation(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /governance/executive_compensation API for company's executive compensation.

    :param symbol: Company ticker.
    :return: A list of dictionaries with executive compensation data.
    :example: executive_compensation('AAPL')
    :endpoint: https://financialmodelingprep.com/api/v4/governance/executive_compensation?symbol={symbol}
    """
    path = "governance/executive_compensation"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def compensation_benchmark(year: int) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /executive-compensation-benchmark API for executive compensation benchmark.

    :param year: Year for compensation benchmark data.
    :return: A list of dictionaries with compensation benchmark data.
    :example: compensation_benchmark(2023)
    :endpoint: https://financialmodelingprep.com/api/v4/executive-compensation-benchmark?year={year}
    """
    path = "executive-compensation-benchmark"
    query_vars = {"apikey": API_KEY, "year": year}
    return __return_json_v4(path=path, query_vars=query_vars)

def company_notes(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /company-notes/ API for company's notes.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: A list of dictionaries with company notes data.
    :example: company_notes('AAPL')
    :endpoint: https://financialmodelingprep.com/api/v4/company-notes?symbol={symbol}
    """
    path = "company-notes"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def historical_employee_count(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical/employee_count API for company's historical employee count.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: A list of dictionaries with historical employee count data.
    :example: historical_employee_count('AAPL')
    :endpoint: https://financialmodelingprep.com/api/v4/historical/employee_count?symbol={symbol}
    """
    path = "historical/employee_count"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def employee_count(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /employee_count API for company's current employee count.

    :param symbol: Company ticker.
    :return: A list of dictionaries with current employee count data.
    :example: employee_count('AAPL')
    :endpoint: https://financialmodelingprep.com/api/v4/employee_count?symbol={symbol}
    """
    path = "employee_count"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def company_core_information(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /company-core-information/ API for company's core information.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: A list of dictionaries with company core information data.
    :example: company_core_information('AAPL')
    :endpoint: https://financialmodelingprep.com/api/v4/company-core-information?symbol={symbol}
    """
    path = "company-core-information"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def all_countries() -> typing.Optional[typing.List[str]]:
    """
    Query FMP /get-all-countries API for list of all countries.

    :return: A list of country names.
    :example: all_countries()
    :endpoint: https://financialmodelingprep.com/api/v3/get-all-countries
    """
    path = "get-all-countries"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def analyst_recommendation(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /analyst-stock-recommendations/ API for company's analyst recommendations.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: A list of dictionaries with analyst recommendations data.
    :example: analyst_recommendation('AAPL')
    :endpoint: https://financialmodelingprep.com/api/v3/analyst-stock-recommendations/{symbol}
    """
    path = f"analyst-stock-recommendations/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def is_market_open(exchange: str = "NASDAQ") -> typing.Optional[typing.Dict]:
    """
    Query FMP /is-the-market-open API for market open/close status.

    :param exchange: Exchange name. Default is 'NASDAQ'.
    :return: A dictionary with market open/close status.
    :example: is_market_open('NYSE')
    :endpoint: https://financialmodelingprep.com/api/v3/is-the-market-open?exchange={exchange}
    """
    path = "is-the-market-open"
    query_vars = {"apikey": API_KEY, "exchange": exchange}
    return __return_json_v3(path=path, query_vars=query_vars)

def available_sectors() -> typing.Optional[typing.List[str]]:
    """
    Query FMP /sectors-list API for list of available sectors.

    :return: A list of sector names.
    :example: available_sectors()
    :endpoint: https://financialmodelingprep.com/api/v3/sectors-list
    """
    path = "sectors-list"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def available_industries() -> typing.Optional[typing.List[str]]:
    """
    Query FMP /industries-list API for list of available industries.

    :return: A list of industry names.
    :example: available_industries()
    :endpoint: https://financialmodelingprep.com/api/v3/industries-list
    """
    path = "industries-list"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def available_exchanges() -> typing.Optional[typing.List[str]]:
    """
    Query FMP /exchanges-list API for list of available exchanges.

    :return: A list of exchange names.
    :example: available_exchanges()
    :endpoint: https://financialmodelingprep.com/api/v3/exchanges-list
    """
    path = "exchanges-list"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def company_outlook(symbol: str) -> typing.Optional[typing.Dict]:
    """
    Query FMP /company-outlook/ API for company's outlook.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: A dictionary with company outlook data.
    :example: company_outlook('AAPL')
    :endpoint: https://financialmodelingprep.com/api/v4/company-outlook?symbol={symbol}
    """
    path = "company-outlook"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)