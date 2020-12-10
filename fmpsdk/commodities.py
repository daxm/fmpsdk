from .url_methods import return_json
import typing


def available_commodities(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP for Commodities available symbols for quotes and historical prices query.

    Example:
        https://financialmodelingprep.com/api/v3/quote/ZGUSD,CLUSD,HGUSD?apikey=demo
        [ {
            "symbol" : "CLUSD",
            "price" : 59.12000000,
            "changesPercentage" : -0.74000000,
            "change" : -0.44000000,
            "dayLow" : 58.85000000,
            "dayHigh" : 59.78000000,
            "yearHigh" : 65.48000000,
            "yearLow" : 0E-8,
            "marketCap" : null,
            "priceAvg50" : 59.56000000,
            "priceAvg200" : 58.34536700,
            "volume" : 553817,
            "avgVolume" : 157504928,
            "exhange" : "COMMODITY"
          }, {
            "symbol" : "ZGUSD",
            "price" : 1566.00000000,
            "changesPercentage" : 0.38000000,
            "change" : 5.90000000,
            "dayLow" : 1566.00000000,
            "dayHigh" : 1566.00000000,
            "yearHigh" : 1566.00000000,
            "yearLow" : 1452.00000000,
            "marketCap" : null,
            "priceAvg50" : 1560.10000000,
            "priceAvg200" : 1521.67500000,
            "volume" : 0,
            "avgVolume" : 1,
            "exhange" : "COMMODITY"
          }, {
            "symbol" : "HGUSD",
            "price" : 2.81000000,
            "changesPercentage" : 0.29000000,
            "change" : 0.00800000,
            "dayLow" : 2.79550000,
            "dayHigh" : 2.83600000,
            "yearHigh" : 2.83600000,
            "yearLow" : 2.75950000,
            "marketCap" : null,
            "priceAvg50" : 2.80200000,
            "priceAvg200" : 2.79850000,
            "volume" : 58820,
            "avgVolume" : 23833272,
            "exhange" : "COMMODITY"
          }, ...
        ]

    :param apikey: Your API Key
    :return: List of Dictionaries
   """
    path = f"available-commodities"
    query_vars = {"apikey": apikey}
    return return_json(path=path, query_vars=query_vars)


def commodities(apikey: str) -> typing.List[typing.Dict]:
    """
    Query FMP for All Real-time Commodities Prices.

    Example:
        https://financialmodelingprep.com/api/v3/quote/ZGUSD,CLUSD,HGUSD?apikey=demo
        [ {
            "symbol" : "CLUSD",
            "price" : 59.12000000,
            "changesPercentage" : -0.74000000,
            "change" : -0.44000000,
            "dayLow" : 58.85000000,
            "dayHigh" : 59.78000000,
            "yearHigh" : 65.48000000,
            "yearLow" : 0E-8,
            "marketCap" : null,
            "priceAvg50" : 59.56000000,
            "priceAvg200" : 58.34536700,
            "volume" : 553817,
            "avgVolume" : 157504928,
            "exhange" : "COMMODITY"
          }, {
            "symbol" : "ZGUSD",
            "price" : 1566.00000000,
            "changesPercentage" : 0.38000000,
            "change" : 5.90000000,
            "dayLow" : 1566.00000000,
            "dayHigh" : 1566.00000000,
            "yearHigh" : 1566.00000000,
            "yearLow" : 1452.00000000,
            "marketCap" : null,
            "priceAvg50" : 1560.10000000,
            "priceAvg200" : 1521.67500000,
            "volume" : 0,
            "avgVolume" : 1,
            "exhange" : "COMMODITY"
          }, {
            "symbol" : "HGUSD",
            "price" : 2.81000000,
            "changesPercentage" : 0.29000000,
            "change" : 0.00800000,
            "dayLow" : 2.79550000,
            "dayHigh" : 2.83600000,
            "yearHigh" : 2.83600000,
            "yearLow" : 2.75950000,
            "marketCap" : null,
            "priceAvg50" : 2.80200000,
            "priceAvg200" : 2.79850000,
            "volume" : 58820,
            "avgVolume" : 23833272,
            "exhange" : "COMMODITY"
          }, ...
        ]

    :param apikey: Your API Key
    :return: List of Dictionaries
   """
    path = f"quotes/commodity"
    query_vars = {"apikey": apikey}
    return return_json(path=path, query_vars=query_vars)
