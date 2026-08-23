# FMP SDK
The idea behind this project is to provide a 'one-stop-shop' to the API endpoints provided by 
[Financial Model Prep](http://financialmodelingprep.com) website.

First, a personal note to you.  My apologies for letting this package get so out of date.  I was waiting for FMP to finish
making changes to their API (things kept getting shifted around) and then I have a personal issue crop up and delay
me working on this project for even longer.  Things are back on track and I should be able to respond to PRs and Issues
in a far more timely manner going forward.

Second, because of the long missing time since I updated this project the FMP API has changed so much that something like
50% of the Python methods in this project were defunct.  Instead of trying to support the old Python methods are have 
been using and make some sort of 'alias' to the new FMP API ways I decide to start over and build up from scratch. Alas,
the versioning numbering I choose for this project (basically the date with a dot patch feature) doesn't provide me a
clean version bump mechanism.  So, the 20250102.0 version is the last version using the old methods and any new version
with a number larger than that will be using the new method schema.

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
print(f"Company Profile: {fmpsdk.company_profile(apikey=apikey, symbol=symbol)}")
```

## Attribution
Special thanks to the following people who have pitched in on this project!  Open source works thanks to people who 
jump in and help!  These are this project's stars.  Thank you.
  - [Ken Caruso](https://github.com/ipl31)
  - [iforgotmypass](https://github.com/iforgotmypass)
  - [Ivelin Ivanov](https://github.com/ivelin)
  - Claude Code
