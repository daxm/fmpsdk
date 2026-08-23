"""Alias-layer group objects — thin namespaces over the canonical methods
defined on :class:`~fmpsdk.client.Client` (REWRITE_ARCHITECTURE.md §3-§4).

Never a second implementation: every attribute assigned here must be the
*same* bound-method object wherever a canonical method is cross-listed into
more than one group — ``client.crypto.quote is client.quote.quote`` must
hold for the 10 cross-listings once they exist (§3.4, §11 invariant 2).

That identity is NOT automatic. ``instance.method`` constructs a fresh
``MethodType`` wrapper on every attribute access in CPython — two groups
each independently doing ``self.quote = client.quote`` in their own
``__init__`` would get two distinct (``==``-equal but not ``is``-identical)
objects. ``_MethodBinder`` below closes over one cache per ``attach_groups``
call so every group asking for the same canonical method name gets back the
exact object bound the first time.
"""

from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from .client import Client


class _MethodBinder:
    """Binds ``client.<name>`` exactly once per name and caches the result,
    so every ``*Group`` built from the same binder shares one object per
    cross-listed method."""

    def __init__(self, client: "Client") -> None:
        self._client = client
        self._cache: dict[str, typing.Callable] = {}

    def __call__(self, name: str) -> typing.Callable:
        if name not in self._cache:
            self._cache[name] = getattr(self._client, name)
        return self._cache[name]


class SearchGroup:
    """``client.search`` — 7 primary methods, no cross-listings."""

    def __init__(self, bind: _MethodBinder) -> None:
        self.company_screener = bind("company_screener")
        self.search_cik = bind("search_cik")
        self.search_cusip = bind("search_cusip")
        self.search_exchange_variants = bind("search_exchange_variants")
        self.search_isin = bind("search_isin")
        self.search_name = bind("search_name")
        self.search_symbol = bind("search_symbol")


def attach_groups(client: "Client") -> None:
    """Attach every alias-group namespace to ``client``.

    Called once from ``Client.__init__``. This is the single place group
    wiring happens — extend it as each new group's endpoint module and
    ``*Group`` class are added. All groups share one ``_MethodBinder`` so
    cross-listed methods stay identity-equal across groups.
    """
    bind = _MethodBinder(client)
    client.search = SearchGroup(bind)
