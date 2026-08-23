"""Live tests for client.insider_trades against the real FMP API. Only
`insider_trading_latest` and `insider_trading_transaction_type` are
free-tier reachable — the other 4 methods (`insider_trading_search`,
`insider_trading_reporting_name`, `insider_trading_statistics`,
`acquisition_of_beneficial_ownership`) all 402 on the free tier despite
no Bucket 2 flag in REWRITE_ARCHITECTURE.md §3.5, confirmed live
2026-08-23 — see `tests/ultimate/test_insider_trades.py`.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.live


def test_insider_trading_latest(live_client):
    result = live_client.insider_trading_latest(limit=1)
    assert len(result) > 0
    assert "symbol" in result[0]


def test_insider_trading_transaction_type(live_client):
    result = live_client.insider_trading_transaction_type()
    assert len(result) > 0
    assert "transactionType" in result[0]


def test_insider_trading_search(live_client):
    result = live_client.insider_trading_search(symbol="AAPL", limit=1)
    assert len(result) > 0
    assert result[0]["symbol"] == "AAPL"


def test_insider_trading_reporting_name(live_client):
    result = live_client.insider_trading_reporting_name(name="Zuckerberg")
    assert len(result) > 0
    assert "reportingCik" in result[0]


def test_insider_trading_statistics(live_client):
    result = live_client.insider_trading_statistics(symbol="AAPL")
    assert len(result) > 0
    assert result[0]["symbol"] == "AAPL"


def test_acquisition_of_beneficial_ownership(live_client):
    result = live_client.acquisition_of_beneficial_ownership(symbol="AAPL", limit=1)
    assert isinstance(result, list)
