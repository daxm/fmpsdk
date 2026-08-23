# fmpsdk Rewrite — Architecture Design Brief

## 1. Context & mandate

`fmpsdk` (github.com/daxm/fmpsdk) is a solo-maintained Python SDK wrapping the Financial
Modeling Prep (FMP) API. It's listed on FMP's own third-party integrations page — the only
Python entry there.

An audit of the current codebase against FMP's live API found:

- FMP discontinued its legacy `/api/v3/` and `/api/v4/` endpoints as of **August 31, 2025**.
  **90 of 143 (63%) of the package's current endpoint call sites are on the dead `v3` base**
  and return an FMP error object today for any non-grandfathered subscriber — confirmed by
  live-testing, not just reading the code.
- That error object has the same shape callers expect for real data (a `dict` where a
  `List[Dict]` is expected), which is why it went unnoticed: GitHub issue #60 flagged the
  failure mode 18 months ago and nothing caught it since.
- Beyond the outage, real coverage gaps exist against FMP's current ~360-endpoint `stable`
  API: whole categories (ESG, TipRanks analyst data, House-of-Representatives trading,
  Crowdfunding/Reg A/equity offerings, granular Form 13F, most of Bulk) have zero
  implementation today.

**Decision: full from-scratch rewrite, not a patch.** New files, new architecture. The
existing code may be read for institutional knowledge (validated constant lists, hard-won
quirks) but is not a structural starting point and is not edited in place.

**What this design pass is for:** produce a structural specification — package layout,
naming, taxonomy, and a resolved reasoning trail for the ambiguous cases below. **Not code.**
Implementation happens afterward, in a separate continuous session, against this spec.

## 2. Primary source material

- **`https://site.financialmodelingprep.com/api-docs.md`** — the authoritative input. Full
  structured markdown: every endpoint's name, description, exact URL with real example
  params, a parameter table, and an example JSON response. ~360+ documented `stable`
  endpoints. A local copy is at the scratchpad path this session used; re-fetch if needed —
  it's a public URL.
- FMP's pricing/plan comparison page groups endpoints into marketing categories (Company &
  Reference Data, Fundamental Data, Market Data, Ownership, Advanced Data, Other Markets,
  Bulk & Batch, etc.). Useful as a **draft input** for the alias-layer taxonomy in section
  3.2 — not a mandate, and not reliable on its own (see section 4, false-duplicate finding).

## 3. Decisions already made — design around these, do not re-litigate

### 3.1 Client-object design, not flat functions

Today's `fmpsdk.quote(apikey=..., symbol=...)` (apikey repeated on every call) becomes:

```python
client = fmpsdk.Client(api_key="...")   # or FMP_API_KEY env var fallback
```

### 3.2 Two-layer namespace: flat canonical methods + thin group aliases

- **Canonical layer** — flat methods on the client, named as closely as possible to FMP's
  own terminology (never invented synonyms), each name globally unique. This is the real
  contract.
- **Alias layer** — thin group objects (e.g. `client.ownership.form_13f_latest`) that are
  pure references to the same canonical methods, never a second implementation, never the
  *only* way to reach a function. Group names should be adapted from FMP's own category
  vocabulary (the way `boto3`'s service names mirror AWS's own naming, not an invented third
  taxonomy) — start from the pricing-page rollup, edit for coherence, don't copy blindly.
- Ship a **generated cross-reference table** (FMP doc term ↔ our method name) in the
  docs/README. This — not "our grouping happens to be intuitive" — is the actual
  discoverability guarantee.
- Because aliases are pure sugar over a stable flat contract, FMP reorganizing their own doc
  categories later is non-breaking for us — we edit aliases, not the real API surface.

### 3.3 Collision rule (validated against the live API, not just theory)

Scanned all ~360 catalogued endpoint slugs for leaf-name reuse across different resource
families. Found 8 candidates; live-tested all 8:

**Real collisions (2 real, distinct, working endpoints sharing a bare name):**
```
insider-trading/latest           → 200
institutional-ownership/latest   → 402   (both real)

sec-filings-company-search/cik   → 200
sec-filings-search/cik           → 400   (both real; "symbol" follows the same pattern)
```

**False positives — FMP's own docs list a bare slug that doesn't actually exist, alongside
the real nested one:**
```
williams                                     → 404 (doesn't exist)
technical-indicators/williams                → 402 (real)
press-releases / holdings / holder-performance-summary / industry-summary → all 404 bare,
  real only under news/, etf/, institutional-ownership/ respectively
```

**Rule:** where a genuine collision exists, qualify the canonical name with FMP's own
enclosing path segment (`insider_trading_latest` vs. `institutional_ownership_latest`). In
every case found, FMP's own path already supplies the needed disambiguator — no invented
qualifier was ever required. Apply this same test-before-trusting-the-docs discipline to the
rest of the catalog rather than assuming the nav/docs are internally consistent.

### 3.4 "One parameterized method vs. N flat methods" — resolve per family, don't default

Worked example already investigated: `sec-filings-search/{cik,symbol,form-type}` looks like
the classic `/users/1` vs `/users/2` anti-pattern (an ID that should be a parameter, not a
path segment) but isn't — FMP documents these as three separately-titled, separately-described
endpoints, each taking a **different parameter name** (`cik`, `symbol`, `formType`), not the
same parameter with different values. Leaning conclusion: keep as separate flat methods,
mirroring FMP's real model rather than inventing a `by=` abstraction FMP's own API doesn't
have. **Apply this same test systematically across the catalog** — for every family that
looks like an enumerated variant, check the actual documented parameters before deciding,
and flag anything genuinely ambiguous rather than resolving it silently.

### 3.5 Naming convention

- No bare/unsuffixed method name unless it is the *only* endpoint in its family. (The current
  codebase's `insider_trading()` — bare, but actually the `/search` variant, next to sibling
  functions that all carry their action suffix — is the bug this rule fixes.)
- snake_case, derived from FMP's kebab-case path segments, with the collision rule (3.3)
  and family judgment (3.4) applied on top of straight mechanical translation.
- Flag (don't silently resolve) cases like `insider_trading_transaction_types` and
  `acquisition_of_beneficial_ownership`, which are conceptually adjacent to the
  `insider-trading/*` family but don't nest under it in FMP's own URL — FMP's structure is
  not fully consistent, and that's expected, not a signal to force consistency we'd be
  inventing.

### 3.6 Fixed engineering decisions (context, not open questions for this pass)

- **Auth:** header (`apikey: KEY`), not query string. Constructor takes `api_key` or falls
  back to `FMP_API_KEY` env var. Key mutable post-construction for rotation.
- **HTTP:** sync only (`requests`), no async/httpx — deliberate deferral, not an oversight.
  Configurable timeouts.
- **Retry:** backoff on connection errors/timeouts/429/5xx only, never on 400/401/402/404.
  All calls are GET, so retries are safe by default.
- **Errors:** typed exception hierarchy, not silent `None`/error-dict returns:
  ```
  FMPError (base)
  ├── FMPAuthenticationError   (401/403)
  ├── FMPPlanLimitError        (402 — whole-endpoint AND single-parameter gating alike)
  ├── FMPRateLimitError        (429)
  ├── FMPNotFoundError         (404)
  ├── FMPValidationError       (400)
  └── FMPServerError           (5xx)
  ```
  `FMPPlanLimitError` message: *"Your current FMP plan doesn't include this request. See
  FMP's pricing plans to upgrade: https://site.financialmodelingprep.com/pricing-plans"* —
  says "request," not "endpoint," deliberately: a single symbol (e.g. MSTR) can be blocked on
  an endpoint that otherwise works fine (e.g. TSLA on the same `quote` call). FMP's own raw
  error text stays attached to the exception for detail.
- **Response typing:** stay `List[Dict]`-shaped at runtime (no pydantic, no new heavy
  dependency). Add `TypedDict` per response shape via `typing.cast()` at the JSON boundary —
  zero runtime cost, generated from the example JSON responses already in `api-docs.md`.
- **Logging:** `logging.getLogger("fmpsdk")`, never the root logger (current bug). Reserved
  for internal diagnostics — user-facing failures go through the exception hierarchy, never
  a silent log-and-return-`None`.
- **Reference data:** carry forward validated constant lists from the current `settings.py`
  (`INDUSTRY_VALUES`, `SECTOR_VALUES`, `PERIOD_VALUES`, etc.) as data, re-verified against
  current docs — real prior effort, not thrown out just because the code around it is new.
- **Explicitly out of scope, name it rather than drop it silently:** async/httpx client;
  FMP's WebSocket streaming API (a separate product surface — "Quote Subscription," "Market
  Stream Subscription" — found in the docs, not addressed here); proactive rate-limit
  self-throttling (no rate-limit headers exist to base it on); a maintained
  endpoint-to-minimum-plan metadata table (v1.1, not core); pagination auto-iteration helpers.
- **Versioning** (context only, not this pass's concern): package keeps its existing
  `DATE.PATCH` CalVer scheme unchanged. Verified via `packaging.version` that any scheme
  leading with a small number (`2.0.0`, `2.DATE.PATCH`, etc.) sorts **behind** the existing
  `20250102.0` release history under real pip version comparison — so nothing resembling a
  leading major-version digit should be proposed anywhere, including in module/package
  naming that might imply a version number.
- **Testing hooks** (context for how the module structure should support scaffolding, not
  this pass's job to write): every method gets a scaffolded test in the same pass it's
  designed, tiered `unit` (mocked)/`live` (free-tier-reachable)/`ultimate` (gated,
  deferred). The structure this pass proposes should make "one test file mirrors one
  method-group" straightforward.

## 4. Deliverable requested

A structural design document covering:

1. **Top-level group taxonomy** (the alias layer) — names, and which canonical methods
   belong to each, derived from FMP's category vocabulary but edited for coherence.
2. **Canonical flat-method naming** for the full `api-docs.md` catalog, or a precisely
   stated, systematic naming rule plus a representative worked sample, if hand-enumerating
   ~360 names in one pass isn't practical — applying the collision rule from 3.3.
3. **The one-method-vs-N-methods question (3.4)** resolved systematically across the whole
   catalog, not just the `sec-filings-search` example — flag genuinely ambiguous families
   rather than picking silently.
4. **Any other structural inconsistency found** in FMP's own path structure (nesting that
   doesn't match conceptual grouping, naming drift between endpoint families, etc.), each
   with a recommended resolution and the reasoning behind it.
5. Wherever this design deviates from a naive mechanical translation of FMP's URL structure,
   say why — the point of using a stronger model for this pass is the judgment calls, not
   the transcription.

**Explicitly not this pass's job:** writing code; deciding anything already fixed in section
3.6 (error handling, retries, response typing, logging, testing internals); anything about
release process or versioning.
