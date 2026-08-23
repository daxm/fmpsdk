"""Live tests for client.funds against the real FMP API.

All methods below were confirmed on 2026-08-23 to require at least an FMP
Starter-tier key (they 402 on the free tier) -- moved here from
tests/ultimate/test_funds.py once Dax upgraded from Free to Starter.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.live


def test_etf_country_weightings(live_client):
    result = live_client.etf_country_weightings(symbol="SPY")
    assert len(result) > 0
    assert "country" in result[0]


def test_etf_info(live_client):
    result = live_client.etf_info(symbol="SPY")
    assert result[0]["symbol"] == "SPY"


def test_etf_sector_weightings(live_client):
    result = live_client.etf_sector_weightings(symbol="SPY")
    assert len(result) > 0
    assert "sector" in result[0]
