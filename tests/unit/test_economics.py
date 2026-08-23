"""Mocked unit tests for client.economics — mirrors fmpsdk/endpoints/economics.py."""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.unit

BASE = "https://financialmodelingprep.com/stable/"


def test_treasury_rates(client, requests_mock):
    requests_mock.get(
        BASE + "treasury-rates",
        json=[
            {
                "date": "2026-07-29",
                "month1": 3.73,
                "month2": 3.83,
                "month3": 3.83,
                "month6": 3.97,
                "year1": 4.04,
                "year2": 4.22,
                "year3": 4.29,
                "year5": 4.37,
                "year7": 4.51,
                "year10": 4.67,
                "year20": 5.21,
                "year30": 5.2,
            }
        ],
    )
    result = client.treasury_rates(from_="2026-01-27", to="2026-04-27")
    assert result[0]["year10"] == 4.67
    sent = requests_mock.last_request.qs
    assert sent["from"] == ["2026-01-27"]
    assert sent["to"] == ["2026-04-27"]


def test_treasury_rates_omits_unset_optional_params(client, requests_mock):
    requests_mock.get(BASE + "treasury-rates", json=[])
    client.treasury_rates()
    assert requests_mock.last_request.qs == {}


def test_economic_indicators(client, requests_mock):
    requests_mock.get(
        BASE + "economic-indicators", json=[{"name": "GDP", "date": "2025-10-01", "value": 31422.526}]
    )
    result = client.economic_indicators(name="GDP", from_="2025-04-27", to="2026-04-27")
    assert result[0]["value"] == 31422.526
    assert requests_mock.last_request.qs["name"] == ["gdp"]


def test_economic_calendar(client, requests_mock):
    requests_mock.get(
        BASE + "economic-calendar",
        json=[
            {
                "date": "2026-07-29 03:30:00",
                "country": "SG",
                "event": "Import Prices YoY (Jun)",
                "currency": "SGD",
                "previous": 18.5,
                "estimate": 21,
                "actual": 13.6,
                "change": -4.9,
                "impact": "Low",
                "changePercentage": -26.486,
                "unit": "%",
            }
        ],
    )
    result = client.economic_calendar(country="US", from_="2026-01-27", to="2026-04-27")
    assert result[0]["impact"] == "Low"
    assert requests_mock.last_request.qs["country"] == ["us"]


def test_market_risk_premium(client, requests_mock):
    requests_mock.get(
        BASE + "market-risk-premium",
        json=[
            {
                "country": "Zimbabwe",
                "continent": "Africa",
                "countryRiskPremium": 11.66,
                "totalEquityRiskPremium": 15.89,
            }
        ],
    )
    result = client.market_risk_premium()
    assert result[0]["country"] == "Zimbabwe"
    assert requests_mock.last_request.qs == {}
