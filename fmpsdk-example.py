#!/usr/bin/env python3

import os
from dotenv import load_dotenv
from fmpsdk import FMPSDK
import pprint

# Actual API key is stored in a .env file.  Not good to store API key directly in script.
load_dotenv()
apikey = os.environ.get('apikey')
symbol = 'AAPL'

pp = pprint.PrettyPrinter(indent=2)

# Create an FMPSDK object
company = FMPSDK(apikey=apikey, symbol=symbol)

# Access the FMPSDK methods.  Most return a List of Dictionaries.
"""
print(f"Company Profile: {company.company_profile()}")
print(f"Company Quote: {company.quote()}")
print(f"Key Executives: {company.key_executives()}")
print(f"Search: {company.search(query='AA', exchange='NYSE', limit=10)}")
print(f"Ticker Search: {company.search_ticker(query='AA', exchange='NYSE', limit=5)}")
company.financial_statement()
print(f"Annual Cash Flow Statement: {company.cash_flow_statement()}")
print(f"Quarterly Cash Flow Statement: {company.cash_flow_statement(period='quarter')}")
company.cash_flow_statement(download=True)
print(f"Annual Income Statement: {company.income_statement()}")
print(f"Quarterly Income Statement: {company.income_statement(period='quarter')}")
company.income_statement(download=True)
print(f"Annual Balance Sheet Statement: {company.balance_sheet_statement()}")
print(f"Quarterly Balance Sheet Statement: {company.balance_sheet_statement(period='quarter')}")
company.balance_sheet_statement(download=True)
print(f"Financial Ratios (TTM): {company.financial_ratios_ttm()}")
print(f"Annual Financial Ratios: {company.financial_ratios(period='annual')}")
print("Quarterly Financial Ratios:")
for item in company.financial_ratios(period='quarter'):
    pp.pprint(item)
print(f"Historical Dividends: {company.historical_stock_dividend()}")
print(f"Historical Stock Split: {company.historical_stock_split()}")
print(f"Financial Statements List: {company.financial_statement_lists()}")
print(f"Income Statement Growth: {company.income_statement_growth(limit=10)}")
print(f"Balance Sheet Statement Growth: {company.balance_sheet_statement_growth(limit=10)}")
print(f"Cash Flow Statement Growth: {company.cash_flow_statement_growth(limit=10)}")
print(f"Annual Income Statement as Reported : {company.income_statement_as_reported()}")
print(f"Quarterly Income Statement as Reported: {company.income_statement_as_reported(period='quarter')}")
company.income_statement_as_reported(download=True)
print(f"Annual Balance Sheet Statement as Reported : {company.balance_sheet_statement_as_reported()}")
print(f"Quarterly Balance Sheet Statement as Reported: "
      f"{company.balance_sheet_statement_as_reported(period='quarter')}")
company.balance_sheet_statement_as_reported(download=True)
print(f"Annual Cash Flow Statement as Reported : {company.cash_flow_statement_as_reported()}")
print(f"Quarterly Cash Flow Statement as Reported: {company.cash_flow_statement_as_reported(period='quarter')}")
company.cash_flow_statement_as_reported(download=True)
print(f"Annual Full Financial Statement as Reported : {company.financial_statement_full_as_reported()}")
print(f"Quarterly Full Financial Statement as Reported:"
      f" {company.financial_statement_full_as_reported(period='quarter')}")
"""
print(f"Annual Enterprise Values: {company.enterprise_values()}")
print(f"Quarterly Enterprise Values: {company.enterprise_values(period='quarter')}")
