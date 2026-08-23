"""Mocked unit tests for client.technical_indicators — mirrors
fmpsdk/endpoints/technical_indicators.py. All 9 methods share the same
`symbol`/`period_length`/`timeframe`/`from_`/`to` param set (built by the
private `_technical_indicator_params` helper) — one param-mapping test
covers that shared plumbing (`test_technical_indicators_sma`), the rest
just confirm each indicator's own value key round-trips.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.unit

BASE = "https://financialmodelingprep.com/stable/"

_OHLCV = {
    "date": "2026-08-21",
    "open": 226.5,
    "high": 229.1,
    "low": 225.9,
    "close": 228.3,
    "volume": 51234000,
}


def test_technical_indicators_sma(client, requests_mock):
    requests_mock.get(
        BASE + "technical-indicators/sma", json=[{**_OHLCV, "sma": 224.7}]
    )
    result = client.technical_indicators_sma(
        symbol="AAPL",
        period_length=10,
        timeframe="1day",
        from_="2026-01-01",
        to="2026-08-21",
    )
    assert result[0]["sma"] == 224.7
    sent = requests_mock.last_request.qs
    assert sent["symbol"] == ["aapl"]
    assert sent["periodlength"] == ["10"]
    assert sent["timeframe"] == ["1day"]
    assert sent["from"] == ["2026-01-01"]
    assert sent["to"] == ["2026-08-21"]


def test_technical_indicators_sma_omits_unset_optional_params(client, requests_mock):
    requests_mock.get(BASE + "technical-indicators/sma", json=[])
    client.technical_indicators_sma(symbol="AAPL", period_length=10, timeframe="1day")
    sent = requests_mock.last_request.qs
    assert "from" not in sent
    assert "to" not in sent


def test_technical_indicators_ema(client, requests_mock):
    requests_mock.get(
        BASE + "technical-indicators/ema", json=[{**_OHLCV, "ema": 225.1}]
    )
    result = client.technical_indicators_ema(
        symbol="AAPL", period_length=10, timeframe="1day"
    )
    assert result[0]["ema"] == 225.1


def test_technical_indicators_wma(client, requests_mock):
    requests_mock.get(
        BASE + "technical-indicators/wma", json=[{**_OHLCV, "wma": 225.6}]
    )
    result = client.technical_indicators_wma(
        symbol="AAPL", period_length=10, timeframe="1day"
    )
    assert result[0]["wma"] == 225.6


def test_technical_indicators_dema(client, requests_mock):
    requests_mock.get(
        BASE + "technical-indicators/dema", json=[{**_OHLCV, "dema": 225.9}]
    )
    result = client.technical_indicators_dema(
        symbol="AAPL", period_length=10, timeframe="1day"
    )
    assert result[0]["dema"] == 225.9


def test_technical_indicators_tema(client, requests_mock):
    requests_mock.get(
        BASE + "technical-indicators/tema", json=[{**_OHLCV, "tema": 226.2}]
    )
    result = client.technical_indicators_tema(
        symbol="AAPL", period_length=10, timeframe="1day"
    )
    assert result[0]["tema"] == 226.2


def test_technical_indicators_rsi(client, requests_mock):
    requests_mock.get(BASE + "technical-indicators/rsi", json=[{**_OHLCV, "rsi": 58.4}])
    result = client.technical_indicators_rsi(
        symbol="AAPL", period_length=14, timeframe="1day"
    )
    assert result[0]["rsi"] == 58.4


def test_technical_indicators_standarddeviation(client, requests_mock):
    requests_mock.get(
        BASE + "technical-indicators/standarddeviation",
        json=[{**_OHLCV, "standardDeviation": 3.21}],
    )
    result = client.technical_indicators_standarddeviation(
        symbol="AAPL", period_length=10, timeframe="1day"
    )
    assert result[0]["standardDeviation"] == 3.21


def test_technical_indicators_williams(client, requests_mock):
    requests_mock.get(
        BASE + "technical-indicators/williams", json=[{**_OHLCV, "williams": -34.2}]
    )
    result = client.technical_indicators_williams(
        symbol="AAPL", period_length=14, timeframe="1day"
    )
    assert result[0]["williams"] == -34.2


def test_technical_indicators_adx(client, requests_mock):
    requests_mock.get(BASE + "technical-indicators/adx", json=[{**_OHLCV, "adx": 21.6}])
    result = client.technical_indicators_adx(
        symbol="AAPL", period_length=14, timeframe="1day"
    )
    assert result[0]["adx"] == 21.6
