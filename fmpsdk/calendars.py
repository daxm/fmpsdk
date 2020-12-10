from .settings import DEFAULT_LIMIT
from .url_methods import return_json
import typing


def earning_calendar(apikey: str, from_date: str = None, to_date: str = None) -> typing.List[typing.Dict]:
    """
    Query FMP API for Earning Calendar

    Example:
    https://financialmodelingprep.com/api/v3/earning_calendar?apikey=demo
    [ {
        "symbol" : "PANW",
        "date" : "2020-05-22 00:00:00.000",
        "epsEstimated" : 0.930000000000000049
        },
      {
        "symbol" : "PRSP",
        "date" : "2020-05-22 00:00:00.000",
        "epsEstimated" : 0.510000000000000009
        },
      {
        "symbol" : "DECK",
        "date" : "2020-05-22 00:00:00.000",
        "epsEstimated" : 0.209999999999999992
      },
      {
        "symbol" : "BHR",
        "date" : "2020-05-22 00:00:00.000",
        "epsEstimated" : -0.599999999999999978
      },
      {
        "symbol" : "CTHR",
        "date" : "2020-05-22 00:00:00.000",
        "epsEstimated" : -0.0200000000000000004
      } ]
    """
    path = f"earning_calendar"
    query_vars = {
        "apikey": apikey,
    }
    if from_date:
        query_vars['from'] = from_date
    if to_date:
        query_vars['to'] = to_date
    return return_json(path=path, query_vars=query_vars)


def historical_earning_calendar(apikey: str, symbol: str, limit: int = DEFAULT_LIMIT) -> typing.List[typing.Dict]:
    """
    Query FMP API for Historical Earning Calendar

    Example:
    https://financialmodelingprep.com/api/v3/earning_calendar?apikey=demo
    [ {
        "symbol" : "PANW",
        "date" : "2020-05-22 00:00:00.000",
        "epsEstimated" : 0.930000000000000049
        },
      {
        "symbol" : "PRSP",
        "date" : "2020-05-22 00:00:00.000",
        "epsEstimated" : 0.510000000000000009
        },
      {
        "symbol" : "DECK",
        "date" : "2020-05-22 00:00:00.000",
        "epsEstimated" : 0.209999999999999992
      },
      {
        "symbol" : "BHR",
        "date" : "2020-05-22 00:00:00.000",
        "epsEstimated" : -0.599999999999999978
      },
      {
        "symbol" : "CTHR",
        "date" : "2020-05-22 00:00:00.000",
        "epsEstimated" : -0.0200000000000000004
      } ]
    """
    path = f"historical/earning_calendar/{symbol}"
    query_vars = {
        "apikey": apikey,
        "symbol": symbol,
        "limit": limit,
    }
    return return_json(path=path, query_vars=query_vars)


def ipo_calendar(apikey: str, from_date: str = None, to_date: str = None) -> typing.List[typing.Dict]:
    """
    Query FMP API for IPO Calendar

    Example:
    https://financialmodelingprep.com/api/v3/ipo_calendar?from=2020-09-01&to=2020-11-01&apikey=demo
    [ {
        "date" : "2020-08-31",
        "company" : "Applied UV, Inc.",
        "symbol" : "AUVI",
        "exchange" : "NASDAQ Capital",
        "actions" : "expected",
        "shares" : 1000000,
        "priceRange" : "5.00",
        "marketCap" : 5750000
      }, {
        "date" : "2020-08-28",
        "company" : "Petra Acquisition Inc.",
        "symbol" : "PAICU",
        "exchange" : "NASDAQ Capital",
        "actions" : "expected",
        "shares" : 7500000,
        "priceRange" : "10.00",
        "marketCap" : 86250000
      }, {
        "date" : "2020-08-28",
        "company" : "Sun BioPharma, Inc.",
        "symbol" : "",
        "exchange" : "NASDAQ Capital",
        "actions" : "expected",
        "shares" : 2100000,
        "priceRange" : "5.00",
        "marketCap" : 10500000
      }, ...
    ]
    """
    path = f"ipo_calendar"
    query_vars = {
        "apikey": apikey,
    }
    if from_date:
        query_vars['from'] = from_date
    if to_date:
        query_vars['to'] = to_date
    return return_json(path=path, query_vars=query_vars)


def stock_split_calendar(apikey: str, from_date: str = None, to_date: str = None) -> typing.List[typing.Dict]:
    """
    Query FMP API for Stock Split Calendar

    Example:
    https://financialmodelingprep.com/api/v3/stock_split_calendar?from=2020-06-01&to=2020-09-10&apikey=demo
    [ {
        "date" : "2020-08-31",
        "label" : "August 31, 20",
        "symbol" : "TSLA",
        "numerator" : 5.0,
        "denominator" : 5.0
      }, {
        "date" : "2020-08-31",
        "label" : "August 31, 20",
        "symbol" : "AAPL",
        "numerator" : 4.0,
        "denominator" : 4.0
      }, {
        "date" : "2020-08-28",
        "label" : "August 28, 20",
        "symbol" : "WEBS",
        "numerator" : 1.0,
        "denominator" : 1.0
      }, {
        "date" : "2020-08-28",
        "label" : "August 28, 20",
        "symbol" : "LABD",
        "numerator" : 1.0,
        "denominator" : 1.0
      }, ...
    ]
    """
    path = f"stock_split_calendar"
    query_vars = {
        "apikey": apikey,
    }
    if from_date:
        query_vars['from'] = from_date
    if to_date:
        query_vars['to'] = to_date
    return return_json(path=path, query_vars=query_vars)


def dividend_calendar(apikey: str, from_date: str = None, to_date: str = None) -> typing.List[typing.Dict]:
    """
    Query FMP API for Dividend Calendar

    Example:
    https://financialmodelingprep.com/api/v3/stock_dividend_calendar?from=2020-01-01&to=2020-09-01&apikey=demo
    [ {
        "date" : "2020-09-02",
        "label" : "September 02, 20",
        "adjDividend" : 0.02,
        "symbol" : "BOL.PA"
      }, {
        "date" : "2020-09-01",
        "label" : "September 01, 20",
        "adjDividend" : 0.47,
        "symbol" : "WKL.AS"
      }, {
        "date" : "2020-09-01",
        "label" : "September 01, 20",
        "adjDividend" : 0.002809,
        "symbol" : "ITUB"
      }, {
        "date" : "2020-09-01",
        "label" : "September 01, 20",
        "adjDividend" : 0.05,
        "symbol" : "FEI"
      }, ...
    ]
    """
    path = f"stock_dividend_calendar"
    query_vars = {
        "apikey": apikey,
    }
    if from_date:
        query_vars['from'] = from_date
    if to_date:
        query_vars['to'] = to_date
    return return_json(path=path, query_vars=query_vars)


def economic_calendar(apikey: str, from_date: str = None, to_date: str = None) -> typing.List[typing.Dict]:
    """
    Query FMP API for Economic Calendar

    Example:
    https://financialmodelingprep.com/api/v3/economic_calendar?from=2020-08-05&to=2020-10-20&apikey=demo
    [{
        "event" : "Euro Zone Retail Sales Retail Sales MM",
        "date" : "2020-08-05 09:00:00",
        "country" : "ERL",
        "actual" : 5.3,
        "previous" : 20.6,
        "change" : -15.3,
        "changePercentage" : -0.7427,
        "estimate" : 5.9
      }, {
        "event" : "United Kingdom PMI Services MarkitCIPS Serv PMI Final",
        "date" : "2020-08-05 08:30:00",
        "country" : "GB",
        "actual" : 56.5,
        "previous" : 47.1,
        "change" : 9.4,
        "changePercentage" : 0.1996,
        "estimate" : 56.6
      }, {
        "event" : "United Kingdom PMI ServicesComposite Composite PMI Final",
        "date" : "2020-08-05 08:30:00",
        "country" : "GB",
        "actual" : 57,
        "previous" : 47.7,
        "change" : 9.3,
        "changePercentage" : 0.1950,
        "estimate" : 57.1
      }, ...
    ]
    """
    path = f"economic_calendar"
    query_vars = {
        "apikey": apikey,
    }
    if from_date:
        query_vars['from'] = from_date
    if to_date:
        query_vars['to'] = to_date
    return return_json(path=path, query_vars=query_vars)
