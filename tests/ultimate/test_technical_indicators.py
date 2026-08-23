"""Ultimate-tier tests for client.technical_indicators — all 9 methods
402 on the free tier (confirmed live 2026-08-23), despite no Bucket 2
flag in REWRITE_ARCHITECTURE.md §3.5. The whole group is gated, not a
subset — no `tests/live/test_technical_indicators.py` exists. Skipped
until the one-month FMP Ultimate verification pass.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.ultimate


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
