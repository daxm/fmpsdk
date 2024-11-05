import typing
import os
from .settings import DEFAULT_LIMIT
from .url_methods import __return_json_v3, __return_json_v4, __validate_period
from .data_compression import compress_json_to_tsv
from typing import List, Dict, Union

API_KEY = os.getenv('FMP_API_KEY')

def rating(
    symbol: str,
    tsv: bool = True
) -> Union[List[Dict], str]:
    """
    Retrieve a comprehensive rating for a company based on various financial factors.

    Provides an assessment of a company's financial health, including ratings
    derived from financial statements, DCF analysis, ratios, and intrinsic value.
    Useful for quick company comparisons and identifying investment opportunities.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with rating data.
    :example: rating('AAPL')
    """
    path = f"rating/{symbol}"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v3(path=path, query_vars=query_vars)
    fields = ('symbol', 'date', 'rating', 'ratingScore', 'ratingRecommendation', 'ratingDetailsDCFScore', 'ratingDetailsDCFRecommendation', 'ratingDetailsROEScore', 'ratingDetailsROERecommendation', 'ratingDetailsROAScore', 'ratingDetailsROARecommendation', 'ratingDetailsDEScore', 'ratingDetailsDERecommendation', 'ratingDetailsPEScore', 'ratingDetailsPERecommendation', 'ratingDetailsPBScore', 'ratingDetailsPBRecommendation')
    return compress_json_to_tsv(result, fields) if tsv else result

def historical_rating(
    symbol: str,
    limit: int = 100,
    tsv: bool = True
) -> Union[List[Dict], str]:
    """
    Retrieve historical ratings for a company over time.

    Provides insights into a company's rating changes, helping investors
    track performance trends and identify potential investment opportunities.
    Includes rating, recommendation, and DCF score for each time period.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param limit: Number of records to retrieve. Default is 100.
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with historical rating data.
    :example: historical_rating('AAPL', limit=5)
    """
    path = f"historical-rating/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit}
    result = __return_json_v3(path=path, query_vars=query_vars)
    fields = ('symbol', 'date', 'rating', 'ratingScore', 'ratingRecommendation', 'ratingDetailsDCFScore', 'ratingDetailsDCFRecommendation', 'ratingDetailsROEScore', 'ratingDetailsROERecommendation', 'ratingDetailsROAScore', 'ratingDetailsROARecommendation', 'ratingDetailsDEScore', 'ratingDetailsDERecommendation', 'ratingDetailsPEScore', 'ratingDetailsPERecommendation', 'ratingDetailsPBScore', 'ratingDetailsPBRecommendation')
    return compress_json_to_tsv(result, fields) if tsv else result

def stock_peers(
    symbol: str,
    tsv: bool = True
) -> Union[List[Dict], str]:
    """
    Retrieve a group of companies similar to the given stock.

    Provides peers trading on the same exchange, in the same sector,
    with similar market capitalization. Useful for competitor analysis
    and identifying well-performing companies in the same industry.

    :param symbol: Company ticker (e.g., 'AAPL')
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with stock peers data.
    :example: stock_peers('AAPL')
    """
    path = f"stock_peers"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    result = __return_json_v4(path=path, query_vars=query_vars)
    fields = ('symbol', 'peersList')
    return compress_json_to_tsv(result, fields) if tsv else result

def analyst_estimates(
    symbol: str,
    period: str = "annual",
    limit: int = 100,
    tsv: bool = True
) -> Union[List[Dict], str]:
    """
    Retrieve analyst estimates for a company's future earnings and revenue.

    Provides forecasts to help identify potential investment opportunities.
    Note that analyst estimates are not always accurate.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param period: Reporting period ('annual' or 'quarter'). Default is 'annual'.
    :param limit: Number of records to retrieve. Default is 100.
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with analyst estimates data.
    :example: analyst_estimates('AAPL', period='quarter', limit=5)
    """
    path = f"/analyst-estimates/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "symbol": symbol,
        "period": __validate_period(value=period),
        "limit": limit,
    }
    result = __return_json_v3(path=path, query_vars=query_vars)
    fields = ('symbol', 'date', 'estimatedRevenueLow', 'estimatedRevenueHigh', 'estimatedRevenueAvg', 'estimatedEbitdaLow', 'estimatedEbitdaHigh', 'estimatedEbitdaAvg', 'estimatedEbitLow', 'estimatedEbitHigh', 'estimatedEbitAvg', 'estimatedNetIncomeLow', 'estimatedNetIncomeHigh', 'estimatedNetIncomeAvg', 'estimatedSgaExpenseLow', 'estimatedSgaExpenseHigh', 'estimatedSgaExpenseAvg', 'estimatedEpsAvg', 'estimatedEpsHigh', 'estimatedEpsLow', 'numberAnalystEstimatedRevenue', 'numberAnalystsEstimatedEps')
    return compress_json_to_tsv(result, fields) if tsv else result

def sales_revenue_by_segments(
    symbol: str,
    structure: str = "flat",
    period: str = "annual", 
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve sales revenue by segments data for a company.

    This function provides a breakdown of a company's revenue by different business segments,
    helping investors understand the company's revenue sources and business diversification.

    :param symbol: The stock symbol of the company (e.g., 'AAPL' for Apple Inc.)
    :param structure: The structure of the data. Can be 'flat' or 'nested' (default is 'flat')
    :param period: The period of the data. Can be 'annual' or 'quarterly' (default is 'annual')
    :return: A list of dictionaries containing sales revenue by segments data,
             or None if the request fails
    :example: sales_revenue_by_segments('AAPL', structure='nested', period='quarterly')
    """
    path = "revenue-product-segmentation"
    query_vars = {
        "apikey": API_KEY,
        "symbol": symbol,
        "structure": structure,
        "period": period
    }
    return __return_json_v4(path=path, query_vars=query_vars)


def revenue_geographic_segmentation(
    symbol: str,
    structure: str = "flat",
    period: str = "annual"
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve revenue geographic segmentation data for a company.

    This function provides a breakdown of a company's revenue by geographic region,
    helping investors understand the company's global market presence and diversification.

    :param symbol: The stock symbol of the company (e.g., 'AAPL' for Apple Inc.)
    :param structure: The structure of the data. Can be 'flat' or 'nested' (default is 'flat')
    :param period: The period of the data. Can be 'annual' or 'quarterly' (default is 'annual')
    :return: A list of dictionaries containing revenue geographic segmentation data,
             or None if the request fails
    :example: revenue_geographic_segmentation('AAPL', structure='nested', period='quarterly')
    """
    path = f"revenue-geographic-segmentation/"
    query_vars = {
        "apikey": API_KEY,
        "symbol": symbol,
        "structure": structure,
        "period": period
    }
    return __return_json_v4(path=path, query_vars=query_vars)

def esg_score(
    symbol: str,
    tsv: bool = True
) -> Union[List[Dict], str]:
    """
    Retrieve Environmental, Social, and Governance (ESG) ratings for a company.

    Provides insights into a company's sustainability and social responsibility performance.
    Useful for making informed investment decisions based on ESG factors.
    Data is sourced from corporate sustainability reports, ESG research firms, and government agencies.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with ESG ratings data.
    :example: esg_score('AAPL')
    """
    path = f"esg-environmental-social-governance-data"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    result = __return_json_v4(path=path, query_vars=query_vars)
    fields = ('date', 'symbol', 'environmentalScore', 'socialScore', 'governanceScore', 'ESGScore')
    return compress_json_to_tsv(result, fields) if tsv else result

def stock_grade(
    symbol: str,
    limit: int = 50,
    tsv: bool = True
) -> Union[List[Dict], str]:
    """
    Retrieve stock grades given by hedge funds, investment firms, and analysts.

    Provides ratings and insights on a company's financial performance,
    business model, and competitive landscape. Useful for understanding
    professional investors' views and identifying investment opportunities.

    :param symbol: Company ticker (e.g., 'AAPL')
    :param limit: Number of results to return (default: 50)
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with stock grade data.
    :example: stock_grade('AAPL', limit=10)
    """
    path = f"grade/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit}
    result = __return_json_v3(path=path, query_vars=query_vars)
    fields = ('symbol', 'date', 'gradingCompany', 'previousGrade', 'newGrade')
    return compress_json_to_tsv(result, fields) if tsv else result


def financial_score(
    symbol: str,
    tsv: bool = True
) -> Union[List[Dict], str]:
    """
    Retrieve the financial score for a company.

    Provides an assessment of a company's financial health and performance.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with financial score data.
    :example: financial_score('AAPL')
    """
    path = "score"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    result = __return_json_v4(path=path, query_vars=query_vars)
    fields = ('symbol', 'altmanZScore', 'piotroskiScore', 'workingCapital', 'totalAssets', 'retainedEarnings', 'ebit', 'marketCap', 'totalLiabilities', 'revenue')
    return compress_json_to_tsv(result, fields) if tsv else result

def owner_earnings(
    symbol: str,
    tsv: bool = True
) -> Union[List[Dict], str]:
    """
    Retrieve owner earnings data for a company.

    Provides insights into a company's earnings available for common shareholders.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with owner earnings data.
    :example: owner_earnings('AAPL')
    """
    path = "owner_earnings"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    result = __return_json_v4(path=path, query_vars=query_vars)
    fields = ('symbol', 'date', 'ownerEarnings', 'netIncome', 'depreciationAndAmortization', 'capitalExpenditure', 'changeInWorkingCapital')
    return compress_json_to_tsv(result, fields) if tsv else result

def upgrades_downgrades_consensus(
    symbol: str,
    tsv: bool = True
) -> Union[List[Dict], str]:
    """
    Retrieve the consensus rating for a company's stock.

    Provides an average rating from different analysts, offering a general
    idea of analysts' opinions about a company's stock. This can be used
    to make more informed investment decisions.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with consensus rating data.
             Data includes overall rating and individual analyst ratings.
    :example: upgrades_downgrades_consensus('AAPL')
    """
    path = "upgrades-downgrades-consensus"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    result = __return_json_v4(path=path, query_vars=query_vars)
    fields = ('symbol', 'date', 'analystRatings', 'rating', 'dcfDiff', 'ratingDetailsDCFScore', 'ratingDetailsDCFRecommendation', 'ratingDetailsROEScore', 'ratingDetailsROERecommendation', 'ratingDetailsROAScore', 'ratingDetailsROARecommendation', 'ratingDetailsDEScore', 'ratingDetailsDERecommendation', 'ratingDetailsPEScore', 'ratingDetailsPERecommendation', 'ratingDetailsPBScore', 'ratingDetailsPBRecommendation')
    return compress_json_to_tsv(result, fields) if tsv else result

def upgrades_downgrades_by_company(
    company: str,
    tsv: bool = True
) -> Union[List[Dict], str]:
    """
    Retrieve stock upgrades and downgrades issued by a specific analyst company.

    Provides a comprehensive list of rating changes for various stocks,
    including the rating change, analyst firm, and date.

    :param company: Name of the analyst company (e.g., 'Morgan Stanley').
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with upgrades and downgrades data.
    :example: upgrades_downgrades_by_company('Morgan Stanley')
    """
    path = "upgrades-downgrades-grading-company"
    query_vars = {"apikey": API_KEY, "company": company}
    result = __return_json_v4(path=path, query_vars=query_vars)
    return compress_json_to_tsv(result) if tsv else result

def search_mergers_acquisitions(
    name: str,
    tsv: bool = True
) -> Union[List[Dict], str]:
    """
    Search for M&A deals based on company name.

    Provides insights into mergers, acquisitions, and other corporate transactions
    for a specific company.

    :param name: Company name (e.g., 'Apple').
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with M&A deal data for the company.
    :example: search_mergers_acquisitions('Apple')
    """
    path = "mergers-acquisitions/search"
    query_vars = {"apikey": API_KEY, "name": name}
    result = __return_json_v4(path=path, query_vars=query_vars)
    fields = ('date', 'symbol', 'companyName', 'targetCompanyName', 'transactionValue', 'multiple', 'paidInCash', 'paidInStock', 'dealType')
    return compress_json_to_tsv(result, fields) if tsv else result

def executive_compensation(
    symbol: str,
    tsv: bool = True
) -> Union[List[Dict], str]:
    """
    Retrieve executive compensation data for a company.

    Provides insights into the compensation of key executives and their impact
    on shareholder value.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with executive compensation data.
    :example: executive_compensation('AAPL')
    """
    path = "governance/executive_compensation"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    result = __return_json_v4(path=path, query_vars=query_vars)
    fields = ('symbol', 'name', 'title', 'year', 'salary', 'bonus', 'stockAwards', 'optionAwards', 'nonEquityIncentives', 'pensionAndDeferred', 'otherComp', 'total')
    return compress_json_to_tsv(result, fields) if tsv else result

def compensation_benchmark(
    year: int,
    tsv: bool = True
) -> Union[List[Dict], str]:
    """
    Retrieve executive compensation benchmark data for a specific year.

    Provides insights into the compensation trends and benchmarks for key
    executives in various industries.

    :param year: Year for compensation benchmark data (e.g., 2023).
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with compensation benchmark data.
    :example: compensation_benchmark(2023)
    """
    path = "executive-compensation-benchmark"
    query_vars = {"apikey": API_KEY, "year": year}
    result = __return_json_v4(path=path, query_vars=query_vars)
    return compress_json_to_tsv(result) if tsv else result

def company_notes(
    symbol: str,
    tsv: bool = True
) -> Union[List[Dict], str]:
    """
    Retrieve company notes for a specific company.

    Provides additional insights and notes about a company's performance
    and operations.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with company notes data.
    :example: company_notes('AAPL')
    """
    path = "company-notes"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    result = __return_json_v4(path=path, query_vars=query_vars)
    fields = ('symbol', 'date', 'note')
    return compress_json_to_tsv(result, fields) if tsv else result

def historical_employee_count(
    symbol: str,
    tsv: bool = True
) -> Union[List[Dict], str]:
    """
    Retrieve historical employee count data for a company.

    Tracks workforce growth or decline over time, providing insights into
    company expansion, efficiency, and industry comparisons.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with historical employee count data.
    :example: historical_employee_count('AAPL')
    """
    path = "historical/employee_count"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    result = __return_json_v4(path=path, query_vars=query_vars)
    fields = ('symbol', 'date', 'acceptedDate', 'period', 'employeeCount')
    return compress_json_to_tsv(result, fields) if tsv else result

def employee_count(
    symbol: str,
    tsv: bool = True
) -> Union[List[Dict], str]:
    """
    Retrieve the current number of employees for a company.

    Provides insight into a company's size and potential operational scale.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with current employee count data.
    :example: employee_count('AAPL')
    """
    path = "employee_count"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    result = __return_json_v4(path=path, query_vars=query_vars)
    fields = ('symbol', 'date', 'acceptedDate', 'period', 'employeeCount')
    return compress_json_to_tsv(result, fields) if tsv else result

def analyst_recommendation(
    symbol: str,
    tsv: bool = True
) -> Union[List[Dict], str]:
    """
    Retrieve analyst recommendations for buying, selling, or holding a stock.

    Provides insights to help make informed investment decisions. Note that
    recommendations are not always accurate; investors should do their own research.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with analyst recommendations data.
             Includes analyst firm, rating, price target, and action (buy/sell/hold).
    :example: analyst_recommendation('AAPL')
    """
    path = f"analyst-stock-recommendations/{symbol}"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v3(path=path, query_vars=query_vars)
    fields = ('symbol', 'date', 'analystFirm', 'rating', 'priceTarget', 'action')
    return compress_json_to_tsv(result, fields) if tsv else result
