# FMP SDK
The idea behind this project is to provide a 'one-stop-shop' to the API endpoints provided by 
[Financial Model Prep](http://financialmodelingprep.com) website.

Each API endpoint is a method within the FMPSDK object.

Example code:
```python
#!/usr/bin/env python3

import os
from dotenv import load_dotenv
import fmpsdk

# Actual API key is stored in a .env file.  Not good to store API key directly in script.
load_dotenv()
apikey = os.environ.get('apikey')
symbol = 'AAPL'

# Access the FMPSDK methods.  Most return a List of Dictionaries.
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
print(f"Annual Cash Flow Statement: {fmpsdk.cash_flow_statement(apikey=apikey, symbol=symbol, )}")
print(f"Quarterly Cash Flow Statement: {fmpsdk.cash_flow_statement(apikey=apikey, symbol=symbol, period='quarter')}")
fmpsdk.cash_flow_statement(apikey=apikey, symbol=symbol, download=True)
print(f"Financial Statement Symbols List: {fmpsdk.financial_statement_symbol_lists(apikey=apikey)}")
print(f"Income Statement Growth: {fmpsdk.income_statement_growth(apikey=apikey, symbol=symbol, limit=10)}")
print(f"Balance Sheet Statement Growth: {fmpsdk.balance_sheet_statement_growth(apikey=apikey, symbol=symbol, limit=10)}")
print(f"Cash Flow Statement Growth: {fmpsdk.cash_flow_statement_growth(apikey=apikey, symbol=symbol, limit=10)}")
print(f"Annual Income Statement as Reported : {fmpsdk.income_statement_as_reported(apikey=apikey, symbol=symbol)}")
print(f"Quarterly Income Statement as Reported: {fmpsdk.income_statement_as_reported(apikey=apikey, symbol=symbol, period='quarter')}")
fmpsdk.income_statement_as_reported(apikey=apikey, symbol=symbol, download=True)
print(f"Annual Balance Sheet Statement as Reported : {fmpsdk.balance_sheet_statement_as_reported(apikey=apikey, symbol=symbol)}")
print(f"Quarterly Balance Sheet Statement as Reported: {fmpsdk.balance_sheet_statement_as_reported(apikey=apikey, symbol=symbol, period='quarter')}")
fmpsdk.balance_sheet_statement_as_reported(apikey=apikey, symbol=symbol, download=True)
print(f"Annual Cash Flow Statement as Reported : {fmpsdk.cash_flow_statement_as_reported(apikey=apikey, symbol=symbol)}")
print(f"Quarterly Cash Flow Statement as Reported: {fmpsdk.cash_flow_statement_as_reported(apikey=apikey, symbol=symbol, period='quarter')}")
fmpsdk.cash_flow_statement_as_reported(apikey=apikey, symbol=symbol, download=True)
print(f"Annual Full Financial Statement as Reported : {fmpsdk.financial_statement_full_as_reported(apikey=apikey, symbol=symbol)}")
print(f"Quarterly Full Financial Statement as Reported: {fmpsdk.financial_statement_full_as_reported(apikey=apikey, symbol=symbol, period='quarter')}")
print(f"Financial Ratios (TTM): {fmpsdk.financial_ratios_ttm(apikey=apikey, symbol=symbol)}")
print(f"Annual Financial Ratios: {fmpsdk.financial_ratios(apikey=apikey, symbol=symbol, period='annual')}")
print(f"Quarterly Financial Ratios: {fmpsdk.financial_ratios(apikey=apikey, symbol=symbol, period='quarter')}")
print(f"Annual Enterprise Values: {fmpsdk.enterprise_values(apikey=apikey, symbol=symbol)}")
print(f"Quarterly Enterprise Values: {fmpsdk.enterprise_values(apikey=apikey, symbol=symbol, period='quarter')}")

print(f"Historical Dividends: {fmpsdk.historical_stock_dividend(apikey=apikey, symbol=symbol)}")
print(f"Historical Stock Split: {fmpsdk.historical_stock_split(apikey=apikey, symbol=symbol)}")
```

Most of these methods will return a dictionary.  It is up to you to parse out the information you are looking for.
