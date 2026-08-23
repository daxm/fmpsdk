"""Response shapes returned by ``client.earnings_transcript`` methods."""

from __future__ import annotations

from typing import TypedDict

# --- client.earnings_transcript ------------------------------------------------


class EarningCallTranscriptResult(TypedDict):
    symbol: str
    period: str
    year: int
    date: str
    content: str


class EarningCallTranscriptDatesResult(TypedDict):
    quarter: int
    fiscalYear: int
    date: str


class EarningCallTranscriptLatestResult(TypedDict):
    symbol: str
    period: str
    fiscalYear: int
    date: str


class EarningsTranscriptListResult(TypedDict):
    """Also reachable as `client.directory.earnings_transcript_list` —
    FMP documents this endpoint under both "Directory" and "Earnings
    Transcripts"."""

    symbol: str
    companyName: str
    noOfTranscripts: str
