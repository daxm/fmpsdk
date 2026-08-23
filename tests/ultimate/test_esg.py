"""Ultimate-tier (Bucket 2) live tests for client.esg.

Confirms the workflow doc's original pricing-tier audit, which already
named ESG as FMP-Ultimate-gated: all 3 methods 402 on the free tier.
Skipped by default (`-m "not ultimate"` / excluded unless explicitly
selected); run for real only during a deliberately-timed FMP Ultimate
month, per the rewrite workflow.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.ultimate


def test_esg_disclosures(live_client):
    result = live_client.esg_disclosures(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"


def test_esg_ratings(live_client):
    result = live_client.esg_ratings(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"


def test_esg_benchmark(live_client):
    result = live_client.esg_benchmark(year="2023")
    assert len(result) > 0
    assert "sector" in result[0]
