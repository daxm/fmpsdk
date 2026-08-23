"""Live tests for client.chart against the real FMP API — the subset of
the group actually reachable on the free tier. One fixed cheap call per
method, per the rewrite's live-testing discipline.

`historical_chart` (all 6 intraday timeframes) 402s on the free tier —
see tests/ultimate/test_chart.py.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.live


def test_historical_price_eod_light(live_client):
    result = live_client.historical_price_eod_light(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"


def test_historical_price_eod_full(live_client):
    result = live_client.historical_price_eod_full(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"


def test_historical_price_eod_non_split_adjusted(live_client):
    result = live_client.historical_price_eod_non_split_adjusted(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"


def test_historical_price_eod_dividend_adjusted(live_client):
    result = live_client.historical_price_eod_dividend_adjusted(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"
