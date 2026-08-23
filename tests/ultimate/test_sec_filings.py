"""Ultimate-tier (Bucket 2) live tests for client.sec_filings.

`industry_classification_search` and `all_industry_classification` 402
on the free tier, confirmed live 2026-08-23 — the other 10 methods are
free-tier reachable (see `tests/live/test_sec_filings.py`). Skipped by
default; run for real only during a deliberately-timed FMP Ultimate
month, per the rewrite workflow.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.ultimate


def test_industry_classification_search(live_client):
    result = live_client.industry_classification_search(symbol="AAPL")
    assert len(result) > 0
    assert result[0]["symbol"] == "AAPL"


def test_all_industry_classification(live_client):
    result = live_client.all_industry_classification(page=0, limit=1)
    assert len(result) > 0
    assert "sicCode" in result[0]
