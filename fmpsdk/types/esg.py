"""Response shapes returned by ``client.esg`` methods."""

from __future__ import annotations

from typing import TypedDict

# --- client.esg ---------------------------------------------------------


class EsgDisclosuresResult(TypedDict):
    """One per-filing environmental/social/governance score set from an SEC disclosure. Returned by `esg_disclosures()`."""

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
    """Current ESG risk rating and industry rank for one company. Returned by `esg_ratings()`."""

    symbol: str
    cik: str
    companyName: str
    industry: str
    fiscalYear: int
    ESGRiskRating: str
    industryRank: str


class EsgBenchmarkResult(TypedDict):
    """Average ESG scores for one sector, for cross-company benchmarking. Returned by `esg_benchmark()`."""

    fiscalYear: int
    sector: str
    environmentalScore: float
    socialScore: float
    governanceScore: float
    ESGScore: float
