"""Ultimate-tier (Bucket 2) live tests for client.quote.

All 11 `batch_*` methods 402 on the free tier, confirmed live
2026-08-23 — the 5 single-symbol methods are free-tier reachable (see
`tests/live/test_quote.py`). A clean split along §7.6's own
singular/plural distinction: every plural `batch-*-quotes` (whole-
asset-class, no scope param) and even the singular-named
`batch-quote`/`batch-quote-short`/`batch-exchange-quote`/
`batch-aftermarket-*` are gated. Skipped by default; run for real only
during a deliberately-timed FMP Ultimate month, per the rewrite
workflow.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.ultimate


# NOTE (2026-08-23): re-tested against Dax's FMP Premium-tier key.
# 4 of this group's remaining methods now pass (moved to
# tests/live/test_quote.py); the 7 below still 402 on
# Premium -- gated at Ultimate, or Premium's own further sub-limits.


def test_batch_exchange_quote(live_client):
    result = live_client.batch_exchange_quote(exchange="NASDAQ")
    assert len(result) > 0


def test_batch_etf_quotes(live_client):
    result = live_client.batch_etf_quotes()
    assert len(result) > 0


def test_batch_mutualfund_quotes(live_client):
    result = live_client.batch_mutualfund_quotes()
    assert len(result) > 0


def test_batch_commodity_quotes(live_client):
    result = live_client.batch_commodity_quotes()
    assert len(result) > 0


def test_batch_crypto_quotes(live_client):
    result = live_client.batch_crypto_quotes()
    assert len(result) > 0


def test_batch_forex_quotes(live_client):
    result = live_client.batch_forex_quotes()
    assert len(result) > 0


def test_batch_index_quotes(live_client):
    result = live_client.batch_index_quotes()
    assert len(result) > 0
