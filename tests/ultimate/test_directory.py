"""Ultimate-tier (Bucket 2) live tests for client.directory.

Discovered live, not predicted by REWRITE_ARCHITECTURE.md's group
directory (which lists no Bucket 2 flag on `directory`): all 10 methods
402 on the free tier — the whole group, not a subset like `search`'s 4/7.
Skipped by default (`-m "not ultimate"` / excluded unless explicitly
selected); run for real only during a deliberately-timed FMP Ultimate
month, per the rewrite workflow.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.ultimate


def test_stock_list(live_client):
    result = live_client.stock_list()
    assert len(result) > 0
    assert "symbol" in result[0]


def test_financial_statement_symbol_list(live_client):
    result = live_client.financial_statement_symbol_list()
    assert len(result) > 0
    assert "symbol" in result[0]


def test_cik_list(live_client):
    result = live_client.cik_list(page=0, limit=10)
    assert len(result) > 0
    assert "cik" in result[0]


def test_symbol_change(live_client):
    result = live_client.symbol_change(limit=10)
    assert len(result) > 0
    assert "oldSymbol" in result[0]


def test_etf_list(live_client):
    result = live_client.etf_list()
    assert len(result) > 0
    assert "symbol" in result[0]


def test_actively_trading_list(live_client):
    result = live_client.actively_trading_list()
    assert len(result) > 0
    assert "symbol" in result[0]


def test_available_exchanges(live_client):
    result = live_client.available_exchanges()
    assert any(r["exchange"] == "NASDAQ" for r in result)


def test_available_sectors(live_client):
    result = live_client.available_sectors()
    assert len(result) > 0
    assert "sector" in result[0]


def test_available_industries(live_client):
    result = live_client.available_industries()
    assert len(result) > 0
    assert "industry" in result[0]


def test_available_countries(live_client):
    result = live_client.available_countries()
    assert len(result) > 0
    assert "country" in result[0]
