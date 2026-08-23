"""Live tests for client.indexes against the real FMP API. Only
`index_list` is free-tier reachable — the other 6 own methods
(`sp500_constituent`, `nasdaq_constituent`, `dowjones_constituent`, and
their 3 `historical_*` siblings) all 402 on the free tier despite no
Bucket 2 flag in REWRITE_ARCHITECTURE.md §3.5, confirmed live
2026-08-23 — see `tests/ultimate/test_indexes.py`. The 6 methods
cross-listed from client.chart/client.quote are covered by those
groups' own live tests.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.live


def test_index_list(live_client):
    result = live_client.index_list()
    assert len(result) > 0
    assert "symbol" in result[0]
