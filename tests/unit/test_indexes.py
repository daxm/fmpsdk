"""Mocked unit tests for client.indexes — mirrors fmpsdk/endpoints/indexes.py.

Only the group's own 7 methods are covered here. `historical_chart`,
`historical_price_eod_full`, `historical_price_eod_light`, `quote`,
`quote_short`, and `batch_index_quotes` are cross-listed in from
`client.chart`/`client.quote` (§4.3) — identical bound methods, already
covered by `tests/unit/test_chart.py` and the future `test_quote.py`, so
retesting them here would just be testing the same object twice.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.unit

BASE = "https://financialmodelingprep.com/stable/"


def test_index_list(client, requests_mock):
    requests_mock.get(
        BASE + "index-list",
        json=[
            {
                "symbol": "^GSPC",
                "name": "S&P 500",
                "exchange": "INDEX",
                "currency": "USD",
            }
        ],
    )
    result = client.index_list()
    assert result[0]["symbol"] == "^GSPC"
    assert requests_mock.last_request.qs == {}


def test_sp500_constituent(client, requests_mock):
    requests_mock.get(
        BASE + "sp500-constituent",
        json=[
            {
                "symbol": "AAPL",
                "name": "Apple Inc.",
                "sector": "Technology",
                "subSector": "Technology",
                "headQuarter": "Cupertino, CA",
                "dateFirstAdded": "1982-11-30",
                "cik": "0000320193",
                "founded": "1976-04-01",
            }
        ],
    )
    result = client.sp500_constituent()
    assert result[0]["symbol"] == "AAPL"


def test_nasdaq_constituent(client, requests_mock):
    requests_mock.get(
        BASE + "nasdaq-constituent",
        json=[
            {
                "symbol": "AAPL",
                "name": "Apple Inc.",
                "sector": "Technology",
                "subSector": "Technology",
                "headQuarter": "Cupertino, CA",
                "dateFirstAdded": None,
                "cik": "0000320193",
                "founded": "1976-04-01",
            }
        ],
    )
    result = client.nasdaq_constituent()
    assert result[0]["dateFirstAdded"] is None


def test_dowjones_constituent(client, requests_mock):
    requests_mock.get(
        BASE + "dowjones-constituent",
        json=[
            {
                "symbol": "AAPL",
                "name": "Apple Inc.",
                "sector": "Technology",
                "subSector": "Technology",
                "headQuarter": "Cupertino, CA",
                "dateFirstAdded": "2015-03-19",
                "cik": "0000320193",
                "founded": "1976-04-01",
            }
        ],
    )
    result = client.dowjones_constituent()
    assert result[0]["cik"] == "0000320193"


def test_historical_sp500_constituent(client, requests_mock):
    requests_mock.get(
        BASE + "historical-sp500-constituent",
        json=[
            {
                "dateAdded": "September 23, 2025",
                "addedSecurity": "AppLovin",
                "removedTicker": "MKTX",
                "removedSecurity": "MarketAxess Holdings",
                "date": "2025-09-19",
                "symbol": "APP",
                "reason": "Market capitalization change.",
            }
        ],
    )
    result = client.historical_sp500_constituent()
    assert result[0]["symbol"] == "APP"


def test_historical_nasdaq_constituent(client, requests_mock):
    requests_mock.get(
        BASE + "historical-nasdaq-constituent",
        json=[
            {
                "dateAdded": "December 23, 2024",
                "addedSecurity": "MicroStrategy",
                "removedTicker": None,
                "removedSecurity": None,
                "date": "2024-12-23",
                "symbol": "MSTR",
                "reason": "Index rebalancing.",
            }
        ],
    )
    result = client.historical_nasdaq_constituent()
    assert result[0]["removedTicker"] is None


def test_historical_dowjones_constituent(client, requests_mock):
    requests_mock.get(
        BASE + "historical-dowjones-constituent",
        json=[
            {
                "dateAdded": "February 26, 2024",
                "addedSecurity": "Amazon.com",
                "removedTicker": "WBA",
                "removedSecurity": "Walgreens Boots Alliance",
                "date": "2024-02-26",
                "symbol": "AMZN",
                "reason": "Market capitalization change.",
            }
        ],
    )
    result = client.historical_dowjones_constituent()
    assert result[0]["addedSecurity"] == "Amazon.com"
