"""Live tests for client.earnings_transcript against the real FMP API.

All methods below were confirmed on 2026-08-24 to require an FMP
Ultimate-tier key (they 402 on free, Starter, and Premium) -- moved
here from tests/ultimate/test_earnings_transcript.py once Dax upgraded from
Premium to Ultimate.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.live


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
