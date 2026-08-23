"""Live tests for client.market_hours against the real FMP API. One
fixed cheap call per method.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.live


def test_exchange_market_hours(live_client):
    result = live_client.exchange_market_hours(exchange="NASDAQ")
    assert len(result) > 0
    assert result[0]["exchange"] == "NASDAQ"


def test_all_exchange_market_hours(live_client):
    result = live_client.all_exchange_market_hours()
    assert len(result) > 0
    assert "exchange" in result[0]


def test_holidays_by_exchange(live_client):
    result = live_client.holidays_by_exchange(
        exchange="NASDAQ", from_="2026-01-01", to="2026-12-31"
    )
    assert isinstance(result, list)
