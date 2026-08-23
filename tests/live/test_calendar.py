"""Live tests for client.calendar against the real FMP API — the subset of
the group actually reachable on the free tier. One fixed cheap call per
method, per the rewrite's live-testing discipline.

All 3 `ipos_*` methods 402 on the free tier — see tests/ultimate/test_calendar.py.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.live

FROM = "2026-08-01"
TO = "2026-08-23"


def test_dividends(live_client):
    result = live_client.dividends(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"


def test_dividends_calendar(live_client):
    result = live_client.dividends_calendar(from_=FROM, to=TO)
    assert len(result) > 0
    assert "symbol" in result[0]


def test_earnings(live_client):
    result = live_client.earnings(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"


def test_earnings_calendar(live_client):
    result = live_client.earnings_calendar(from_=FROM, to=TO)
    assert len(result) > 0
    assert "symbol" in result[0]


def test_splits(live_client):
    result = live_client.splits(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"


def test_splits_calendar(live_client):
    result = live_client.splits_calendar(from_=FROM, to=TO)
    assert isinstance(result, list)


def test_ipos_calendar(live_client):
    result = live_client.ipos_calendar(from_=FROM, to=TO)
    assert len(result) > 0
    assert "symbol" in result[0]


def test_ipos_disclosure(live_client):
    result = live_client.ipos_disclosure(from_=FROM, to=TO)
    assert len(result) > 0
    assert "symbol" in result[0]


def test_ipos_prospectus(live_client):
    result = live_client.ipos_prospectus(from_=FROM, to=TO)
    assert len(result) > 0
    assert "symbol" in result[0]
