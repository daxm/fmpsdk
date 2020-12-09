from .url_methods import return_response


def earning_calendar(apikey: str, from_date: str = None, to_date: str = None):
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
    return return_response(path=path, query_vars=query_vars)
