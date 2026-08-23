"""Ultimate-tier (Bucket 2) live tests for client.calendar.

Discovered live, not predicted by REWRITE_ARCHITECTURE.md's group
directory (which lists no Bucket 2 flag on `calendar`): the 3 `ipos_*`
methods 402 on the free tier — the whole IPOs category, while
dividends/earnings/splits are all free-tier reachable. Skipped by default
(`-m "not ultimate"` / excluded unless explicitly selected); run for real
only during a deliberately-timed FMP Ultimate month, per the rewrite
workflow.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.ultimate

FROM = "2026-08-01"
TO = "2026-08-23"


def test_ipos_calendar(live_client):
    result = live_client.ipos_calendar(from_=FROM, to=TO)
    assert len(result) > 0
    assert "symbol" in result[0]


def test_ipos_disclosure(live_client):
    result = live_client.ipos_disclosure(from_=FROM, to=TO)
    assert len(result) > 0
    assert "symbol" in result[0]


def test_ipos_prospectus(live_client):
    result = live_client.ipos_prospectus(from_=FROM, to=TO)
    assert len(result) > 0
    assert "symbol" in result[0]
