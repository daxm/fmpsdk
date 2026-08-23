"""Live tests for client.analyst against the real FMP API. One fixed
cheap call per method, per the rewrite's live-testing discipline.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.live


def test_analyst_estimates(live_client):
    result = live_client.analyst_estimates(symbol="AAPL", period="annual")
    assert len(result) > 0
    assert result[0]["symbol"] == "AAPL"


def test_ratings_snapshot(live_client):
    result = live_client.ratings_snapshot(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"


def test_ratings_historical(live_client):
    result = live_client.ratings_historical(symbol="AAPL", limit=1)
    assert result[0]["symbol"] == "AAPL"


def test_price_target_summary(live_client):
    result = live_client.price_target_summary(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"


def test_price_target_consensus(live_client):
    result = live_client.price_target_consensus(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"


def test_grades(live_client):
    result = live_client.grades(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"


def test_grades_historical(live_client):
    result = live_client.grades_historical(symbol="AAPL", limit=10)
    assert result[0]["symbol"] == "AAPL"


def test_grades_consensus(live_client):
    result = live_client.grades_consensus(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"
