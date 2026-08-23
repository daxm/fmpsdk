"""Live tests for client.congress against the real FMP API. Only
`house_latest` and `senate_latest` (the parameterless "-latest"
listings) are free-tier reachable — the other 10 methods (every
symbol/id/name-scoped lookup) all 402 on the free tier, confirmed live
2026-08-23 — see `tests/ultimate/test_congress.py`.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.live


def test_house_latest(live_client):
    result = live_client.house_latest(page=0, limit=1)
    assert len(result) > 0
    assert "symbol" in result[0]


def test_senate_latest(live_client):
    result = live_client.senate_latest(page=0, limit=1)
    assert len(result) > 0
    assert "symbol" in result[0]
