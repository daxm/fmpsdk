"""fmpsdk-mcp — Model Context Protocol server over the fmpsdk library.

Exposes the Financial Modeling Prep API to an MCP client in three layers:

* ~10 **curated tools** for the common asks (quote, profile, the three
  statements, ratios, key metrics, price history, symbol search, news) —
  hand-shaped signatures, safe by construction.
* three **discovery tools** (``list_fmp_endpoints`` / ``describe_fmp_endpoint``
  / ``call_fmp_endpoint``) that reach the full ~238-method surface at runtime,
  so nothing has to be curated ahead of time.
* the package reference as a **resource** (``fmpsdk://llms.txt``).

Run:  ``FMP_API_KEY=... fmpsdk-mcp``          (stdio transport)
Dev:  ``fastmcp dev fmpsdk_mcp/server.py``   (opens the MCP Inspector)
"""

from __future__ import annotations

import os
from importlib.resources import files
from typing import Any

from fastmcp import FastMCP
from fastmcp.exceptions import ToolError

from fmpsdk import Client
from fmpsdk.exceptions import (
    FMPAuthenticationError,
    FMPError,
    FMPNotFoundError,
    FMPPlanLimitError,
    FMPRateLimitError,
)

from . import catalog
from .policy import CallRefused, ResultCache, paginate, screen_call

mcp = FastMCP("fmpsdk")
_cache = ResultCache()
_client: Client | None = None


def client() -> Client:
    """The shared fmpsdk client, built once from ``FMP_API_KEY``."""
    global _client
    if _client is None:
        key = os.environ.get("FMP_API_KEY")
        if not key:
            raise ToolError(
                "FMP_API_KEY is not set. Add it to the MCP server's `env` block."
            )
        _client = Client(api_key=key)
    return _client


def _fmp_message(name: str, tier: str | None, exc: FMPError) -> str:
    """Turn an fmpsdk exception into a plain-language string for the model."""
    if isinstance(exc, FMPPlanLimitError):
        need = f" (needs the {tier} tier)" if tier and tier != "Free" else ""
        return f"`{name}` is not included in this API key's FMP plan{need}."
    if isinstance(exc, FMPAuthenticationError):
        return "FMP rejected the API key (check FMP_API_KEY)."
    if isinstance(exc, FMPRateLimitError):
        return "FMP rate limit reached — retry in a moment."
    if isinstance(exc, FMPNotFoundError):
        return f"FMP returned no data for that request to `{name}`."
    return f"FMP error on `{name}`: {exc}"


def _call(group: str, method: str, /, **kwargs: Any) -> Any:
    """Invoke one fmpsdk method via its namespace (avoids the ``client.quote``
    name-shadowing gotcha), mapping fmpsdk errors to ToolError."""
    fn = getattr(getattr(client(), group), method)
    try:
        return fn(**{k: v for k, v in kwargs.items() if v is not None})
    except FMPError as exc:
        raise ToolError(_fmp_message(method, None, exc)) from exc


# --------------------------------------------------------------------------- #
# Curated tools                                                              #
# --------------------------------------------------------------------------- #


@mcp.tool
def get_quote(symbol: str) -> list[dict]:
    """Full real-time quote for one symbol (equity, index, commodity, crypto,
    or forex pair): price, change, day/52-week range, volume, market cap,
    50/200-day averages."""
    return _call("quote", "quote", symbol=symbol)


@mcp.tool
def get_company_profile(symbol: str) -> list[dict]:
    """Company profile: price and market cap, identifiers (CIK/ISIN/CUSIP),
    sector and industry, headquarters, leadership, description, exchange."""
    return _call("company", "profile", symbol=symbol)


@mcp.tool
def get_income_statement(
    symbol: str, period: str = "annual", limit: int = 5
) -> list[dict]:
    """Income statement (revenue, expenses, net income) for one company.

    period: "annual" or "quarter".  limit: how many periods, newest first.
    """
    return _call(
        "statements", "income_statement", symbol=symbol, period=period, limit=limit
    )


@mcp.tool
def get_balance_sheet(
    symbol: str, period: str = "annual", limit: int = 5
) -> list[dict]:
    """Balance sheet (assets, liabilities, equity) for one company.

    period: "annual" or "quarter".  limit: how many periods, newest first.
    """
    return _call(
        "statements",
        "balance_sheet_statement",
        symbol=symbol,
        period=period,
        limit=limit,
    )


@mcp.tool
def get_cash_flow(symbol: str, period: str = "annual", limit: int = 5) -> list[dict]:
    """Cash flow statement (operating, investing, financing) for one company.

    period: "annual" or "quarter".  limit: how many periods, newest first.
    """
    return _call(
        "statements", "cash_flow_statement", symbol=symbol, period=period, limit=limit
    )


@mcp.tool
def get_key_metrics(symbol: str, period: str = "annual", limit: int = 5) -> list[dict]:
    """Per-period key metrics: valuation multiples, per-share figures, returns
    on capital, margins — FMP-computed from the statements."""
    return _call("statements", "key_metrics", symbol=symbol, period=period, limit=limit)


@mcp.tool
def get_financial_ratios(
    symbol: str, period: str = "annual", limit: int = 5
) -> list[dict]:
    """Per-period financial ratios: liquidity, leverage, efficiency,
    profitability, and valuation — FMP-computed from the statements."""
    return _call("statements", "ratios", symbol=symbol, period=period, limit=limit)


@mcp.tool
def get_historical_prices(
    symbol: str, from_date: str | None = None, to_date: str | None = None
) -> Any:
    """Daily close price and volume for one symbol between two dates
    (YYYY-MM-DD). Leave dates unset for FMP's default recent window. Long
    ranges are returned page by page — see the response's `note`."""
    result = _call(
        "chart",
        "historical_price_eod_light",
        symbol=symbol,
        from_=from_date,
        to=to_date,
    )
    return paginate(catalog.by_name("historical_price_eod_light"), result)


@mcp.tool
def search_symbol(query: str, limit: int = 10) -> list[dict]:
    """Resolve a ticker symbol from a name or fragment (e.g. "apple" -> AAPL)."""
    return _call("search", "search_symbol", query=query, limit=limit)


@mcp.tool
def get_stock_news(symbols: str, limit: int = 20) -> list[dict]:
    """Recent news articles for one or more symbols (comma-separated, e.g.
    "AAPL,MSFT"): headline, publisher, url, published date, snippet."""
    return _call("news", "news_stock", symbols=symbols, limit=limit)


# --------------------------------------------------------------------------- #
# Discovery tools — the full ~238-method surface, at runtime                  #
# --------------------------------------------------------------------------- #


@mcp.tool
def list_fmp_endpoints(
    query: str = "", group: str = "", free_only: bool = False
) -> list[dict]:
    """Find FMP endpoints beyond the curated tools. `query` is a substring
    match over name/group/summary; `group` filters to one category (e.g.
    "congress", "institutional_ownership"); `free_only` drops endpoints that
    need a paid FMP plan. Returns name, group, plan tier ("Free"/"Starter"/
    "Premium"/"Ultimate"/"Add-on"), and one-line summary — pass a name to
    `describe_fmp_endpoint` for the full signature."""
    hits = catalog.search(query)
    if group:
        hits = [e for e in hits if e.group == group]
    if free_only:
        hits = [e for e in hits if e.tier == "Free"]
    return [
        {
            "name": e.name,
            "group": e.group,
            "tier": e.tier,
            "summary": e.summary,
        }
        for e in hits
    ]


@mcp.tool
def describe_fmp_endpoint(name: str) -> dict:
    """Full detail for one endpoint: call signature, every parameter, return
    type, plan tier, FMP wire path, and the complete docstring. Use before
    `call_fmp_endpoint` so the arguments are right."""
    e = catalog.by_name(name)
    if e is None:
        raise ToolError(
            f"No endpoint named {name!r}. Use list_fmp_endpoints to find one."
        )
    return {
        "name": e.name,
        "group": e.group,
        "signature": e.signature,
        "http_method": e.http_method,
        "wire_path": e.wire_path,
        "tier": e.tier,
        "return_type": e.return_type,
        "params": [
            {
                "name": p.name,
                "type": p.annotation,
                "required": p.required,
                "default": p.default,
            }
            for p in e.params
        ],
        "doc": e.doc,
    }


@mcp.tool
def call_fmp_endpoint(
    name: str, params: dict[str, Any] | None = None, page: int = 0
) -> Any:
    """Invoke any FMP endpoint by its fmpsdk method name. `params` is a dict of
    that method's arguments (see `describe_fmp_endpoint`). Large list results
    are paged: the response carries `page`, `total`, `more`, and a `note` on
    how to get the rest. `bulk` and whole-asset-class batch endpoints are
    refused here — use the fmpsdk library directly for those."""
    e = catalog.by_name(name)
    if e is None:
        raise ToolError(
            f"No endpoint named {name!r}. Use list_fmp_endpoints to find one."
        )
    params = params or {}
    try:
        screen_call(e, params)
    except CallRefused as refused:
        raise ToolError(str(refused)) from refused

    cache_key = ResultCache.key(name, params)
    full = _cache.get(cache_key)
    if full is None:
        fn = getattr(getattr(client(), e.group), e.name)
        try:
            full = fn(**params)
        except TypeError as exc:
            raise ToolError(f"Bad arguments for {e.signature}: {exc}") from exc
        except FMPError as exc:
            raise ToolError(_fmp_message(name, e.tier, exc)) from exc
        _cache.put(cache_key, full)
    return paginate(e, full, page)


# --------------------------------------------------------------------------- #
# Resource                                                                   #
# --------------------------------------------------------------------------- #


@mcp.resource("fmpsdk://llms.txt", mime_type="text/plain")
def llms_txt() -> str:
    """Orientation for the fmpsdk package behind this server."""
    return (files("fmpsdk_mcp") / "resources" / "llms.txt").read_text(encoding="utf-8")


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
