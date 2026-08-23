"""Ultimate-tier (Bucket 2) live tests for client.congress.

Every symbol/id/name-scoped method 402s on the free tier, confirmed
live 2026-08-23 — only the parameterless `house_latest`/`senate_latest`
listings are free-tier reachable (see `tests/live/test_congress.py`).
`senate_id` examples are real member IDs taken from
REWRITE_ARCHITECTURE.md's own documented examples (``"P000197"``), not
invented. Skipped by default; run for real only during a
deliberately-timed FMP Ultimate month, per the rewrite workflow.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.ultimate

_SENATE_ID = "P000197"


def test_house_trades(live_client):
    result = live_client.house_trades(symbol="AAPL", limit=1)
    assert isinstance(result, list)


def test_house_trades_by_id(live_client):
    result = live_client.house_trades_by_id(senate_id=_SENATE_ID, limit=1)
    assert isinstance(result, list)


def test_house_trades_by_name(live_client):
    result = live_client.house_trades_by_name(name="James")
    assert isinstance(result, list)


def test_senate_trades(live_client):
    result = live_client.senate_trades(symbol="AAPL", limit=1)
    assert isinstance(result, list)


def test_senate_trades_by_id(live_client):
    result = live_client.senate_trades_by_id(senate_id=_SENATE_ID, limit=1)
    assert isinstance(result, list)


def test_senate_trades_by_name(live_client):
    result = live_client.senate_trades_by_name(name="Jerry")
    assert isinstance(result, list)


def test_senate_profile(live_client):
    result = live_client.senate_profile(senate_id=_SENATE_ID)
    assert isinstance(result, list)


def test_senate_positions(live_client):
    result = live_client.senate_positions(senate_id=_SENATE_ID)
    assert isinstance(result, list)


def test_senate_net_worth(live_client):
    result = live_client.senate_net_worth(senate_id=_SENATE_ID)
    assert isinstance(result, list)


def test_senate_net_worth_aggregated(live_client):
    result = live_client.senate_net_worth_aggregated(senate_id=_SENATE_ID)
    assert isinstance(result, list)
