"""Introspect the installed ``fmpsdk`` package into a flat catalog of callable
endpoints.

This is the single source of truth shared by two consumers:

* ``fmpsdk_mcp.server`` — the discovery tools (``list_fmp_endpoints`` /
  ``describe_fmp_endpoint`` / ``call_fmp_endpoint``) read the catalog so the
  model can find and invoke any of the ~238 methods at runtime.
* ``tools/gen_openapi.py`` — the OpenAPI generator walks the same catalog so
  the emitted ``openapi.json`` describes exactly the surface the server exposes.

Nothing here is hand-maintained: every field is read back from the SDK's own
signatures and docstrings, so the catalog can never drift from the installed
version of ``fmpsdk``.
"""

from __future__ import annotations

import inspect
import json
import re
from dataclasses import dataclass
from functools import lru_cache
from importlib.resources import files

import fmpsdk
from fmpsdk.client import Client

# The first paragraph of every endpoint docstring is shaped like:
#
#     ``GET income-statement`` — revenue, expenses, and net income
#     for one company, periodic.
#
# Capture the HTTP verb, the FMP ``stable/`` wire path, and the prose that
# follows the em-dash (or hyphen). DOTALL so a summary that wraps across
# lines is captured whole; we collapse the whitespace afterwards.
_WIRE_RE = re.compile(
    r"``([A-Z]+)\s+([^`]+)``\s*(?:[—-]\s*(?P<summary>.*))?",
    re.DOTALL,
)

# Authoritative plan tier per method, generated from REWRITE_PROGRESS.md's
# live-verified 402 results by ``tools/gen_tiers.py``. One of "Free", "Starter",
# "Premium", "Ultimate", or "Add-on" (a separate FMP purchase, e.g. TipRanks).
try:
    _TIERS: dict[str, str] = json.loads(
        (files("fmpsdk_mcp") / "resources" / "tiers.json").read_text(encoding="utf-8")
    )
except (FileNotFoundError, ModuleNotFoundError):  # pragma: no cover
    _TIERS = {}

# Fallback only, for a method missing from tiers.json (e.g. added after the
# file was last regenerated): scrape a tier phrase out of the docstring.
_TIER_RE = re.compile(r"\b(Starter|Premium|Ultimate)\b[- ]tier", re.IGNORECASE)


@dataclass(frozen=True)
class Param:
    """One parameter of an endpoint method."""

    name: str
    annotation: str  # str form of the hint, e.g. "str" or "int | None"
    required: bool
    default: object = None


@dataclass(frozen=True)
class Endpoint:
    """One callable ``fmpsdk`` method, flattened for lookup and dispatch."""

    name: str  # SDK method name, e.g. "income_statement"
    group: str  # namespace it lives under, e.g. "statements"
    http_method: str  # always "GET" today, but read from the docstring
    wire_path: str  # FMP stable/ path, e.g. "income-statement"
    summary: str  # one-line purpose, collapsed to a single line
    doc: str  # the full method docstring (normalised by inspect.getdoc)
    params: tuple[Param, ...]
    return_type: str  # e.g. "list[IncomeStatementResult]"
    tier: str  # "Free" | "Starter" | "Premium" | "Ultimate" | "Add-on"

    @property
    def signature(self) -> str:
        """A human-readable call signature, e.g.
        ``income_statement(symbol, limit=None, period=None)``."""
        parts = []
        for p in self.params:
            parts.append(p.name if p.required else f"{p.name}={p.default!r}")
        return f"{self.name}({', '.join(parts)})"


def _endpoint_mixins() -> list[type]:
    """The per-category mixin classes composed onto ``Client`` (everything in
    its MRO whose module lives under ``fmpsdk.endpoints``)."""
    return [
        klass
        for klass in Client.__mro__
        if klass.__module__.startswith("fmpsdk.endpoints.")
    ]


def _derst(text: str) -> str:
    """Strip the Sphinx/RST roles that appear in docstrings (``:meth:`foo```,
    ``:class:`~pkg.Bar```, `` ``literal`` ``) down to plain words, for a
    summary that reads cleanly in a tool listing."""
    text = re.sub(r":\w+:`~?\.?([^`]+)`", r"\1", text)
    text = text.replace("``", "").replace("`", "")
    return text


def _parse_doc(func) -> tuple[str, str, str, str, str | None]:
    """Return ``(http_method, wire_path, summary, full_doc, doc_tier)`` for a
    method, pulled from its docstring. ``doc_tier`` is a best-effort fallback
    used only when tiers.json does not cover the method."""
    doc = inspect.getdoc(func) or ""
    first_para = doc.split("\n\n", 1)[0]
    match = _WIRE_RE.match(first_para)
    if match:
        http_method = match.group(1)
        wire_path = match.group(2).strip()
        summary = " ".join((match.group("summary") or "").split())
    else:
        # No recognised prefix — fall back so the endpoint still appears.
        http_method = "GET"
        wire_path = ""
        summary = " ".join(first_para.split())
    tier_match = _TIER_RE.search(doc)
    doc_tier = tier_match.group(1).capitalize() if tier_match else None
    return http_method, wire_path, _derst(summary), doc, doc_tier


def _params(func) -> tuple[Param, ...]:
    """Signature parameters of a method, excluding ``self``."""
    sig = inspect.signature(func)
    out: list[Param] = []
    for name, p in sig.parameters.items():
        if name == "self":
            continue
        annotation = (
            "" if p.annotation is inspect.Parameter.empty else str(p.annotation)
        )
        has_default = p.default is not inspect.Parameter.empty
        out.append(
            Param(
                name=name,
                annotation=annotation,
                required=not has_default,
                default=None if not has_default else p.default,
            )
        )
    return tuple(out)


@lru_cache(maxsize=1)
def build_catalog() -> tuple[Endpoint, ...]:
    """Introspect ``fmpsdk`` once and return every public endpoint method.

    Cached: the installed package cannot change under a running process.
    """
    seen: set[str] = set()
    endpoints: list[Endpoint] = []
    for mixin in _endpoint_mixins():
        group = mixin.__module__.rsplit(".", 1)[-1]
        for name, func in vars(mixin).items():
            if name.startswith("_") or not callable(func) or name in seen:
                continue
            seen.add(name)
            http_method, wire_path, summary, doc, doc_tier = _parse_doc(func)
            tier = _TIERS.get(name) or doc_tier or "Free"
            sig = inspect.signature(func)
            return_type = (
                ""
                if sig.return_annotation is inspect.Signature.empty
                else str(sig.return_annotation)
            )
            endpoints.append(
                Endpoint(
                    name=name,
                    group=group,
                    http_method=http_method,
                    wire_path=wire_path,
                    summary=summary,
                    doc=doc,
                    params=_params(func),
                    return_type=return_type,
                    tier=tier,
                )
            )
    endpoints.sort(key=lambda e: (e.group, e.name))
    return tuple(endpoints)


def by_name(name: str) -> Endpoint | None:
    """Look up a single endpoint by its SDK method name."""
    for endpoint in build_catalog():
        if endpoint.name == name:
            return endpoint
    return None


def search(query: str) -> list[Endpoint]:
    """Case-insensitive substring match over method name, group, and summary.
    An empty query returns the whole catalog."""
    q = query.strip().lower()
    if not q:
        return list(build_catalog())
    return [
        e
        for e in build_catalog()
        if q in e.name.lower() or q in e.group.lower() or q in e.summary.lower()
    ]


__all__ = ["Endpoint", "Param", "build_catalog", "by_name", "search"]

# The package version the catalog was built against — handy for the OpenAPI
# ``info.version`` and for a discovery-tool "about" response.
FMPSDK_VERSION = getattr(fmpsdk, "__version__", "unknown")
