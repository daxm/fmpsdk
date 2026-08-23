"""Response shapes returned by ``client.earnings_transcript`` methods."""

from __future__ import annotations

from typing import TypedDict

# --- client.earnings_transcript ------------------------------------------------


class EarningCallTranscriptResult(TypedDict):
    """Full text of one earnings call for one fiscal quarter. Returned
    by `earning_call_transcript()`."""

    symbol: str
    period: str
    year: int
    date: str
    content: str


class EarningCallTranscriptDatesResult(TypedDict):
    """One fiscal year/quarter a company has an earnings-call transcript
    on file for. Returned by `earning_call_transcript_dates()`."""

    quarter: int
    fiscalYear: int
    date: str


class EarningCallTranscriptLatestResult(TypedDict):
    """One recent earnings-call transcript, across all companies.
    Returned by `earning_call_transcript_latest()`."""

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
