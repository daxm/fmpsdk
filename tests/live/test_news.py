"""Live tests for client.news against the real FMP API. Only
`fmp_articles` is free-tier reachable — the other 9 methods (the whole
`NewsArticleResult`-shaped family: general/press-releases/stock/crypto/
forex, each with a "-latest" sibling) all 402 on the free tier, confirmed
live 2026-08-23 — see `tests/ultimate/test_news.py`.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.live


def test_fmp_articles(live_client):
    result = live_client.fmp_articles(page=0, limit=1)
    assert len(result) > 0
    assert "title" in result[0]


def test_news_crypto(live_client):
    result = live_client.news_crypto(symbols="BTCUSD", limit=1)
    assert isinstance(result, list)


def test_news_crypto_latest(live_client):
    result = live_client.news_crypto_latest(limit=1)
    assert len(result) > 0
    assert "title" in result[0]


def test_news_forex(live_client):
    result = live_client.news_forex(symbols="EURUSD", limit=1)
    assert isinstance(result, list)


def test_news_forex_latest(live_client):
    result = live_client.news_forex_latest(limit=1)
    assert len(result) > 0
    assert "title" in result[0]


def test_news_general_latest(live_client):
    result = live_client.news_general_latest(limit=1)
    assert len(result) > 0
    assert "publisher" in result[0]


def test_news_stock(live_client):
    result = live_client.news_stock(symbols="AAPL", limit=1)
    assert isinstance(result, list)


def test_news_stock_latest(live_client):
    result = live_client.news_stock_latest(limit=1)
    assert len(result) > 0
    assert "title" in result[0]
