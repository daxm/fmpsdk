#!/usr/bin/env python3

import os
import typing

from dotenv import load_dotenv

import fmpsdk

# Load API key from environment
load_dotenv()
apikey = os.environ.get("apikey")

# Common variables used across multiple sections
symbol: str = "AAPL"
symbols: typing.List[str] = ["AAPL", "CSCO", "QQQQ"]
exchange: str = "NYSE"
exchanges: typing.List[str] = ["NYSE", "NASDAQ"]
query: str = "AA"
limit: int = 3
period: str = "quarter"
download: bool = True
from_date: str = "2020-04-26"
to_date: str = "2020-07-26"
time_delta_5min: str = "5min"
time_delta_15min: str = "15min"
time_delta_daily: str = "daily"

# Company Valuation Methods
market_cap_more_than: int = 1000000000
beta_more_than: int = 1
volume_more_than: int = 10000
sector: str = "Technology"
dividend_more_than: int = 0
industry: str = "Software"
filing_type: str = "10-K"

print(f"Company Profile: {fmpsdk.company_profile(apikey=apikey, symbol=symbol)=}")
print(f"Company Quote: {fmpsdk.quote(apikey=apikey, symbol=symbol)=}")
print(f"Multiple Company Quotes: {fmpsdk.quote(apikey=apikey, symbol=symbols)=}")
print(f"Key Executives: {fmpsdk.key_executives(apikey=apikey, symbol=symbol)=}")
print(f"Search: {fmpsdk.search(apikey=apikey, query=query, exchange=exchange, limit=limit)=}")
print(f"Ticker Search: {fmpsdk.search_ticker(apikey=apikey, query=query, exchange=exchange, limit=limit)=}")

# Financial Statements
print(f"Annual Income Statement: {fmpsdk.income_statement(apikey=apikey, symbol=symbol)=}")
print(f"Quarterly Income Statement: {fmpsdk.income_statement(apikey=apikey, symbol=symbol, period=period)=}")
print(f"Annual Balance Sheet Statement: {fmpsdk.balance_sheet_statement(apikey=apikey, symbol=symbol)=}")
print(f"Quarterly Balance Sheet Statement: {fmpsdk.balance_sheet_statement(apikey=apikey, symbol=symbol, period=period)=}")
print(f"Annual Cash Flow Statement: {fmpsdk.cash_flow_statement(apikey=apikey, symbol=symbol)=}")
print(f"Quarterly Cash Flow Statement: {fmpsdk.cash_flow_statement(apikey=apikey, symbol=symbol, period=period)=}")
print(f"Financial Statement Symbols List: {fmpsdk.financial_statement_symbol_lists(apikey=apikey)=}")

# Financial Statement Growth
print(f"Income Statement Growth: {fmpsdk.income_statement_growth(apikey=apikey, symbol=symbol, limit=limit)=}")
print(f"Balance Sheet Statement Growth: {fmpsdk.balance_sheet_statement_growth(apikey=apikey, symbol=symbol, limit=limit)=}")
print(f"Cash Flow Statement Growth: {fmpsdk.cash_flow_statement_growth(apikey=apikey, symbol=symbol, limit=limit)=}")

# As Reported Financial Statements
print(f"Annual Income Statement as Reported: {fmpsdk.income_statement_as_reported(apikey=apikey, symbol=symbol)=}")
print(f"Quarterly Income Statement as Reported: {fmpsdk.income_statement_as_reported(apikey=apikey, symbol=symbol, period=period)=}")
print(f"Annual Balance Sheet Statement as Reported: {fmpsdk.balance_sheet_statement_as_reported(apikey=apikey, symbol=symbol)=}")
print(f"Quarterly Balance Sheet Statement as Reported: {fmpsdk.balance_sheet_statement_as_reported(apikey=apikey, symbol=symbol, period=period)=}")
print(f"Annual Cash Flow Statement as Reported: {fmpsdk.cash_flow_statement_as_reported(apikey=apikey, symbol=symbol)=}")
print(f"Quarterly Cash Flow Statement as Reported: {fmpsdk.cash_flow_statement_as_reported(apikey=apikey, symbol=symbol, period=period)=}")
print(f"Annual Full Financial Statement as Reported: {fmpsdk.financial_statement_full_as_reported(apikey=apikey, symbol=symbol)=}")
print(f"Quarterly Full Financial Statement as Reported: {fmpsdk.financial_statement_full_as_reported(apikey=apikey, symbol=symbol, period=period)=}")

# Financial Metrics and Ratios
print(f"Financial Ratios (TTM): {fmpsdk.financial_ratios_ttm(apikey=apikey, symbol=symbol)=}")
print(f"Annual Financial Ratios: {fmpsdk.financial_ratios(apikey=apikey, symbol=symbol)=}")
print(f"Quarterly Financial Ratios: {fmpsdk.financial_ratios(apikey=apikey, symbol=symbol, period=period)=}")
print(f"Annual Enterprise Values: {fmpsdk.enterprise_values(apikey=apikey, symbol=symbol)=}")
print(f"Quarterly Enterprise Values: {fmpsdk.enterprise_values(apikey=apikey, symbol=symbol, period=period)=}")
print(f"Key Metrics (TTM): {fmpsdk.key_metrics_ttm(apikey=apikey, symbol=symbol)=}")
print(f"Annual Key Metrics: {fmpsdk.key_metrics(apikey=apikey, symbol=symbol)=}")
print(f"Quarterly Key Metrics: {fmpsdk.key_metrics(apikey=apikey, symbol=symbol, period=period)=}")
print(f"Annual Financial Growth: {fmpsdk.financial_growth(apikey=apikey, symbol=symbol)=}")
print(f"Quarterly Financial Growth: {fmpsdk.financial_growth(apikey=apikey, symbol=symbol, period=period)=}")

# Company Analysis and Ratings
print(f"Company Rating: {fmpsdk.rating(apikey=apikey, symbol=symbol)=}")
print(f"Historical Company Rating: {fmpsdk.historical_rating(apikey=apikey, symbol=symbol, limit=limit)=}")
print(f"Discounted Cash Flow: {fmpsdk.discounted_cash_flow(apikey=apikey, symbol=symbol)=}")
print(f"Annual Historical Discounted Cash Flow: {fmpsdk.historical_discounted_cash_flow(apikey=apikey, symbol=symbol)=}")
print(f"Quarterly Historical Discounted Cash Flow: {fmpsdk.historical_discounted_cash_flow(apikey=apikey, symbol=symbol, period=period)=}")
print(f"Daily Historical Discounted Cash Flow: {fmpsdk.historical_daily_discounted_cash_flow(apikey=apikey, symbol=symbol)=}")
print(f"Market Capitalization: {fmpsdk.market_capitalization(apikey=apikey, symbol=symbol)=}")
print(f"Historical Market Capitalization: {fmpsdk.historical_market_capitalization(apikey=apikey, symbol=symbol, limit=limit)=}")
print(f"Historical Employee Count: {fmpsdk.historical_employee_count(apikey=apikey, symbol=symbol)=}")
print(f"Upgrades/Downgrades Consensus: {fmpsdk.upgrades_downgrades_consensus(apikey=apikey, symbol=symbol)=}")

# Stock Screening and Lists
print(f"Symbols List: {fmpsdk.symbols_list(apikey=apikey)=}")
print(f"Stock Screener (Sector): {fmpsdk.stock_screener(apikey=apikey, market_cap_more_than=market_cap_more_than, beta_more_than=beta_more_than, volume_more_than=volume_more_than, sector=sector, exchange=exchange, dividend_more_than=dividend_more_than, limit=limit)=}")
print(f"Stock Screener (Industry): {fmpsdk.stock_screener(apikey=apikey, market_cap_more_than=market_cap_more_than, beta_more_than=beta_more_than, volume_more_than=volume_more_than, sector=sector, industry=industry, exchange=exchange, dividend_more_than=dividend_more_than, limit=limit)=}")
print(f"Stock Screener (Multiple Exchanges): {fmpsdk.stock_screener(apikey=apikey, market_cap_more_than=market_cap_more_than, beta_more_than=beta_more_than, volume_more_than=volume_more_than, exchange=exchanges)=}")
print(f"Delisted Companies: {fmpsdk.delisted_companies(apikey=apikey, limit=limit)=}")

# News and Press Releases
print(f"Stock News (Single): {fmpsdk.stock_news(apikey=apikey, tickers=symbol)=}")
print(f"Stock News (Multiple): {fmpsdk.stock_news(apikey=apikey, tickers=symbols)=}")
print(f"Stock News (Latest): {fmpsdk.stock_news(apikey=apikey, limit=limit)=}")
print(f"Press Releases: {fmpsdk.press_releases(apikey=apikey, symbol=symbol)=}")
print(f"FMP Articles: {fmpsdk.fmp_articles(apikey=apikey, page=0, size=10)=}")
print(f"General News: {fmpsdk.general_news(apikey=apikey, page=0)=}")
print(f"News Sentiment RSS: {fmpsdk.news_sentiment_rss(apikey=apikey, page=0)=}")
print(f"Mergers & Acquisitions News: {fmpsdk.mergers_acquisitions_rss_feed(apikey=apikey, page=0)=}")

# SEC Filings and Institutional Data
print(f"SEC Filings: {fmpsdk.sec_filings(apikey=apikey, symbol=symbol, filing_type=filing_type)=}")
print(f"SEC RSS Feeds: {fmpsdk.sec_rss_feeds(apikey=apikey, limit=10)=}")
print(f"Institutional Holders: {fmpsdk.institutional_holders(apikey=apikey, symbol=symbol)=}")
print(f"Mutual Fund Holders: {fmpsdk.mutual_fund_holders(apikey=apikey, symbol=symbol)=}")
print(f"Institutional Symbol Ownership: {fmpsdk.institutional_symbol_ownership(apikey=apikey, symbol='AAPL', limit=4, includeCurrentQuarter=True)=}")

# CIK and Form 13F Data
print(f"CIK List: {fmpsdk.cik_list(apikey=apikey)=}")
print(f"CIK Search by Name: {fmpsdk.cik_search(apikey=apikey, name='APPLE')=}")
print(f"CIK Search by CIK: {fmpsdk.cik(apikey=apikey, cik_id='0000320193')=}")
print(f"Form 13F: {fmpsdk.form_13f(apikey=apikey, cik_id='0000320193', date='2023-12-31')=}")
print(f"CUSIP Mapping: {fmpsdk.cusip(apikey=apikey, cik_id='0000320193')=}")
print(f"CIK to Name Mapping: {fmpsdk.mapper_cik_name(apikey=apikey, name='APPLE')=}")
print(f"CIK to Company Mapping: {fmpsdk.mapper_cik_company(apikey=apikey, ticker='AAPL')=}")

# Insider Trading
print(f"Insider Trading RSS Feed: {fmpsdk.insider_trading_rss_feed(apikey=apikey, limit=10)=}")
print(f"Insider Trading Statistics: {fmpsdk.insider_trade_statistics(apikey=apikey, symbol='AAPL')=}")
print(f"Insider Trading with Name: {fmpsdk.insider_trading(apikey=apikey, symbol='AAPL', reporting_name='Tim Cook', limit=10)=}")

# Senate Trading
print(f"Senate Trading RSS Feed: {fmpsdk.senate_trading_rss(apikey=apikey, page=0)=}")
print(f"Senate Trading by Symbol: {fmpsdk.senate_trading_symbol(apikey=apikey, symbol='AAPL')=}")
print(f"Senate Disclosure RSS Feed: {fmpsdk.senate_disclosure_rss(apikey=apikey, page=0)=}")

# Market Performance and Activity
print(f"Active Stock in Market: {fmpsdk.actives(apikey=apikey)=}")
print(f"Stock in Market Gainers: {fmpsdk.gainers(apikey=apikey)=}")
print(f"Active Stock in Market Losers: {fmpsdk.losers(apikey=apikey)=}")
print(f"Market Hours: {fmpsdk.market_hours(apikey=apikey)=}")
print(f"Market Open: {fmpsdk.market_open(apikey=apikey)=}")
print(f"All Exchange Market Hours: {fmpsdk.all_exchange_market_hours(apikey=apikey)=}")
print(f"Sectors Performance: {fmpsdk.sectors_performance(apikey=apikey, limit=limit)=}")
print(f"Historical Sectors Performance: {fmpsdk.historical_sectors_performance(apikey=apikey)=}")

# Market Indexes
index_symbol: str = "^RUITR"
print(f"List Market Indexes: {fmpsdk.indexes(apikey=apikey)=}")
print(f"Index Quote: {fmpsdk.quote(apikey=apikey, symbol=index_symbol)=}")
print(f"Available Indexes: {fmpsdk.available_indexes(apikey=apikey)=}")
print(f"Intraday Historical Index Prices: {fmpsdk.historical_chart(apikey=apikey, symbol=index_symbol, time_delta=time_delta_15min, from_date=from_date, to_date=to_date)=}")
print(f"Historical Market Index: {fmpsdk.historical_price_full(apikey=apikey, symbol=index_symbol)=}")

# Market Constituents
print(f"SP500 Constituents: {fmpsdk.sp500_constituent(apikey=apikey)=}")
print(f"Historical SP500 Constituents: {fmpsdk.historical_sp500_constituent(apikey=apikey)=}")
print(f"NASDAQ Constituents: {fmpsdk.nasdaq_constituent(apikey=apikey)=}")
print(f"Historical NASDAQ Constituents: {fmpsdk.historical_nasdaq_constituent(apikey=apikey)=}")
print(f"Dow Jones Constituents: {fmpsdk.dowjones_constituent(apikey=apikey)=}")
print(f"Historical Dow Jones Constituents: {fmpsdk.historical_dowjones_constituent(apikey=apikey)=}")

# Commodities
commodity_symbol: str = "ZGUSD"
commodity_symbols: typing.List[str] = ["ZGUSD", "CLUSD", "HGUSD"]
print(f"Available Commodities: {fmpsdk.available_commodities(apikey=apikey)=}")
print(f"Commodities List: {fmpsdk.commodities_list(apikey=apikey)=}")
print(f"Commodity Quote: {fmpsdk.quote(apikey=apikey, symbol=commodity_symbols)=}")
print(f"Historical Commodity Prices: {fmpsdk.historical_chart(apikey=apikey, symbol=commodity_symbol, time_delta=time_delta_5min, from_date=from_date, to_date=to_date)=}")
print(f"Historical Daily Commodity Prices: {fmpsdk.historical_price_full(apikey=apikey, symbol=commodity_symbol, from_date=from_date, to_date=to_date)=}")

# ETF
etf_symbol: str = "PRNT"
print(f"Available ETFs: {fmpsdk.available_etfs(apikey=apikey)=}")
print(f"ETFs List: {fmpsdk.etf_list(apikey=apikey)=}")
print(f"ETF Quote: {fmpsdk.quote(apikey=apikey, symbol=etf_symbol)=}")
print(f"ETF Price Realtime: {fmpsdk.etf_price_realtime(apikey=apikey)=}")
print(f"ETF Info: {fmpsdk.etf_info(apikey=apikey, symbol='SPY')=}")
print(f"ETF Sector Weightings: {fmpsdk.etf_sector_weightings(apikey=apikey, symbol='SPY')=}")
print(f"ETF Country Weightings: {fmpsdk.etf_country_weightings(apikey=apikey, symbol='SPY')=}")
print(f"Historical ETF Prices: {fmpsdk.historical_chart(apikey=apikey, symbol=etf_symbol, time_delta=time_delta_5min, from_date=from_date, to_date=to_date)=}")
print(f"Historical Daily ETF Prices: {fmpsdk.historical_price_full(apikey=apikey, symbol=etf_symbol)=}")
print(f"Historical ETF Dividends: {fmpsdk.historical_stock_dividend(apikey=apikey, symbol=etf_symbol)=}")
print(f"Historical ETF Split: {fmpsdk.historical_stock_split(apikey=apikey, symbol=etf_symbol)=}")

# Mutual Funds
mutual_fund_symbol: str = "JMCRX"
mutual_funds: typing.List[str] = ["JBFRX", "BPLEX", "VEVRX"]
print(f"Available Mutual Funds: {fmpsdk.available_mutual_funds(apikey=apikey)=}")
print(f"Mutual Funds List: {fmpsdk.mutual_fund_list(apikey=apikey)=}")
print(f"Mutual Fund Quote: {fmpsdk.quote(apikey=apikey, symbol=mutual_funds)=}")
print(f"Historical Mutual Fund Prices: {fmpsdk.historical_chart(apikey=apikey, symbol=mutual_fund_symbol, time_delta=time_delta_5min, from_date=from_date, to_date=to_date)=}")
print(f"Historical Daily Mutual Fund Prices: {fmpsdk.historical_price_full(apikey=apikey, symbol=mutual_fund_symbol)=}")
print(f"Historical Mutual Fund Dividends: {fmpsdk.historical_stock_dividend(apikey=apikey, symbol=mutual_fund_symbol)=}")
print(f"Historical Mutual Fund Split: {fmpsdk.historical_stock_split(apikey=apikey, symbol=mutual_fund_symbol)=}")

# EuroNext
euronext_symbol: str = "KIN.BR"
print(f"Available EuroNext: {fmpsdk.available_euronext(apikey=apikey)=}")
print(f"EuroNext List: {fmpsdk.euronext_list(apikey=apikey)=}")
print(f"EuroNext Quote: {fmpsdk.quote(apikey=apikey, symbol=euronext_symbol)=}")
print(f"Historical EuroNext Prices: {fmpsdk.historical_chart(apikey=apikey, symbol=euronext_symbol, time_delta=time_delta_5min, from_date=from_date, to_date=to_date)=}")
print(f"Historical Daily EuroNext Prices: {fmpsdk.historical_price_full(apikey=apikey, symbol=euronext_symbol)=}")
print(f"Historical EuroNext Dividends: {fmpsdk.historical_stock_dividend(apikey=apikey, symbol=euronext_symbol)=}")
print(f"Historical EuroNext Split: {fmpsdk.historical_stock_split(apikey=apikey, symbol=euronext_symbol)=}")

# TSX
tsx_symbol: str = "FNV.TO"
print(f"Available TSX: {fmpsdk.available_tsx(apikey=apikey)=}")
print(f"TSX List: {fmpsdk.tsx_list(apikey=apikey)=}")
print(f"TSX Quote: {fmpsdk.quote(apikey=apikey, symbol=tsx_symbol)=}")
print(f"Historical TSX Prices: {fmpsdk.historical_chart(apikey=apikey, symbol=tsx_symbol, time_delta=time_delta_5min, from_date=from_date, to_date=to_date)=}")
print(f"Historical Daily TSX Prices: {fmpsdk.historical_price_full(apikey=apikey, symbol=tsx_symbol)=}")
print(f"Historical TSX Dividends: {fmpsdk.historical_stock_dividend(apikey=apikey, symbol=tsx_symbol)=}")
print(f"Historical TSX Split: {fmpsdk.historical_stock_split(apikey=apikey, symbol=tsx_symbol)=}")

# Cryptocurrencies
crypto_symbol: str = "BTCUSD"
news_symbol: str = "BTC"
print(f"Cryptocurrencies List: {fmpsdk.cryptocurrencies_list(apikey=apikey)=}")
print(f"Available Cryptocurrencies: {fmpsdk.available_cryptocurrencies(apikey=apikey)=}")
print(f"Last Crypto Price: {fmpsdk.last_crypto_price(apikey=apikey, symbol=crypto_symbol)=}")
print(f"Historical Cryptocurrencies Prices: {fmpsdk.historical_chart(apikey=apikey, symbol=crypto_symbol, time_delta=time_delta_5min, from_date=from_date, to_date=to_date)=}")
print(f"Historical Daily Cryptocurrencies Prices: {fmpsdk.historical_price_full(apikey=apikey, symbol=crypto_symbol)=}")
print(f"Crypto News: {fmpsdk.crypto_news(apikey=apikey, symbol=news_symbol, from_date='2023-01-01', to_date='2023-12-31', limit=10)=}")

# FOREX (FX)
forex_symbol: str = "EURUSD"
print(f"Currency Exchange Rates: {fmpsdk.forex(apikey=apikey)=}")
print(f"Forex List: {fmpsdk.forex_list(apikey=apikey)=}")
print(f"Available Forex Pairs: {fmpsdk.available_forex(apikey=apikey)=}")
print(f"Historical Forex Prices: {fmpsdk.historical_chart(apikey=apikey, symbol=forex_symbol, time_delta=time_delta_5min, from_date=from_date, to_date=to_date)=}")
print(f"Historical Daily Forex Prices: {fmpsdk.historical_price_full(apikey=apikey, symbol=forex_symbol)=}")
print(f"Forex News: {fmpsdk.forex_news(apikey=apikey, symbol=forex_symbol, from_date='2023-01-01', to_date='2023-12-31', limit=10)=}")

# Real-time Data
print(f"Live Full Price: {fmpsdk.live_full_price(apikey=apikey)=}")
print(f"Full Real Time Price: {fmpsdk.full_real_time_price(apikey=apikey)=}")

# Sentiment Analysis
print(f"Trending Bullish Sentiment: {fmpsdk.trending_sentiment(apikey=apikey, type='bullish', source='stocktwits')=}")
print(f"Bearish Sentiment Change: {fmpsdk.sentiment_change(apikey=apikey, type='bearish', source='stocktwits')=}")

# Economic Indicators
indicator_name: str = "GDP"
print(f"GDP Data: {fmpsdk.economic_indicator(apikey=apikey, name=indicator_name, from_date='2020-01-01', to_date='2023-12-31')=}")
print(f"Treasury Rates: {fmpsdk.treasury_rates(apikey=apikey, from_date='2023-01-01', to_date='2023-12-31')=}")

# Calendar Events
print(f"Earning Calendar: {fmpsdk.earning_calendar(apikey=apikey)=}")
print(f"Earning Calendar with Date Range: {fmpsdk.earning_calendar(apikey=apikey, from_date=from_date, to_date=to_date)=}")
print(f"Historical Earning Calendar: {fmpsdk.historical_earning_calendar(apikey=apikey, symbol=symbol, limit=limit)=}")
print(f"Confirmed Earnings Calendar: {fmpsdk.earning_calendar_confirmed(apikey=apikey, from_date='2024-01-01', to_date='2024-12-31')=}")
print(f"IPO Calendar: {fmpsdk.ipo_calendar(apikey=apikey, from_date=from_date, to_date=to_date)=}")
print(f"Stock Split Calendar: {fmpsdk.stock_split_calendar(apikey=apikey, from_date=from_date, to_date=to_date)=}")
print(f"Dividend Calendar: {fmpsdk.dividend_calendar(apikey=apikey, from_date=from_date, to_date=to_date)=}")
print(f"Economic Calendar: {fmpsdk.economic_calendar(apikey=apikey, from_date=from_date, to_date=to_date)=}")

# Bulk Data Operations
print(f"Bulk Historical EOD: {fmpsdk.bulk_historical_eod(apikey=apikey, date='2023-12-31')=}")
print(f"Bulk Company Profiles: {fmpsdk.bulk_profiles(apikey=apikey)=}")
print(f"Historical Survivorship Bias Free EOD: {fmpsdk.historical_survivorship_bias_free_eod(apikey=apikey)=}")

# Available Market Data
print(f"Available Sectors: {fmpsdk.available_sectors(apikey=apikey)=}")
print(f"Available Industries: {fmpsdk.available_industries(apikey=apikey)=}")

# Commitment of Traders Report
print(f"COT Report List: {fmpsdk.commitment_of_traders_report_list(apikey=apikey)=}")
print(f"COT Report: {fmpsdk.commitment_of_traders_report(apikey=apikey, symbol='ES', from_date='2023-01-01', to_date='2023-12-31')=}")

# Bulk Operations and Batch Quotes
print(f"Batch Quote: {fmpsdk.batch_quote(apikey=apikey, symbol=symbols)=}")
print(f"Batch Pre/Post Market Trade: {fmpsdk.batch_pre_post_market_trade(apikey=apikey, symbol=symbols)=}")
print(f"Scores Bulk: {fmpsdk.scores_bulk(apikey=apikey)=}")
print(f"Upgrades/Downgrades Consensus Bulk: {fmpsdk.upgrades_downgrades_consensus_bulk(apikey=apikey)=}")

# Additional ETF Functions
print(f"ETF Info: {fmpsdk.etf_info(apikey=apikey, symbol='SPY')=}")
print(f"ETF Holders: {fmpsdk.etf_holders(apikey=apikey, symbol='SPY')=}")

# Additional Market Performance Functions
print(f"Biggest Gainers: {fmpsdk.biggest_gainers(apikey=apikey)=}")
print(f"Biggest Losers: {fmpsdk.biggest_losers(apikey=apikey)=}")
print(f"Most Actives: {fmpsdk.most_actives(apikey=apikey)=}")

# Additional Stock Time Series Functions
print(f"Quote Short: {fmpsdk.quote_short(apikey=apikey, symbol=symbol)=}")
print(f"Exchange Realtime: {fmpsdk.exchange_realtime(apikey=apikey, exchange=exchange)=}")

# Additional Institutional Functions
print(f"ETF Holders: {fmpsdk.etf_holders(apikey=apikey, symbol='SPY')=}")

# Additional Senate Trading Functions
print(f"Senate Disclosure Symbol: {fmpsdk.senate_disclosure_symbol(apikey=apikey, symbol='AAPL')=}")

# Additional Technical Analysis
print(f"Technical Indicators: {fmpsdk.technical_indicators(apikey=apikey, symbol='AAPL', period=60, type='ema')=}")

# Additional Available Lists
print(f"Available Traded List: {fmpsdk.available_traded_list(apikey=apikey)=}")

# Additional Commitment of Traders Report
print(f"COT Report Analysis: {fmpsdk.commitment_of_traders_report_analysis(apikey=apikey, symbol='ES')=}")

# Additional IPO Calendar
print(f"IPO Calendar Confirmed: {fmpsdk.ipo_calendar_confirmed(apikey=apikey, from_date=from_date, to_date=to_date)=}")

# Additional Social Sentiment
print(f"Social Sentiments: {fmpsdk.social_sentiments(apikey=apikey, symbol='AAPL')=}")

# Additional Earnings Surprises
print(f"Earnings Surprises: {fmpsdk.earnings_surprises(apikey=apikey, symbol='AAPL')=}")

# Additional Financial Statement
print(f"Financial Statement: {fmpsdk.financial_statement(apikey=apikey, symbol='AAPL', period=period)=}")

# Additional Shares Float
print(f"Shares Float: {fmpsdk.shares_float(apikey=apikey, symbol='AAPL')=}")
