"""Ultimate-tier tests for client.indexes — 6 of the group's 7 own
methods 402 on the free tier (confirmed live 2026-08-23), despite no
Bucket 2 flag in REWRITE_ARCHITECTURE.md §3.5. Only `index_list` works
free-tier — see `tests/live/test_indexes.py`. Skipped until the
one-month FMP Ultimate verification pass (see the rewrite workflow
notes); `pytest -m ultimate` still requires `FMP_API_KEY` to run for
real rather than skip.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.ultimate


def test_sp500_constituent(live_client):
    result = live_client.sp500_constituent()
    assert len(result) > 0
    assert "symbol" in result[0]


def test_nasdaq_constituent(live_client):
    result = live_client.nasdaq_constituent()
    assert len(result) > 0
    assert "symbol" in result[0]


def test_dowjones_constituent(live_client):
    result = live_client.dowjones_constituent()
    assert len(result) > 0
    assert "symbol" in result[0]


def test_historical_sp500_constituent(live_client):
    result = live_client.historical_sp500_constituent()
    assert len(result) > 0
    assert "symbol" in result[0]


def test_historical_nasdaq_constituent(live_client):
    result = live_client.historical_nasdaq_constituent()
    assert len(result) > 0
    assert "symbol" in result[0]


def test_historical_dowjones_constituent(live_client):
    result = live_client.historical_dowjones_constituent()
    assert len(result) > 0
    assert "symbol" in result[0]
