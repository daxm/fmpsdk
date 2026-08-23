"""Live tests for client.directory against the real FMP API.

All methods below were confirmed on 2026-08-23 to require at least an FMP
Starter-tier key (they 402 on the free tier) -- moved here from
tests/ultimate/test_directory.py once Dax upgraded from Free to Starter.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.live


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
