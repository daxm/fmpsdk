"""Mocked unit tests for client.tipranks — mirrors
fmpsdk/endpoints/tipranks.py.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.unit

BASE = "https://financialmodelingprep.com/stable/"

_RATING_ROW = {
    "symbol": "AAPL",
    "date": "2026-08-15",
    "recommendationDate": "2026-08-15",
    "expertUID": "abc123",
    "analystName": "Jane Analyst",
    "firmName": "Morgan Stanley",
    "recommendation": "Buy",
    "analystAction": "maintained",
    "articleTitle": "Apple: Buy rating reiterated",
    "articleSite": "example.com",
    "priceTarget": 250.0,
    "priceTargetCurrency": "USD",
    "url": "https://example.com/article",
}

_PIT_ROW = {
    "symbol": "AAPL",
    "date": "2026-08-15",
    "expertUID": "abc123",
    "analystName": "Jane Analyst",
    "stockSuccessRate": 0.72,
    "firmName": "Morgan Stanley",
    "lastRecommendation": "Buy",
    "lastRecommendationDate": "2026-08-15",
    "articleTitle": "Apple: Buy rating reiterated",
    "articleSite": "example.com",
    "priceTarget": 250.0,
    "priceTargetCurrency": "USD",
    "url": "https://example.com/article",
    "lastAnalystAction": "maintained",
    "stockReturn": 0.1,
    "beatTarget": True,
}

_SUMMARY_BREAKDOWNS = {
    "recommendations": {"buy": 20, "hold": 5, "sell": 1},
    "analystAction": {
        "initiated": 1,
        "maintained": 15,
        "upgraded": 3,
        "downgraded": 1,
        "reiterated": 5,
        "resumed": 1,
    },
}


def test_tipranks_search(client, requests_mock):
    requests_mock.get(BASE + "tipranks-search", json=[_RATING_ROW])
    result = client.tipranks_search(symbol="AAPL")
    assert result[0]["recommendation"] == "Buy"
    assert requests_mock.last_request.qs["symbol"] == ["aapl"]


def test_tipranks_pit_symbol(client, requests_mock):
    requests_mock.get(BASE + "tipranks-pit-symbol", json=[_PIT_ROW])
    result = client.tipranks_pit_symbol(symbol="AAPL")
    assert result[0]["lastRecommendation"] == "Buy"
    assert requests_mock.last_request.qs["symbol"] == ["aapl"]


def test_tipranks_pit_analyst(client, requests_mock):
    requests_mock.get(BASE + "tipranks-pit-analyst", json=[_PIT_ROW])
    result = client.tipranks_pit_analyst(analyst_name="Jane Analyst")
    assert result[0]["analystName"] == "Jane Analyst"
    assert requests_mock.last_request.qs["analystname"] == ["jane analyst"]


def test_tipranks_symbol_summary(client, requests_mock):
    requests_mock.get(
        BASE + "tipranks-symbol-summary",
        json=[
            {
                "symbol": "AAPL",
                "from": "2025-08-15",
                "to": "2026-08-15",
                "totalRecommendations": 26,
                "distinctSymbols": 1,
                "distinctAnalysts": 20,
                "validPriceTargets": 24,
                "comparedPriceTargets": 24,
                "beats": 15,
                "misses": 9,
                "averageReturn": 0.08,
                "topReturn": 0.3,
                "worstReturn": -0.05,
                **_SUMMARY_BREAKDOWNS,
            }
        ],
    )
    result = client.tipranks_symbol_summary(symbol="AAPL")
    assert result[0]["totalRecommendations"] == 26
    assert requests_mock.last_request.qs["symbol"] == ["aapl"]


def test_tipranks_analyst_summary(client, requests_mock):
    requests_mock.get(
        BASE + "tipranks-analyst-summary",
        json=[
            {
                "expertUID": "abc123",
                "from": "2025-08-15",
                "to": "2026-08-15",
                "totalRecommendations": 40,
                "distinctSymbols": 30,
                "distinctAnalysts": 1,
                "validPriceTargets": 38,
                "comparedPriceTargets": 38,
                "beats": 25,
                "misses": 13,
                "averageReturn": 0.12,
                "topReturn": 0.5,
                "worstReturn": -0.1,
                **_SUMMARY_BREAKDOWNS,
            }
        ],
    )
    result = client.tipranks_analyst_summary(expert_uid="abc123")
    assert result[0]["distinctSymbols"] == 30
    assert requests_mock.last_request.qs["expertuid"] == ["abc123"]


def test_tipranks_firm_summary(client, requests_mock):
    requests_mock.get(
        BASE + "tipranks-firm-summary",
        json=[
            {
                "firmName": "Morgan Stanley",
                "from": "2025-08-15",
                "to": "2026-08-15",
                "totalRecommendations": 500,
                "distinctSymbols": 300,
                "distinctAnalysts": 25,
                "validPriceTargets": 480,
                "comparedPriceTargets": 480,
                "beats": 300,
                "misses": 180,
                "averageReturn": 0.09,
                "topReturn": 0.6,
                "worstReturn": -0.2,
                **_SUMMARY_BREAKDOWNS,
            }
        ],
    )
    result = client.tipranks_firm_summary(firm_name="Morgan Stanley")
    assert result[0]["totalRecommendations"] == 500
    assert requests_mock.last_request.qs["firmname"] == ["morgan stanley"]


def test_tipranks_analysts(client, requests_mock):
    requests_mock.get(
        BASE + "tipranks-analysts",
        json=[
            {
                "expertUID": "abc123",
                "analystName": "Jane Analyst",
                "firmName": "Morgan Stanley",
                "successRate": 0.72,
                "excessReturn": 0.05,
                "totalRecommendations": 500,
                "goodRecommendations": 360,
                "analystRank": 15,
                "numOfStars": 5,
            }
        ],
    )
    result = client.tipranks_analysts(firm_name="Morgan Stanley")
    assert result[0]["numOfStars"] == 5
    assert requests_mock.last_request.qs["firmname"] == ["morgan stanley"]
