"""Mocked unit tests for client.directory — mirrors fmpsdk/endpoints/directory.py."""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.unit

BASE = "https://financialmodelingprep.com/stable/"


def test_stock_list(client, requests_mock):
    requests_mock.get(
        BASE + "stock-list",
        json=[{"symbol": "URBANCO.BO", "companyName": "Urban Company Limited"}],
    )
    result = client.stock_list()
    assert result[0]["symbol"] == "URBANCO.BO"
    assert requests_mock.last_request.qs == {}


def test_financial_statement_symbol_list(client, requests_mock):
    requests_mock.get(
        BASE + "financial-statement-symbol-list",
        json=[
            {
                "symbol": "RMES.CN",
                "companyName": "Red Metal Resources Ltd.",
                "tradingCurrency": "CAD",
                "reportingCurrency": "USD",
            }
        ],
    )
    result = client.financial_statement_symbol_list()
    assert result[0]["reportingCurrency"] == "USD"


def test_cik_list(client, requests_mock):
    requests_mock.get(
        BASE + "cik-list",
        json=[{"cik": "0002137358", "companyName": "Osotspa Public Co Limited/ADR"}],
    )
    result = client.cik_list(page=0, limit=1000)
    assert result[0]["cik"] == "0002137358"
    sent = requests_mock.last_request.qs
    assert sent["page"] == ["0"]
    assert sent["limit"] == ["1000"]


def test_cik_list_omits_unset_optional_params(client, requests_mock):
    requests_mock.get(BASE + "cik-list", json=[])
    client.cik_list()
    sent = requests_mock.last_request.qs
    assert "page" not in sent
    assert "limit" not in sent


def test_symbol_change(client, requests_mock):
    requests_mock.get(
        BASE + "symbol-change",
        json=[
            {
                "date": "2026-07-28",
                "companyName": "Yarrow Bioscience, Inc. Common Stock",
                "oldSymbol": "VYNE",
                "newSymbol": "YARW",
            }
        ],
    )
    result = client.symbol_change(invalid=False, limit=100)
    assert result[0]["newSymbol"] == "YARW"
    sent = requests_mock.last_request.qs
    assert sent["invalid"] == ["false"]
    assert sent["limit"] == ["100"]


def test_etf_list(client, requests_mock):
    requests_mock.get(
        BASE + "etf-list",
        json=[{"symbol": "P60.SI", "name": "MULTI-UNITS LUXEMBOURG - Lyxor ETF"}],
    )
    result = client.etf_list()
    assert result[0]["symbol"] == "P60.SI"


def test_actively_trading_list(client, requests_mock):
    requests_mock.get(
        BASE + "actively-trading-list",
        json=[{"symbol": "URBANCO.BO", "name": "Urban Company Limited"}],
    )
    result = client.actively_trading_list()
    assert result[0]["name"] == "Urban Company Limited"


def test_available_exchanges(client, requests_mock):
    requests_mock.get(
        BASE + "available-exchanges",
        json=[
            {
                "exchange": "AMEX",
                "name": "New York Stock Exchange Arca",
                "countryName": "United States of America",
                "countryCode": "US",
                "symbolSuffix": "N/A",
                "delay": "Real-time",
            }
        ],
    )
    result = client.available_exchanges(extended=False)
    assert result[0]["exchange"] == "AMEX"
    assert requests_mock.last_request.qs["extended"] == ["false"]


def test_available_sectors(client, requests_mock):
    requests_mock.get(BASE + "available-sectors", json=[{"sector": "Basic Materials"}])
    result = client.available_sectors()
    assert result[0]["sector"] == "Basic Materials"


def test_available_industries(client, requests_mock):
    requests_mock.get(BASE + "available-industries", json=[{"industry": "Steel"}])
    result = client.available_industries()
    assert result[0]["industry"] == "Steel"


def test_available_countries(client, requests_mock):
    requests_mock.get(BASE + "available-countries", json=[{"country": "FK"}])
    result = client.available_countries()
    assert result[0]["country"] == "FK"
