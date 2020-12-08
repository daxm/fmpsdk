from .settings import BASE_URL
from .url_methods import *


def historical_stock_dividend(apikey: str, symbol: str):
    """
    Query FMP API for Historical Stock Dividends

    Example:
    https://financialmodelingprep.com/api/v3/historical-price-full/stock_dividend/AAPL?apikey=demo
    {
      "symbol" : "AAPL",
      "historical" : [ {
        "date" : "2020-08-07",
        "label" : "August 07, 20",
        "adjDividend" : 0.2050000000,
        "dividend" : 0.82,
        "recordDate" : "2020-08-10",
        "paymentDate" : "2020-08-13",
        "declarationDate" : "2020-07-30"
      }, {
        "date" : "2020-05-08",
        "label" : "May 08, 20",
        "adjDividend" : 0.2050000000,
        "dividend" : 0.82,
        "recordDate" : "2020-05-11",
        "paymentDate" : "2020-05-14",
        "declarationDate" : "2020-04-30"
      }, {
        "date" : "2020-02-07",
        "label" : "February 07, 20",
        "adjDividend" : 0.1925000000,
        "dividend" : 0.77,
        "recordDate" : "2020-02-10",
        "paymentDate" : "2020-02-13",
        "declarationDate" : "2020-01-28"
      }, ... ]
    }
    """
    path = f"historical-price-full/stock_dividend/{symbol}"
    query_vars = {
        "apikey": apikey,
    }
    return return_response(base=BASE_URL, path=path, query_vars=query_vars)


def historical_stock_split(apikey: str, symbol: str):
    """
    Query FMP API for Historical Stock Splits

    Example:
    https://financialmodelingprep.com/api/v3/historical-price-full/stock_split/AAPL?apikey=demo
    {
      "symbol" : "AAPL",
      "historical" : [ {
        "date" : "2020-08-31",
        "label" : "August 31, 20",
        "numerator" : 4.00,
        "denominator" : 1.00
      }, {
        "date" : "2014-06-09",
        "label" : "June 09, 14",
        "numerator" : 7.00,
        "denominator" : 1.00
      }, {
        "date" : "2005-02-28",
        "label" : "February 28, 05",
        "numerator" : 2.00,
        "denominator" : 1.00
      }, {
        "date" : "2000-06-21",
        "label" : "June 21, 00",
        "numerator" : 2.00,
        "denominator" : 1.00
      }, {
        "date" : "1987-06-16",
        "label" : "June 16, 87",
        "numerator" : 2.00,
        "denominator" : 1.00
      } ]
    }
    """
    path = f"historical-price-full/stock_split/{symbol}"
    query_vars = {
        "apikey": apikey,
    }
    return return_response(base=BASE_URL, path=path, query_vars=query_vars)
