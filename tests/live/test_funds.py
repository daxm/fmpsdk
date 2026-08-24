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


def test_etf_holdings(live_client):
    result = live_client.etf_holdings(symbol="SPY")
    assert len(result) > 0
    assert "asset" in result[0]


def test_etf_asset_exposure(live_client):
    result = live_client.etf_asset_exposure(symbol="AAPL")
    assert len(result) > 0
    assert "asset" in result[0]


def test_funds_disclosure(live_client):
    result = live_client.funds_disclosure(symbol="VWO", year="2023", quarter="4")
    assert len(result) > 0
    assert "symbol" in result[0]


def test_funds_disclosure_dates(live_client):
    result = live_client.funds_disclosure_dates(symbol="VWO")
    assert len(result) > 0
    assert "year" in result[0]


def test_funds_disclosure_holders_latest(live_client):
    result = live_client.funds_disclosure_holders_latest(symbol="AAPL")
    assert len(result) > 0
    assert "holder" in result[0]


def test_funds_disclosure_holders_search(live_client):
    result = live_client.funds_disclosure_holders_search(name="Vanguard")
    assert isinstance(result, list)
