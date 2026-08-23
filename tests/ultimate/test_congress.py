"""Ultimate-tier (Bucket 2) live tests for client.congress.

Every symbol/id/name-scoped method 402s on the free tier, confirmed
live 2026-08-23 — only the parameterless `house_latest`/`senate_latest`
listings are free-tier reachable (see `tests/live/test_congress.py`).
`senate_id` examples are real member IDs taken from
REWRITE_ARCHITECTURE.md's own documented examples (``"P000197"``), not
invented. Skipped by default; run for real only during a
deliberately-timed FMP Ultimate month, per the rewrite workflow.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.ultimate

_SENATE_ID = "P000197"


# NOTE (2026-08-23): re-tested against Dax's FMP Starter-tier key.
# 6 of this group's methods now pass (moved to
# tests/live/test_congress.py); the 4 below still 402 on
# Starter -- gated at Premium or Ultimate, exact tier not yet confirmed.


def test_senate_net_worth(live_client):
    result = live_client.senate_net_worth(senate_id=_SENATE_ID)
    assert isinstance(result, list)


def test_senate_net_worth_aggregated(live_client):
    result = live_client.senate_net_worth_aggregated(senate_id=_SENATE_ID)
    assert isinstance(result, list)


def test_senate_positions(live_client):
    result = live_client.senate_positions(senate_id=_SENATE_ID)
    assert isinstance(result, list)


def test_senate_profile(live_client):
    result = live_client.senate_profile(senate_id=_SENATE_ID)
    assert isinstance(result, list)
