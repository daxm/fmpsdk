# FMP SDK

[![PyPI version](https://img.shields.io/pypi/v/fmpsdk)](https://pypi.org/project/fmpsdk/)
[![Python versions](https://img.shields.io/pypi/pyversions/fmpsdk)](https://pypi.org/project/fmpsdk/)
[![License: BSD-3-Clause](https://img.shields.io/badge/license-BSD--3--Clause-blue)](LICENSE.md)

The idea behind this project is to provide a 'one-stop-shop' to the API endpoints provided by
[Financial Modeling Prep](http://financialmodelingprep.com) (FMP).

A personal note to you: my apologies for letting this package get so out of date. FMP kept
reshuffling its API, then I had a personal issue delay me further. Things are back on track now.
Because of that gap, roughly half of this package's old methods had gone defunct against FMP's
current API, so rather than patch around that I rebuilt it from scratch against FMP's `stable/`
API. If you're on `20250102.0` or earlier you're on the old, pre-rewrite methods; anything newer
uses the schema described below.

## What's covered

29 data groups, ~240 methods total, each reachable both as `client.<method>(...)` and grouped
under a matching namespace, e.g. `client.statements.income_statement(...)`:

- **Company & fundamentals** — profile, executives, M&A, DCF valuation, financial statements/
  ratios/growth (income, balance sheet, cash flow — as-reported, TTM, and growth variants)
- **Market data** — real-time & aftermarket quotes, historical price charts, technical indicators
- **Reference & screening** — symbol/CIK/CUSIP/ISIN search, the company screener, sector/
  industry/exchange directories
- **Calendars & events** — earnings, dividends, splits, IPOs, the economic calendar
- **Ownership & compliance** — insider trades, Form 13F institutional ownership, SEC filings, ESG
  disclosures
- **Alternative markets** — crypto, forex, commodities, indexes, ETFs & mutual funds
- **Sentiment & analysis** — analyst grades/price targets, TipRanks ratings, congressional
  trading, market movers
- **Bulk downloads** — whole-universe data dumps, one call instead of one per symbol

Every method's own docstring says whether it works on FMP's free tier or requires an
Ultimate-tier plan — see [Pricing tiers](#pricing-tiers) below.

## How to Use
1. Requires Python 3.9+. Install the package: `pip install fmpsdk python-dotenv` (`python-dotenv`
   is optional — it's just how the example below loads your API key from a `.env` file).
1. Create a `.env` file and put your API key in it. Inside `.env`: `FMP_API_KEY='blah'`
1. Build a `Client` and call methods on it, grouped by data category — e.g.
   `client.company.profile(symbol="AAPL")`, `client.statements.income_statement(symbol="AAPL")`.
1. The return from a method call is almost always a list of dictionaries. It is up to you to
   parse it.

## Example code
```python
#!/usr/bin/env python3

from dotenv import load_dotenv

import fmpsdk

# Actual API key is stored in a .env file. Not good to store API key directly in script.
load_dotenv()
client = fmpsdk.Client()  # reads FMP_API_KEY from the environment

# Company Valuation Methods
symbol = "AAPL"
print(f"Company Profile: {client.company.profile(symbol=symbol)}")

# Every non-2xx FMP response raises a typed exception instead of returning
# None or an error-shaped dict, so a plan-gated or bad-key call is obvious:
try:
    client.statements.income_statement_ttm(symbol=symbol)
except fmpsdk.FMPPlanLimitError:
    print("This endpoint needs an FMP Ultimate-tier plan.")
except fmpsdk.FMPAuthenticationError:
    print("Check your FMP_API_KEY.")
```

One naming quirk worth knowing up front: `client.quote` is the namespace for the whole quote
group (`client.quote.aftermarket_quote(...)`, `client.quote.batch_quote(...)`, etc.), so it
shadows the top-level `quote()` method of the same name — call that one as
`client.quote.quote(symbol="AAPL")`.

## Pricing tiers
FMP gates a lot of endpoints behind its paid Ultimate-tier plan; a gated call raises
`fmpsdk.FMPPlanLimitError` rather than returning data. There's no single tier table to keep in
sync here — instead, every group module's docstring (e.g. `fmpsdk/endpoints/search.py`) and every
method's own docstring says plainly whether it's free-tier or Ultimate-tier, right next to the
code that calls it. Check those, or just try the call and catch `FMPPlanLimitError`.

## License
BSD 3-Clause — see [LICENSE.md](LICENSE.md).

## Attribution
Special thanks to the following people who have pitched in on this project!  Open source works thanks to people who 
jump in and help!  These are this project's stars.  Thank you.
  - [Ken Caruso](https://github.com/ipl31)
  - [iforgotmypass](https://github.com/iforgotmypass)
  - [Ivelin Ivanov](https://github.com/ivelin)
  - Claude Code
