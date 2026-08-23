"""TypedDicts for ``client.earnings_transcript`` response shapes (REWRITE_ARCHITECTURE.md §6, ``client.earnings_transcript``).

Split out of the former single ``types.py`` for size — see
``fmpsdk/types/__init__.py`` for the shared conventions (naming,
when shapes are/aren't reused, the functional-TypedDict-form cases)
and the re-export barrel that keeps ``from fmpsdk.types import X``
working unchanged for every caller.
"""

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
    """Primary group `client.earnings_transcript`; cross-listed into
    `client.directory` per §4.3 (FMP documents this path under both
    "Directory" and "EarningsTranscript")."""

    symbol: str
    companyName: str
    noOfTranscripts: str
