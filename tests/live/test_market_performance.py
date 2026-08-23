"""Live tests for client.market_performance against the real FMP API.
All 11 methods, one fixed cheap call each per the workflow's
one-test-case rule.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.live

_DATE = "2026-08-21"  # most recent trading day as of writing
_SECTOR = "Technology"
_INDUSTRY = "Semiconductors"
_EXCHANGE = "NASDAQ"


def test_biggest_gainers(live_client):
    result = live_client.biggest_gainers()
    assert len(result) > 0
    assert "symbol" in result[0]


def test_biggest_losers(live_client):
    result = live_client.biggest_losers()
    assert len(result) > 0
    assert "symbol" in result[0]


def test_most_actives(live_client):
    result = live_client.most_actives()
    assert len(result) > 0
    assert "symbol" in result[0]


def test_sector_performance_snapshot(live_client):
    result = live_client.sector_performance_snapshot(date=_DATE)
    assert len(result) > 0


def test_industry_performance_snapshot(live_client):
    result = live_client.industry_performance_snapshot(date=_DATE)
    assert len(result) > 0


def test_historical_sector_performance(live_client):
    result = live_client.historical_sector_performance(
        sector=_SECTOR, exchange=_EXCHANGE
    )
    assert len(result) > 0


def test_historical_industry_performance(live_client):
    result = live_client.historical_industry_performance(
        industry=_INDUSTRY, exchange=_EXCHANGE
    )
    assert len(result) > 0


def test_sector_pe_snapshot(live_client):
    result = live_client.sector_pe_snapshot(date=_DATE)
    assert len(result) > 0


def test_industry_pe_snapshot(live_client):
    result = live_client.industry_pe_snapshot(date=_DATE)
    assert len(result) > 0


def test_historical_sector_pe(live_client):
    result = live_client.historical_sector_pe(sector=_SECTOR, exchange=_EXCHANGE)
    assert len(result) > 0


def test_historical_industry_pe(live_client):
    result = live_client.historical_industry_pe(industry=_INDUSTRY, exchange=_EXCHANGE)
    assert len(result) > 0
