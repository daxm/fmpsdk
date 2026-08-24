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


def test_batch_quote(live_client):
    result = live_client.batch_quote(symbols="AAPL,MSFT")
    assert len(result) > 0


def test_batch_quote_short(live_client):
    result = live_client.batch_quote_short(symbols="AAPL,MSFT")
    assert len(result) > 0


def test_batch_aftermarket_quote(live_client):
    result = live_client.batch_aftermarket_quote(symbols="AAPL,MSFT")
    assert isinstance(result, list)


def test_batch_aftermarket_trade(live_client):
    result = live_client.batch_aftermarket_trade(symbols="AAPL,MSFT")
    assert isinstance(result, list)


def test_batch_exchange_quote(live_client):
    result = live_client.batch_exchange_quote(exchange="NASDAQ")
    assert len(result) > 0


def test_batch_etf_quotes(live_client):
    result = live_client.batch_etf_quotes()
    assert len(result) > 0


def test_batch_mutualfund_quotes(live_client):
    result = live_client.batch_mutualfund_quotes()
    assert len(result) > 0


def test_batch_commodity_quotes(live_client):
    result = live_client.batch_commodity_quotes()
    assert len(result) > 0


def test_batch_crypto_quotes(live_client):
    result = live_client.batch_crypto_quotes()
    assert len(result) > 0


def test_batch_forex_quotes(live_client):
    result = live_client.batch_forex_quotes()
    assert len(result) > 0


def test_batch_index_quotes(live_client):
    result = live_client.batch_index_quotes()
    assert len(result) > 0
