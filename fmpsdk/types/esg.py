"""TypedDicts for ``client.esg`` response shapes (REWRITE_ARCHITECTURE.md §6, ``client.esg``).

Split out of the former single ``types.py`` for size — see
``fmpsdk/types/__init__.py`` for the shared conventions (naming,
when shapes are/aren't reused, the functional-TypedDict-form cases)
and the re-export barrel that keeps ``from fmpsdk.types import X``
working unchanged for every caller.
"""

from __future__ import annotations

from typing import TypedDict

# --- client.esg ---------------------------------------------------------


class EsgDisclosuresResult(TypedDict):
    date: str
    acceptedDate: str
    symbol: str
    cik: str
    companyName: str
    formType: str
    environmentalScore: float
    socialScore: float
    governanceScore: float
    ESGScore: float
    url: str


class EsgRatingsResult(TypedDict):
    symbol: str
    cik: str
    companyName: str
    industry: str
    fiscalYear: int
    ESGRiskRating: str
    industryRank: str


class EsgBenchmarkResult(TypedDict):
    fiscalYear: int
    sector: str
    environmentalScore: float
    socialScore: float
    governanceScore: float
    ESGScore: float
