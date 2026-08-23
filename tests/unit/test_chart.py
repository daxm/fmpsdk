"""Mocked unit tests for client.chart — mirrors fmpsdk/endpoints/chart.py."""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.unit

BASE = "https://financialmodelingprep.com/stable/"


def test_historical_chart_builds_timeframe_into_path(client, requests_mock):
    requests_mock.get(
        BASE + "historical-chart/1min",
        json=[
            {
                "date": "2026-07-30 13:16:00",
                "open": 332.4,
                "low": 332.27499,
                "high": 332.48,
                "close": 332.47,
                "volume": 67660,
            }
        ],
    )
    result = client.historical_chart(
        symbol="AAPL", timeframe="1min", from_="2024-01-01", to="2024-03-01", nonadjusted=False, extended=False
    )
    assert result[0]["close"] == 332.47
    sent = requests_mock.last_request.qs
    assert sent["symbol"] == ["aapl"]
    assert sent["from"] == ["2024-01-01"]
    assert sent["nonadjusted"] == ["false"]
    assert sent["extended"] == ["false"]


def test_historical_chart_different_timeframe_different_path(client, requests_mock):
    requests_mock.get(BASE + "historical-chart/4hour", json=[])
    client.historical_chart(symbol="AAPL", timeframe="4hour")
    assert requests_mock.last_request.path == "/stable/historical-chart/4hour"


def test_historical_price_eod_light(client, requests_mock):
    requests_mock.get(
        BASE + "historical-price-eod/light",
        json=[{"symbol": "AAPL", "date": "2026-07-30", "price": 332.39, "volume": 29207295}],
    )
    result = client.historical_price_eod_light(symbol="AAPL", from_="2026-04-30", to="2026-07-30")
    assert result[0]["price"] == 332.39


def test_historical_price_eod_full(client, requests_mock):
    requests_mock.get(
        BASE + "historical-price-eod/full",
        json=[
            {
                "symbol": "AAPL",
                "date": "2026-07-30",
                "open": 333.13,
                "high": 334.48,
                "low": 329.59,
                "close": 332.39,
                "volume": 29207295,
                "change": -0.74,
                "changePercent": -0.2221355,
                "vwap": 332.15,
            }
        ],
    )
    result = client.historical_price_eod_full(symbol="AAPL")
    assert result[0]["vwap"] == 332.15


def test_historical_price_eod_non_split_adjusted(client, requests_mock):
    requests_mock.get(
        BASE + "historical-price-eod/non-split-adjusted",
        json=[
            {
                "symbol": "AAPL",
                "date": "2026-07-30",
                "adjOpen": 333.13,
                "adjHigh": 334.48,
                "adjLow": 329.59,
                "adjClose": 332.39,
                "volume": 29207295,
            }
        ],
    )
    result = client.historical_price_eod_non_split_adjusted(symbol="AAPL")
    assert result[0]["adjClose"] == 332.39


def test_historical_price_eod_dividend_adjusted(client, requests_mock):
    requests_mock.get(
        BASE + "historical-price-eod/dividend-adjusted",
        json=[
            {
                "symbol": "AAPL",
                "date": "2026-07-30",
                "adjOpen": 333.13,
                "adjHigh": 334.48,
                "adjLow": 329.59,
                "adjClose": 332.39,
                "volume": 29207295,
            }
        ],
    )
    result = client.historical_price_eod_dividend_adjusted(symbol="AAPL")
    assert result[0]["adjClose"] == 332.39
