"""Ultimate-tier (Bucket 2) live tests for client.company.

Discovered live, not predicted by REWRITE_ARCHITECTURE.md's group
directory (which lists no Bucket 2 flag on `company`): these 3 methods
402 on the free tier, while the other 14 in the group work fine. Skipped
by default (`-m "not ultimate"` / excluded unless explicitly selected);
run for real only during a deliberately-timed FMP Ultimate month, per the
rewrite workflow.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.ultimate


# NOTE (2026-08-23): re-tested against Dax's FMP Starter-tier key.
# 1 of this group's methods now pass (moved to
# tests/live/test_company.py); the 2 below still 402 on
# Starter -- gated at Premium or Ultimate, exact tier not yet confirmed.


def test_mergers_acquisitions_search(live_client):
    result = live_client.mergers_acquisitions_search(name="Apple")
    assert isinstance(result, list)


def test_executive_compensation_benchmark(live_client):
    result = live_client.executive_compensation_benchmark(year="2024")
    assert len(result) > 0
    assert "industryTitle" in result[0]
