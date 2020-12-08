#!/usr/bin/env python3

import os
from dotenv import load_dotenv
import fmpsdk

# Actual API key is stored in a .env file.  Not good to store API key directly in script.
load_dotenv()
apikey = os.environ.get('apikey')
symbol = 'AAPL'

# Access the FMPSDK methods.  Most return a List of Dictionaries.
"""
print(f"Company Profile: {fmpsdk.company_profile(apikey=apikey, symbol=symbol)}")
print(f"Company Quote: {fmpsdk.quote(apikey=apikey, symbol=symbol)}")
print(f"Key Executives: {fmpsdk.key_executives(apikey=apikey, symbol=symbol)}")
print(f"Search: {fmpsdk.search(apikey=apikey, query='AA', exchange='NYSE', limit=10)}")
print(f"Ticker Search: {fmpsdk.search_ticker(apikey=apikey, query='AA', exchange='NYSE', limit=5)}")
fmpsdk.financial_statement(apikey=apikey, symbol=symbol)
print(f"Annual Income Statement: {fmpsdk.income_statement(apikey=apikey, symbol=symbol)}")
print(f"Quarterly Income Statement: {fmpsdk.income_statement(apikey=apikey, symbol=symbol, period='quarter')}")
fmpsdk.income_statement(apikey=apikey, symbol=symbol, download=True)
print(f"Annual Balance Sheet Statement: {fmpsdk.balance_sheet_statement(apikey=apikey, symbol=symbol)}")
print(f"Quarterly Balance Sheet Statement: {fmpsdk.balance_sheet_statement(apikey=apikey, symbol=symbol, period='quarter')}")
fmpsdk.balance_sheet_statement(apikey=apikey, symbol=symbol, download=True)
"""


"""
print(f"Annual Cash Flow Statement: {fmpsdk.cash_flow_statement()}")
print(f"Quarterly Cash Flow Statement: {fmpsdk.cash_flow_statement(period='quarter')}")
fmpsdk.cash_flow_statement(download=True)
print(f"Annual Income Statement: {fmpsdk.income_statement()}")
print(f"Quarterly Income Statement: {fmpsdk.income_statement(period='quarter')}")
fmpsdk.income_statement(download=True)
print(f"Annual Balance Sheet Statement: {fmpsdk.balance_sheet_statement()}")
print(f"Quarterly Balance Sheet Statement: {fmpsdk.balance_sheet_statement(period='quarter')}")
fmpsdk.balance_sheet_statement(download=True)
print(f"Financial Ratios (TTM): {fmpsdk.financial_ratios_ttm()}")
print(f"Annual Financial Ratios: {fmpsdk.financial_ratios(period='annual')}")
print("Quarterly Financial Ratios:")
for item in fmpsdk.financial_ratios(period='quarter'):
    pp.pprint(item)
print(f"Historical Dividends: {fmpsdk.historical_stock_dividend()}")
print(f"Historical Stock Split: {fmpsdk.historical_stock_split()}")
print(f"Financial Statements List: {fmpsdk.financial_statement_lists()}")
print(f"Income Statement Growth: {fmpsdk.income_statement_growth(limit=10)}")
print(f"Balance Sheet Statement Growth: {fmpsdk.balance_sheet_statement_growth(limit=10)}")
print(f"Cash Flow Statement Growth: {fmpsdk.cash_flow_statement_growth(limit=10)}")
print(f"Annual Income Statement as Reported : {fmpsdk.income_statement_as_reported()}")
print(f"Quarterly Income Statement as Reported: {fmpsdk.income_statement_as_reported(period='quarter')}")
fmpsdk.income_statement_as_reported(download=True)
print(f"Annual Balance Sheet Statement as Reported : {fmpsdk.balance_sheet_statement_as_reported()}")
print(f"Quarterly Balance Sheet Statement as Reported: "
      f"{fmpsdk.balance_sheet_statement_as_reported(period='quarter')}")
fmpsdk.balance_sheet_statement_as_reported(download=True)
print(f"Annual Cash Flow Statement as Reported : {fmpsdk.cash_flow_statement_as_reported()}")
print(f"Quarterly Cash Flow Statement as Reported: {fmpsdk.cash_flow_statement_as_reported(period='quarter')}")
fmpsdk.cash_flow_statement_as_reported(download=True)
print(f"Annual Full Financial Statement as Reported : {fmpsdk.financial_statement_full_as_reported()}")
print(f"Quarterly Full Financial Statement as Reported:"
      f" {fmpsdk.financial_statement_full_as_reported(period='quarter')}")
print(f"Annual Enterprise Values: {fmpsdk.enterprise_values()}")
print(f"Quarterly Enterprise Values: {fmpsdk.enterprise_values(period='quarter')}")
"""
