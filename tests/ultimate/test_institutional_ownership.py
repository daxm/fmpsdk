"""Ultimate-tier (Bucket 2) live tests for client.institutional_ownership.

Confirms the workflow doc's original pricing-tier audit, which already
named "granular Form 13F" as FMP-Ultimate-gated: all 8 methods 402 on the
free tier. Skipped by default (`-m "not ultimate"` / excluded unless
explicitly selected); run for real only during a deliberately-timed FMP
Ultimate month, per the rewrite workflow.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.ultimate

# Filer's CIK (Berkshire Hathaway), not an issuer's — matches
# REWRITE_ARCHITECTURE.md's own doc examples for these filer-scoped
# endpoints.
BERKSHIRE_CIK = "0001067983"


def test_institutional_ownership_latest(live_client):
    result = live_client.institutional_ownership_latest(page=0, limit=10)
    assert len(result) > 0
    assert "cik" in result[0]


def test_institutional_ownership_extract(live_client):
    result = live_client.institutional_ownership_extract(
        cik=BERKSHIRE_CIK, year="2023", quarter="3"
    )
    assert len(result) > 0
    assert "symbol" in result[0]


def test_institutional_ownership_dates(live_client):
    result = live_client.institutional_ownership_dates(cik=BERKSHIRE_CIK)
    assert len(result) > 0
    assert "quarter" in result[0]


def test_institutional_ownership_extract_analytics_holder(live_client):
    result = live_client.institutional_ownership_extract_analytics_holder(
        symbol="AAPL", year="2023", quarter="3"
    )
    assert len(result) > 0
    assert "investorName" in result[0]


def test_institutional_ownership_holder_performance_summary(live_client):
    result = live_client.institutional_ownership_holder_performance_summary(
        cik=BERKSHIRE_CIK
    )
    assert len(result) > 0
    assert "investorName" in result[0]


def test_institutional_ownership_holder_industry_breakdown(live_client):
    result = live_client.institutional_ownership_holder_industry_breakdown(
        cik=BERKSHIRE_CIK, year="2023", quarter="3"
    )
    assert len(result) > 0
    assert "industryTitle" in result[0]


def test_institutional_ownership_symbol_positions_summary(live_client):
    result = live_client.institutional_ownership_symbol_positions_summary(
        symbol="AAPL", year="2023", quarter="3"
    )
    assert len(result) > 0
    assert result[0]["symbol"] == "AAPL"


def test_institutional_ownership_industry_summary(live_client):
    result = live_client.institutional_ownership_industry_summary(
        year="2023", quarter="3"
    )
    assert len(result) > 0
    assert "industryTitle" in result[0]
