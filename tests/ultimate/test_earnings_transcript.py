"""Ultimate-tier (Bucket 2) live tests for client.earnings_transcript.

Confirms the workflow doc's original pricing-tier audit, which already
named Earnings Transcripts as FMP-Ultimate-gated: all 4 methods 402 on
the free tier, confirmed live 2026-08-23. `earnings_transcript_list` is
cross-listed into `client.directory` (§4.3), which is itself fully
gated (see `tests/ultimate/test_directory.py`) — consistent with this
result. Skipped by default; run for real only during a
deliberately-timed FMP Ultimate month, per the rewrite workflow.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.ultimate


def test_earning_call_transcript(live_client):
    result = live_client.earning_call_transcript(
        symbol="AAPL", year="2026", quarter="3"
    )
    assert isinstance(result, list)


def test_earning_call_transcript_dates(live_client):
    result = live_client.earning_call_transcript_dates(symbol="AAPL")
    assert isinstance(result, list)


def test_earning_call_transcript_latest(live_client):
    result = live_client.earning_call_transcript_latest(limit=1)
    assert isinstance(result, list)


def test_earnings_transcript_list(live_client):
    result = live_client.earnings_transcript_list()
    assert isinstance(result, list)
