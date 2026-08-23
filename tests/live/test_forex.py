"""Live test for client.forex against the real FMP API."""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.live


def test_forex_list(live_client):
    result = live_client.forex_list()
    assert len(result) > 0
    assert "symbol" in result[0]
