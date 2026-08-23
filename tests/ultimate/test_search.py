"""Ultimate-tier (Bucket 2) live tests for client.search.

Discovered live, not predicted by REWRITE_ARCHITECTURE.md's group
directory (which lists no Bucket 2 flag on `search`): these 4 methods
402 on the free tier. Skipped by default (`-m "not ultimate"` /
excluded unless explicitly selected); run for real only during a
deliberately-timed FMP Ultimate month, per the rewrite workflow.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.ultimate


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
