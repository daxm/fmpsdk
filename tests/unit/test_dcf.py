"""Mocked unit tests for client.dcf — mirrors fmpsdk/endpoints/dcf.py."""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.unit

BASE = "https://financialmodelingprep.com/stable/"


def test_discounted_cash_flow(client, requests_mock):
    requests_mock.get(
        BASE + "discounted-cash-flow",
        json=[{"symbol": "AAPL", "date": "2026-07-30", "dcf": 147.10881272667325, "Stock Price": 338.19}],
    )
    result = client.discounted_cash_flow(symbol="AAPL")
    assert result[0]["dcf"] == 147.10881272667325
    assert result[0]["Stock Price"] == 338.19


def test_levered_discounted_cash_flow(client, requests_mock):
    requests_mock.get(
        BASE + "levered-discounted-cash-flow",
        json=[{"symbol": "AAPL", "date": "2026-07-30", "dcf": 140.6429495133426, "Stock Price": 338.19}],
    )
    result = client.levered_discounted_cash_flow(symbol="AAPL")
    assert result[0]["dcf"] == 140.6429495133426


def test_custom_discounted_cash_flow(client, requests_mock):
    requests_mock.get(
        BASE + "custom-discounted-cash-flow",
        json=[
            {
                "year": "2030",
                "symbol": "AAPL",
                "revenue": 529528728806,
                "wacc": 9.42,
                "equityValuePerShare": 147.18,
            }
        ],
    )
    result = client.custom_discounted_cash_flow(
        symbol="AAPL",
        revenue_growth_pct=0.1094119804597946,
        tax_rate=0.14919579658453103,
        long_term_growth_rate=4,
        beta=1.244,
    )
    assert result[0]["equityValuePerShare"] == 147.18
    sent = requests_mock.last_request.qs
    assert sent["symbol"] == ["aapl"]
    assert sent["revenuegrowthpct"] == ["0.1094119804597946"]
    assert sent["taxrate"] == ["0.14919579658453103"]
    assert sent["longtermgrowthrate"] == ["4"]
    assert sent["beta"] == ["1.244"]
    # Unset overrides never hit the wire (§8.8 — no invented defaults).
    assert "ebitdapct" not in sent
    assert "costofdebt" not in sent


def test_custom_discounted_cash_flow_only_symbol_required(client, requests_mock):
    requests_mock.get(BASE + "custom-discounted-cash-flow", json=[])
    client.custom_discounted_cash_flow(symbol="AAPL")
    sent = requests_mock.last_request.qs
    assert sent["symbol"] == ["aapl"]
    assert len(sent) == 1


def test_custom_levered_discounted_cash_flow(client, requests_mock):
    requests_mock.get(
        BASE + "custom-levered-discounted-cash-flow",
        json=[
            {
                "year": "2030",
                "symbol": "AAPL",
                "revenue": 529528728806,
                "wacc": 9.42,
                "equityValuePerShare": 140.71,
                "operatingCashFlowPercentage": 29.06,
            }
        ],
    )
    result = client.custom_levered_discounted_cash_flow(
        symbol="AAPL", cost_of_debt=3.64, risk_free_rate=3.64
    )
    assert result[0]["equityValuePerShare"] == 140.71
    sent = requests_mock.last_request.qs
    assert sent["costofdebt"] == ["3.64"]
    assert sent["riskfreerate"] == ["3.64"]
