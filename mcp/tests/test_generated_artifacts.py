"""The committed ``openapi.json`` and ``tiers.json`` must match what the
generators produce from the current source — same contract as the CI
``--check`` step, but catchable from a local ``pytest`` run too.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]


def _load(name: str):
    path = REPO / "tools" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def test_tiers_json_is_current():
    gen = _load("gen_tiers")
    expected = gen.render(gen.build_map())
    assert (
        gen.OUT.read_text(encoding="utf-8") == expected
    ), "tiers.json is stale — run: python tools/gen_tiers.py"


def test_openapi_json_is_current():
    import json

    gen = _load("gen_openapi")
    expected = json.dumps(gen.build_spec(), indent=2, ensure_ascii=False) + "\n"
    assert (
        gen.OUT.read_text(encoding="utf-8") == expected
    ), "openapi.json is stale — run: python tools/gen_openapi.py"
