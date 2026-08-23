"""Response shapes returned by ``client.esg`` methods."""

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
