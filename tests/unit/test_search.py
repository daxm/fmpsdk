"""Mocked unit tests for client.search — mirrors fmpsdk/endpoints/search.py."""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.unit

BASE = "https://financialmodelingprep.com/stable/"


def test_search_symbol(client, requests_mock):
    requests_mock.get(
        BASE + "search-symbol",
        json=[
            {
                "symbol": "AAPL",
                "name": "Apple Inc.",
                "currency": "USD",
                "exchangeFullName": "NASDAQ Global Select",
                "exchange": "NASDAQ",
            }
        ],
    )
    result = client.search_symbol(query="AAPL", limit=5, exchange="NASDAQ")
    assert result[0]["symbol"] == "AAPL"
    sent = requests_mock.last_request.qs
    assert sent["query"] == ["aapl"]
    assert sent["limit"] == ["5"]
    assert sent["exchange"] == ["nasdaq"]


def test_search_symbol_omits_unset_optional_params(client, requests_mock):
    requests_mock.get(BASE + "search-symbol", json=[])
    client.search_symbol(query="AAPL")
    sent = requests_mock.last_request.qs
    assert "limit" not in sent
    assert "exchange" not in sent


def test_search_name_shares_symbol_shape(client, requests_mock):
    requests_mock.get(
        BASE + "search-name",
        json=[
            {
                "symbol": "AAGUSD",
                "name": "AAG USD",
                "currency": "USD",
                "exchangeFullName": "CCC",
                "exchange": "CRYPTO",
            }
        ],
    )
    result = client.search_name(query="AA")
    assert result[0]["name"] == "AAG USD"


def test_search_cik(client, requests_mock):
    requests_mock.get(
        BASE + "search-cik",
        json=[
            {
                "symbol": "AAPL",
                "companyName": "Apple Inc.",
                "cik": "0000320193",
                "exchangeFullName": "NASDAQ Global Select",
                "exchange": "NASDAQ",
                "currency": "USD",
            }
        ],
    )
    result = client.search_cik(cik="320193")
    assert result[0]["cik"] == "0000320193"
    assert requests_mock.last_request.qs["cik"] == ["320193"]


def test_search_cusip(client, requests_mock):
    requests_mock.get(
        BASE + "search-cusip",
        json=[{"symbol": "APC.F", "companyName": "Apple Inc.", "cusip": "037833100", "marketCap": 4227021056800}],
    )
    result = client.search_cusip(cusip="037833100")
    assert result[0]["cusip"] == "037833100"


def test_search_isin(client, requests_mock):
    requests_mock.get(
        BASE + "search-isin",
        json=[{"symbol": "AAPL", "name": "Apple Inc.", "isin": "US0378331005", "marketCap": 4874072686740}],
    )
    result = client.search_isin(isin="US0378331005")
    assert result[0]["isin"] == "US0378331005"


def test_search_exchange_variants(client, requests_mock):
    requests_mock.get(
        BASE + "search-exchange-variants",
        json=[{"symbol": "AAPL", "exchange": "NASDAQ Global Select", "exchangeShortName": "NASDAQ"}],
    )
    result = client.search_exchange_variants(symbol="AAPL")
    assert result[0]["exchangeShortName"] == "NASDAQ"
    assert requests_mock.last_request.qs["symbol"] == ["aapl"]


def test_company_screener_maps_snake_case_to_camel_case(client, requests_mock):
    requests_mock.get(BASE + "company-screener", json=[])
    client.company_screener(
        market_cap_more_than=1_000_000,
        sector="Technology",
        is_etf=False,
        is_actively_trading=True,
        include_all_share_classes=False,
    )
    sent = requests_mock.last_request.qs
    assert sent["marketcapmorethan"] == ["1000000"]
    assert sent["sector"] == ["technology"]
    assert sent["isetf"] == ["false"]
    assert sent["isactivelytrading"] == ["true"]
    assert sent["includeallshareclasses"] == ["false"]
    # Params never passed stay off the wire entirely (§8.8 — no invented defaults).
    assert "marketcaplowerthan" not in sent
    assert "limit" not in sent


def test_company_screener_response_shape(client, requests_mock):
    requests_mock.get(
        BASE + "company-screener",
        json=[
            {
                "symbol": "AAPL",
                "companyName": "Apple Inc.",
                "marketCap": 4885602246714,
                "sector": "Technology",
                "industry": "Consumer Electronics",
                "beta": 1.097,
                "price": 332.64001,
                "lastAnnualDividend": 1.05,
                "volume": 29909012,
                "exchange": "NASDAQ Global Select",
                "exchangeShortName": "NASDAQ",
                "country": "US",
                "isEtf": False,
                "isFund": False,
                "isActivelyTrading": True,
            }
        ],
    )
    result = client.company_screener()
    assert result[0]["symbol"] == "AAPL"
    assert result[0]["isActivelyTrading"] is True
