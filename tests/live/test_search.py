"""Live tests for client.search against the real FMP API — the subset of
the group actually reachable on the free tier. One fixed cheap call per
method, per the rewrite's live-testing discipline — not exploring edge
cases here, that belongs in ongoing CI, not the build pass.

REWRITE_ARCHITECTURE.md's group directory doesn't flag `search` as
Bucket 2, but live-testing found 4 of its 7 methods 402 on the free tier
anyway (search_cusip, search_isin, search_exchange_variants,
company_screener) — see tests/ultimate/test_search.py. Per the workflow
doc: "if a 'Bucket 1' method 402s, mark it ultimate-pending and move on."
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.live


def test_search_symbol(live_client):
    result = live_client.search_symbol(query="AAPL")
    assert any(r["symbol"] == "AAPL" for r in result)


def test_search_name(live_client):
    result = live_client.search_name(query="Apple")
    assert len(result) > 0
    assert "symbol" in result[0]


def test_search_cik(live_client):
    result = live_client.search_cik(cik="320193")
    assert any(r["symbol"] == "AAPL" for r in result)


def test_search_cusip(live_client):
    result = live_client.search_cusip(cusip="037833100")
    assert len(result) > 0
    assert result[0]["cusip"] == "037833100"


def test_search_isin(live_client):
    result = live_client.search_isin(isin="US0378331005")
    assert len(result) > 0
    assert result[0]["isin"] == "US0378331005"


def test_search_exchange_variants(live_client):
    result = live_client.search_exchange_variants(symbol="AAPL")
    assert any(r["symbol"] == "AAPL" for r in result)


def test_company_screener(live_client):
    result = live_client.company_screener(sector="Technology", limit=1)
    assert len(result) == 1
