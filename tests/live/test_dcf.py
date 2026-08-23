"""Live tests for client.dcf against the real FMP API. One fixed cheap
call per method, per the rewrite's live-testing discipline.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.live


def test_discounted_cash_flow(live_client):
    result = live_client.discounted_cash_flow(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"


def test_levered_discounted_cash_flow(live_client):
    result = live_client.levered_discounted_cash_flow(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"


def test_custom_discounted_cash_flow(live_client):
    result = live_client.custom_discounted_cash_flow(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"


def test_custom_levered_discounted_cash_flow(live_client):
    result = live_client.custom_levered_discounted_cash_flow(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"
