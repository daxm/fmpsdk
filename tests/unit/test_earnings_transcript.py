"""Mocked unit tests for client.earnings_transcript — mirrors
fmpsdk/endpoints/earnings_transcript.py.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.unit

BASE = "https://financialmodelingprep.com/stable/"


def test_earning_call_transcript(client, requests_mock):
    requests_mock.get(
        BASE + "earning-call-transcript",
        json=[
            {
                "symbol": "AAPL",
                "period": "Q3",
                "year": 2026,
                "date": "2026-07-31",
                "content": "Good afternoon...",
            }
        ],
    )
    result = client.earning_call_transcript(symbol="AAPL", year="2026", quarter="3")
    assert result[0]["period"] == "Q3"
    sent = requests_mock.last_request.qs
    assert sent["symbol"] == ["aapl"]
    assert sent["year"] == ["2026"]
    assert sent["quarter"] == ["3"]


def test_earning_call_transcript_dates(client, requests_mock):
    requests_mock.get(
        BASE + "earning-call-transcript-dates",
        json=[{"quarter": 3, "fiscalYear": 2026, "date": "2026-07-31"}],
    )
    result = client.earning_call_transcript_dates(symbol="AAPL")
    assert result[0]["fiscalYear"] == 2026


def test_earning_call_transcript_latest(client, requests_mock):
    requests_mock.get(
        BASE + "earning-call-transcript-latest",
        json=[
            {
                "symbol": "AAPL",
                "period": "Q3",
                "fiscalYear": 2026,
                "date": "2026-07-31",
            }
        ],
    )
    result = client.earning_call_transcript_latest(limit=10, page=0)
    assert result[0]["symbol"] == "AAPL"
    sent = requests_mock.last_request.qs
    assert sent["limit"] == ["10"]
    assert sent["page"] == ["0"]


def test_earnings_transcript_list(client, requests_mock):
    requests_mock.get(
        BASE + "earnings-transcript-list",
        json=[
            {"symbol": "AAPL", "companyName": "Apple Inc.", "noOfTranscripts": "180"}
        ],
    )
    result = client.earnings_transcript_list()
    assert result[0]["companyName"] == "Apple Inc."
    assert requests_mock.last_request.qs == {}
