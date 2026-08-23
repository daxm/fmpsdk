"""Ultimate-tier (Bucket 2) live tests for client.bulk.

Confirms the workflow doc's original pricing-tier audit, which already
named most Bulk as FMP-Ultimate-gated: all 18 methods 402 on the free
tier, confirmed live 2026-08-23 — the whole group, not a subset.
Skipped by default; run for real only during a deliberately-timed FMP
Ultimate month, per the rewrite workflow.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.ultimate


def test_profile_bulk(live_client):
    result = live_client.profile_bulk(part="0")
    assert isinstance(result, list)


def test_rating_bulk(live_client):
    result = live_client.rating_bulk()
    assert isinstance(result, list)


def test_dcf_bulk(live_client):
    result = live_client.dcf_bulk()
    assert isinstance(result, list)


def test_scores_bulk(live_client):
    result = live_client.scores_bulk()
    assert isinstance(result, list)


def test_price_target_summary_bulk(live_client):
    result = live_client.price_target_summary_bulk()
    assert isinstance(result, list)


def test_etf_holder_bulk(live_client):
    result = live_client.etf_holder_bulk(part="1")
    assert isinstance(result, list)


def test_upgrades_downgrades_consensus_bulk(live_client):
    result = live_client.upgrades_downgrades_consensus_bulk()
    assert isinstance(result, list)


def test_key_metrics_ttm_bulk(live_client):
    result = live_client.key_metrics_ttm_bulk()
    assert isinstance(result, list)


def test_ratios_ttm_bulk(live_client):
    result = live_client.ratios_ttm_bulk()
    assert isinstance(result, list)


def test_peers_bulk(live_client):
    result = live_client.peers_bulk()
    assert isinstance(result, list)


def test_earnings_surprises_bulk(live_client):
    result = live_client.earnings_surprises_bulk(year="2025")
    assert isinstance(result, list)


def test_income_statement_bulk(live_client):
    result = live_client.income_statement_bulk(year="2025", period="FY")
    assert isinstance(result, list)


def test_income_statement_growth_bulk(live_client):
    result = live_client.income_statement_growth_bulk(year="2025", period="FY")
    assert isinstance(result, list)


def test_balance_sheet_statement_bulk(live_client):
    result = live_client.balance_sheet_statement_bulk(year="2025", period="FY")
    assert isinstance(result, list)


def test_balance_sheet_statement_growth_bulk(live_client):
    result = live_client.balance_sheet_statement_growth_bulk(year="2025", period="FY")
    assert isinstance(result, list)


def test_cash_flow_statement_bulk(live_client):
    result = live_client.cash_flow_statement_bulk(year="2025", period="FY")
    assert isinstance(result, list)


def test_cash_flow_statement_growth_bulk(live_client):
    result = live_client.cash_flow_statement_growth_bulk(year="2025", period="FY")
    assert isinstance(result, list)


def test_eod_bulk(live_client):
    result = live_client.eod_bulk(date="2026-08-20")
    assert isinstance(result, list)
