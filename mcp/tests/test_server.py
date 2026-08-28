"""Server wiring: tools registered, error mapping, dispatch guards.

These never touch the network — they exercise registration, the discovery
tools (which read the catalog), and the pre-flight guards in
``call_fmp_endpoint`` that fire before any FMP request.
"""

from __future__ import annotations

import asyncio

import pytest
from fastmcp.exceptions import ToolError

from fmpsdk.exceptions import (
    FMPAuthenticationError,
    FMPNotFoundError,
    FMPPlanLimitError,
    FMPRateLimitError,
)
from fmpsdk_mcp import server

CURATED = {
    "get_quote",
    "get_company_profile",
    "get_income_statement",
    "get_balance_sheet",
    "get_cash_flow",
    "get_key_metrics",
    "get_financial_ratios",
    "get_historical_prices",
    "search_symbol",
    "get_stock_news",
}
DISCOVERY = {"list_fmp_endpoints", "describe_fmp_endpoint", "call_fmp_endpoint"}


def test_exactly_the_expected_tools_are_registered():
    names = {t.name for t in asyncio.run(server.mcp.list_tools())}
    assert names == CURATED | DISCOVERY


def test_llms_txt_resource_is_registered():
    uris = {str(r.uri) for r in asyncio.run(server.mcp.list_resources())}
    assert "fmpsdk://llms.txt" in uris


def test_fmp_error_messages_are_plain_language():
    plan = server._fmp_message("income_statement_ttm", "Ultimate", FMPPlanLimitError())
    assert "not included" in plan and "Ultimate tier" in plan

    # a "Free" endpoint that 402s (per-symbol gating) must not claim a tier
    assert "tier" not in server._fmp_message("quote", "Free", FMPPlanLimitError())

    assert "API key" in server._fmp_message("x", None, FMPAuthenticationError("bad"))
    assert (
        "rate limit"
        in server._fmp_message("x", None, FMPRateLimitError("slow")).lower()
    )
    assert "no data" in server._fmp_message("x", None, FMPNotFoundError("missing"))


def test_call_fmp_endpoint_rejects_unknown_name():
    with pytest.raises(ToolError):
        server.call_fmp_endpoint(name="does_not_exist")


def test_call_fmp_endpoint_refuses_bulk_and_whole_asset_batches():
    with pytest.raises(ToolError):
        server.call_fmp_endpoint(name="profile_bulk", params={})
    with pytest.raises(ToolError):
        server.call_fmp_endpoint(name="batch_crypto_quotes", params={})


def test_describe_reports_tier_and_signature():
    d = server.describe_fmp_endpoint("ratios")
    assert d["tier"] == "Free"
    assert d["signature"] == "ratios(symbol, limit=None, period=None)"
    assert {p["name"] for p in d["params"]} == {"symbol", "limit", "period"}


def test_describe_rejects_unknown_name():
    with pytest.raises(ToolError):
        server.describe_fmp_endpoint("nope")


def test_list_free_only_filter():
    everything = server.list_fmp_endpoints()
    free = server.list_fmp_endpoints(free_only=True)
    assert 0 < len(free) < len(everything)
    assert all(row["tier"] == "Free" for row in free)


def test_list_group_filter():
    congress = server.list_fmp_endpoints(group="congress")
    assert congress and all(row["group"] == "congress" for row in congress)
