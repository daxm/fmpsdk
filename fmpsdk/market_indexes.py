from .settings import BASE_URL, SP500_CONSTITUENTS_FILENAME, NASDAQ_CONSTITUENTS_FILENAME, \
    DOWJONES_CONSTITUENTS_FILENAME
from .url_methods import return_json, set_time_delta
import requests
import logging
import typing


def market_indexes(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP API for list of Market Indexes.

    Example:
    https://financialmodelingprep.com/api/v3/quotes/index?apikey=demo
    [ {
        "symbol" : "^RUITR",
        "name" : "Russell 1000 Total Return",
        "price" : 11175.62700000,
        "changesPercentage" : -0.86000000,
        "change" : -96.47300000,
        "dayLow" : 10910.42500000,
        "dayHigh" : 11349.33700000,
        "yearHigh" : 11349.33700000,
        "yearLow" : 10910.42500000,
        "marketCap" : null,
        "priceAvg50" : null,
        "priceAvg200" : null,
        "volume" : 0,
        "avgVolume" : null,
        "exchange" : "INDEX",
        "open" : 11267.76800000,
        "previousClose" : 11272.10000000,
        "eps" : null,
        "pe" : null,
        "earningsAnnouncement" : null,
        "sharesOutstanding" : null,
        "timestamp" : 1599436300
      }, {
        "symbol" : "^NSEI",
        "name" : "NIFTY 50",
        "price" : 11333.85000000,
        "changesPercentage" : -1.68000000,
        "change" : -193.65000000,
        "dayLow" : 11303.65000000,
        "dayHigh" : 11452.05000000,
        "yearHigh" : 12430.50000000,
        "yearLow" : 7511.10000000,
        "marketCap" : null,
        "priceAvg50" : 11287.06100000,
        "priceAvg200" : 10177.60000000,
        "volume" : 0,
        "avgVolume" : 676837,
        "exchange" : "INDEX",
        "open" : 11354.40000000,
        "previousClose" : 11527.50000000,
        "eps" : null,
        "pe" : null,
        "earningsAnnouncement" : null,
        "sharesOutstanding" : null,
        "timestamp" : 1599436300
      }, ...
    ]
   """
    path = f"quotes/index"
    query_vars = {"apikey": apikey}
    return return_json(path=path, query_vars=query_vars)


def index_quote(apikey: str, index: str) -> typing.List[typing.Dict]:
    """
    Query FMP API Market Indexes.

    Example:
    https://financialmodelingprep.com/api/v3/quotes/index?apikey=demo
    [ {
        "symbol" : "^RUITR",
        "name" : "Russell 1000 Total Return",
        "price" : 11175.62700000,
        "changesPercentage" : -0.86000000,
        "change" : -96.47300000,
        "dayLow" : 10910.42500000,
        "dayHigh" : 11349.33700000,
        "yearHigh" : 11349.33700000,
        "yearLow" : 10910.42500000,
        "marketCap" : null,
        "priceAvg50" : null,
        "priceAvg200" : null,
        "volume" : 0,
        "avgVolume" : null,
        "exchange" : "INDEX",
        "open" : 11267.76800000,
        "previousClose" : 11272.10000000,
        "eps" : null,
        "pe" : null,
        "earningsAnnouncement" : null,
        "sharesOutstanding" : null,
        "timestamp" : 1599436300
      }, {
        "symbol" : "^NSEI",
        "name" : "NIFTY 50",
        "price" : 11333.85000000,
        "changesPercentage" : -1.68000000,
        "change" : -193.65000000,
        "dayLow" : 11303.65000000,
        "dayHigh" : 11452.05000000,
        "yearHigh" : 12430.50000000,
        "yearLow" : 7511.10000000,
        "marketCap" : null,
        "priceAvg50" : 11287.06100000,
        "priceAvg200" : 10177.60000000,
        "volume" : 0,
        "avgVolume" : 676837,
        "exchange" : "INDEX",
        "open" : 11354.40000000,
        "previousClose" : 11527.50000000,
        "eps" : null,
        "pe" : null,
        "earningsAnnouncement" : null,
        "sharesOutstanding" : null,
        "timestamp" : 1599436300
      }, ...
    ]
   """
    path = f"quote/{index}"
    query_vars = {"apikey": apikey}
    return return_json(path=path, query_vars=query_vars)


def sp500_constituent(
        apikey: str,
        download: bool = False,
        filename: str = SP500_CONSTITUENTS_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP API for list of SP500 companies.

    Example:
    https://financialmodelingprep.com/api/v3/sp500_constituent?apikey=demo
    [ {
        "symbol" : "MMM",
        "name" : "3M Company",
        "sector" : "Industrials",
        "subSector" : "Industrial Conglomerates",
        "headQuarter" : "St. Paul, Minnesota",
        "dateFirstAdded" : "1976-08-09",
        "cik" : "0000066740",
        "founded" : "1902"
      },
      {
        "symbol" : "ABT",
        "name" : "Abbott Laboratories",
        "sector" : "Health Care",
        "subSector" : "Health Care Equipment",
        "headQuarter" : "North Chicago, Illinois",
        "dateFirstAdded" : "1964-03-31",
        "cik" : "0000001800",
        "founded" : "1888"
      },
      {
        "symbol" : "ABBV",
        "name" : "AbbVie Inc.",
        "sector" : "Health Care",
        "subSector" : "Pharmaceuticals",
        "headQuarter" : "North Chicago, Illinois",
        "dateFirstAdded" : "2012-12-31",
        "cik" : "0001551152",
        "founded" : "2013 (1888)"
    }, ...
    ]
    """
    path = f"sp500_constituent"
    query_vars = {"apikey": apikey}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f'{BASE_URL}{path}', params=query_vars)
        open(filename, 'wb').write(response.content)
        logging.info(f"Saving SP500 Constituents as {filename}.")
    else:
        return return_json(path=path, query_vars=query_vars)


def historical_sp500_constituent(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP API for Historical list of SP500 companies.

    Example:
    https://financialmodelingprep.com/api/v3/historical/sp500_constituent?apikey=demo
    [ {
        "dateAdded" : "May 22, 2020",
        "addedSecurity" : "West Pharmaceutical Services",
        "removedTicker" : "HP",
        "removedSecurity" : "Helmerich & Payne",
        "reason" : "Market capitalization change.",
        "symbol" : "WST"
      }, {
        "dateAdded" : "May 12, 2020",
        "addedSecurity" : "Domino's Pizza",
        "removedTicker" : "CPRI",
        "removedSecurity" : "Capri Holdings",
        "reason" : "Market capitalization change.",
        "symbol" : "DPZ"
      }, {
        "dateAdded" : "May 12, 2020",
        "addedSecurity" : "Dexcom",
        "removedTicker" : "AGN",
        "removedSecurity" : "Allergan",
        "reason" : "Allergan acquired by AbbVie.",
        "symbol" : "DXCM"
      }, {
        "dateAdded" : "April 3, 2020",
        "addedSecurity" : "Otis Worldwide",
        "removedTicker" : "",
        "removedSecurity" : "",
        "reason" : "United Technologies spun off Otis and Carrier and acquired Raytheon Company.",
        "symbol" : "OTIS"
      },
    ]
    """
    path = f"historical/sp500_constituent"
    query_vars = {"apikey": apikey}
    return return_json(path=path, query_vars=query_vars)


def nasdaq_constituent(
        apikey: str,
        download: bool = False,
        filename: str = NASDAQ_CONSTITUENTS_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP API for list of NASDAQ companies.

    Example:
    https://financialmodelingprep.com/api/v3/nasdaq_constituent?apikey=demo
    [ {
        "symbol" : "ZM",
        "name" : "Zoom Video Communications Inc",
        "sector" : "Communication Services",
        "subSector" : "Communication Services",
        "headQuarter" : "San Jose, CALIFORNIA",
        "dateFirstAdded" : "2019-04-18",
        "cik" : "0001585521",
        "founded" : "2019-04-18"
      }, {
        "symbol" : "ADP",
        "name" : "Automatic Data Processing Inc",
        "sector" : "Industrials",
        "subSector" : "Industrials",
        "headQuarter" : "Roseland, NEW JERSEY",
        "dateFirstAdded" : "1961-09-01",
        "cik" : "0000008670",
        "founded" : "1961-09-01"
      }, ...
    ]
    """
    path = f"nasdaq_constituent"
    query_vars = {"apikey": apikey}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f'{BASE_URL}{path}', params=query_vars)
        open(filename, 'wb').write(response.content)
        logging.info(f"Saving NASDAQ Constituents as {filename}.")
    else:
        return return_json(path=path, query_vars=query_vars)


def historical_nasdaq_constituent(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP API for Historical list of NASDAQ companies.

    Example:
    https://financialmodelingprep.com/api/v3/historical/nasdaq_constituent?apikey=demo
    [ {
        "dateAdded" : "August 24, 2020",
        "addedSecurity" : "Pinduoduo Inc",
        "removedTicker" : "",
        "removedSecurity" : "",
        "date" : "2020-08-24",
        "reason" : "Market capitalization change.",
        "symbol" : "PDD"
      }, {
        "dateAdded" : "August 24, 2020",
        "addedSecurity" : "",
        "removedTicker" : "NTAP",
        "removedSecurity" : "NetApp Inc",
        "date" : "2020-08-24",
        "reason" : "Market capitalization change",
        "symbol" : "NTAP"
      }, ...
    ]
    """
    path = f"historical/nasdaq_constituent"
    query_vars = {"apikey": apikey}
    return return_json(path=path, query_vars=query_vars)


def dowjones_constituent(
        apikey: str,
        download: bool = False,
        filename: str = DOWJONES_CONSTITUENTS_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP API for list of DOWJONES companies.

    Example:
    https://financialmodelingprep.com/api/v3/dowjones_constituent?apikey=demo
    [ {
        "symbol" : "HON",
        "name" : "Honeywell International Inc",
        "sector" : "Industrials",
        "subSector" : "Industrials",
        "headQuarter" : "Charlotte, NORTH CAROLINA",
        "dateFirstAdded" : "1985-09-19",
        "cik" : "0000773840",
        "founded" : "1985-09-19"
      }, {
        "symbol" : "HD",
        "name" : "Home Depot Inc",
        "sector" : "Consumer Cyclical",
        "subSector" : "Consumer Cyclical",
        "headQuarter" : "Atlanta, GEORGIA",
        "dateFirstAdded" : "1984-04-19",
        "cik" : "0000354950",
        "founded" : "1984-04-19"
      }, ...
    ]
    """
    path = f"dowjones_constituent"
    query_vars = {"apikey": apikey}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f'{BASE_URL}{path}', params=query_vars)
        open(filename, 'wb').write(response.content)
        logging.info(f"Saving DOWJONES Constituents as {filename}.")
    else:
        return return_json(path=path, query_vars=query_vars)


def historical_dowjones_constituent(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP API for Historical list of DOWJONES companies.

    Example:
    https://financialmodelingprep.com/api/v3/historical/dowjones_constituent?apikey=demo
    [ {
        "dateAdded" : "August 31, 2020",
        "addedSecurity" : "Salesforce.Com Inc",
        "removedTicker" : "",
        "removedSecurity" : "",
        "date" : "2020-08-31",
        "reason" : "Market capitalization change.",
        "symbol" : "CRM"
      }, {
        "dateAdded" : "August 31, 2020",
        "addedSecurity" : "",
        "removedTicker" : "RTX",
        "removedSecurity" : "Raytheon Technologies Corp",
        "date" : "2020-08-31",
        "reason" : "Market capitalization change",
        "symbol" : "RTX"
      }, ...
    ]
    """
    path = f"historical/dowjones_constituent"
    query_vars = {"apikey": apikey}
    return return_json(path=path, query_vars=query_vars)


def available_indexes(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP API for list of Indexes.

    Example:
        https://financialmodelingprep.com/api/v3/available-indexes?apikey=demo
        [ {
            "symbol" : "^DJI",
            "name" : "Dow Jones Industrial Average",
            "currency" : "USD",
            "stockExchange" : "DJI",
            "exchangeShortName" : "INDEX"
          }, {
            "symbol" : "^STI",
            "name" : "STI Index",
            "currency" : "SGD",
            "stockExchange" : "SES",
            "exchangeShortName" : "INDEX"
          }, {
            "symbol" : "^BVSP",
            "name" : "IBOVESPA",
            "currency" : "BRL",
            "stockExchange" : "Sao Paolo",
            "exchangeShortName" : "INDEX"
          }, {
            "symbol" : "^MXX",
            "name" : "IPC MEXICO",
            "currency" : "MXN",
            "stockExchange" : "Mexico",
            "exchangeShortName" : "INDEX"
          }, {
            "symbol" : "^GSPTSE",
            "name" : "S&P/TSX Composite index",
            "currency" : "CAD",
            "stockExchange" : "Toronto",
            "exchangeShortName" : "INDEX"
          }, ...
        ]

    :param apikey: String of your API Key
    :return: List of Dictionaries
    """
    path = f"symbol/available-indexes"
    query_vars = {"apikey": apikey}
    return return_json(path=path, query_vars=query_vars)


def historical_stock_prices(
        apikey: str,
        index: str,
        time_delta: str = '4hour',
) -> typing.List[typing.Dict]:
    """
    Query FMP API for Historical Stock Prices.

    Example:
        https://financialmodelingprep.com/api/v3/historical-chart/1min/%5EGSPC?apikey=demo
        [ {
            "date" : "2020-03-02 15:59:00",
            "open" : 3083.600000000000,
            "low" : 3082.960000000000,
            "high" : 3086.340000000000,
            "close" : 3086.270000000000,
            "volume" : 3175295690
          }, {
            "date" : "2020-03-02 15:58:00",
            "open" : 3077.860000000000,
            "low" : 3077.830000000000,
            "high" : 3084.190000000000,
            "close" : 3083.600000000000,
            "volume" : 3134482742
          }, {
            "date" : "2020-03-02 15:57:00",
            "open" : 3079.020000000000,
            "low" : 3077.860000000000,
            "high" : 3083.130000000000,
            "close" : 3077.860000000000,
            "volume" : 3097586111
          }, {
            "date" : "2020-03-02 15:56:00",
            "open" : 3086.600000000000,
            "low" : 3077.440000000000,
            "high" : 3087.050000000000,
            "close" : 3079.020000000000,
            "volume" : 3063276038
          }, {
            "date" : "2020-03-02 15:55:00",
            "open" : 3076.260000000000,
            "low" : 3074.730000000000,
            "high" : 3086.600000000000,
            "close" : 3086.600000000000,
            "volume" : 3024975592
          }, ...
        ]

    :param apikey: String of your API Key
    :param index: String of Market Index
    :param time_delta: String of time to query.  Valid values are in  TIME_DELTA_VALUES var.
    :return: List of Dictionaries
   """
    path = f"historical-chart/{set_time_delta(time_delta)}/{index}"
    query_vars = {"apikey": apikey}
    return return_json(path=path, query_vars=query_vars)


def historical_index(apikey: str, index: str) -> typing.List[typing.Dict]:
    """
    Query FMP API for Historical an Index.

    Example:

    :param apikey: String of your API Key
    :param index: String of Market Index
    :return: List of Dictionaries
   """
    path = f"historical-price-full/{index}"
    query_vars = {"apikey": apikey}
    return return_json(path=path, query_vars=query_vars)
