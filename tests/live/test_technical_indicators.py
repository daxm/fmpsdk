"""Live tests for client.technical_indicators against the real FMP API.

All methods below were confirmed on 2026-08-23 to require at least an FMP
Starter-tier key (they 402 on the free tier) -- moved here from
tests/ultimate/test_technical_indicators.py once Dax upgraded from Free to Starter.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.live


def test_technical_indicators_sma(live_client):
    result = live_client.technical_indicators_sma(
        symbol="AAPL", period_length=10, timeframe="1day"
    )
    assert len(result) > 0
    assert "sma" in result[0]


def test_technical_indicators_ema(live_client):
    result = live_client.technical_indicators_ema(
        symbol="AAPL", period_length=10, timeframe="1day"
    )
    assert len(result) > 0
    assert "ema" in result[0]


def test_technical_indicators_wma(live_client):
    result = live_client.technical_indicators_wma(
        symbol="AAPL", period_length=10, timeframe="1day"
    )
    assert len(result) > 0
    assert "wma" in result[0]


def test_technical_indicators_dema(live_client):
    result = live_client.technical_indicators_dema(
        symbol="AAPL", period_length=10, timeframe="1day"
    )
    assert len(result) > 0
    assert "dema" in result[0]


def test_technical_indicators_tema(live_client):
    result = live_client.technical_indicators_tema(
        symbol="AAPL", period_length=10, timeframe="1day"
    )
    assert len(result) > 0
    assert "tema" in result[0]


def test_technical_indicators_rsi(live_client):
    result = live_client.technical_indicators_rsi(
        symbol="AAPL", period_length=14, timeframe="1day"
    )
    assert len(result) > 0
    assert "rsi" in result[0]


def test_technical_indicators_standarddeviation(live_client):
    result = live_client.technical_indicators_standarddeviation(
        symbol="AAPL", period_length=10, timeframe="1day"
    )
    assert len(result) > 0
    assert "standardDeviation" in result[0]


def test_technical_indicators_williams(live_client):
    result = live_client.technical_indicators_williams(
        symbol="AAPL", period_length=14, timeframe="1day"
    )
    assert len(result) > 0
    assert "williams" in result[0]


def test_technical_indicators_adx(live_client):
    result = live_client.technical_indicators_adx(
        symbol="AAPL", period_length=14, timeframe="1day"
    )
    assert len(result) > 0
    assert "adx" in result[0]
