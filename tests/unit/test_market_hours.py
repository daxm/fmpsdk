"""Mocked unit tests for client.market_hours — mirrors fmpsdk/endpoints/market_hours.py."""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.unit

BASE = "https://financialmodelingprep.com/stable/"

_HOURS_ROW = {
    "exchange": "NASDAQ",
    "name": "NASDAQ Global Market",
    "openingHour": "09:30 AM -04:00",
    "closingHour": "04:00 PM -04:00",
    "timezone": "America/New_York",
    "isMarketOpen": True,
}


def test_exchange_market_hours(client, requests_mock):
    requests_mock.get(BASE + "exchange-market-hours", json=[_HOURS_ROW])
    client.exchange_market_hours(exchange="NASDAQ", timestamp="1735689600")
    sent = requests_mock.last_request.qs
    assert sent["exchange"] == ["nasdaq"]
    assert sent["timestamp"] == ["1735689600"]


def test_exchange_market_hours_omits_unset_optional_param(client, requests_mock):
    requests_mock.get(BASE + "exchange-market-hours", json=[_HOURS_ROW])
    client.exchange_market_hours(exchange="NASDAQ")
    assert "timestamp" not in requests_mock.last_request.qs


def test_all_exchange_market_hours(client, requests_mock):
    requests_mock.get(BASE + "all-exchange-market-hours", json=[_HOURS_ROW])
    result = client.all_exchange_market_hours()
    assert result[0]["isMarketOpen"] is True
    assert requests_mock.last_request.qs == {}


def test_holidays_by_exchange(client, requests_mock):
    requests_mock.get(
        BASE + "holidays-by-exchange",
        json=[
            {
                "exchange": "NASDAQ",
                "date": "2026-01-01",
                "name": "New Year's Day",
                "isClosed": True,
                "adjOpenTime": None,
                "adjCloseTime": None,
            }
        ],
    )
    client.holidays_by_exchange(exchange="NASDAQ", from_="2026-01-01", to="2026-12-31")
    sent = requests_mock.last_request.qs
    assert sent["from"] == ["2026-01-01"]
    assert sent["to"] == ["2026-12-31"]
