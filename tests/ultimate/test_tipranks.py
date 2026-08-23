"""Ultimate-tier (Bucket 2) live tests for client.tipranks.

Confirms the workflow doc's treat-as-Ultimate-until-proven-otherwise
call: all 7 methods 402 on the free tier, confirmed live 2026-08-23 —
the whole group. Skipped by default; run for real only during a
deliberately-timed FMP Ultimate month, per the rewrite workflow.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.ultimate


def test_tipranks_search(live_client):
    result = live_client.tipranks_search(symbol="AAPL", limit=1)
    assert isinstance(result, list)


def test_tipranks_pit_symbol(live_client):
    result = live_client.tipranks_pit_symbol(symbol="AAPL", limit=1)
    assert isinstance(result, list)


def test_tipranks_pit_analyst(live_client):
    result = live_client.tipranks_pit_analyst(analyst_name="Jane Analyst", limit=1)
    assert isinstance(result, list)


def test_tipranks_symbol_summary(live_client):
    result = live_client.tipranks_symbol_summary(symbol="AAPL")
    assert isinstance(result, list)


def test_tipranks_analyst_summary(live_client):
    result = live_client.tipranks_analyst_summary(expert_uid="abc123")
    assert isinstance(result, list)


def test_tipranks_firm_summary(live_client):
    result = live_client.tipranks_firm_summary(firm_name="Morgan Stanley")
    assert isinstance(result, list)


def test_tipranks_analysts(live_client):
    result = live_client.tipranks_analysts(limit=1)
    assert isinstance(result, list)
