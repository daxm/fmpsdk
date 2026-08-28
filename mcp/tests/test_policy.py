"""The call_fmp_endpoint guardrails: screening, pagination, and the page cache."""

from __future__ import annotations

import time

import pytest

from fmpsdk_mcp import catalog
from fmpsdk_mcp.policy import (
    PAGE_SIZE,
    CallRefused,
    ResultCache,
    paginate,
    screen_call,
)

HP = catalog.by_name("historical_price_eod_light")


def test_screen_blocks_the_bulk_group():
    with pytest.raises(CallRefused):
        screen_call(catalog.by_name("profile_bulk"), {})


def test_screen_blocks_whole_asset_class_batch_quotes():
    with pytest.raises(CallRefused):
        screen_call(catalog.by_name("batch_forex_quotes"), {})


def test_screen_allows_ordinary_calls():
    assert screen_call(catalog.by_name("quote"), {"symbol": "AAPL"}) is None
    # an explicit symbol list is fine — its size is caller-bounded
    assert screen_call(catalog.by_name("batch_quote"), {"symbols": ["AAPL"]}) is None


def test_paginate_passes_non_list_through():
    assert paginate(HP, {"x": 1}) == {"x": 1}
    assert paginate(HP, "raw") == "raw"


def test_paginate_small_list_has_no_note():
    r = paginate(HP, [{"i": i} for i in range(5)])
    assert r["total"] == 5
    assert r["returned"] == 5
    assert r["more"] is False
    assert "note" not in r


def test_paginate_walks_pages():
    rows = [{"i": i} for i in range(125)]
    p0 = paginate(HP, rows, page=0)
    assert p0["returned"] == PAGE_SIZE and p0["more"] is True and "note" in p0
    assert p0["data"][0]["i"] == 0

    p2 = paginate(HP, rows, page=2)
    assert p2["returned"] == 25 and p2["more"] is False
    assert p2["data"][0]["i"] == 100


def test_paginate_page_past_the_end_is_empty_not_an_error():
    r = paginate(HP, [{"i": i} for i in range(60)], page=9)
    assert r["returned"] == 0 and r["more"] is False


def test_result_cache_roundtrip_and_expiry():
    c = ResultCache(ttl=0.05, maxsize=4)
    key = ResultCache.key("quote", {"symbol": "AAPL"})
    c.put(key, [1, 2, 3])
    assert c.get(key) == [1, 2, 3]
    time.sleep(0.06)
    assert c.get(key) is None


def test_result_cache_evicts_oldest_over_maxsize():
    c = ResultCache(ttl=100, maxsize=2)
    c.put("a", 1)
    c.put("b", 2)
    c.put("c", 3)
    assert c.get("a") is None
    assert c.get("c") == 3


def test_cache_key_is_stable_and_handles_unhashable_params():
    k1 = ResultCache.key("batch_quote", {"symbols": ["A", "B"]})
    k2 = ResultCache.key("batch_quote", {"symbols": ["A", "B"]})
    assert isinstance(k1, str) and k1 == k2
