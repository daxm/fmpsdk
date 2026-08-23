"""Live tests for client.company against the real FMP API — the subset of
the group actually reachable on the free tier. One fixed cheap call per
method, per the rewrite's live-testing discipline.

mergers_acquisitions_latest, mergers_acquisitions_search, and
executive_compensation_benchmark 402 on the free tier — see
tests/ultimate/test_company.py.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.live


def test_profile(live_client):
    result = live_client.profile(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"


def test_profile_cik(live_client):
    result = live_client.profile_cik(cik="320193")
    assert result[0]["symbol"] == "AAPL"


def test_company_notes(live_client):
    result = live_client.company_notes(symbol="AAPL")
    assert isinstance(result, list)


def test_stock_peers(live_client):
    result = live_client.stock_peers(symbol="AAPL")
    assert len(result) > 0
    assert "symbol" in result[0]


def test_delisted_companies(live_client):
    result = live_client.delisted_companies(page=0, limit=10)
    assert len(result) > 0
    assert "symbol" in result[0]


def test_employee_count(live_client):
    result = live_client.employee_count(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"


def test_historical_employee_count(live_client):
    result = live_client.historical_employee_count(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"


def test_market_capitalization(live_client):
    result = live_client.market_capitalization(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"


def test_market_capitalization_batch(live_client):
    result = live_client.market_capitalization_batch(symbols="AAPL,MSFT")
    assert len(result) > 0


def test_historical_market_capitalization(live_client):
    result = live_client.historical_market_capitalization(symbol="AAPL", limit=10)
    assert result[0]["symbol"] == "AAPL"


def test_shares_float(live_client):
    result = live_client.shares_float(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"


def test_shares_float_all(live_client):
    result = live_client.shares_float_all(limit=10)
    assert len(result) > 0
    assert "symbol" in result[0]


def test_key_executives(live_client):
    result = live_client.key_executives(symbol="AAPL")
    assert len(result) > 0
    assert "name" in result[0]


def test_governance_executive_compensation(live_client):
    result = live_client.governance_executive_compensation(symbol="AAPL")
    assert isinstance(result, list)


def test_mergers_acquisitions_latest(live_client):
    result = live_client.mergers_acquisitions_latest(limit=10)
    assert len(result) > 0
    assert "symbol" in result[0]


def test_mergers_acquisitions_search(live_client):
    result = live_client.mergers_acquisitions_search(name="Apple")
    assert isinstance(result, list)


def test_executive_compensation_benchmark(live_client):
    result = live_client.executive_compensation_benchmark(year="2024")
    assert len(result) > 0
    assert "industryTitle" in result[0]
