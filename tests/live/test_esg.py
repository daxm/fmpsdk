"""Live tests for client.esg against the real FMP API.

All methods below were confirmed on 2026-08-24 to require an FMP
Ultimate-tier key (they 402 on free, Starter, and Premium) -- moved
here from tests/ultimate/test_esg.py once Dax upgraded from
Premium to Ultimate.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.live


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
