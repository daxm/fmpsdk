"""Live tests for client.commitment_of_traders against the real FMP API.

All methods below were confirmed on 2026-08-23 to require at least an FMP
Premium-tier key (they 402 on free and Starter) -- moved here from
tests/ultimate/test_commitment_of_traders.py once Dax upgraded from Starter to Premium.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.live


def test_commitment_of_traders_report(live_client):
    result = live_client.commitment_of_traders_report(symbol="NG")
    assert len(result) > 0
    assert "symbol" in result[0]


def test_commitment_of_traders_analysis(live_client):
    result = live_client.commitment_of_traders_analysis(symbol="NG")
    assert len(result) > 0
    assert "symbol" in result[0]


def test_commitment_of_traders_list(live_client):
    result = live_client.commitment_of_traders_list()
    assert len(result) > 0
    assert "symbol" in result[0]
