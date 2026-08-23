"""Ultimate-tier (Bucket 2) live tests for client.economics.

Discovered live, not predicted by REWRITE_ARCHITECTURE.md's group
directory (which lists no Bucket 2 flag on `economics`): `economic_calendar`
402s on the free tier, while treasury_rates, economic_indicators, and
market_risk_premium all work fine. Skipped by default (`-m "not ultimate"`
/ excluded unless explicitly selected); run for real only during a
deliberately-timed FMP Ultimate month, per the rewrite workflow.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.ultimate


def test_economic_calendar(live_client):
    result = live_client.economic_calendar(country="US")
    assert len(result) > 0
    assert "event" in result[0]
