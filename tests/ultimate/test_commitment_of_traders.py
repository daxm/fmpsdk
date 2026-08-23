"""Ultimate-tier (Bucket 2) live tests for client.commitment_of_traders.

Discovered live, not predicted by REWRITE_ARCHITECTURE.md's group
directory (which lists no Bucket 2 flag on `commitment_of_traders`): all
3 methods 402 on the free tier — the whole group. Skipped by default
(`-m "not ultimate"` / excluded unless explicitly selected); run for real
only during a deliberately-timed FMP Ultimate month, per the rewrite
workflow.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.ultimate


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
