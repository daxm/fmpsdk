"""Guardrails for the generic ``call_fmp_endpoint`` dispatch tool.

The curated tools in ``server.py`` are hand-shaped and safe by construction.
``call_fmp_endpoint`` is different: it lets the model invoke *any* of the ~238
endpoints by name, so it needs a policy layer deciding

  1. which calls to refuse before they reach FMP        (``screen_call``), and
  2. how to serve a large result without flooding the
     model's context window                             (``paginate``).

Both hooks are deliberately small and live here, separate from the protocol
plumbing, so the policy is easy to read and change in one place.

Why paginate at all: a tool result is injected into the model's context, which
is a hard capacity ceiling (~200K tokens), not a spend dial. A single unbounded
FMP list endpoint (20 years of daily prices, a "latest" feed, a screener) can be
hundreds of thousands of tokens — it does not fit, and a truncated JSON blob is
worse than a clean slice plus a pointer to the full dataset.
"""

from __future__ import annotations

import json
import time
from typing import Any

from .catalog import Endpoint

# Rows per page for an oversized list result.
PAGE_SIZE = 50

# Endpoints whose *whole point* is a dataset too big for a tool response.
# These are redirected to the fmpsdk library rather than served here.
_BLOCKED_GROUPS = {"bulk"}
_BLOCKED_METHODS = {
    # whole-asset-class quote dumps (thousands of rows, Ultimate-gated)
    "batch_exchange_quote",
    "batch_etf_quotes",
    "batch_mutualfund_quotes",
    "batch_commodity_quotes",
    "batch_crypto_quotes",
    "batch_forex_quotes",
    "batch_index_quotes",
}

_REDIRECT = (
    "returns a bulk dataset far larger than an MCP tool response can carry. "
    "Call it through the fmpsdk Python library directly "
    "(`from fmpsdk import Client`) for full-dataset work."
)


class CallRefused(Exception):
    """Raised by :func:`screen_call` to block a dispatch. The message is shown
    to the model so it can adjust (narrow the query, or use the library)."""


def screen_call(endpoint: Endpoint, params: dict[str, Any]) -> None:
    """Return ``None`` to allow the dispatch; raise :class:`CallRefused` to
    block it with a message the model will see.

    An explicit ``batch_quote(["AAPL", "MSFT"])`` with a caller-supplied
    symbol list is fine — it's the *whole-asset-class* batch endpoints and the
    ``bulk`` group that are refused, because their response size is unbounded
    by anything the caller passes.
    """
    if endpoint.group in _BLOCKED_GROUPS or endpoint.name in _BLOCKED_METHODS:
        raise CallRefused(f"`{endpoint.name}` {_REDIRECT}")
    return None


def paginate(endpoint: Endpoint, result: Any, page: int = 0) -> Any:
    """Shape an fmpsdk return value for a tool response.

    * Non-list results (a dict, a scalar) pass through untouched.
    * A list is always returned inside an envelope with ``page`` / ``total`` /
      ``more`` so the contract is predictable, and sliced to :data:`PAGE_SIZE`
      when it is longer than that.
    """
    if not isinstance(result, list):
        return result

    total = len(result)
    page = max(int(page), 0)
    start = page * PAGE_SIZE
    window = result[start : start + PAGE_SIZE]
    more = start + PAGE_SIZE < total

    if more or page > 0:
        note = (
            f"Showing rows {start}–{start + len(window)} of {total}. "
            f"Call again with page={page + 1} for the next slice"
            if more
            else f"Showing rows {start}–{start + len(window)} of {total}. No more pages."
        )
        note += (
            f". To narrow at the source, pass this endpoint's own limiting "
            f"params ({endpoint.signature}); for full-dataset analysis use the "
            f"fmpsdk library directly."
        )
    else:
        note = None

    return {
        "data": window,
        "page": page,
        "page_size": PAGE_SIZE,
        "returned": len(window),
        "total": total,
        "more": more,
        **({"note": note} if note else {}),
    }


class ResultCache:
    """Tiny TTL cache so paging through an oversized result does not re-hit FMP
    (and re-spend quota) once per page. Per-process, bounded, not thread-safe —
    a stdio MCP server handles one request at a time.
    """

    def __init__(self, ttl: float = 120.0, maxsize: int = 32) -> None:
        self.ttl = ttl
        self.maxsize = maxsize
        self._store: dict[str, tuple[float, Any]] = {}

    @staticmethod
    def key(name: str, params: dict[str, Any]) -> str:
        return name + "|" + json.dumps(params, sort_keys=True, default=str)

    def get(self, key: str) -> Any | None:
        hit = self._store.get(key)
        if hit is None:
            return None
        stored_at, value = hit
        if time.monotonic() - stored_at > self.ttl:
            del self._store[key]
            return None
        return value

    def put(self, key: str, value: Any) -> None:
        if len(self._store) >= self.maxsize:
            oldest = min(self._store, key=lambda k: self._store[k][0])
            del self._store[oldest]
        self._store[key] = (time.monotonic(), value)


__all__ = ["CallRefused", "PAGE_SIZE", "ResultCache", "paginate", "screen_call"]
