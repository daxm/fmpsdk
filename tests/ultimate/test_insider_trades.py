"""Ultimate-tier tests for client.insider_trades — 4 of the group's 6
methods 402 on the free tier (confirmed live 2026-08-23), despite no
Bucket 2 flag in REWRITE_ARCHITECTURE.md §3.5. `insider_trading_latest`
and `insider_trading_transaction_type` work free-tier — see
`tests/live/test_insider_trades.py`. Skipped until the one-month FMP
Ultimate verification pass.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.ultimate


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
