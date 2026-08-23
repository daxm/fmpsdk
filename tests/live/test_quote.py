"""Live tests for client.quote against the real FMP API. The 5 single-
symbol methods are free-tier reachable; all 11 `batch_*` methods 402 on
the free tier — confirmed live 2026-08-23, see
`tests/ultimate/test_quote.py`. A clean split along §7.6's own
singular/plural distinction.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.live


def test_quote(live_client):
    result = live_client.quote.quote(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"


def test_quote_short(live_client):
    result = live_client.quote_short(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"


def test_aftermarket_quote(live_client):
    result = live_client.aftermarket_quote(symbol="AAPL")
    assert isinstance(result, list)


def test_aftermarket_trade(live_client):
    result = live_client.aftermarket_trade(symbol="AAPL")
    assert isinstance(result, list)


def test_stock_price_change(live_client):
    result = live_client.stock_price_change(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"
