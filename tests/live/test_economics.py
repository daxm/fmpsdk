"""Live tests for client.economics against the real FMP API — the subset
of the group actually reachable on the free tier. One fixed cheap call
per method, per the rewrite's live-testing discipline.

economic_calendar 402s on the free tier — see tests/ultimate/test_economics.py.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.live


def test_treasury_rates(live_client):
    result = live_client.treasury_rates()
    assert len(result) > 0
    assert "year10" in result[0]


def test_economic_indicators(live_client):
    result = live_client.economic_indicators(name="GDP")
    assert len(result) > 0
    assert result[0]["name"] == "GDP"


def test_market_risk_premium(live_client):
    result = live_client.market_risk_premium()
    assert len(result) > 0
    assert "country" in result[0]
