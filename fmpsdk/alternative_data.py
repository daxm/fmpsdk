import typing

from .url_methods import __return_json_v4


def commitment_of_traders_report_list(
    apikey: str,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /commitment_of_traders_report/list API.

    List of symbols for COT.

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"commitment_of_traders_report/list"
    query_vars = {"apikey": apikey}
    return __return_json_v4(path=path, query_vars=query_vars)


def commitment_of_traders_report(
    apikey: str,
    symbol: str,
    from_date: str,
    to_date: str,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /commitment_of_traders_report API.

    The Commodity Futures Trading Commission (Commission or CFTC) publishes the Commitments of Traders (COT)
    reports to help the public understand market dynamics. Specifically, the COT reports provide a breakdown of
    each Tuesday’s open interest for futures and options on futures markets in which 20 or more traders hold
    positions equal to or above the reporting levels established by the CFTC.

    Generally, the data in the COT reports is from Tuesday and released Friday. The CFTC receives the data from the
    reporting firms on Wednesday morning and then corrects and verifies the data for release by Friday afternoon.

    :param apikey: Your API key.
    :param symbol: COT symbol.
    :param from_date: YYYY-MM-DD string.
    :param to_date: YYYY-MM-DD string.
    :return: A list of dictionaries.
    """
    path = f"commitment_of_traders_report"
    query_vars = {"apikey": apikey}
    if symbol:
        path = f"{path}/{symbol}"
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    return __return_json_v4(path=path, query_vars=query_vars)


def commitment_of_traders_report_analysis(
    apikey: str,
    symbol: str,
    from_date: str,
    to_date: str,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /commitment_of_traders_report_analysis API.

    Analysis of reports for time period or symbol.

    :param apikey: Your API key.
    :param symbol: trading symbol.
    :param from_date: YYYY-MM-DD string.
    :param to_date: YYYY-MM-DD string.
    :return: A list of dictionaries.
    """
    path = f"commitment_of_traders_report_analysis"
    query_vars = {"apikey": apikey}
    if symbol:
        path = f"{path}/{symbol}"
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    return __return_json_v4(path=path, query_vars=query_vars)
