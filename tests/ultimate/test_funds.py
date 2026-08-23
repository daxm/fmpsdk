"""Ultimate-tier (Bucket 2) live tests for client.funds.

Discovered live, not predicted by REWRITE_ARCHITECTURE.md's group
directory (which lists no Bucket 2 flag on `funds`): all 9 methods 402 on
the free tier — the whole group. Skipped by default (`-m "not ultimate"`
/ excluded unless explicitly selected); run for real only during a
deliberately-timed FMP Ultimate month, per the rewrite workflow.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.ultimate


# NOTE (2026-08-23): re-tested against Dax's FMP Starter-tier key.
# 3 of this group's methods now pass (moved to
# tests/live/test_funds.py); the 6 below still 402 on
# Starter -- gated at Premium or Ultimate, exact tier not yet confirmed.


def test_etf_holdings(live_client):
    result = live_client.etf_holdings(symbol="SPY")
    assert len(result) > 0
    assert "asset" in result[0]


def test_etf_asset_exposure(live_client):
    result = live_client.etf_asset_exposure(symbol="AAPL")
    assert len(result) > 0
    assert "asset" in result[0]


def test_funds_disclosure(live_client):
    result = live_client.funds_disclosure(symbol="VWO", year="2023", quarter="4")
    assert len(result) > 0
    assert "symbol" in result[0]


def test_funds_disclosure_dates(live_client):
    result = live_client.funds_disclosure_dates(symbol="VWO")
    assert len(result) > 0
    assert "year" in result[0]


def test_funds_disclosure_holders_latest(live_client):
    result = live_client.funds_disclosure_holders_latest(symbol="AAPL")
    assert len(result) > 0
    assert "holder" in result[0]


def test_funds_disclosure_holders_search(live_client):
    result = live_client.funds_disclosure_holders_search(name="Vanguard")
    assert isinstance(result, list)
