#!/usr/bin/env python3
"""Derive each endpoint's FMP plan tier from ``REWRITE_PROGRESS.md`` and write
``mcp/fmpsdk_mcp/resources/tiers.json``.

    python tools/gen_tiers.py            # writes the json
    python tools/gen_tiers.py --check    # exit 1 if it is stale

``REWRITE_PROGRESS.md`` is the project's source of truth for which tier each
method was actually verified against (a live 402-or-not result, not a guess).
It lives at the repo root and is *not* shipped in any wheel, so we bake its
verdict into a small JSON file inside the ``fmpsdk_mcp`` package, where the
catalog can load it at runtime.

Checklist lines look like:

    - [x] done `income_statement` — `income-statement`
    - [x] done `company_screener` — `company-screener` (works on Starter tier; 402 on free tier)
    - [x] untested (community add-on) `tipranks_search` — `tipranks-search` (... add-on ...)

No "works on <tier>" parenthetical means it was verified on the free tier.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PROGRESS = REPO / "REWRITE_PROGRESS.md"
OUT = REPO / "mcp" / "fmpsdk_mcp" / "resources" / "tiers.json"

_LINE = re.compile(
    r"^- \[x\] (?P<status>.*?) `(?P<name>[a-z0-9_]+)` — `[^`]+`(?P<rest>.*)$"
)

# Order matters: check the highest tier phrase first.
_TIER_PHRASES = [
    ("Ultimate", "works on Ultimate tier"),
    ("Premium", "works on Premium tier"),
    ("Starter", "works on Starter tier"),
]

TIERS = ("Free", "Starter", "Premium", "Ultimate", "Add-on")


def build_map() -> dict[str, str]:
    tiers: dict[str, str] = {}
    for line in PROGRESS.read_text(encoding="utf-8").splitlines():
        m = _LINE.match(line)
        if not m:
            continue
        status, name, rest = m["status"], m["name"], m["rest"]
        if "community add-on" in status or "add-on" in rest.lower():
            tiers[name] = "Add-on"
            continue
        tiers[name] = next(
            (tier for tier, phrase in _TIER_PHRASES if phrase in rest), "Free"
        )
    return dict(sorted(tiers.items()))


def render(tiers: dict[str, str]) -> str:
    return json.dumps(tiers, indent=2) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    tiers = build_map()
    rendered = render(tiers)

    if args.check:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if current != rendered:
            print(
                "tiers.json is stale — run: python tools/gen_tiers.py", file=sys.stderr
            )
            return 1
        print("tiers.json is up to date.")
        return 0

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(rendered, encoding="utf-8")
    counts = {t: sum(1 for v in tiers.values() if v == t) for t in TIERS}
    print(f"wrote {OUT.relative_to(REPO)} — {len(tiers)} methods: {counts}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
