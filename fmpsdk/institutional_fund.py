from .settings import DEFAULT_LIMIT, SEC_RSS_FEEDS_FILENAME
from .url_methods import return_response, make_url
from urllib.request import urlopen
import typing
import shutil
import logging


def institutional_holders(apikey: str, symbol: str) -> typing.List[typing.Dict]:
    """
    Query FMP API for Institutional Holders.

    Example:
    https://financialmodelingprep.com/api/v3/institutional-holder/AAPL?apikey=demo
    [ {
        "holder" : "The Vanguard Group, Inc.",
        "shares" : 336729000,
        "dateReported" : "2020-03-31",
        "change" : 7405180
      }, {
        "holder" : "Berkshire Hathaway Inc.",
        "shares" : 245156000,
        "dateReported" : "2020-03-31",
        "change" : 0
      }, {
        "holder" : "BlackRock Institutional Trust Company, N.A.",
        "shares" : 187355000,
        "dateReported" : "2020-03-31",
        "change" : -2500560
      }, {
        "holder" : "State Street Global Advisors (US)",
        "shares" : 180559000,
        "dateReported" : "2020-03-31",
        "change" : -2295830
      }, {
        "holder" : "Fidelity Management & Research Company",
        "shares" : 89764900,
        "dateReported" : "2020-03-31",
        "change" : -2990180
      }, {
        "holder" : "Geode Capital Management, L.L.C.",
        "shares" : 64178600,
        "dateReported" : "2020-03-31",
        "change" : 1696500
      }, ...
    ]
   """
    path = f"institutional-holder/{symbol}"
    query_vars = {"apikey": apikey}
    return return_response(path=path, query_vars=query_vars)


def mutual_fund_holders(apikey: str, symbol: str) -> typing.List[typing.Dict]:
    """
    Query FMP API for Mutual Fund Holders.

    Example:
    https://financialmodelingprep.com/api/v3/mutual-fund-holder/AAPL?apikey=demo
    [ {
        "holder" : "Vanguard Total Stock Market Index Fund",
        "shares" : 115914000,
        "dateReported" : "2020-04-30",
        "change" : -1331370,
        "weightPercent" : 4.65
      }, {
        "holder" : "Vanguard 500 Index Fund",
        "shares" : 85467200,
        "dateReported" : "2020-04-30",
        "change" : -487891,
        "weightPercent" : 5.09
      }, {
        "holder" : "Statens Pensjonsfond Utland",
        "shares" : 45329200,
        "dateReported" : "2019-12-31",
        "change" : -603878,
        "weightPercent" : 0
      }, {
        "holder" : "SPDR S&P 500 ETF",
        "shares" : 44553400,
        "dateReported" : "2020-05-31",
        "change" : -391609,
        "weightPercent" : 5.24
      }, {
        "holder" : "Invesco QQQ Trust",
        "shares" : 38712400,
        "dateReported" : "2020-05-31",
        "change" : 1171600,
        "weightPercent" : 11.23
      }, ...
    ]
   """
    path = f"mutual-fund-holder/{symbol}"
    query_vars = {"apikey": apikey}
    return return_response(path=path, query_vars=query_vars)


def etf_holders(apikey: str, symbol: str) -> typing.List[typing.Dict]:
    """
    Query FMP API for ETF Holders.

    Example:
    https://financialmodelingprep.com/api/v3/etf-holder/SPY?apikey=demo
    [ {
        "asset" : "AAPL",
        "sharesNumber" : 43766308,
        "weightPercentage" : 5.92
      }, {
        "asset" : "MSFT",
        "sharesNumber" : 81420240,
        "weightPercentage" : 5.82
      }, {
        "asset" : "AMZN",
        "sharesNumber" : 4501968,
        "weightPercentage" : 4.73
      }, {
        "asset" : "FB",
        "sharesNumber" : 25837586,
        "weightPercentage" : 2.18
      }, {
        "asset" : "GOOGL",
        "sharesNumber" : 3224102,
        "weightPercentage" : 1.71
      }, ...
    ]
   """
    path = f"etf-holder/{symbol}"
    query_vars = {"apikey": apikey}
    return return_response(path=path, query_vars=query_vars)


def etf_sector_weightings(apikey: str, symbol: str) -> typing.List[typing.Dict]:
    """
    Query FMP API for ETF Sector Weightings.

    Example:
    https://financialmodelingprep.com/api/v3/etf-sector-weightings/SPY?apikey=demo
    [ {
        "sector" : "Healthcare",
        "weightPercentage" : "14.79%"
      }, {
        "sector" : "Telecommunications Services",
        "weightPercentage" : "1.98%"
      }, {
        "sector" : "Energy",
        "weightPercentage" : "2.96%"
      }, {
        "sector" : "Basic Materials",
        "weightPercentage" : "2.43%"
      }, ...
    ]
   """
    path = f"etf-sector-weightings/{symbol}"
    query_vars = {"apikey": apikey}
    return return_response(path=path, query_vars=query_vars)


def etf_country_weightings(apikey: str, symbol: str) -> typing.List[typing.Dict]:
    """
    Query FMP API for ETF Country Weightings.

    Example:
    https://financialmodelingprep.com/api/v3/etf-country-weightings/SPY?apikey=demo
    [ {
      "country" : "United States",
      "weightPercentage" : "100.00%"
    } ]
   """
    path = f"etf-country-weightings/{symbol}"
    query_vars = {"apikey": apikey}
    return return_response(path=path, query_vars=query_vars)


def sec_rss_feeds(
        apikey: str,
        limit: int = DEFAULT_LIMIT,
        download: bool = False,
        filename: str = SEC_RSS_FEEDS_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP API for SEC RSS Feeds.

    Example:
    https://financialmodelingprep.com/api/v3/rss_feeds?apikey=demo
    [
        {
            "title" : "6-K - ONCOLYTICS BIOTECH INC (0001129928) (Filer)",
            "date" : "2020-05-29 16:48:22",
            "link" : "https://www.sec.gov/Archives/edgar/data/1129928/000112992820000034/0001129928-20-000034-index.htm",
            "cik" : "0001129928",
            "form_type" : "6-K",
            "ticker" : "ONCY"
        }, {
            "title" : "10-Q - BERKSHIRE HILLS BANCORP INC (0001108134) (Filer)",
            "date" : "2020-05-29 16:45:47",
            "link" : "https://www.sec.gov/Archives/edgar/data/1108134/000110813420000012/0001108134-20-000012-index.htm",
            "cik" : "0001108134",
            "form_type" : "10-Q",
            "ticker" : "BHLB"
        }, {
            "title" : "10-Q - URBAN ONE, INC. (0001041657) (Filer)",
            "date" : "2020-05-29 16:45:24",
            "link" : "https://www.sec.gov/Archives/edgar/data/1041657/000110465920067812/0001104659-20-067812-index.htm",
            "cik" : "0001041657",
            "form_type" : "10-Q",
            "ticker" : "UONEK"
        }, {
            "title" : "10-K - REMARK HOLDINGS, INC. (0001368365) (Filer)",
            "date" : "2020-05-29 16:42:40",
            "link" : "https://www.sec.gov/Archives/edgar/data/1368365/000136836520000028/0001368365-20-000028-index.htm",
            "cik" : "0001368365",
            "form_type" : "10-K",
            "ticker" : "MARK"
        }, {
            "title" : "10-K - SONO TEK CORP (0000806172) (Filer)",
            "date" : "2020-05-29 16:41:11",
            "link" : "https://www.sec.gov/Archives/edgar/data/806172/000117152020000252/0001171520-20-000252-index.htm",
            "cik" : "0000806172",
            "form_type" : "10-K",
            "ticker" : "SOTK"
      }
    ]
   """
    path = f"rss_feed"
    query_vars = {"apikey": apikey}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        url = make_url(path=path, query_vars=query_vars)
        with urlopen(url) as response, open(filename, "wb") as out_file:
            logging.info(f"Saving SEC RSS Feeds as {filename}.")
            shutil.copyfileobj(response, out_file)
    else:
        query_vars["limit"] = limit
        return return_response(path=path, query_vars=query_vars)


def form_13f_list(apikey: str) -> typing.List[typing.Dict]:
    """
    Complete list of all institutional investment managers by cik

    Example:
    https://financialmodelingprep.com/api/v3/cik_list?apikey=demo
    [
        {
            "cik" : "0001694461",
            "name" : "HARVEST GROUP WEALTH MANAGEMENT, LLC "
        },
        {
            "cik" : "0001583751",
            "name" : "TCI Wealth Advisors, Inc. "
        },
        {
            "cik" : "0001356202",
            "name" : "Beech Hill Advisors, Inc. "
        },
        {
            "cik" : "0001799859",
            "name" : "Birch Capital Management, LLC "
        },
        {
            "cik" : "0001767045",
            "name" : "Lindbrook Capital, LLC "
        },
        {
            "cik" : "0000913760",
            "name" : "INTL FCSTONE INC. "
        },
        {
            "cik" : "0001424322",
            "name" : "Cubic Asset Management, LLC "
        },
    ]
   """
    path = f"cik_list"
    query_vars = {"apikey": apikey}
    return return_response(path=path, query_vars=query_vars)


def cik_search(apikey: str, name: str) -> typing.List[typing.Dict]:
    """
    FORM 13F cik search by name
   """
    path = f"cik-search/{name}"
    query_vars = {"apikey": apikey}
    return return_response(path=path, query_vars=query_vars)


def cik(apikey: str, cik_id: str) -> typing.List[typing.Dict]:
    """
    FORM 13F get company name by cik
   """
    path = f"cik/{cik_id}"
    query_vars = {"apikey": apikey}
    return return_response(path=path, query_vars=query_vars)


def form_13f(apikey: str, cik_id: str, date: str = None) -> typing.List[typing.Dict]:
    """
    FORM 13F statements provides position-level report of all institutional investment managers with more than $100m
    in assets under management.
   """
    path = f"form-thirteen/{cik_id}"
    query_vars = {"apikey": apikey}
    if date:
        query_vars["date"] = date
    return return_response(path=path, query_vars=query_vars)


def cusip(apikey: str, cik_id: str) -> typing.List[typing.Dict]:
    """
    FORM 13F get company name by cik
   """
    path = f"cusip/{cik_id}"
    query_vars = {"apikey": apikey}
    return return_response(path=path, query_vars=query_vars)
