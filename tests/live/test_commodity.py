"""Live test for client.commodity against the real FMP API."""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.live


def test_commodities_list(live_client):
    result = live_client.commodities_list()
    assert len(result) > 0
    assert "symbol" in result[0]
