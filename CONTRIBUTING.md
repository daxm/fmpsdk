# Contributing to fmpsdk

Thanks for considering it. This is a hobby project with one maintainer, so the bar is
"clearly correct and tested," not perfection — but a few conventions below are load-
bearing for how the test suite works, so please read before opening a PR.

## Dev setup

```bash
git clone https://github.com/daxm/fmpsdk.git
cd fmpsdk
python -m venv .venv && source .venv/bin/activate
pip install poetry
poetry config virtualenvs.create false --local   # installs into the venv above, not a separate one
poetry install --with dev
```

Create a `.env` file with a real FMP API key if you want to run anything against the
live API: `FMP_API_KEY=your-key-here`. Not required for unit tests.

## The three test tiers

Every test is marked `unit`, `live`, or `ultimate` (see `pyproject.toml`'s
`[tool.pytest.ini_options]`). A bare `pytest` only runs `unit` — it never makes a real
network call and never costs API quota.

- **`unit`** (`tests/unit/`) — mocked via `requests-mock`, no network. Every one of the
  238 methods has one of these. Always run these; CI runs them on every push/PR.
- **`live`** (`tests/live/`) — a real call against the real API, for a method **confirmed
  to work on some FMP plan tier** (the docstring says which). Skipped by default; run
  explicitly with `pytest tests/live/ -m live` (needs `FMP_API_KEY`).
- **`ultimate`** (`tests/ultimate/`) — a real call against a method **not yet confirmed
  working on any tier this maintainer has access to**. Currently that's just the 7
  `client.tipranks` methods (see below). Skipped by default; run with
  `pytest tests/ultimate/ -m ultimate`.

`REWRITE_PROGRESS.md` is the source of truth for exactly which of the 238 methods are
`done` (verified, and on which tier) vs. `untested`. Check it before assuming something
is broken — it might just be genuinely unverified, and that's stated plainly, not hidden.

## Fixing/verifying `client.tipranks`

FMP's TipRanks endpoints need a separate paid add-on ("TipRanks data boost"), not covered
by any Free/Starter/Premium/Ultimate plan tier. This maintainer doesn't have it, so these
7 methods are implemented and unit-tested against FMP's documented example shapes, but
**never verified against a real response**. If you have that add-on:

1. Run `pytest tests/ultimate/test_tipranks.py -m ultimate -v` against your real key.
2. For each method that passes as-is: move its test function from
   `tests/ultimate/test_tipranks.py` into a new `tests/live/test_tipranks.py` (module
   docstring + `pytestmark = pytest.mark.live`, same shape as any other file in
   `tests/live/`), and update its status in `REWRITE_PROGRESS.md` from
   `untested (community add-on)` to `done`.
3. For each method whose real response doesn't match `fmpsdk/types/tipranks.py`'s
   `TypedDict`s: fix the type (and the mocked unit test's fixture in
   `tests/unit/test_tipranks.py`) to match what you actually saw, not what FMP's docs
   show — every other type in this package was corrected against a live response at
   least once, and this is the one group that hasn't been yet.
4. Update `fmpsdk/endpoints/tipranks.py`'s module docstring to drop the "never
   verified" caveat once it's genuinely verified.

A PR that does even one of these methods, with the real response body pasted into the
PR description for review, is very welcome.

## Adding or changing an endpoint

- One method, one FMP endpoint. Parameters use Python-safe names (`from_` for FMP's
  `from`, etc.) and get mapped back to the real query-param name inside the method.
- Response shape goes in `fmpsdk/types/<group>.py` as a `TypedDict`, named
  `<Thing>Result`. Use the functional `TypedDict(...)` call form instead of class syntax
  if a real field name collides with a Python keyword or contains a space.
- Write the `unit` test first (mocked, cheap, no quota). Then, if you can reach the
  endpoint on your own FMP plan, add a `live` test with one fixed, cheap test case
  (e.g. `symbol="AAPL"`) — this project deliberately doesn't explore multiple
  symbols/edge cases in the test suite; that's what the mocked unit tests are for.
- Docstrings should be self-contained for someone who only has this package installed
  (via `pip`) — no references to this repo's internal `REWRITE_*.md` design docs or
  `§`-numbered sections. State plan-tier requirements as a plain fact
  ("Requires an FMP Starter-tier plan or higher"), not a hedge.

## Code style

`black` formatting is enforced in CI. Run `black .` before committing. No other linter
is currently wired up; keep new code's style consistent with what's around it.

## Versioning

This package intentionally keeps FMP's inherited `DATE.PATCH` version scheme (e.g.
`20250102.0`), not SemVer — a version bump is out of scope for a typical PR; the
maintainer handles releases.
