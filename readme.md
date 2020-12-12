# FMP SDK
The idea behind this project is to provide a 'one-stop-shop' to the API endpoints provided by 
[Financial Model Prep](http://financialmodelingprep.com) website.

## How to Use
1. Install the package: `pip install fmpsdk`
1. Create a .env file and put your apikey in it.  Inside .env: `apikey='blah'`
1. Use `fmpsdk.<some function>(apikey=apikey, <possibly more variables>)` to query the API for that "some function".
1. The return from that function call is almost always a List of Dictionaries.  It is up to you to parse it.

## Example code
Here is a "quick start" script example.  A larger, more detailed example is in the file `fmpsdk-example.py`.
```python
#!/usr/bin/env python3

import os
from dotenv import load_dotenv
import typing
import fmpsdk

# Actual API key is stored in a .env file.  Not good to store API key directly in script.
load_dotenv()
apikey = os.environ.get("apikey")

# Company Valuation Methods
symbol: str = "AAPL"
print(f"Company Profile: {fmpsdk.company_profile(apikey=apikey, symbol=symbol)=}")
```
