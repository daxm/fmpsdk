"""Live test for client.crypto against the real FMP API."""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.live


def test_cryptocurrency_list(live_client):
    result = live_client.cryptocurrency_list()
    assert len(result) > 0
    assert "symbol" in result[0]
