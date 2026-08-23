"""Live tests for client.fundraisers against the real FMP API. One fixed
cheap call per method. CIKs are real issuers taken from
REWRITE_ARCHITECTURE.md's own documented examples, not AAPL — neither
crowdfunding nor Reg D/A filings exist under Apple's CIK.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.live


def test_crowdfunding_offerings(live_client):
    result = live_client.crowdfunding_offerings(cik="0001916078")
    assert isinstance(result, list)


def test_crowdfunding_offerings_latest(live_client):
    result = live_client.crowdfunding_offerings_latest(limit=1)
    assert len(result) > 0
    assert "cik" in result[0]


def test_crowdfunding_offerings_search(live_client):
    result = live_client.crowdfunding_offerings_search(name="enotap")
    assert isinstance(result, list)


def test_fundraising(live_client):
    result = live_client.fundraising(cik="0001547416")
    assert isinstance(result, list)


def test_fundraising_latest(live_client):
    result = live_client.fundraising_latest(limit=1)
    assert len(result) > 0
    assert "cik" in result[0]


def test_fundraising_search(live_client):
    result = live_client.fundraising_search(name="NJOY")
    assert isinstance(result, list)
