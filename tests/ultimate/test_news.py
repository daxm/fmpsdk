"""Ultimate-tier (Bucket 2) live tests for client.news.

`fmp_articles` is free-tier reachable (see `tests/live/test_news.py`);
these 9 remaining methods — the whole `NewsArticleResult`-shaped family
(general/press-releases/stock/crypto/forex, each with a "-latest"
sibling) — all 402 on the free tier, confirmed live 2026-08-23 despite
no Bucket 2 flag in REWRITE_ARCHITECTURE.md §3.5. Skipped by default;
run for real only during a deliberately-timed FMP Ultimate month, per
the rewrite workflow.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.ultimate


# NOTE (2026-08-23): re-tested against Dax's FMP Starter-tier key.
# 7 of this group's methods now pass (moved to
# tests/live/test_news.py); the 2 below still 402 on
# Starter -- gated at Premium or Ultimate, exact tier not yet confirmed.


def test_news_press_releases(live_client):
    result = live_client.news_press_releases(symbols="AAPL", limit=1)
    assert isinstance(result, list)


def test_news_press_releases_latest(live_client):
    result = live_client.news_press_releases_latest(limit=1)
    assert len(result) > 0
    assert "title" in result[0]
