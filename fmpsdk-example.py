#!/usr/bin/env python3

import os
import typing

from dotenv import load_dotenv

import fmpsdk

# Actual API key is stored in a .env file.  Not good to store API key directly in script.
load_dotenv()
apikey = os.environ.get("apikey")

# Company Valuation Methods
symbol: str = "AAPL"
symbols: typing.List[str] = ["AAPL", "CSCO", "QQQQ"]
exchange: str = "NYSE"
exchanges: typing.List[str] = ["NYSE", "NASDAQ"]
query: str = "AA"
limit: int = 3
period: str = "quarter"
download: bool = True
market_cap_more_than: int = 1000000000
beta_more_than: int = 1
volume_more_than: int = 10000
sector: str = "Technology"
dividend_more_than: int = 0
industry: str = "Software"
filing_type: str = "10-K"
print(f"Company Profile: {fmpsdk.company_profile(apikey=apikey, symbol=symbol)=}")
# print(f"Company Quote: {fmpsdk.quote(apikey=apikey, symbol=symbol)=}")
# print(f"Multiple Company Quotes: {fmpsdk.quote(apikey=apikey, symbol=symbols)=}")
# print(f"Key Executives: {fmpsdk.key_executives(apikey=apikey, symbol=symbol)=}")
# print(f"Search: {fmpsdk.search(apikey=apikey, query=query, exchange=exchange, limit=limit)=}")
# print(f"Ticker Search: {fmpsdk.search_ticker(apikey=apikey, query=query, exchange=exchange, limit=limit)=}")
# fmpsdk.financial_statement(apikey=apikey, symbol=symbol)
# print(f"Annual Income Statement: {fmpsdk.income_statement(apikey=apikey, symbol=symbol)=}")
# print(f"Quarterly Income Statement: {fmpsdk.income_statement(apikey=apikey, symbol=symbol, period=quarter)=}")
# fmpsdk.income_statement(apikey=apikey, symbol=symbol, download=download)
# print(f"Annual Balance Sheet Statement: {fmpsdk.balance_sheet_statement(apikey=apikey, symbol=symbol)=}")
# print(f"Quarterly Balance Sheet Statement: {fmpsdk.balance_sheet_statement(apikey=apikey, symbol=symbol, period=period)=}")
# fmpsdk.balance_sheet_statement(apikey=apikey, symbol=symbol, download=download)
# print(f"Annual Cash Flow Statement: {fmpsdk.cash_flow_statement(apikey=apikey, symbol=symbol, )=}")
# print(f"Quarterly Cash Flow Statement: {fmpsdk.cash_flow_statement(apikey=apikey, symbol=symbol, period=period)=}")
# fmpsdk.cash_flow_statement(apikey=apikey, symbol=symbol, download=download)
# print(f"Financial Statement Symbols List: {fmpsdk.financial_statement_symbol_lists(apikey=apikey)=}")
# print(f"Income Statement Growth: {fmpsdk.income_statement_growth(apikey=apikey, symbol=symbol, limit=limit)=}")
# print(f"Balance Sheet Statement Growth: {fmpsdk.balance_sheet_statement_growth(apikey=apikey, symbol=symbol, limit=limit)=}")
# print(f"Cash Flow Statement Growth: {fmpsdk.cash_flow_statement_growth(apikey=apikey, symbol=symbol, limit=limit)=}")
# print(f"Annual Income Statement as Reported : {fmpsdk.income_statement_as_reported(apikey=apikey, symbol=symbol)=}")
# print(f"Quarterly Income Statement as Reported: {fmpsdk.income_statement_as_reported(apikey=apikey, symbol=symbol, period=period)=}")
# fmpsdk.income_statement_as_reported(apikey=apikey, symbol=symbol, download=download)
# print(f"Annual Balance Sheet Statement as Reported : {fmpsdk.balance_sheet_statement_as_reported(apikey=apikey, symbol=symbol)=}")
# print(f"Quarterly Balance Sheet Statement as Reported: {fmpsdk.balance_sheet_statement_as_reported(apikey=apikey, symbol=symbol, period=period)=}")
# fmpsdk.balance_sheet_statement_as_reported(apikey=apikey, symbol=symbol, download=download)
# print(f"Annual Cash Flow Statement as Reported : {fmpsdk.cash_flow_statement_as_reported(apikey=apikey, symbol=symbol)=}")
# print(f"Quarterly Cash Flow Statement as Reported: {fmpsdk.cash_flow_statement_as_reported(apikey=apikey, symbol=symbol, period=period)=}")
# fmpsdk.cash_flow_statement_as_reported(apikey=apikey, symbol=symbol, download=download)
# print(f"Annual Full Financial Statement as Reported : {fmpsdk.financial_statement_full_as_reported(apikey=apikey, symbol=symbol)=}")
# print(f"Quarterly Full Financial Statement as Reported: {fmpsdk.financial_statement_full_as_reported(apikey=apikey, symbol=symbol, period=period)=}")
# print(f"Financial Ratios (TTM): {fmpsdk.financial_ratios_ttm(apikey=apikey, symbol=symbol)=}")
# print(f"Annual Financial Ratios: {fmpsdk.financial_ratios(apikey=apikey, symbol=symbol)=}")
# print(f"Quarterly Financial Ratios: {fmpsdk.financial_ratios(apikey=apikey, symbol=symbol, period=period)=}")
# print(f"Annual Enterprise Values: {fmpsdk.enterprise_values(apikey=apikey, symbol=symbol)=}")
# print(f"Quarterly Enterprise Values: {fmpsdk.enterprise_values(apikey=apikey, symbol=symbol, period=period)=}")
# print(f"Key Metrics (TTM): {fmpsdk.key_metrics_ttm(apikey=apikey, symbol=symbol)=}")
# print(f"Annual Key Metrics: {fmpsdk.key_metrics(apikey=apikey, symbol=symbol)=}")
# print(f"Quarterly Key Metrics: {fmpsdk.key_metrics(apikey=apikey, symbol=symbol, period=period)=}")
# print(f"Annual Financial Growth: {fmpsdk.financial_growth(apikey=apikey, symbol=symbol)=}")
# print(f"Quarterly Financial Growth: {fmpsdk.financial_growth(apikey=apikey, symbol=symbol, period=period)=}")
# print(f"Company Rating: {fmpsdk.rating(apikey=apikey, symbol=symbol)=}")
# print(f"Historical Company Rating: {fmpsdk.historical_rating(apikey=apikey, symbol=symbol, limit=limit)=}")
# print(f"Discounted Cash Flow: {fmpsdk.discounted_cash_flow(apikey=apikey, symbol=symbol)=}")
# print(f"Annual Historical Discounted Cash Flow: {fmpsdk.historical_discounted_cash_flow(apikey=apikey, symbol=symbol)=}")
# print(f"Quarterly Historical Discounted Cash Flow: {fmpsdk.historical_discounted_cash_flow(apikey=apikey, symbol=symbol, period=period)=}")
# print(f"Daily Historical Discounted Cash Flow: {fmpsdk.historical_daily_discounted_cash_flow(apikey=apikey, symbol=symbol)=}")
# print(f"Market Capitalization: {fmpsdk.market_capitalization(apikey=apikey, symbol=symbol)=}")
# print(f"Historical Market Capitalization: {fmpsdk.historical_market_capitalization(apikey=apikey, symbol=symbol, limit=limit)=}")
# print(f"Symbols List: {fmpsdk.symbols_list(apikey=apikey)=}")
# print(f"Stock Screener (Sector Example): {fmpsdk.stock_screener(apikey=apikey, market_cap_more_than=market_cap_more_than, beta_more_than=beta_more_than, volume_more_than=volume_more_than, sector=sector, exchange=exchange, dividend_more_than=dividend_more_than, limit=limit)=}")
# print(f"Stock Screener (Industry Example): {fmpsdk.stock_screener(apikey=apikey, market_cap_more_than=market_cap_more_than, beta_more_than=beta_more_than, volume_more_than=volume_more_than, sector=sector, industry=industry, exchange=exchange, dividend_more_than=dividend_more_than, limit=limit)=}")
# print(f"Stock Screener (Multiple Exchanges Example): {fmpsdk.stock_screener(apikey=apikey, market_cap_more_than=market_cap_more_than, beta_more_than=beta_more_than, volume_more_than=volume_more_than, exchange=exchanges)=}")
# print(f"Delisted Companies: {fmpsdk.delisted_companies(apikey=apikey, limit=limit)=}")
# print(f"Stock News (Single): {fmpsdk.stock_news(apikey=apikey, tickers=symbol)=}")
# print(f"Stock News (Multiple): {fmpsdk.stock_news(apikey=apikey, tickers=symbols)=}")
# print(f"Stock News (Latest): {fmpsdk.stock_news(apikey=apikey, limit=limit)=}")
# print(f"Earnings Surprises: {fmpsdk.earnings_surprises(apikey=apikey, symbol=symbol)=}")
# print(f"SEC Filings: {fmpsdk.sec_filings(apikey=apikey, symbol=symbol, filing_type=filing_type)=}")
# print(f"Press Releases: {fmpsdk.press_releases(apikey=apikey, symbol=symbol)=}")

# Calendars
from_date: str = "2020-04-26"
to_date: str = "2020-07-26"
symbol: str = "CSCO"
limit: int = 3
# print(f"Earning Calendar: {fmpsdk.earning_calendar(apikey=apikey)=}")
# print(f"Earning Calendar: {fmpsdk.earning_calendar(apikey=apikey, from_date=from_date, to_date=to_date)=}")
# print(f"Historical Earning Calendar: {fmpsdk.historical_earning_calendar(apikey=apikey, symbol=symbol, limit=limit)=}")
# print(f"IPO Calendar: {fmpsdk.ipo_calendar(apikey=apikey, from_date=from_date, to_date=to_date)=}")
# print(f"Stock Split Calendar: {fmpsdk.stock_split_calendar(apikey=apikey, from_date=from_date, to_date=to_date)=}")
# print(f"Dividend Calendar: {fmpsdk.dividend_calendar(apikey=apikey, from_date=from_date, to_date=to_date)=}")
# print(f"Economic Calendar: {fmpsdk.economic_calendar(apikey=apikey, from_date=from_date, to_date=to_date)=}")

# Institutional Fund
symbol: str = "SPY"
download: bool = True
name: str = "Berkshire"
cik_id: str = "0000913760"
date: str = "2020-06-30"
# print(f"Institutional Holders: {fmpsdk.institutional_holders(apikey=apikey, symbol=symbol)=}")
# print(f"Mutual Fund Holders: {fmpsdk.mutual_fund_holders(apikey=apikey, symbol=symbol)=}")
# print(f"ETF Holders: {fmpsdk.etf_holders(apikey=apikey, symbol=symbol)=}")
# print(f"ETF Sector Weightings: {fmpsdk.etf_sector_weightings(apikey=apikey, symbol=symbol)=}")
# print(f"ETF Country Weightings: {fmpsdk.etf_country_weightings(apikey=apikey, symbol=symbol)=}")
# print(f"SEC RSS Feeds: {fmpsdk.sec_rss_feeds(apikey=apikey)=}")
# print(f"SEC RSS Feeds: {fmpsdk.sec_rss_feeds(apikey=apikey, download=download)=}")
# print(f"Form 13F List: {fmpsdk.cik_list(apikey=apikey)=}")
# print(f"CIK Search by Company Name: {fmpsdk.cik_search(apikey=apikey, name=name)=}")
# print(f"CIK Search by CIK: {fmpsdk.cik(apikey=apikey, cik_id=cik_id)=}")
# print(f"Form 13F: {fmpsdk.form_13f(apikey=apikey, cik_id=cik_id, date=date)=}")
# print(f"CUSIP: {fmpsdk.cusip(apikey=apikey, cik_id=cik_id)=}")

# Stock Time Series Methods
symbol: str = "MSFT"
exchange: str = "NYSE"
time_delta: str = "5min"
series_type: str = "line"
from_date: str = "2020-04-26"
to_date: str = "2020-07-26"
time_series: int = 5
symbols: typing.List[str] = ["AAPL", "CSCO", "QQQQ"]
mutual_funds: typing.List[str] = ["JBFRX", "BPLEX", "VEVRX"]
# print(f"Quote Realtime: {fmpsdk.quote_short(apikey=apikey, symbol=symbol)=}")
# print(f"Exchange Realtime: {fmpsdk.exchange_realtime(apikey=apikey, exchange=exchange)=}")
# print(f"Historical Stock Prices: {fmpsdk.historical_chart(apikey=apikey, symbol=symbol, time_delta=time_delta)=}")
# print(f"Historical Daily Prices: {fmpsdk.historical_price_full(apikey=apikey, symbol=symbol, series_type=series_type)=}")
# print(f"Historical Daily Prices with Change and Volume: {fmpsdk.historical_price_full(apikey=apikey, symbol=symbol)=}")
# print(f"Historical Daily Prices with Change and Volume (Interval): {fmpsdk.historical_price_full(apikey=apikey, symbol=symbol, from_date=from_date, to_date=to_date)=}")
# print(f"Historical Daily Prices with Change and Volume (Time Series): {fmpsdk.historical_price_full(apikey=apikey, symbol=symbol, time_series=time_series)=}")
# print(f"Historical Daily Prices (Batch Stocks): {fmpsdk.historical_price_full(apikey=apikey, symbol=symbols)=}")
# print(f"Historical Daily Prices (Batch Mutual Funds): {fmpsdk.historical_price_full(apikey=apikey, symbol=mutual_funds)=}")
# print(f"Historical Dividends: {fmpsdk.historical_stock_dividend(apikey=apikey, symbol=symbol)=}")
# print(f"Historical Stock Split: {fmpsdk.historical_stock_split(apikey=apikey, symbol=symbol)=}")

# Technical Indicators
symbol: str = "AAPL"
period: int = 10
statistics_type: str = "sma"
time_delta_daily: str = "daily"
time_delta_15min: str = "15min"
# print(f"Daily Technical Indicators: {fmpsdk.technical_indicators(apikey=apikey, symbol=symbol, period=period, statistics_type=statistics_type, time_delta=time_delta_daily)=}")
# print(f"Intraday Technical Indicators: {fmpsdk.technical_indicators(apikey=apikey, symbol=symbol, period=period, statistics_type=statistics_type, time_delta=time_delta_15min)=}")

# Market Indexes
symbol: str = "^RUITR"
download: bool = True
time_delta_15min: str = "15min"
# print(f"List Market Indexes: {fmpsdk.indexes(apikey=apikey)=}")
# print(f"Index Quote: {fmpsdk.quote(apikey=apikey, symbol=symbol)=}")
# print(f"SP500 Contituent: {fmpsdk.sp500_constituent(apikey=apikey)=}")
# fmpsdk.sp500_constituent(apikey=apikey, download=download)
# print(f"Historical SP500 Contituent: {fmpsdk.historical_sp500_constituent(apikey=apikey)=}")
# print(f"NASDAQ Contituent: {fmpsdk.nasdaq_constituent(apikey=apikey)=}")
# fmpsdk.nasdaq_constituent(apikey=apikey, download=download)
# print(f"Historical NASDAQ Contituent: {fmpsdk.historical_nasdaq_constituent(apikey=apikey)=}")
# print(f"DOWJONES Contituent: {fmpsdk.dowjones_constituent(apikey=apikey)=}")
# fmpsdk.dowjones_constituent(apikey=apikey, download=download)
# print(f"Historical DOWJONES Contituent: {fmpsdk.historical_dowjones_constituent(apikey=apikey)=}")
# print(f"Available Indexes: {fmpsdk.available_indexes(apikey=apikey)=}")
# print(f"Intraday Historical Index Prices: {fmpsdk.historical_chart(apikey=apikey, symbol=symbol, time_delta=time_delta_15min)=}")
# print(f"Historical Market Index: {fmpsdk.historical_price_full(apikey=apikey, symbol=symbol)=}")

# Commodities
symbol: str = "ZGUSD"
symbols: typing.List[str] = ["ZGUSD", "CLUSD", "HGUSD"]
time_delta_15min: str = "15min"
# print(f"Available Commodities': {fmpsdk.available_commodities(apikey=apikey)=}")
# print(f"Commodities': {fmpsdk.commodities_list(apikey=apikey)=}")
# print(f"Commodity Quote': {fmpsdk.quote(apikey=apikey, symbol=symbols)=}")
# print(f"Historical Commodity Prices: {fmpsdk.historical_chart(apikey=apikey, symbol=symbol, time_delta=time_delta_5min)=}")
# print(f"Historical Daily Commodity Prices: {fmpsdk.historical_price_full(apikey=apikey, symbol=symbol)=}")

# ETF
symbol = "PRNT"
symbols = ["PRNT", "DFVS", "VQT"]
time_delta_5min: str = "5min"
# print(f"Available ETFs': {fmpsdk.available_efts(apikey=apikey)=}")
# print(f"ETFs': {fmpsdk.etf_list(apikey=apikey)=}")
# print(f"ETF Quote': {fmpsdk.quote(apikey=apikey, symbol=symbols)=}")
# print(f"Historical ETF Prices: {fmpsdk.historical_chart(apikey=apikey, symbol=symbol, time_delta=time_delta_5min)=}")
# print(f"Historical Daily ETF Prices: {fmpsdk.historical_price_full(apikey=apikey, symbol=symobl)=}")
# print(f"Historical Dividends: {fmpsdk.historical_stock_dividend(apikey=apikey, symbol=symbol)=}")
# print(f"Historical Stock Split: {fmpsdk.historical_stock_split(apikey=apikey, symbol=symbol)=}")

# Mutual Funds
symbol: str = "JMCRX"
symbols: typing.List[str] = ["JMCRX", "JSMTX", "JUESX"]
time_delta_5min: str = "5min"
# print(f"Available Mutual Funds: {fmpsdk.available_mutual_funds(apikey=apikey)=}")
# print(f"Mutual Funds: {fmpsdk.mutual_fund_list(apikey=apikey)=}")
# print(f"Mutual Fund Quote: {fmpsdk.quote(apikey=apikey, symbol=symbols)=}")
# print(f"Historical Mutual Fund Prices: {fmpsdk.historical_chart(apikey=apikey, symbol=symbol, time_delta=time_delta_5min)=}")
# print(f"Historical Daily Mutual Fund Prices: {fmpsdk.historical_price_full(apikey=apikey, symbol=symbol)=}")
# print(f"Historical Dividends: {fmpsdk.historical_stock_dividend(apikey=apikey, symbol=symbol)=}")
# print(f"Historical Stock Split: {fmpsdk.historical_stock_split(apikey=apikey, symbol=symbol)=}")

# EuroNext
symbol: str = "KIN.BR"
symbols: typing.List[str] = ["EDF.PA", "KIN.BR", "SCB.LS"]
time_delta_5min: str = "5min"
# print(f"Available EuroNext: {fmpsdk.available_euronext(apikey=apikey)=}")
# print(f"EuroNext: {fmpsdk.euronext_list(apikey=apikey)=}")
# print(f"EuroNext Quote: {fmpsdk.quote(apikey=apikey, symbol=symbols)=}")
# print(f"Historical EuroNext Prices: {fmpsdk.historical_chart(apikey=apikey, symbol=symbol, time_delta=time_delta_5min)=}")
# print(f"Historical Daily EuroNext Prices: {fmpsdk.historical_price_full(apikey=apikey, symbol=symbol)=}")
# print(f"Historical Dividends: {fmpsdk.historical_stock_dividend(apikey=apikey, symbol=symbol)=}")
# print(f"Historical Stock Split: {fmpsdk.historical_stock_split(apikey=apikey, symbol=symbol)=}")

# TSX
symbol: str = "FNV.TO"
symbols: typing.List[str] = ["FNV.TO", "XAW.TO", "DR.TO"]
time_delta_5min: str = "5min"
# print(f"Available TSX: {fmpsdk.available_tsx(apikey=apikey)=}")
# print(f"TSX: {fmpsdk.tsx_list(apikey=apikey)=}")
# print(f"TSX Quote: {fmpsdk.quote(apikey=apikey, symbol=symbols)=}")
# print(f"Historical TSX Prices: {fmpsdk.historical_chart(apikey=apikey, symbol=symbol, time_delta=time_delta_5min)=}")
# print(f"Historical Daily TSX Prices: {fmpsdk.historical_price_full(apikey=apikey, symbol=symbol)=}")
# print(f"Historical Dividends: {fmpsdk.historical_stock_dividend(apikey=apikey, symbol=symbol)=}")
# print(f"Historical Stock Split: {fmpsdk.historical_stock_split(apikey=apikey, symbol=symbol)=}")

# Stock Market
limit: int = 3
# print(f"Active Stock in Market: {fmpsdk.actives(apikey=apikey)=}")
# print(f"Stock in Market Gainers: {fmpsdk.gainers(apikey=apikey)=}")
# print(f"Active Stock in Market Losers: {fmpsdk.losers(apikey=apikey)=}")
# print(f"Market Hours: {fmpsdk.market_hours(apikey=apikey)=}")
# print(f"Sector's Performance: {fmpsdk.sectors_performance(apikey=apikey, limit=limit)=}")


# Cryptocurrencies
symbol: str = "BTCUSD"
time_delta_5min: str = "5min"
# print(f"Cryptocurrencies: {fmpsdk.cryptocurrencies_list(apikey=apikey)=}")
# print(f"Cryptocurrencies Quote: {fmpsdk.quote(apikey=apikey, symbol=symbol)=}")
# print(f"Available Cryptocurrencies: {fmpsdk.available_cryptocurrencies(apikey=apikey)=}")
# print(f"Historical Cryptocurrencies Prices: {fmpsdk.historical_chart(apikey=apikey, symbol=symbol, time_delta=time_delta_5min)=}")
# print(f"Historical Daily Cryptocurrencies Prices: {fmpsdk.historical_price_full(apikey=apikey, symbol=symbol)=}")

# FOREX (FX)
symbol: str = "JPYUSD"
time_delta_5min: str = "5min"
# print(f"Currency Exchange Rates: {fmpsdk.forex(apikey=apikey)}")
# print(f"Forex: {fmpsdk.forex_list(apikey=apikey)=}")
# print(f"Forex Quote: {fmpsdk.quote(apikey=apikey, symbol=symbol)=}")
# print(f"Available Forex Currency Pairs: {fmpsdk.available_cryptocurrencies(apikey=apikey)=}")
# print(f"Historical Forex Prices: {fmpsdk.historical_chart(apikey=apikey, symbol=symbol, time_delta=time_delta_5min)=}")
# print(f"Historical Daily Forex Prices: {fmpsdk.historical_price_full(apikey=apikey, symbol=symbol)=}")
