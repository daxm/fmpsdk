"""Mocked unit tests for client.market_performance — mirrors
fmpsdk/endpoints/market_performance.py.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.unit

BASE = "https://financialmodelingprep.com/stable/"

_MOVER_ROW = {
    "symbol": "SMCI",
    "price": 44.21,
    "name": "Super Micro Computer, Inc.",
    "change": 5.1,
    "changesPercentage": 13.03,
    "exchange": "NASDAQ",
}


def test_biggest_gainers(client, requests_mock):
    requests_mock.get(BASE + "biggest-gainers", json=[_MOVER_ROW])
    result = client.biggest_gainers()
    assert result[0]["symbol"] == "SMCI"
    assert requests_mock.last_request.qs == {}


def test_biggest_losers(client, requests_mock):
    requests_mock.get(BASE + "biggest-losers", json=[_MOVER_ROW])
    result = client.biggest_losers()
    assert result[0]["symbol"] == "SMCI"


def test_most_actives(client, requests_mock):
    requests_mock.get(BASE + "most-actives", json=[_MOVER_ROW])
    result = client.most_actives()
    assert result[0]["symbol"] == "SMCI"


def test_sector_performance_snapshot(client, requests_mock):
    requests_mock.get(
        BASE + "sector-performance-snapshot",
        json=[
            {
                "date": "2026-08-21",
                "sector": "Technology",
                "exchange": "NASDAQ",
                "averageChange": 1.42,
            }
        ],
    )
    client.sector_performance_snapshot(
        date="2026-08-21", exchange="NASDAQ", sector="Technology"
    )
    sent = requests_mock.last_request.qs
    assert sent["date"] == ["2026-08-21"]
    assert sent["exchange"] == ["nasdaq"]
    assert sent["sector"] == ["technology"]


def test_industry_performance_snapshot(client, requests_mock):
    requests_mock.get(
        BASE + "industry-performance-snapshot",
        json=[
            {
                "date": "2026-08-21",
                "industry": "Consumer Electronics",
                "exchange": "NASDAQ",
                "averageChange": 0.87,
            }
        ],
    )
    result = client.industry_performance_snapshot(date="2026-08-21")
    assert result[0]["industry"] == "Consumer Electronics"
    assert "exchange" not in requests_mock.last_request.qs


def test_historical_sector_performance(client, requests_mock):
    requests_mock.get(
        BASE + "historical-sector-performance",
        json=[
            {
                "date": "2026-08-21",
                "sector": "Technology",
                "exchange": "NASDAQ",
                "averageChange": 1.42,
            }
        ],
    )
    client.historical_sector_performance(
        sector="Technology", exchange="NASDAQ", from_="2026-01-01", to="2026-08-21"
    )
    sent = requests_mock.last_request.qs
    assert sent["from"] == ["2026-01-01"]
    assert sent["to"] == ["2026-08-21"]


def test_historical_industry_performance(client, requests_mock):
    requests_mock.get(
        BASE + "historical-industry-performance",
        json=[
            {
                "date": "2026-08-21",
                "industry": "Consumer Electronics",
                "exchange": "NASDAQ",
                "averageChange": 0.87,
            }
        ],
    )
    result = client.historical_industry_performance(industry="Consumer Electronics")
    assert result[0]["averageChange"] == 0.87


def test_sector_pe_snapshot(client, requests_mock):
    requests_mock.get(
        BASE + "sector-pe-snapshot",
        json=[
            {
                "date": "2026-08-21",
                "sector": "Technology",
                "exchange": "NASDAQ",
                "pe": 31.4,
            }
        ],
    )
    result = client.sector_pe_snapshot(date="2026-08-21", sector="Technology")
    assert result[0]["pe"] == 31.4


def test_industry_pe_snapshot(client, requests_mock):
    requests_mock.get(
        BASE + "industry-pe-snapshot",
        json=[
            {
                "date": "2026-08-21",
                "industry": "Consumer Electronics",
                "exchange": "NASDAQ",
                "pe": 28.9,
            }
        ],
    )
    result = client.industry_pe_snapshot(
        date="2026-08-21", industry="Consumer Electronics"
    )
    assert result[0]["pe"] == 28.9


def test_historical_sector_pe(client, requests_mock):
    requests_mock.get(
        BASE + "historical-sector-pe",
        json=[
            {
                "date": "2026-08-21",
                "sector": "Technology",
                "exchange": "NASDAQ",
                "pe": 31.4,
            }
        ],
    )
    client.historical_sector_pe(
        sector="Technology", from_="2026-01-01", to="2026-08-21"
    )
    sent = requests_mock.last_request.qs
    assert sent["sector"] == ["technology"]
    assert sent["from"] == ["2026-01-01"]


def test_historical_industry_pe(client, requests_mock):
    requests_mock.get(
        BASE + "historical-industry-pe",
        json=[
            {
                "date": "2026-08-21",
                "industry": "Consumer Electronics",
                "exchange": "NASDAQ",
                "pe": 28.9,
            }
        ],
    )
    result = client.historical_industry_pe(
        industry="Consumer Electronics", to="2026-08-21"
    )
    assert result[0]["pe"] == 28.9
    assert requests_mock.last_request.qs["to"] == ["2026-08-21"]
