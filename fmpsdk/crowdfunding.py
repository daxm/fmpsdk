import typing
from .url_methods import __return_json_v4
import os

API_KEY = os.getenv("FMP_API_KEY")

def crowdfunding_rss_feed(page: int = 0) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Provides an RSS feed of crowdfunding campaigns, updated in real time.

    :param page: The page number for pagination (default is 0)
    :return: A list of dictionaries containing crowdfunding campaign information
    """
    path = "crowdfunding-offerings-rss-feed"
    query_vars = {"page": page, "apikey": API_KEY}
    return __return_json_v4(path=path, query_vars=query_vars)

def crowdfunding_search(name: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Allows users to search for crowdfunding campaigns by company name, campaign name, or platform.

    :param name: The name to search for
    :return: A list of dictionaries containing matching crowdfunding campaigns
    """
    path = "crowdfunding-offerings/search"
    query_vars = {"name": name, "apikey": API_KEY}
    return __return_json_v4(path=path, query_vars=query_vars)

def crowdfunding_by_cik(cik: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Provides a list of all crowdfunding campaigns that have been launched by a particular company.

    :param cik: The Central Index Key (CIK) of the company
    :return: A list of dictionaries containing crowdfunding campaigns for the specified company
    """
    path = "crowdfunding-offerings"
    query_vars = {"cik": cik, "apikey": API_KEY}
    return __return_json_v4(path=path, query_vars=query_vars)