import logging

from .alternative_data import (
    commitment_of_traders_report,
    commitment_of_traders_report_analysis,
    commitment_of_traders_report_list,
)
from .calendar import (
    dividend_calendar,
    earning_calendar,
    economic_calendar,
    historical_earning_calendar,
    ipo_calendar,
    stock_split_calendar,
)
from .commodities import available_commodities, commodities_list
from .company_valuation import (
    advanced_discounted_cash_flow,
    all_countries,
    analyst_estimates,
    analyst_recommendation,
    available_exchanges,
    available_industries,
    available_sectors,
    available_traded_list,
    balance_sheet_statement,
    balance_sheet_statement_as_reported,
    balance_sheet_statement_growth,
    batch_earning_call_transcript,
    cash_flow_statement,
    cash_flow_statement_as_reported,
    cash_flow_statement_growth,
    company_core_information,
    company_notes,
    company_outlook,
    company_profile,
    compensation_benchmark,
    delisted_companies,
    discounted_cash_flow,
    earning_call_transcript,
    earning_call_transcripts_available_dates,
    earnings_surprises,
    employee_count,
    enterprise_values,
    esg_score,
    etf_list,
    executive_compensation,
    financial_growth,
    financial_ratios,
    financial_ratios_ttm,
    financial_score,
    financial_statement,
    financial_statement_full_as_reported,
    financial_statement_symbol_lists,
    historical_daily_discounted_cash_flow,
    historical_discounted_cash_flow,
    historical_employee_count,
    historical_market_capitalization,
    historical_rating,
    income_statement,
    income_statement_as_reported,
    income_statement_growth,
    is_market_open,
    key_executives,
    key_metrics,
    key_metrics_ttm,
    market_capitalization,
    mergers_acquisitions_rss_feed,
    owner_earnings,
    press_releases,
    rating,
    revenue_geographic_segmentation,
    sales_revenue_by_segments,
    search,
    search_mergers_acquisitions,
    search_ticker,
    sec_filings,
    stock_grade,
    stock_peers,
    stock_screener,
    symbols_list,
    upgrades_downgrades,
    upgrades_downgrades_by_company,
    upgrades_downgrades_consensus,
    upgrades_downgrades_rss_feed,
)
from .cryptocurrencies import available_cryptocurrencies, cryptocurrencies_list
from .etf import available_efts, available_etfs, etf_price_realtime
from .euronext import available_euronext, euronext_list
from .forex import (
    available_forex,
    forex,
    forex_list,
    fx_price_quote
)
from .general import historical_chart, historical_price_full, quote
from .insider_trading import (
    insider_trading,
    insider_trading_rss_feed,
    mapper_cik_company,
    mapper_cik_name,
)
from .institutional_fund import (
    cik,
    cik_list,
    cik_search,
    cusip,
    etf_country_weightings,
    etf_holders,
    etf_sector_weightings,
    form_13f,
    institutional_holders,
    mutual_fund_holders,
    sec_rss_feeds,
)
from .market_indexes import (
    available_indexes,
    dowjones_constituent,
    historical_dowjones_constituent,
    historical_nasdaq_constituent,
    historical_sp500_constituent,
    indexes,
    nasdaq_constituent,
    sp500_constituent,
)
from .mutual_funds import available_mutual_funds, mutual_fund_list
from .news import fmp_articles, general_news, stock_news
from .senate import (
    senate_disclosure_rss,
    senate_disclosure_symbol,
    senate_trading_rss,
    senate_trading_symbol,
)
from .shares_float import shares_float, historical_share_float
from .stock_market import (
    actives,
    gainers,
    losers,
    market_hours,
    sectors_performance,
    fail_to_deliver,
    sector_pe_ratio,
    industry_pe_ratio,
    batch_eod_prices,
    multiple_company_prices,
)
from .stock_time_series import (
    exchange_realtime,
    historical_stock_dividend,
    historical_stock_split,
    historical_survivorship_bias_free_eod,
    quote_short,
)
from .technical_indicators import technical_indicators
from .tsx import available_tsx, tsx_list
from .price_target import (
    price_targets,
    price_target_summary,
    price_target_by_analyst_name,
    price_target_by_company,
    price_target_consensus,
    price_target_rss_feed,
)
from .social_sentiment import (
    historical_social_sentiment,
    trending_social_sentiment,
    social_sentiment_changes,
)
from .economics import (
    treasury_rates,
    economic_indicators,
    market_risk_premium,
)
from .crowdfunding import crowdfunding_rss_feed, crowdfunding_search, crowdfunding_by_cik

attribution: str = "Data provided by Financial Modeling Prep"
logging.info(attribution)

__all__ = [
    "actives",
    "advanced_discounted_cash_flow",
    "all_countries",
    "all_shares_float",
    "analyst_estimates",
    "analyst_recommendation",
    "available_commodities",
    "available_cryptocurrencies",
    "available_etfs",
    "available_euronext",
    "available_exchanges",
    "available_forex",
    "available_indexes",
    "available_industries",
    "available_mutual_funds",
    "available_sectors",
    "available_traded_list",
    "available_tsx",
    "balance_sheet_statement",
    "balance_sheet_statement_as_reported",
    "balance_sheet_statement_growth",
    "batch_earning_call_transcript",
    "batch_eod_prices",
    "cash_flow_statement",
    "cash_flow_statement_as_reported",
    "cash_flow_statement_growth",
    "cik",
    "cik_list",
    "cik_search",
    "commitment_of_traders_report",
    "commitment_of_traders_report_analysis",
    "commitment_of_traders_report_list",
    "commodities_list",
    "company_core_information",
    "company_notes",
    "company_outlook",
    "company_profile",
    "company_share_float",
    "compensation_benchmark",
    "crowdfunding_by_cik",
    "crowdfunding_offerings",
    "crowdfunding_rss_feed",
    "crowdfunding_search",
    "cryptocurrencies_list",
    "cusip",
    "delisted_companies",
    "discounted_cash_flow",
    "dividend_calendar",
    "dowjones_constituent",
    "earning_call_transcript",
    "earning_call_transcripts_available_dates",
    "earning_calendar",
    "earnings_surprises",
    "economic_calendar",
    "economic_indicators",
    "employee_count",
    "enterprise_values",
    "esg_score",
    "etf_country_weightings",
    "etf_holders",
    "etf_list",
    "etf_price_realtime",
    "etf_sector_weightings",
    "euronext_list",
    "exchange_realtime",
    "executive_compensation",
    "fail_to_deliver",
    "financial_growth",
    "financial_ratios",
    "financial_ratios_ttm",
    "financial_score",
    "financial_statement",
    "financial_statement_full_as_reported",
    "financial_statement_symbol_lists",
    "fmp_articles",
    "form_13f",
    "forex",
    "forex_list",
    "fx_price_quote",
    "gainers",
    "general_news",
    "historical_chart",
    "historical_daily_discounted_cash_flow",
    "historical_discounted_cash_flow",
    "historical_dowjones_constituent",
    "historical_earning_calendar",
    "historical_employee_count",
    "historical_market_capitalization",
    "historical_nasdaq_constituent",
    "historical_price_full",
    "historical_rating",
    "historical_share_float",
    "historical_social_sentiment",
    "historical_sp500_constituent",
    "historical_stock_dividend",
    "historical_stock_split",
    "historical_survivorship_bias_free_eod",
    "income_statement",
    "income_statement_as_reported",
    "income_statement_growth",
    "indexes",
    "industry_pe_ratio",
    "insider_trading",
    "insider_trading_rss_feed",
    "institutional_holders",
    "ipo_calendar",
    "is_market_open",
    "key_executives",
    "key_metrics",
    "key_metrics_ttm",
    "losers",
    "mapper_cik_company",
    "mapper_cik_name",
    "market_capitalization",
    "market_hours",
    "market_risk_premium",
    "mergers_acquisitions_rss_feed",
    "multiple_company_prices",
    "mutual_fund_holders",
    "mutual_fund_list",
    "nasdaq_constituent",
    "owner_earnings",
    "press_releases",
    "price_target_by_analyst_name",
    "price_target_by_company",
    "price_target_consensus",
    "price_target_rss_feed",
    "price_target_summary",
    "price_targets",
    "quote",
    "quote_short",
    "rating",
    "revenue_geographic_segmentation",
    "sales_revenue_by_segments",
    "search",
    "search_mergers_acquisitions",
    "search_ticker",
    "sec_filings",
    "sec_rss_feeds",
    "sector_pe_ratio",
    "sectors_performance",
    "senate_disclosure_rss",
    "senate_disclosure_symbol",
    "senate_trading_rss",
    "senate_trading_symbol",
    "shares_float",
    "social_sentiment_changes",
    "sp500_constituent",
    "stock_grade",
    "stock_news",
    "stock_peers",
    "stock_screener",
    "stock_split_calendar",
    "symbols_list",
    "technical_indicators",
    "trending_social_sentiment",
    "treasury_rates",
    "tsx_list",
    "upgrades_downgrades",
    "upgrades_downgrades_by_company",
    "upgrades_downgrades_consensus",
    "upgrades_downgrades_rss_feed",
]