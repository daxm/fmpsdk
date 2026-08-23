"""Live tests for client.congress against the real FMP API.

`house_latest`/`senate_latest` (the parameterless "-latest" listings)
are free-tier reachable. The 6 symbol/id/name-scoped trade lookups
below were confirmed on 2026-08-23 to need at least an FMP Starter-tier
key (402 on the free tier) — moved here from
tests/ultimate/test_congress.py once Dax upgraded from Free to
Starter. The remaining 4 senate-profile-shaped methods
(senate_profile/senate_positions/senate_net_worth*) still 402 on
Starter — see tests/ultimate/test_congress.py.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.live

_SENATE_ID = "P000197"


def test_house_latest(live_client):
    result = live_client.house_latest(page=0, limit=1)
    assert len(result) > 0
    assert "symbol" in result[0]


def test_senate_latest(live_client):
    result = live_client.senate_latest(page=0, limit=1)
    assert len(result) > 0
    assert "symbol" in result[0]


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
