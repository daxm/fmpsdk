"""Live tests for client.news against the real FMP API. Only
`fmp_articles` is free-tier reachable — the other 9 methods (the whole
`NewsArticleResult`-shaped family: general/press-releases/stock/crypto/
forex, each with a "-latest" sibling) all 402 on the free tier, confirmed
live 2026-08-23 — see `tests/ultimate/test_news.py`.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.live


def test_fmp_articles(live_client):
    result = live_client.fmp_articles(page=0, limit=1)
    assert len(result) > 0
    assert "title" in result[0]
