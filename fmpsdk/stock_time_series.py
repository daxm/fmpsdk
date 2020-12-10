from .url_methods import return_json, set_exchange, set_time_delta, set_symbol, set_series_type
import typing


def quote_realtime(apikey: str, symbol: str) -> typing.List[typing.Dict]:
    """
    Query FMP API for Realtime Stock Quote

    Example:
    https://financialmodelingprep.com/api/v3/quote-short/AAPL?apikey=demo
    [ {
        "symbol" : "AAPL",
        "price" : 120.96000000,
        "volume" : 332607163
    } ]
    """
    path = f"quote-short/{symbol}"
    query_vars = {
        "apikey": apikey,
    }
    return return_json(path=path, query_vars=query_vars)


def exchange_realtime(apikey: str, exchange: str) -> typing.List[typing.Dict]:
    """
    Query FMP API for Realtime Stock Quote

    Example:
    https://financialmodelingprep.com/api/v3/quote-short/AAPL?apikey=demo
    [ {
        "symbol" : "AAPL",
        "price" : 120.96000000,
        "volume" : 332607163
    } ]
    """
    path = f"quotes/{set_exchange(exchange)}"
    query_vars = {
        "apikey": apikey,
    }
    return return_json(path=path, query_vars=query_vars)


def historical_chart(apikey: str, symbol: str, time_delta: str) -> typing.List[typing.Dict]:
    """
    Query FMP API for Historical Charts

    Example:
    https://financialmodelingprep.com/api/v3/historical-chart/1min/AAPL?apikey=demo
    [ {
        "date" : "2020-03-02 15:59:00",
        "open" : 297.230000000000,
        "low" : 297.230000000000,
        "high" : 298.280000000000,
        "close" : 298.252300000000,
        "volume" : 78679246
      }, {
        "date" : "2020-03-02 15:58:00",
        "open" : 296.190000000000,
        "low" : 296.190000000000,
        "high" : 297.430000000000,
        "close" : 297.230000000000,
        "volume" : 77982786
      }, {
        "date" : "2020-03-02 15:57:00",
        "open" : 295.860000000000,
        "low" : 295.860000000000,
        "high" : 296.580000000000,
        "close" : 296.190000000000,
        "volume" : 77400704
      }, {
        "date" : "2020-03-02 15:56:00",
        "open" : 297.100000000000,
        "low" : 295.578600000000,
        "high" : 297.100000000000,
        "close" : 295.860000000000,
        "volume" : 76885430
      }, {
        "date" : "2020-03-02 15:55:00",
        "open" : 295.144600000000,
        "low" : 295.110000000000,
        "high" : 297.100000000000,
        "close" : 297.100000000000,
        "volume" : 76202093
      }, ...
    ]
    """
    path = f"historical-chart/{set_time_delta(time_delta)}/{symbol}"
    query_vars = {
        "apikey": apikey,
    }
    return return_json(path=path, query_vars=query_vars)


def historical_price(
        apikey: str,
        symbol: typing.Union[str, typing.List],
        time_series: int = None,
        series_type: str = None,
        from_date: str = None,
        to_date: str = None,
) -> typing.Dict:
    """
    Query FMP API for Historical Stock Prices

    Example:
    https://financialmodelingprep.com/api/v3/historical-price-full/AAPL?apikey=demo
    {
        "symbol" : "AAPL",
        "historical" : [ {
            "date" : "2015-01-20",
            "open" : 107.84,
            "high" : 108.97,
            "low" : 106.5,
            "close" : 108.72,
            "volume" : 4.98999E7,
            "unadjustedVolume" : 4.98999E7,
            "change" : -0.88,
            "changePercent" : -0.816,
            "vwap" : 108.06333,
            "label" : "January 20, 15",
            "changeOverTime" : -0.00816
          }, {
            "date" : "2015-01-21",
            "open" : 108.95,
            "high" : 111.06,
            "low" : 108.27,
            "close" : 109.55,
            "volume" : 4.85759E7,
            "unadjustedVolume" : 4.85759E7,
            "change" : -0.6,
            "changePercent" : -0.551,
            "vwap" : 109.62667,
            "label" : "January 21, 15",
            "changeOverTime" : -0.00551
          }, {
            "date" : "2015-01-22",
            "open" : 110.26,
            "high" : 112.47,
            "low" : 109.72,
            "close" : 112.4,
            "volume" : 5.37964E7,
            "unadjustedVolume" : 5.37964E7,
            "change" : -2.14,
            "changePercent" : -1.941,
            "vwap" : 111.53,
            "label" : "January 22, 15",
            "changeOverTime" : -0.01941
          }, ...
        } ]
      }
    """
    path = f"historical-price-full/{set_symbol(symbol)}"
    query_vars = {
        "apikey": apikey,
    }
    if time_series:
        query_vars['timeseries'] = time_series
    if series_type:
        query_vars['serietype'] = set_series_type(series_type)
    if from_date:
        query_vars['from'] = from_date
    if to_date:
        query_vars['to'] = to_date
    return return_json(path=path, query_vars=query_vars)


def historical_stock_dividend(apikey: str, symbol: str) -> typing.List[typing.Dict]:
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
    return return_json(path=path, query_vars=query_vars)


def historical_stock_split(apikey: str, symbol: str) -> typing.List[typing.Dict]:
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
    return return_json(path=path, query_vars=query_vars)
