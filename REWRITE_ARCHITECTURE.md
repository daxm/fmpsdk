# fmpsdk Rewrite — Architecture Specification

**Status:** structural specification, ready to implement against. No code in this document.
**Source of truth:** `https://site.financialmodelingprep.com/api-docs.md`, re-fetched live and
verified byte-identical to the session cache before this pass began.
**Companion document:** `REWRITE_DESIGN_BRIEF.md`. This document is written to stand alone —
you do not need to re-read the brief to implement from it — but section 10 records where this
pass questions decisions the brief locked in, and those need the maintainer's sign-off.

---

## 0. Executive summary

| | |
|---|---|
| Documented endpoint sections in `api-docs.md` | 287 |
| …that are REST endpoints with a `stable/` URL | **276** |
| …that are WebSocket / Socket.io (out of scope per brief 3.6) | 11 |
| **Unique `stable/` paths** after removing FMP's own doc duplication | **243** |
| **Canonical client methods** after the one family collapse recommended in §5 | **238** |
| Alias groups | **29** |
| Methods cross-listed into more than one alias group | 10 |
| Genuine leaf-name collisions found | 3 leaf names / 6 endpoints |
| Collisions that survive this spec's naming rule | **0** |

**The single most consequential finding of this pass:** the catalog is **243 unique endpoints,
not ~360**. The gap is not a doc error and not endpoints we are missing — it is FMP documenting
**the same path up to five times**, once per asset class. `stable/quote` is documented as
"Stock Quote," "Index Quote," "Commodities Quote," "Full Cryptocurrency Quote," and "Forex
Quote" — five doc sections, five titles, one endpoint, one identical parameter table. Thirteen
paths are duplicated this way, accounting for 33 of the 276 REST sections.

A naive one-method-per-doc-section translation would ship five methods that issue byte-identical
HTTP requests. Section 4 handles this; it is the clearest case in the whole catalog where the
alias layer earns its existence, because the *asset-class views* users actually want
(`client.crypto.quote`) are recovered as aliases without duplicating a single implementation.

**The second finding, which touches a decision already fixed in brief 3.6:** the `period`
parameter accepts **three mutually incompatible value sets** across the 25 endpoints that take
it. The carried-forward `PERIOD_VALUES = ["annual", "quarter"]` from the legacy `settings.py` is
correct for only 7 of those 25. See §8.1.

---

## 1. How to read this document

- §2 — the naming rule. One rule, stated precisely, mechanically checkable.
- §3 — the alias-layer taxonomy: 29 group names and what each is for.
- §4 — duplicate-path deduplication (the 243-vs-276 finding) and how aliases recover the views.
- §5 — the flat-vs-parameterized question (brief 3.4), resolved with an explicit four-part test
  applied to every candidate family in the catalog. Includes the families that could not be
  cleanly resolved.
- §6 — the full 238-method catalog, grouped, with FMP paths and parameters.
- §7 — structural inconsistencies in FMP's own path design, each with a recommended resolution.
- §8 — parameter-level findings that affect implementation (constants, doc drift, response-type
  exceptions).
- §9 — where this spec deliberately deviates from mechanical URL translation, and why.
- §10 — review of the brief itself: decisions in section 3 that this pass believes will cause
  problems at full-catalog scale.
- §11 — package layout implied by all of the above.

---

## 2. Canonical naming rule

### 2.1 The rule

> **A canonical method name is the endpoint's full `stable/` path with `/` and `-` replaced by
> `_`, lowercased. Nothing is added, nothing is removed, nothing is reordered.**

```
stable/quote                                         -> quote
stable/insider-trading/latest                        -> insider_trading_latest
stable/institutional-ownership/latest                -> institutional_ownership_latest
stable/sec-filings-search/cik                        -> sec_filings_search_cik
stable/sec-filings-company-search/cik                -> sec_filings_company_search_cik
stable/institutional-ownership/extract-analytics/holder
                                                     -> institutional_ownership_extract_analytics_holder
stable/etf/holdings                                  -> etf_holdings
stable/news/press-releases-latest                    -> news_press_releases_latest
stable/funds/disclosure                              -> funds_disclosure
```

### 2.2 Verification

Applied mechanically to all 243 unique paths, this rule yields:

- **243 names, 243 unique** — zero collisions.
- **Zero Python keyword conflicts.**
- Longest name 50 characters (`institutional_ownership_holder_performance_summary`).
- Nine names exceed 36 characters; five of those are the `institutional-ownership/*` family,
  which is genuinely five path segments deep in FMP's own URL.

### 2.3 Why full-path and not bare-leaf

The brief (3.3, 3.5) reads as though the default is the **bare leaf name**, with FMP's enclosing
path segment added *only where a collision is detected*. That default does not survive contact
with the full catalog. Bare-leaf would produce:

```
institutional-ownership/extract     -> extract()      (extract what?)
institutional-ownership/dates       -> dates()
funds/disclosure                    -> disclosure()
etf/holdings                        -> holdings()
news/stock                          -> stock()
insider-trading/search              -> search()
technical-indicators/sma            -> sma()
```

Seven methods on a client object named `extract`, `dates`, `disclosure`, `holdings`, `stock`,
`search`, and `sma` is not a usable API surface, and each one would have to be individually
argued back to a qualified name — which is exactly the ad-hoc, per-name judgment the brief is
trying to eliminate.

Full-path qualification is **strictly better and strictly simpler**: it produces the qualified
names the brief wants in the collision cases (`insider_trading_latest` vs.
`institutional_ownership_latest`, `sec_filings_search_cik` vs. `sec_filings_company_search_cik`
— exactly the names the brief specifies), it produces good names in the non-collision cases too,
and it makes collisions **structurally impossible** rather than something a maintainer has to
remember to test for when FMP adds an endpoint.

**This is not an override of brief 3.3 — it is a way of satisfying 3.3 by construction.** The
brief's rule ("qualify with FMP's own enclosing path segment") is applied unconditionally
instead of conditionally. Every name 3.3 explicitly specifies is unchanged.

> **Resolved:** accepted as proposed, including all three §2.5 "ugly name" exceptions kept as-is
> (no further exceptions to be added).

### 2.4 Property this rule buys you

Every method name round-trips to its URL and back with a single `str.replace`. That means:

- The FMP-term ↔ method-name cross-reference table required by brief 3.2 is **generated, not
  maintained** — it is a one-line transformation over the docs.
- A user who has an FMP URL can find the method by mechanical transformation, and vice versa.
  This is the actual discoverability guarantee, and it is stronger than "our grouping is
  intuitive."
- Adding a new FMP endpoint requires zero naming judgment.

Preserving this property is the reason for several decisions below that otherwise look like
they favour ugliness over ergonomics (§2.5, §7.1, §7.2).

### 2.5 Accepted ugly names — zero lexical exceptions

Three FMP slugs run words together. The rule is applied anyway:

| FMP path | Canonical name | The "nicer" name we are declining |
|---|---|---|
| `technical-indicators/standarddeviation` | `technical_indicators_standarddeviation` | `..._standard_deviation` |
| `dowjones-constituent` | `dowjones_constituent` | `dow_jones_constituent` |
| `batch-mutualfund-quotes` | `batch_mutualfund_quotes` | `batch_mutual_fund_quotes` |

**Reasoning:** each of these would be individually defensible, but together they establish that
the rule has a judgment-call escape hatch — and the next maintainer will not know where its
boundary is. Three slightly awkward names is a smaller cost than a naming rule that requires
taste. Note that FMP's own JSON response key for the first one is `standardDeviation`, i.e. FMP
itself is inconsistent between its path and its payload; splitting the word in our method name
would make us agree with the payload and disagree with the path, which is the wrong trade under
§2.4.

*Maintainer call:* if you want these three split, say so once and the exception list stays
frozen at exactly these three, enumerated in code. Do not leave it open-ended.

### 2.6 Parameter naming

Python parameter names are FMP's query-parameter names converted `camelCase` → `snake_case`.
`from`/`to` are Python-safe as `from_`/`to`? **No** — `from` is a reserved word. Use
`from_date` / `to_date` as the Python parameter names for the `from` / `to` query parameters,
consistently across all 60+ endpoints that take them, and map them back to `from` / `to` on the
wire. This is the one place a Python-level rename is forced by the language rather than chosen.

All other parameters translate mechanically: `periodLength` → `period_length`, `reportingCik` →
`reporting_cik`, `expertUID` → `expert_uid`, `sicCode` → `sic_code`, `includeAllShareClasses` →
`include_all_share_classes`, `senateID` → `senate_id`, `totalsCol` → `totals_col`.

---

## 3. Alias-layer taxonomy

### 3.1 Derivation rule

Group names are FMP's own top-level documentation categories (the `#` headings in
`api-docs.md`), snake_cased, **edited only where the verbatim name fails on one of three
specific grounds**:

- **(a) factually wrong** — the name misdescribes its own contents;
- **(b) stutters** — `client.<group>.<method>` would repeat the same words;
- **(c) describes FMP's business relationship rather than the data.**

Style preferences (pluralization, brevity) are explicitly *not* grounds for an edit. This keeps
the taxonomy anchored to FMP's vocabulary the way `boto3` service names are anchored to AWS's,
per brief 3.2.

### 3.2 The five edits

| FMP category | Group name | Ground | Reasoning |
|---|---|---|---|
| `Senate` | `congress` | (a) | The category contains `house-latest`, `house-trades`, `house-trades-by-name`, `house-trades-by-id` — four House of Representatives endpoints. "Senate" is factually wrong for a third of its own contents. `congress` covers both chambers and is standard U.S. terminology, not an invented synonym. |
| `Partners` | `tipranks` | (c) | All seven endpoints are TipRanks; every slug is literally `tipranks-*`. "Partners" describes FMP's commercial arrangement. If FMP adds a second partner, we add a second group — which is the correct behaviour, since the data is unrelated. |
| `Form13F` | `institutional_ownership` | (a)+(b) | Every path in the category is `institutional-ownership/*`. "Form 13F" names the SEC document; the path names the concept. Using the path also makes the group name and the method prefix agree, which matters given the brief's own collision example (`institutional_ownership_latest`). |
| `EtfAndMutualFunds` | `funds` | (b) | Verbatim gives `client.etf_and_mutual_funds.etf_holdings()`. `funds` matches FMP's own `funds/` path prefix and covers both ETFs and mutual funds. |
| `DiscountedCashFlow` | `dcf` | (b) | Verbatim gives `client.discounted_cash_flow.discounted_cash_flow()`. FMP's own sub-heading for this category is literally "Dcf". |

`Websockets` is dropped entirely — out of scope per brief 3.6. Its 11 doc sections are not
endpoints; two are `wss://` connection URLs and nine are message payload schemas.

The remaining 24 categories are used verbatim: `search`, `directory`, `analyst`, `calendar`,
`chart`, `company`, `commitment_of_traders`, `economics`, `esg`, `statements`, `indexes`,
`commodity`, `crypto`, `fundraisers`, `forex`, `insider_trades`, `market_performance`,
`market_hours`, `technical_indicators`, `news`, `quote`, `sec_filings`, `earnings_transcript`,
`bulk`.

### 3.3 Group name vs. method prefix drift — accepted, not fixed

`client.insider_trades` contains methods prefixed `insider_trading_`. FMP's category is
"InsiderTrades"; FMP's paths are `insider-trading/*`. Both are FMP's own vocabulary and they
disagree with each other.

**Resolution: keep both, unchanged.** The group name follows FMP's category (rule §3.1); the
method name follows FMP's path (rule §2.1). Forcing agreement would require overriding one of
FMP's two vocabularies with the other, i.e. inventing. The cross-reference table makes the
mismatch a non-issue for discoverability. The same applies to `dcf` (methods prefixed
`discounted_cash_flow` / `custom_`), `funds` (methods prefixed `etf_` and `funds_`), and
`congress` (methods prefixed `senate_` and `house_`).

### 3.4 Multi-group membership

A canonical method may appear in more than one alias group. Exactly **one** group is its
**primary** group; the rest are **cross-listings**.

- Primary group determines documentation placement and the test file that mirrors it
  (brief 3.6: "one test file mirrors one method-group").
- Cross-listings are pure attribute references — the same bound method object, no wrapper.
- Cross-listings exist **only** where FMP itself documents the same path under more than one
  category. No cross-listing is invented by us. There are exactly 10 (§4).

`assert client.crypto.quote is client.quote.quote` must hold. This is worth an actual test —
it is the property that guarantees the alias layer never becomes a second implementation
(brief 3.2).

### 3.5 Group directory

| Group | Primary methods | One-line purpose |
|---|---:|---|
| `search` | 7 | Identifier lookup (symbol / name / CIK / CUSIP / ISIN) and the stock screener. |
| `directory` | 10 | Whole-universe reference lists: symbols, exchanges, sectors, industries, countries. |
| `analyst` | 8 | Sell-side estimates, ratings, price targets, and grades. |
| `calendar` | 9 | Date-driven corporate events: dividends, earnings, IPOs, splits. |
| `chart` | 5 | Historical price series, EOD and intraday, for every asset class. |
| `company` | 17 | Company reference and profile data: market cap, float, executives, notes, M&A. |
| `commitment_of_traders` | 3 | CFTC Commitment-of-Traders reports and analysis. |
| `dcf` | 4 | Discounted-cash-flow valuations, standard and custom-input. |
| `economics` | 4 | Macro series, treasury rates, economic calendar, market risk premium. |
| `esg` | 3 | ESG disclosures, ratings, and benchmarks. |
| `funds` | 9 | ETF and mutual-fund composition, info, and holder disclosures. |
| `statements` | 27 | Financial statements and everything computed directly from them. |
| `institutional_ownership` | 8 | Form 13F institutional holdings, holders, and derived analytics. |
| `indexes` | 7 | Stock-market indexes and their current/historical constituent lists. |
| `commodity` | 1 | Commodity instrument reference list (quotes and charts are cross-listed in). |
| `crypto` | 1 | Cryptocurrency instrument reference list (quotes and charts cross-listed in). |
| `fundraisers` | 6 | Reg CF crowdfunding and Reg D/A equity offerings. |
| `forex` | 1 | FX pair reference list (quotes and charts cross-listed in). |
| `insider_trades` | 6 | Form 4 insider transactions, statistics, beneficial-ownership acquisitions. |
| `market_performance` | 11 | Sector/industry performance and P/E, snapshot and historical, plus leaders. |
| `market_hours` | 3 | Exchange trading sessions and holiday calendars. |
| `technical_indicators` | 9 | Computed technical-indicator series. |
| `news` | 10 | News, press releases, and FMP editorial articles. |
| `quote` | 16 | Real-time and aftermarket quotes, single and batch. |
| `sec_filings` | 12 | SEC filing search, SEC company identity, SIC industry classification. |
| `earnings_transcript` | 4 | Earnings-call transcripts and availability metadata. |
| `congress` | 12 | U.S. Senate and House financial disclosures, trades, member profiles. |
| `bulk` | 18 | Whole-universe bulk downloads. |
| `tipranks` | 7 | TipRanks partner analyst data. |
| **Total** | **238** | |

The three single-method asset-class groups (`commodity`, `crypto`, `forex`) look anaemic in the
"primary" column and are not. Each reaches 7 members once cross-listings are attached; see §4.3.

---

## 4. Duplicate-path deduplication

### 4.1 The finding

276 REST doc sections resolve to 243 unique `stable/` paths. Thirteen paths are documented more
than once, always because FMP repeats the same generic endpoint inside each asset-class chapter:

| `stable/` path | Times documented | Doc titles FMP gives it |
|---|---:|---|
| `quote` | 5 | Stock Quote · Index Quote · Commodities Quote · Full Cryptocurrency Quote · Forex Quote |
| `quote-short` | 5 | Stock Quote Short · Index Short Quote · Commodities Quote Short · Cryptocurrency Quote Short · Forex Short Quote |
| `historical-price-eod/light` | 5 | Stock Chart Light · Historical Index Light Chart · Light Chart · Historical Cryptocurrency Light Chart · Historical Forex Light Chart |
| `historical-price-eod/full` | 5 | Stock Price and Volume Data · Historical Index Full Chart · Full Chart · Historical Cryptocurrency Full Chart · Historical Forex Full Chart |
| `historical-chart/1min` | 5 | (one per asset class) |
| `historical-chart/5min` | 5 | (one per asset class) |
| `historical-chart/1hour` | 5 | (one per asset class) |
| `batch-index-quotes` | 2 | All Index Quotes · Full Index Quotes |
| `batch-commodity-quotes` | 2 | All Commodities Quotes · Full Commodities Quotes |
| `batch-crypto-quotes` | 2 | All Cryptocurrencies Quotes · Full Cryptocurrency Quotes |
| `batch-forex-quotes` | 2 | Batch Forex Quotes · Full Forex Quote |
| `earnings-transcript-list` | 2 | Earnings Transcript List *(Directory)* · Available Transcript Symbols *(EarningsTranscript)* |

The parameter tables are identical across copies in every case but one (§4.2). The example
responses are identical in shape. These are unambiguously the same endpoint.

### 4.2 One asymmetry, and it is a doc-completeness bug, not an API difference

The `Chart` chapter documents `historical-chart/{interval}` with parameters
`symbol, from, to, nonadjusted, extended`. The `Indexes` / `Commodity` / `Crypto` / `Forex`
copies of the *same path* document only `symbol, from, to`.

The server is one server. `nonadjusted` and `extended` are accepted on the path regardless of
what symbol you pass; the asset-class chapters simply did not repeat the two parameters that
are only *meaningful* for equities.

**Resolution:** the single canonical method carries the **union** — all five parameters. Document
in the docstring that `nonadjusted` and `extended` are equity-only in effect. Do not build
per-asset-class parameter validation; that would be inventing a restriction FMP does not
enforce, and it would break the day FMP extends extended-hours data to another asset class.

### 4.3 How the asset-class views are recovered

This is the case that justifies the whole two-layer design. One implementation, five names:

```
client.quote.quote        (primary)
client.indexes.quote      (cross-listing)
client.commodity.quote    (cross-listing)
client.crypto.quote       (cross-listing)
client.forex.quote        (cross-listing)
```

The 10 cross-listings, exhaustively:

| Canonical method | Primary group | Cross-listed into |
|---|---|---|
| `quote` | `quote` | `indexes`, `commodity`, `crypto`, `forex` |
| `quote_short` | `quote` | `indexes`, `commodity`, `crypto`, `forex` |
| `historical_price_eod_light` | `chart` | `indexes`, `commodity`, `crypto`, `forex` |
| `historical_price_eod_full` | `chart` | `indexes`, `commodity`, `crypto`, `forex` |
| `historical_chart` | `chart` | `indexes`, `commodity`, `crypto`, `forex` |
| `batch_index_quotes` | `quote` | `indexes` |
| `batch_commodity_quotes` | `quote` | `commodity` |
| `batch_crypto_quotes` | `quote` | `crypto` |
| `batch_forex_quotes` | `quote` | `forex` |
| `earnings_transcript_list` | `earnings_transcript` | `directory` |

Which means the asset-class groups are substantial after all:

```
client.crypto.cryptocurrency_list          client.commodity.commodities_list
client.crypto.quote                        client.commodity.quote
client.crypto.quote_short                  client.commodity.quote_short
client.crypto.batch_crypto_quotes          client.commodity.batch_commodity_quotes
client.crypto.historical_price_eod_light   client.commodity.historical_price_eod_light
client.crypto.historical_price_eod_full    client.commodity.historical_price_eod_full
client.crypto.historical_chart             client.commodity.historical_chart
```

**Primary-group assignment rule for duplicates:** the primary is the group whose *subject* the
endpoint actually is, which for all 13 duplicates is the generic-mechanism group (`quote`,
`chart`) rather than the asset class, and for `earnings-transcript-list` is the subject-matter
group (`earnings_transcript`) rather than the catch-all (`directory`).

### 4.4 What NOT to do

Do not create `client.crypto.crypto_quote()` or any per-asset-class canonical name. There is no
`crypto-quote` path. Inventing one breaks §2.4's round-trip property and creates five methods
that must be kept in sync forever.

---

## 5. Flat methods vs. one parameterized method (brief §3.4), resolved

### 5.1 The test

Applied to every set of sibling endpoints in the catalog that differ only by a trailing path
segment. **Collapse into one parameterized method only if all four hold:**

- **V1 — Identical parameter sets.** Same required parameters, same optional parameters, same
  names. (A family whose members take *different* parameter names is not an enumeration; it is a
  set of distinct operations. This is the brief's own `sec-filings-search` reasoning, generalized.)
- **V2 — Identical response schema.** Same keys, same types. Directly load-bearing given brief
  3.6's per-response-shape `TypedDict` decision: two shapes cannot share one method's return type
  without either a union return or a fabricated common supertype.
- **V3 — FMP itself treats the varying token as a value.** The token set must appear as the
  documented value of some FMP *query parameter* somewhere in the API. This is the test that
  keeps us from inventing an abstraction FMP does not have — if FMP has already conceded
  somewhere that the token is a value rather than an identity, we are following FMP, not
  overriding it.
- **V4 — FMP documents the members as one family** under a single sub-heading.

Otherwise: **N flat methods.**

V3 is the discriminating test and it is deliberately strict. Without it, "these two endpoints
have the same params and shape" would collapse things like `biggest-gainers` / `biggest-losers`,
which are plainly two different questions.

### 5.2 Results — every candidate family in the catalog

| Family | Members | V1 | V2 | V3 | V4 | Decision |
|---|---:|:--:|:--:|:--:|:--:|---|
| `historical-chart/{1min,5min,15min,30min,1hour,4hour}` | 6 | ✅ | ✅ | ✅ | ✅ | **COLLAPSE** → `historical_chart(symbol, timeframe, …)` |
| `technical-indicators/{sma,ema,wma,dema,tema,rsi,standarddeviation,williams,adx}` | 9 | ✅ | ❌ | ❌ | ✅ | 9 flat methods |
| `historical-price-eod/{light,full,non-split-adjusted,dividend-adjusted}` | 4 | ✅ | ❌ | ❌ | ✅ | 4 flat methods |
| `sec-filings-search/{form-type,symbol,cik}` | 3 | ❌ | — | — | ✅ | 3 flat methods |
| `sec-filings-company-search/{name,symbol,cik}` | 3 | ❌ | — | — | ❌ | 3 flat methods |
| `{sp500,nasdaq,dowjones}-constituent` | 3 | ✅ | ✅ | ❌ | ✅ | 3 flat — **flagged, §5.4a** |
| `historical-{sp500,nasdaq,dowjones}-constituent` | 3 | ✅ | ✅ | ❌ | ✅ | 3 flat — **flagged, §5.4a** |
| `batch-{index,commodity,crypto,forex,etf,mutualfund}-quotes` | 6 | ✅ | ✅ | ❌ | ❌ | 6 flat — **flagged, §5.4b** |
| `news/{general,press-releases,stock,crypto,forex}-latest` | 5 | ✅ | ✅ | ❌ | ✅ | 5 flat — **flagged, §5.4c** |
| `news/{press-releases,stock,crypto,forex}` | 4 | ✅ | ✅ | ❌ | ✅ | 4 flat — **flagged, §5.4c** |
| `institutional-ownership/*` | 8 | ❌ | ❌ | ❌ | ❌ | 8 flat methods |
| `funds/disclosure*` | 4 | ❌ | ❌ | ❌ | ✅ | 4 flat methods |
| `{income,balance-sheet,cash-flow}-statement` and all `-ttm` / `-growth` / `-as-reported` variants | 15 | ✅ | ❌ | ❌ | ✅ | 15 flat methods |
| `{crowdfunding-offerings,fundraising}{,-latest,-search}` | 6 | ❌ | ❌ | ❌ | ✅ | 6 flat methods |
| `{senate,house}-{latest,trades,trades-by-name,trades-by-id}` | 8 | ✅ | ✅ | ❌ | ✅ | 8 flat — **flagged, §5.4d** |
| `{sector,industry}-{performance,pe}-snapshot` + `historical-{sector,industry}-{performance,pe}` | 8 | ❌ | ✅ | ❌ | ✅ | 8 flat methods |
| `*-bulk` (18) | 18 | ❌ | ❌ | ❌ | ✅ | 18 flat methods |
| `insider-trading/{latest,search,statistics,reporting-name}` | 4 | ❌ | ❌ | ❌ | ❌ | 4 flat methods |
| `search-{symbol,name,cik,cusip,isin,exchange-variants}` | 6 | ❌ | ❌ | ❌ | ✅ | 6 flat methods |
| `quote` / `quote-short` | 2 | ✅ | ❌ | ❌ | ✅ | 2 flat methods |

### 5.3 The one collapse, in detail

`historical-chart/{1min,5min,15min,30min,1hour,4hour}` → **`historical_chart(symbol, timeframe, from_date=None, to_date=None, nonadjusted=None, extended=None)`**

- **V1 ✅** — identical parameter tables across all six (once §4.2's doc-completeness gap is
  accounted for).
- **V2 ✅** — verified against the example responses: every interval returns
  `{date, open, low, high, close, volume}`. Identical, including key order.
- **V3 ✅ — this is the decisive evidence.** FMP's `technical-indicators/*` endpoints take a
  **required query parameter literally named `timeframe`**, documented with the values
  `1min, 5min, 15min, 30min, 1hour, 4hour, 1day`. That is the same token vocabulary FMP puts in
  the `historical-chart` **path**. FMP has already decided, in its own API, that a bar interval
  is a parameter value. We are not inventing a `by=`-style abstraction here; we are using FMP's
  own parameter name for FMP's own token set.
- **V4 ✅** — all six sit under a single "Intraday" sub-heading.

**Wrinkle, stated honestly:** the two token sets are not *identical*. `technical-indicators`
accepts `1day`; `historical-chart` has no `1day` path (daily bars live at
`historical-price-eod/full`). So `historical_chart` accepts 6 of the 7 `timeframe` tokens. This
requires two constants, not one — see §8.2. The subset relationship weakens V3 slightly but does
not break it: the concept is identical and the vocabulary is FMP's.

**Cost of the collapse:** it is the only place in this spec where a method name does not
round-trip to a URL by §2.4's string replacement. `historical_chart` maps to
`historical-chart/{timeframe}`, one template rather than one path. Mitigation: the generated
cross-reference table lists all six paths against the one method, and the docstring shows the
mapping explicitly.

**Rejected alternative:** keep all six flat *and* add a parameterized convenience method. That
violates brief 3.2's "never the only way to reach a function, never a second implementation" in
spirit — it creates two ways to do the same thing at the canonical layer, which is precisely
what the flat-canonical design exists to prevent.

**This is the single decision in this spec that most deserves the maintainer's explicit
sign-off**, because it is the one place where the spec chooses ergonomics (6 methods → 1) over
strict path mirroring. See §9.1.

> **Resolved (maintainer sign-off obtained):** collapse accepted as specified.

### 5.4 Families that could NOT be cleanly resolved

These four pass some tests and fail others in ways where reasonable people differ. Each has a
recommendation and the case against it. **Flagged rather than silently decided, per brief 3.4.**

#### 5.4a Index constituents (6 endpoints)

```
sp500-constituent · nasdaq-constituent · dowjones-constituent
historical-sp500-constituent · historical-nasdaq-constituent · historical-dowjones-constituent
```

*For collapsing:* zero parameters, identical response schema (verified: all three current
endpoints return `{symbol, name, sector, subSector, headQuarter, dateFirstAdded, cik, founded}`),
same sub-heading, and three near-identical methods is the textbook parameterization case.
`index_constituents(index="sp500")` reads well.

*Against (why the recommendation is flat):* **V3 fails hard.** These are not siblings under a
shared path — they are three *top-level* slugs that happen to share a suffix. `sp500`, `nasdaq`,
and `dowjones` appear nowhere in FMP's API as the value of any query parameter. Collapsing means
we author and maintain a private `{"sp500": "sp500-constituent", ...}` mapping — a genuine
invention — and the day FMP adds `russell2000-constituent` we must ship a release before users
can call it, whereas with flat methods they get a new method that mirrors the new path.

**Recommendation: 6 flat methods.** Confidence: medium. If the maintainer prefers the collapse,
this is the most defensible of the four to reverse, because the token set is tiny and closed.

> **Resolved:** flat, as recommended.

#### 5.4b Batch quotes by asset class (6 endpoints)

```
batch-index-quotes · batch-commodity-quotes · batch-crypto-quotes
batch-forex-quotes · batch-etf-quotes · batch-mutualfund-quotes
```

*For collapsing:* identical parameter (`short`), identical response schema (verified:
`{symbol, price, change, volume}`), obviously an enumeration over asset class.

*Against:* **V3 and V4 both fail.** No FMP query parameter takes `index|commodity|crypto|forex|etf|mutualfund`
as a value, and FMP splits these six across two different chapters (four in the asset-class
chapters, all six in `Quote/Batch List`). Also note `batch-exchange-quote` sits in the same
sub-heading with the same response shape but takes `exchange*` — so a collapsed
`batch_quotes(asset_class=...)` would still leave one odd sibling out, which is a smell.

**Recommendation: 6 flat methods.** Confidence: high.

> **Resolved:** flat, as recommended.

#### 5.4c News by category (9 endpoints)

```
news/general-latest · news/press-releases-latest · news/stock-latest · news/crypto-latest · news/forex-latest
news/press-releases · news/stock · news/crypto · news/forex
```

*For collapsing:* within each of the two sub-families, parameters and response shapes match.

*Against:* the two sub-families **cannot** merge into one method (`*-latest` takes no `symbols`;
the others require `symbols*`) — that is V1 failing, and it is the brief's `sec-filings-search`
situation exactly. Within each sub-family, V3 fails: `general|press-releases|stock|crypto|forex`
is not an FMP parameter value anywhere. And `general` has no by-symbol counterpart, so the two
sub-families would have *different* category enums — 5 vs. 4 — which is a strong signal these
are not one enumerated dimension.

**Recommendation: 9 flat methods.** Confidence: high. Note `fmp-articles` is a tenth, unrelated
endpoint in the same group (FMP editorial content, not third-party news) and must not be folded
in — different path root, different response shape.

> **Resolved:** flat, as recommended.

#### 5.4d Senate vs. House (8 endpoints)

```
senate-latest / house-latest · senate-trades / house-trades
senate-trades-by-name / house-trades-by-name · senate-trades-by-id / house-trades-by-id
```

*For collapsing:* perfectly parallel, identical parameters, identical response shapes. A
`chamber="senate"|"house"` parameter is the obvious modelling.

*Against:* **these are not siblings under a shared path at all** — they are eight independent
top-level slugs. There is no varying trailing segment; the discriminator is a *prefix*. And the
parallelism is incomplete: `senate-profile`, `senate-positions`, `senate-net-worth`, and
`senate-net-worth-aggregated` have **no House counterpart**, so a `chamber` parameter would be
valid on exactly half the group and meaningless on the other half.

**Recommendation: 8 flat methods.** Confidence: high. See §7.5 for the related FMP parameter-naming
bug in this family, which the implementation must expose rather than silently correct.

> **Resolved:** flat, as recommended.

### 5.5 Families explicitly confirmed as flat (agreeing with the brief)

- **`sec-filings-search/{cik,symbol,form-type}`** — confirmed. Required parameters are `cik*`,
  `symbol*`, `formType*` respectively: three different parameter *names*, not one parameter with
  three values. The brief's leaning conclusion is correct.
- **`sec-filings-company-search/{cik,symbol,name}`** — same reasoning; note the third member's
  required parameter is `company*`, not `name*`, and it is documented under a *different*
  sub-heading ("Search Filings") from its two siblings ("Company Info"). Two independent
  reasons to keep flat.
- **`technical-indicators/*`** — 9 flat. V2 fails: each returns OHLCV **plus a value key named
  after the indicator** (`sma`, `ema`, `wma`, `dema`, `tema`, `rsi`, `standardDeviation`,
  `williams`, `adx`). Under brief 3.6's per-shape `TypedDict` rule these are nine distinct
  response types; one method would have to return a nine-way union. V3 also fails — FMP never
  names the indicator as a query value.
- **`historical-price-eod/{light,full,non-split-adjusted,dividend-adjusted}`** — 4 flat. V2 fails
  decisively; verified shapes: `light` → `{symbol, date, price, volume}`; `full` →
  `{symbol, date, open, high, low, close, volume, change, changePercent, vwap}`;
  `non-split-adjusted` and `dividend-adjusted` → `{symbol, date, adjOpen, adjHigh, adjLow, adjClose, volume}`.
  Note the last two share a shape but answer different questions, so they stay separate on V3/V4
  grounds anyway.

---

## 6. Full canonical catalog

238 methods across 29 groups. Paths are relative to `https://financialmodelingprep.com/stable/`.
Parameters are FMP's own query-parameter names; `*` marks required. See §2.6 for the Python
parameter-name transformation.


#### `client.search` — Identifier lookup (symbol/name/CIK/CUSIP/ISIN) and the screener.

*7 primary methods*

| canonical method | FMP `stable/` path | params (`*` = required) | also cross-listed in |
|---|---|---|---|
| `company_screener` | `company-screener` | `marketCapMoreThan`, `marketCapLowerThan`, `sector`, `industry`, `betaMoreThan`, `betaLowerThan`, `priceMoreThan`, `priceLowerThan`, `dividendMoreThan`, `dividendLowerThan`, `volumeMoreThan`, `volumeLowerThan`, `exchange`, `country`, `isEtf`, `isFund`, `isActivelyTrading`, `page`, `limit`, `includeAllShareClasses` | — |
| `search_cik` | `search-cik` | `cik*`, `limit` | — |
| `search_cusip` | `search-cusip` | `cusip*` | — |
| `search_exchange_variants` | `search-exchange-variants` | `symbol*` | — |
| `search_isin` | `search-isin` | `isin*` | — |
| `search_name` | `search-name` | `query*`, `limit`, `exchange` | — |
| `search_symbol` | `search-symbol` | `query*`, `limit`, `exchange` | — |

#### `client.directory` — Whole-universe reference lists: symbols, exchanges, sectors, industries, countries.

*10 primary methods*

| canonical method | FMP `stable/` path | params (`*` = required) | also cross-listed in |
|---|---|---|---|
| `actively_trading_list` | `actively-trading-list` | — | — |
| `available_countries` | `available-countries` | — | — |
| `available_exchanges` | `available-exchanges` | `extended` | — |
| `available_industries` | `available-industries` | — | — |
| `available_sectors` | `available-sectors` | — | — |
| `cik_list` | `cik-list` | `page`, `limit` | — |
| `etf_list` | `etf-list` | — | — |
| `financial_statement_symbol_list` | `financial-statement-symbol-list` | — | — |
| `stock_list` | `stock-list` | — | — |
| `symbol_change` | `symbol-change` | `invalid`, `limit` | — |

#### `client.analyst` — Sell-side estimates, ratings, price targets, grades.

*8 primary methods*

| canonical method | FMP `stable/` path | params (`*` = required) | also cross-listed in |
|---|---|---|---|
| `analyst_estimates` | `analyst-estimates` | `symbol*`, `period*`, `page`, `limit` | — |
| `grades` | `grades` | `symbol*` | — |
| `grades_consensus` | `grades-consensus` | `symbol*` | — |
| `grades_historical` | `grades-historical` | `symbol*`, `limit` | — |
| `price_target_consensus` | `price-target-consensus` | `symbol*` | — |
| `price_target_summary` | `price-target-summary` | `symbol*` | — |
| `ratings_historical` | `ratings-historical` | `symbol*`, `limit` | — |
| `ratings_snapshot` | `ratings-snapshot` | `symbol*` | — |

#### `client.calendar` — Date-driven corporate events: dividends, earnings, IPOs, splits.

*9 primary methods*

| canonical method | FMP `stable/` path | params (`*` = required) | also cross-listed in |
|---|---|---|---|
| `dividends` | `dividends` | `symbol*`, `limit` | — |
| `dividends_calendar` | `dividends-calendar` | `from`, `to`, `page` | — |
| `earnings` | `earnings` | `symbol*`, `limit`, `includeReportTimes` | — |
| `earnings_calendar` | `earnings-calendar` | `from`, `to`, `page`, `includeReportTimes` | — |
| `ipos_calendar` | `ipos-calendar` | `from`, `to` | — |
| `ipos_disclosure` | `ipos-disclosure` | `from`, `to` | — |
| `ipos_prospectus` | `ipos-prospectus` | `from`, `to` | — |
| `splits` | `splits` | `symbol*`, `limit` | — |
| `splits_calendar` | `splits-calendar` | `from`, `to`, `page` | — |

#### `client.chart` — Historical price series, EOD and intraday, for every asset class.

*5 primary methods*

| canonical method | FMP `stable/` path | params (`*` = required) | also cross-listed in |
|---|---|---|---|
| `historical_chart` | `historical-chart/{timeframe}` | `symbol*`, `timeframe*`, `from`, `to`, `nonadjusted`, `extended` | `indexes`, `commodity`, `crypto`, `forex` |
| `historical_price_eod_dividend_adjusted` | `historical-price-eod/dividend-adjusted` | `symbol*`, `from`, `to` | — |
| `historical_price_eod_full` | `historical-price-eod/full` | `symbol*`, `from`, `to` | `indexes`, `commodity`, `crypto`, `forex` |
| `historical_price_eod_light` | `historical-price-eod/light` | `symbol*`, `from`, `to` | `indexes`, `commodity`, `crypto`, `forex` |
| `historical_price_eod_non_split_adjusted` | `historical-price-eod/non-split-adjusted` | `symbol*`, `from`, `to` | — |

#### `client.company` — Company-level reference and profile data, incl. market cap, float, executives, M&A.

*17 primary methods*

| canonical method | FMP `stable/` path | params (`*` = required) | also cross-listed in |
|---|---|---|---|
| `company_notes` | `company-notes` | `symbol*` | — |
| `delisted_companies` | `delisted-companies` | `page`, `limit` | — |
| `employee_count` | `employee-count` | `symbol*`, `limit` | — |
| `executive_compensation_benchmark` | `executive-compensation-benchmark` | `year` | — |
| `governance_executive_compensation` | `governance-executive-compensation` | `symbol*` | — |
| `historical_employee_count` | `historical-employee-count` | `symbol*`, `limit` | — |
| `historical_market_capitalization` | `historical-market-capitalization` | `symbol*`, `limit`, `from`, `to` | — |
| `key_executives` | `key-executives` | `symbol*` | — |
| `market_capitalization` | `market-capitalization` | `symbol*` | — |
| `market_capitalization_batch` | `market-capitalization-batch` | `symbols*` | — |
| `mergers_acquisitions_latest` | `mergers-acquisitions-latest` | `page`, `limit` | — |
| `mergers_acquisitions_search` | `mergers-acquisitions-search` | `name*` | — |
| `profile` | `profile` | `symbol*` | — |
| `profile_cik` | `profile-cik` | `cik*` | — |
| `shares_float` | `shares-float` | `symbol*` | — |
| `shares_float_all` | `shares-float-all` | `limit`, `page` | — |
| `stock_peers` | `stock-peers` | `symbol*` | — |

#### `client.commitment_of_traders` — CFTC Commitment-of-Traders reports and analysis.

*3 primary methods*

| canonical method | FMP `stable/` path | params (`*` = required) | also cross-listed in |
|---|---|---|---|
| `commitment_of_traders_analysis` | `commitment-of-traders-analysis` | `symbol`, `from`, `to` | — |
| `commitment_of_traders_list` | `commitment-of-traders-list` | — | — |
| `commitment_of_traders_report` | `commitment-of-traders-report` | `symbol`, `from`, `to` | — |

#### `client.dcf` — Discounted-cash-flow valuations, standard and custom-input.

*4 primary methods*

| canonical method | FMP `stable/` path | params (`*` = required) | also cross-listed in |
|---|---|---|---|
| `custom_discounted_cash_flow` | `custom-discounted-cash-flow` | `symbol*`, `revenueGrowthPct`, `ebitdaPct`, `depreciationAndAmortizationPct`, `cashAndShortTermInvestmentsPct`, `receivablesPct`, `inventoriesPct`, `payablePct`, `ebitPct`, `capitalExpenditurePct`, `operatingCashFlowPct`, `sellingGeneralAndAdministrativeExpensesPct`, `taxRate`, `longTermGrowthRate`, `costOfDebt`, `costOfEquity`, `marketRiskPremium`, `beta`, `riskFreeRate` | — |
| `custom_levered_discounted_cash_flow` | `custom-levered-discounted-cash-flow` | `symbol*`, `revenueGrowthPct`, `ebitdaPct`, `depreciationAndAmortizationPct`, `cashAndShortTermInvestmentsPct`, `receivablesPct`, `inventoriesPct`, `payablePct`, `ebitPct`, `capitalExpenditurePct`, `operatingCashFlowPct`, `sellingGeneralAndAdministrativeExpensesPct`, `taxRate`, `longTermGrowthRate`, `costOfDebt`, `costOfEquity`, `marketRiskPremium`, `beta`, `riskFreeRate` | — |
| `discounted_cash_flow` | `discounted-cash-flow` | `symbol*` | — |
| `levered_discounted_cash_flow` | `levered-discounted-cash-flow` | `symbol*` | — |

#### `client.economics` — Macroeconomic series, treasury rates, economic calendar, risk premium.

*4 primary methods*

| canonical method | FMP `stable/` path | params (`*` = required) | also cross-listed in |
|---|---|---|---|
| `economic_calendar` | `economic-calendar` | `country`, `from`, `to` | — |
| `economic_indicators` | `economic-indicators` | `name*`, `from`, `to` | — |
| `market_risk_premium` | `market-risk-premium` | — | — |
| `treasury_rates` | `treasury-rates` | `from`, `to` | — |

#### `client.esg` — ESG disclosures, ratings, and benchmarks.

*3 primary methods*

| canonical method | FMP `stable/` path | params (`*` = required) | also cross-listed in |
|---|---|---|---|
| `esg_benchmark` | `esg-benchmark` | `year` | — |
| `esg_disclosures` | `esg-disclosures` | `symbol*` | — |
| `esg_ratings` | `esg-ratings` | `symbol*` | — |

#### `client.funds` — ETF and mutual-fund composition, info, and N-PORT/13F-style disclosures.

*9 primary methods*

| canonical method | FMP `stable/` path | params (`*` = required) | also cross-listed in |
|---|---|---|---|
| `etf_asset_exposure` | `etf/asset-exposure` | `symbol*` | — |
| `etf_country_weightings` | `etf/country-weightings` | `symbol*` | — |
| `etf_holdings` | `etf/holdings` | `symbol*` | — |
| `etf_info` | `etf/info` | `symbol*` | — |
| `etf_sector_weightings` | `etf/sector-weightings` | `symbol*` | — |
| `funds_disclosure` | `funds/disclosure` | `symbol*`, `year*`, `quarter*`, `cik` | — |
| `funds_disclosure_dates` | `funds/disclosure-dates` | `symbol*`, `cik` | — |
| `funds_disclosure_holders_latest` | `funds/disclosure-holders-latest` | `symbol*` | — |
| `funds_disclosure_holders_search` | `funds/disclosure-holders-search` | `name*` | — |

#### `client.statements` — Financial statements and everything computed directly from them.

*27 primary methods*

| canonical method | FMP `stable/` path | params (`*` = required) | also cross-listed in |
|---|---|---|---|
| `balance_sheet_statement` | `balance-sheet-statement` | `symbol*`, `limit`, `period` | — |
| `balance_sheet_statement_as_reported` | `balance-sheet-statement-as-reported` | `symbol*`, `limit`, `period` | — |
| `balance_sheet_statement_growth` | `balance-sheet-statement-growth` | `symbol*`, `limit`, `period` | — |
| `balance_sheet_statement_ttm` | `balance-sheet-statement-ttm` | `symbol*`, `limit` | — |
| `cash_flow_statement` | `cash-flow-statement` | `symbol*`, `limit`, `period` | — |
| `cash_flow_statement_as_reported` | `cash-flow-statement-as-reported` | `symbol*`, `limit`, `period` | — |
| `cash_flow_statement_growth` | `cash-flow-statement-growth` | `symbol*`, `limit`, `period` | — |
| `cash_flow_statement_ttm` | `cash-flow-statement-ttm` | `symbol*`, `limit` | — |
| `enterprise_values` | `enterprise-values` | `symbol*`, `limit`, `period` | — |
| `financial_growth` | `financial-growth` | `symbol*`, `limit`, `period` | — |
| `financial_reports_dates` | `financial-reports-dates` | `symbol*` | — |
| `financial_reports_json` | `financial-reports-json` | `symbol*`, `year*`, `period*` | — |
| `financial_reports_xlsx` | `financial-reports-xlsx` | `symbol*`, `year*`, `period*` | — |
| `financial_scores` | `financial-scores` | `symbol*` | — |
| `financial_statement_full_as_reported` | `financial-statement-full-as-reported` | `symbol*`, `limit`, `period` | — |
| `income_statement` | `income-statement` | `symbol*`, `limit`, `period` | — |
| `income_statement_as_reported` | `income-statement-as-reported` | `symbol*`, `limit`, `period` | — |
| `income_statement_growth` | `income-statement-growth` | `symbol*`, `limit`, `period` | — |
| `income_statement_ttm` | `income-statement-ttm` | `symbol*`, `limit` | — |
| `key_metrics` | `key-metrics` | `symbol*`, `limit`, `period` | — |
| `key_metrics_ttm` | `key-metrics-ttm` | `symbol*` | — |
| `latest_financial_statements` | `latest-financial-statements` | `page`, `limit` | — |
| `owner_earnings` | `owner-earnings` | `symbol*`, `limit` | — |
| `ratios` | `ratios` | `symbol*`, `limit`, `period` | — |
| `ratios_ttm` | `ratios-ttm` | `symbol*` | — |
| `revenue_geographic_segmentation` | `revenue-geographic-segmentation` | `symbol*`, `period`, `structure` | — |
| `revenue_product_segmentation` | `revenue-product-segmentation` | `symbol*`, `period`, `structure` | — |

#### `client.institutional_ownership` — Form 13F institutional holdings, holders, and derived analytics.

*8 primary methods*

| canonical method | FMP `stable/` path | params (`*` = required) | also cross-listed in |
|---|---|---|---|
| `institutional_ownership_dates` | `institutional-ownership/dates` | `cik*` | — |
| `institutional_ownership_extract` | `institutional-ownership/extract` | `cik*`, `year*`, `quarter*` | — |
| `institutional_ownership_extract_analytics_holder` | `institutional-ownership/extract-analytics/holder` | `symbol*`, `year*`, `quarter*`, `page`, `limit` | — |
| `institutional_ownership_holder_industry_breakdown` | `institutional-ownership/holder-industry-breakdown` | `cik*`, `year*`, `quarter*` | — |
| `institutional_ownership_holder_performance_summary` | `institutional-ownership/holder-performance-summary` | `cik*`, `page` | — |
| `institutional_ownership_industry_summary` | `institutional-ownership/industry-summary` | `year*`, `quarter*` | — |
| `institutional_ownership_latest` | `institutional-ownership/latest` | `page`, `limit` | — |
| `institutional_ownership_symbol_positions_summary` | `institutional-ownership/symbol-positions-summary` | `symbol*`, `year*`, `quarter*` | — |

#### `client.indexes` — Stock-market indexes, their quotes/charts, and their constituent lists.

*7 primary methods*

| canonical method | FMP `stable/` path | params (`*` = required) | also cross-listed in |
|---|---|---|---|
| `dowjones_constituent` | `dowjones-constituent` | — | — |
| `historical_dowjones_constituent` | `historical-dowjones-constituent` | — | — |
| `historical_nasdaq_constituent` | `historical-nasdaq-constituent` | — | — |
| `historical_sp500_constituent` | `historical-sp500-constituent` | — | — |
| `index_list` | `index-list` | — | — |
| `nasdaq_constituent` | `nasdaq-constituent` | — | — |
| `sp500_constituent` | `sp500-constituent` | — | — |

#### `client.commodity` — Commodity instruments: list, quotes, charts.

*1 primary methods*

| canonical method | FMP `stable/` path | params (`*` = required) | also cross-listed in |
|---|---|---|---|
| `commodities_list` | `commodities-list` | — | — |

#### `client.crypto` — Cryptocurrency instruments: list, quotes, charts.

*1 primary methods*

| canonical method | FMP `stable/` path | params (`*` = required) | also cross-listed in |
|---|---|---|---|
| `cryptocurrency_list` | `cryptocurrency-list` | — | — |

#### `client.fundraisers` — Reg CF crowdfunding and Reg D/A equity offerings.

*6 primary methods*

| canonical method | FMP `stable/` path | params (`*` = required) | also cross-listed in |
|---|---|---|---|
| `crowdfunding_offerings` | `crowdfunding-offerings` | `cik*` | — |
| `crowdfunding_offerings_latest` | `crowdfunding-offerings-latest` | `page`, `limit` | — |
| `crowdfunding_offerings_search` | `crowdfunding-offerings-search` | `name*` | — |
| `fundraising` | `fundraising` | `cik*` | — |
| `fundraising_latest` | `fundraising-latest` | `page`, `limit`, `cik` | — |
| `fundraising_search` | `fundraising-search` | `name*` | — |

#### `client.forex` — FX pairs: list, quotes, charts.

*1 primary methods*

| canonical method | FMP `stable/` path | params (`*` = required) | also cross-listed in |
|---|---|---|---|
| `forex_list` | `forex-list` | — | — |

#### `client.insider_trades` — Form 4 insider transactions, statistics, and beneficial-ownership acquisitions.

*6 primary methods*

| canonical method | FMP `stable/` path | params (`*` = required) | also cross-listed in |
|---|---|---|---|
| `acquisition_of_beneficial_ownership` | `acquisition-of-beneficial-ownership` | `symbol*`, `limit` | — |
| `insider_trading_latest` | `insider-trading/latest` | `date`, `page`, `limit` | — |
| `insider_trading_reporting_name` | `insider-trading/reporting-name` | `name*` | — |
| `insider_trading_search` | `insider-trading/search` | `symbol`, `page`, `limit`, `reportingCik`, `companyCik`, `transactionType` | — |
| `insider_trading_statistics` | `insider-trading/statistics` | `symbol*` | — |
| `insider_trading_transaction_type` | `insider-trading-transaction-type` | — | — |

#### `client.market_performance` — Sector/industry performance and P/E, snapshot and historical, plus market leaders.

*11 primary methods*

| canonical method | FMP `stable/` path | params (`*` = required) | also cross-listed in |
|---|---|---|---|
| `biggest_gainers` | `biggest-gainers` | — | — |
| `biggest_losers` | `biggest-losers` | — | — |
| `historical_industry_pe` | `historical-industry-pe` | `industry*`, `exchange`, `from`, `to` | — |
| `historical_industry_performance` | `historical-industry-performance` | `industry*`, `exchange`, `from`, `to` | — |
| `historical_sector_pe` | `historical-sector-pe` | `from`, `exchange`, `sector*`, `to` | — |
| `historical_sector_performance` | `historical-sector-performance` | `from`, `exchange`, `sector*`, `to` | — |
| `industry_pe_snapshot` | `industry-pe-snapshot` | `date*`, `exchange`, `industry` | — |
| `industry_performance_snapshot` | `industry-performance-snapshot` | `date*`, `exchange`, `industry` | — |
| `most_actives` | `most-actives` | — | — |
| `sector_pe_snapshot` | `sector-pe-snapshot` | `date*`, `exchange`, `sector` | — |
| `sector_performance_snapshot` | `sector-performance-snapshot` | `date*`, `exchange`, `sector` | — |

#### `client.market_hours` — Exchange trading sessions and holiday calendars.

*3 primary methods*

| canonical method | FMP `stable/` path | params (`*` = required) | also cross-listed in |
|---|---|---|---|
| `all_exchange_market_hours` | `all-exchange-market-hours` | `timestamp` | — |
| `exchange_market_hours` | `exchange-market-hours` | `exchange*`, `timestamp` | — |
| `holidays_by_exchange` | `holidays-by-exchange` | `exchange*`, `from`, `to` | — |

#### `client.technical_indicators` — Computed technical indicator series.

*9 primary methods*

| canonical method | FMP `stable/` path | params (`*` = required) | also cross-listed in |
|---|---|---|---|
| `technical_indicators_adx` | `technical-indicators/adx` | `symbol*`, `periodLength*`, `timeframe*`, `from`, `to` | — |
| `technical_indicators_dema` | `technical-indicators/dema` | `symbol*`, `periodLength*`, `timeframe*`, `from`, `to` | — |
| `technical_indicators_ema` | `technical-indicators/ema` | `symbol*`, `periodLength*`, `timeframe*`, `from`, `to` | — |
| `technical_indicators_rsi` | `technical-indicators/rsi` | `symbol*`, `periodLength*`, `timeframe*`, `from`, `to` | — |
| `technical_indicators_sma` | `technical-indicators/sma` | `symbol*`, `periodLength*`, `timeframe*`, `from`, `to` | — |
| `technical_indicators_standarddeviation` | `technical-indicators/standarddeviation` | `symbol*`, `periodLength*`, `timeframe*`, `from`, `to` | — |
| `technical_indicators_tema` | `technical-indicators/tema` | `symbol*`, `periodLength*`, `timeframe*`, `from`, `to` | — |
| `technical_indicators_williams` | `technical-indicators/williams` | `symbol*`, `periodLength*`, `timeframe*`, `from`, `to` | — |
| `technical_indicators_wma` | `technical-indicators/wma` | `symbol*`, `periodLength*`, `timeframe*`, `from`, `to` | — |

#### `client.news` — News, press releases, and FMP editorial articles.

*10 primary methods*

| canonical method | FMP `stable/` path | params (`*` = required) | also cross-listed in |
|---|---|---|---|
| `fmp_articles` | `fmp-articles` | `page`, `limit` | — |
| `news_crypto` | `news/crypto` | `symbols*`, `from`, `to`, `page`, `limit` | — |
| `news_crypto_latest` | `news/crypto-latest` | `from`, `to`, `page`, `limit` | — |
| `news_forex` | `news/forex` | `symbols*`, `from`, `to`, `page`, `limit` | — |
| `news_forex_latest` | `news/forex-latest` | `from`, `to`, `page`, `limit` | — |
| `news_general_latest` | `news/general-latest` | `from`, `to`, `page`, `limit` | — |
| `news_press_releases` | `news/press-releases` | `symbols*`, `from`, `to`, `page`, `limit` | — |
| `news_press_releases_latest` | `news/press-releases-latest` | `from`, `to`, `page`, `limit` | — |
| `news_stock` | `news/stock` | `symbols*`, `from`, `to`, `page`, `limit` | — |
| `news_stock_latest` | `news/stock-latest` | `from`, `to`, `page`, `limit` | — |

#### `client.quote` — Real-time and aftermarket quotes, single and batch.

*16 primary methods*

| canonical method | FMP `stable/` path | params (`*` = required) | also cross-listed in |
|---|---|---|---|
| `aftermarket_quote` | `aftermarket-quote` | `symbol*` | — |
| `aftermarket_trade` | `aftermarket-trade` | `symbol*` | — |
| `batch_aftermarket_quote` | `batch-aftermarket-quote` | `symbols*` | — |
| `batch_aftermarket_trade` | `batch-aftermarket-trade` | `symbols*` | — |
| `batch_commodity_quotes` | `batch-commodity-quotes` | `short` | `commodity` |
| `batch_crypto_quotes` | `batch-crypto-quotes` | `short` | `crypto` |
| `batch_etf_quotes` | `batch-etf-quotes` | `short` | — |
| `batch_exchange_quote` | `batch-exchange-quote` | `exchange*`, `short` | — |
| `batch_forex_quotes` | `batch-forex-quotes` | `short` | `forex` |
| `batch_index_quotes` | `batch-index-quotes` | `short` | `indexes` |
| `batch_mutualfund_quotes` | `batch-mutualfund-quotes` | `short` | — |
| `batch_quote` | `batch-quote` | `symbols*` | — |
| `batch_quote_short` | `batch-quote-short` | `symbols*` | — |
| `quote` | `quote` | `symbol*` | `indexes`, `commodity`, `crypto`, `forex` |
| `quote_short` | `quote-short` | `symbol*` | `indexes`, `commodity`, `crypto`, `forex` |
| `stock_price_change` | `stock-price-change` | `symbol*` | — |

#### `client.sec_filings` — SEC filing search, SEC company identity, and SIC industry classification.

*12 primary methods*

| canonical method | FMP `stable/` path | params (`*` = required) | also cross-listed in |
|---|---|---|---|
| `all_industry_classification` | `all-industry-classification` | `page`, `limit` | — |
| `industry_classification_search` | `industry-classification-search` | `symbol`, `cik`, `sicCode` | — |
| `sec_filings_8k` | `sec-filings-8k` | `from*`, `to*`, `page`, `limit` | — |
| `sec_filings_company_search_cik` | `sec-filings-company-search/cik` | `cik*` | — |
| `sec_filings_company_search_name` | `sec-filings-company-search/name` | `company*` | — |
| `sec_filings_company_search_symbol` | `sec-filings-company-search/symbol` | `symbol*` | — |
| `sec_filings_financials` | `sec-filings-financials` | `from*`, `to*`, `page`, `limit` | — |
| `sec_filings_search_cik` | `sec-filings-search/cik` | `cik*`, `from*`, `to*`, `page`, `limit` | — |
| `sec_filings_search_form_type` | `sec-filings-search/form-type` | `formType*`, `from*`, `to*`, `page`, `limit` | — |
| `sec_filings_search_symbol` | `sec-filings-search/symbol` | `symbol*`, `from*`, `to*`, `page`, `limit` | — |
| `sec_profile` | `sec-profile` | `symbol*`, `cik-A` | — |
| `standard_industrial_classification_list` | `standard-industrial-classification-list` | `industryTitle`, `sicCode` | — |

#### `client.earnings_transcript` — Earnings-call transcripts and their availability metadata.

*4 primary methods*

| canonical method | FMP `stable/` path | params (`*` = required) | also cross-listed in |
|---|---|---|---|
| `earning_call_transcript` | `earning-call-transcript` | `symbol*`, `year*`, `quarter*`, `limit` | — |
| `earning_call_transcript_dates` | `earning-call-transcript-dates` | `symbol*` | — |
| `earning_call_transcript_latest` | `earning-call-transcript-latest` | `limit`, `page` | — |
| `earnings_transcript_list` | `earnings-transcript-list` | — | `directory` |

#### `client.congress` — U.S. Senate and House financial disclosures, trades, and member profiles.

*12 primary methods*

| canonical method | FMP `stable/` path | params (`*` = required) | also cross-listed in |
|---|---|---|---|
| `house_latest` | `house-latest` | `page`, `limit` | — |
| `house_trades` | `house-trades` | `symbol*`, `page`, `limit` | — |
| `house_trades_by_id` | `house-trades-by-id` | `page`, `limit`, `senateID` | — |
| `house_trades_by_name` | `house-trades-by-name` | `name*` | — |
| `senate_latest` | `senate-latest` | `page`, `limit` | — |
| `senate_net_worth` | `senate-net-worth` | `senateID*` | — |
| `senate_net_worth_aggregated` | `senate-net-worth-aggregated` | `senateID*`, `totalsCol` | — |
| `senate_positions` | `senate-positions` | `senateID`, `party`, `position`, `page`, `limit` | — |
| `senate_profile` | `senate-profile` | `active`, `senateID`, `latestParty`, `latestPosition`, `page`, `limit` | — |
| `senate_trades` | `senate-trades` | `symbol*`, `page`, `limit` | — |
| `senate_trades_by_id` | `senate-trades-by-id` | `page`, `limit`, `senateID` | — |
| `senate_trades_by_name` | `senate-trades-by-name` | `name*` | — |

#### `client.bulk` — Whole-universe bulk downloads.

*18 primary methods*

| canonical method | FMP `stable/` path | params (`*` = required) | also cross-listed in |
|---|---|---|---|
| `balance_sheet_statement_bulk` | `balance-sheet-statement-bulk` | `year*`, `period*` | — |
| `balance_sheet_statement_growth_bulk` | `balance-sheet-statement-growth-bulk` | `year*`, `period*` | — |
| `cash_flow_statement_bulk` | `cash-flow-statement-bulk` | `year*`, `period*` | — |
| `cash_flow_statement_growth_bulk` | `cash-flow-statement-growth-bulk` | `year*`, `period*` | — |
| `dcf_bulk` | `dcf-bulk` | — | — |
| `earnings_surprises_bulk` | `earnings-surprises-bulk` | `year*` | — |
| `eod_bulk` | `eod-bulk` | `date*` | — |
| `etf_holder_bulk` | `etf-holder-bulk` | `part*` | — |
| `income_statement_bulk` | `income-statement-bulk` | `year*`, `period*` | — |
| `income_statement_growth_bulk` | `income-statement-growth-bulk` | `year*`, `period*` | — |
| `key_metrics_ttm_bulk` | `key-metrics-ttm-bulk` | — | — |
| `peers_bulk` | `peers-bulk` | — | — |
| `price_target_summary_bulk` | `price-target-summary-bulk` | — | — |
| `profile_bulk` | `profile-bulk` | `part*` | — |
| `rating_bulk` | `rating-bulk` | — | — |
| `ratios_ttm_bulk` | `ratios-ttm-bulk` | — | — |
| `scores_bulk` | `scores-bulk` | — | — |
| `upgrades_downgrades_consensus_bulk` | `upgrades-downgrades-consensus-bulk` | — | — |

#### `client.tipranks` — TipRanks partner analyst data.

*7 primary methods*

| canonical method | FMP `stable/` path | params (`*` = required) | also cross-listed in |
|---|---|---|---|
| `tipranks_analyst_summary` | `tipranks-analyst-summary` | `expertUID*`, `from`, `to` | — |
| `tipranks_analysts` | `tipranks-analysts` | `page`, `limit`, `firmName` | — |
| `tipranks_firm_summary` | `tipranks-firm-summary` | `firmName*`, `from`, `to` | — |
| `tipranks_pit_analyst` | `tipranks-pit-analyst` | `expertUID`, `analystName`, `date`, `limit`, `page`, `nonadjusted` | — |
| `tipranks_pit_symbol` | `tipranks-pit-symbol` | `symbol*`, `date`, `limit`, `page`, `nonadjusted` | — |
| `tipranks_search` | `tipranks-search` | `expertUID`, `symbol`, `from`, `to`, `limit`, `page`, `nonadjusted` | — |
| `tipranks_symbol_summary` | `tipranks-symbol-summary` | `symbol*`, `from`, `to` | — |

**Total canonical methods: 238**

---

## 7. Structural inconsistencies in FMP's own path design

Every item below is a real inconsistency in FMP's URL structure. The recommended resolution is
**"mirror it, document it, do not normalize it"** in almost every case, and §7.0 explains why
that is a decision rather than laziness.

### 7.0 The general policy on FMP's inconsistency

FMP's paths are inconsistent in at least eight distinct ways. We could normalize any of them.
We normalize none of them, because:

1. Normalizing breaks §2.4's round-trip property, which is the SDK's actual discoverability
   guarantee (brief 3.2).
2. Normalizing requires a hand-maintained exception table, which is a permanent maintenance tax
   and a permanent source of drift between our names and FMP's.
3. A user debugging against FMP's own docs or a raw `curl` needs our name and FMP's path to be
   the same string modulo punctuation. Every normalization we apply is a translation step they
   have to perform in their head.
4. Brief 3.5 says this explicitly: "FMP's structure is not fully consistent, and that's expected,
   not a signal to force consistency we'd be inventing."

The alias layer and the generated cross-reference table are where the inconsistency gets
*absorbed*, not the canonical names.

### 7.1 `historical-` prefix vs. `-historical` suffix

19 paths use `historical-` as a **prefix** (`historical-market-capitalization`,
`historical-employee-count`, `historical-sector-pe`, `historical-sp500-constituent`,
`historical-chart/*`, `historical-price-eod/*`, …). **Exactly two** use `-historical` as a
suffix: `ratings-historical` and `grades-historical`.

**Resolution:** mirror both. `ratings_historical` and `grades_historical` sit alphabetically
adjacent to `ratings_snapshot` and `grades_consensus` in the `analyst` group, which is arguably
*better* grouping than `historical_ratings` would give. Document the exception in the
`analyst` group docstring.

### 7.2 `-latest` suffix vs. `latest-` prefix

14 paths use `-latest` / `/latest` as a suffix. **Exactly one** uses it as a prefix:
`latest-financial-statements`.

**Resolution:** mirror. `latest_financial_statements` is unambiguous and its group
(`statements`) makes it findable. Not worth an exception.

### 7.3 `search-X` prefix vs. `X-search` suffix — not drift, a real distinction

Six paths are `search-<identifier-type>` (`search-symbol`, `search-name`, `search-cik`,
`search-cusip`, `search-isin`, `search-exchange-variants`). Thirteen are `<dataset>-search` or
`<dataset>/search`.

On inspection this is **not** inconsistency: `search-X` means *"resolve an identifier"* (input is
a fragment, output is identity records), while `X-search` means *"query a dataset"* (input is a
filter, output is domain records). The two conventions encode two different operations.

**Resolution:** mirror, and document the distinction in the `search` group docstring — it is
genuinely useful information for users, and it is FMP's, not ours.

### 7.4 Conceptual families that do not nest in the URL

Brief 3.5 flags two of these; here is the complete set.

| Endpoint | Conceptually belongs with | But its path is |
|---|---|---|
| `insider-trading-transaction-type` | `insider-trading/*` | hyphen-joined, not slash-nested |
| `acquisition-of-beneficial-ownership` | `insider-trading/*` | no shared prefix at all |
| `governance-executive-compensation` | `key-executives`, `executive-compensation-benchmark` | orphan `governance-` prefix used by no other endpoint |
| `executive-compensation-benchmark` | `governance-executive-compensation` | shares the words, not the prefix |
| `sec-profile` | `sec-filings-company-search/*` | different root, same subject (SEC company identity) |
| `all-industry-classification`, `industry-classification-search`, `standard-industrial-classification-list` | each other | three prefixes for one concept: `all-`, bare, and `standard-industrial-` |
| `fmp-articles` | `news/*` | outside the `news/` root |
| `earnings-transcript-list` | `earning-call-transcript*` | singular/plural drift *and* `earnings` vs `earning` (see §7.6) |

**Resolution: this is exactly what the alias layer is for.** Canonical names mirror the paths
verbatim (so `acquisition_of_beneficial_ownership` gets **no** invented `insider_trading_`
prefix), and the alias groups put them where users will look:

- `client.insider_trades` contains `insider_trading_latest`, `insider_trading_search`,
  `insider_trading_statistics`, `insider_trading_reporting_name`,
  `insider_trading_transaction_type`, and `acquisition_of_beneficial_ownership`.
- `client.company` contains `key_executives`, `governance_executive_compensation`, and
  `executive_compensation_benchmark`.
- `client.sec_filings` contains `sec_profile` alongside the `sec_filings_*` family and all three
  industry-classification endpoints.
- `client.news` contains `fmp_articles`.

This is the strongest argument in the whole catalog for the brief's two-layer design: it lets us
be 100% faithful to FMP's paths at the contract layer *and* 100% coherent at the discovery layer,
with no tension between the two.

### 7.5 FMP parameter-naming bug: `house-trades-by-id` takes `senateID`

```
stable/senate-trades-by-id?...&senateID=S000033
stable/house-trades-by-id?...&senateID=P000197     <-- House endpoint, "senate" parameter
```

This is a bug in FMP's API, not their docs — the wire parameter really is `senateID`.

**Resolution:** expose the Python parameter as `senate_id` on **both** methods, because the wire
name is `senateID` on both and a `member_id` alias would be an invented name that does not match
what a user sees in a request log or in FMP's docs. **Call this out loudly in the
`house_trades_by_id` docstring** — a House method taking `senate_id` looks like *our* bug and
will generate an issue otherwise.

Do not "fix" it by accepting `member_id` and translating. If FMP renames it, that is a
breaking change we mirror.

### 7.6 Singular/plural and stem drift inside single families

- `earning-call-transcript`, `earning-call-transcript-dates`, `earning-call-transcript-latest`
  (singular "earning") vs. `earnings-transcript-list` (plural "earnings", different stem) — one
  four-endpoint family, two stems.
- `-list` endpoints mix singular and plural subjects: `commodities-list` (plural) vs.
  `cryptocurrency-list`, `forex-list`, `index-list`, `etf-list`, `stock-list`, `cik-list`
  (singular).
- `batch-quote` / `batch-quote-short` / `batch-aftermarket-quote` / `batch-exchange-quote`
  (singular) vs. `batch-etf-quotes` / `batch-mutualfund-quotes` / `batch-commodity-quotes` /
  `batch-crypto-quotes` / `batch-forex-quotes` / `batch-index-quotes` (plural).

The `batch-*` case turns out to encode a real signal: **singular `-quote` = you supply the scope**
(`symbols*` or `exchange*`); **plural `-quotes` = the whole asset class, no scope parameter**.
That is worth documenting in the `quote` group docstring rather than treating as noise.

**Resolution:** mirror all of it. Document the `batch` singular/plural signal.

### 7.7 `market-capitalization-batch` — the one `batch` suffix

Every other batch endpoint puts `batch` first. `market-capitalization-batch` puts it last.

**Resolution:** mirror (`market_capitalization_batch`). It sorts next to `market_capitalization`
and `historical_market_capitalization` in the `company` group, which is where a user looking for
it will actually look.

### 7.8 `profile` means five different things

`profile` (company), `profile-cik` (company by CIK), `profile-bulk` (all companies),
`sec-profile` (SEC registrant identity), `senate-profile` (a member of Congress).

**Resolution:** mirror. The full-path rule keeps all five distinct and each one's group makes its
meaning obvious. No action needed — noted so the implementer does not assume a shared response
shape. **They do not share a response shape.** Five separate `TypedDict`s.

### 7.9 The two "Latest Filings" endpoints are not parallel

`sec-filings-8k` is scoped by **form type**; `sec-filings-financials` is scoped by a **category**
of forms. They sit under one sub-heading as if they were a pair. Additionally, `sec-filings-8k`
is functionally a special case of `sec-filings-search/form-type?formType=8-K`.

**Resolution:** ship both as flat methods (they are separately billed/gated paths and may differ
in latency or plan tier). Note the overlap in both docstrings so users are not surprised that two
methods can answer the same question.

### 7.10 Path depth is almost flat

Only 55 of 243 paths contain a `/` at all, and exactly one —
`institutional-ownership/extract-analytics/holder` — has two. FMP's `stable` API is
overwhelmingly a flat namespace with a handful of prefix groupings
(`etf/`, `funds/`, `news/`, `insider-trading/`, `institutional-ownership/`,
`technical-indicators/`, `historical-chart/`, `historical-price-eod/`, `sec-filings-search/`,
`sec-filings-company-search/`).

**Why this matters:** it independently validates the brief's flat-canonical decision. A deeply
nested URL space would argue for a nested SDK; a flat one does not. The 29 alias groups are
carrying almost all of the organizational weight, which is the correct division of labour.

Note that `extract-analytics/holder` is a family with exactly one member. Per brief 3.5's rule
("no bare/unsuffixed name unless it is the only endpoint in its family") there is no bare-name
risk here, but flag it: if FMP later adds `extract-analytics/symbol`, the existing method name
`institutional_ownership_extract_analytics_holder` needs no change. The full-path rule is
forward-compatible here; a bare-leaf rule would not have been.

---

## 8. Parameter-level findings that affect implementation

### 8.1 `period` accepts three incompatible value sets — the legacy constant is wrong

25 endpoints take a `period` parameter. FMP documents **three different value sets**:

| Value set | Endpoints | Examples |
|---|---:|---|
| `annual`, `quarter` | 7 | `income-statement-as-reported`, `balance-sheet-statement-as-reported`, `cash-flow-statement-as-reported`, `financial-statement-full-as-reported`, `revenue-product-segmentation`, `revenue-geographic-segmentation`, `analyst-estimates` |
| `Q1`, `Q2`, `Q3`, `Q4`, `FY` | 8 | `financial-reports-json`, `financial-reports-xlsx`, and all six `*-bulk` financial statements |
| `Q1`, `Q2`, `Q3`, `Q4`, `FY`, `annual`, `quarter` | 10 | `income-statement`, `balance-sheet-statement`, `cash-flow-statement`, `key-metrics`, `ratios`, `enterprise-values`, and the four `*-growth` statements |

The legacy `settings.py` carries `PERIOD_VALUES = ["annual", "quarter"]`. **Carried forward
unchanged, that constant is correct for 7 of 25 endpoints** and would reject valid input on the
other 18.

**Required action:** replace with three constants, and bind the right one per endpoint:

```
PERIOD_ANNUAL_QUARTER  = ("annual", "quarter")
PERIOD_FISCAL          = ("Q1", "Q2", "Q3", "Q4", "FY")
PERIOD_ANY             = PERIOD_FISCAL + PERIOD_ANNUAL_QUARTER
```

This is a direct correction to a decision fixed in brief 3.6 ("carry forward validated constant
lists … re-verified against current docs"). The re-verification finds the list invalid; flagging
it rather than silently carrying it forward is the point.

### 8.2 Two `timeframe` vocabularies, not one

| Constant | Values | Used by |
|---|---|---|
| `TIMEFRAME_INTRADAY` | `1min, 5min, 15min, 30min, 1hour, 4hour` | `historical_chart` (the §5.3 collapse) |
| `TIMEFRAME_TECHNICAL` | `1min, 5min, 15min, 30min, 1hour, 4hour, 1day` | all 9 `technical_indicators_*` |

Legacy `settings.py` has both, but `TECHNICAL_INDICATORS_TIME_DELTA_VALUES` ends in **`daily`**,
which is a `v3`-era token. Current `stable` docs say **`1day`**. Carrying the legacy list forward
unchanged would silently reject the only valid daily value.

### 8.3 Legacy `settings.py` carry-forward audit

| Legacy constant | Verdict |
|---|---|
| `INDUSTRY_VALUES`, `SECTOR_VALUES` | Re-verify against live `available-industries` / `available-sectors`, which are now endpoints. Consider shipping the constants as a fallback and the endpoints as the source of truth. |
| `PERIOD_VALUES` | **Invalid as-is.** Replace per §8.1. |
| `TIME_DELTA_VALUES` | Valid — matches `historical-chart` exactly. Rename to `TIMEFRAME_INTRADAY`. |
| `TECHNICAL_INDICATORS_TIME_DELTA_VALUES` | **Invalid** — `daily` → `1day`. |
| `STATISTICS_TYPE_VALUES` | Valid — matches the 9 `technical-indicators/*` paths exactly, including `standardDeviation`'s casing. Useful as a cross-check that no indicator is missing. |
| `SERIES_TYPE_VALUES` (`["line"]`) | **Dead.** No `stable` endpoint takes a `seriesType` parameter. Drop. |
| `ECONOMIC_INDICATOR_VALUES` | Nearly valid: 23 entries, all still documented, but current docs list **24** — `tradeBalanceGoodsAndServices` is missing from the legacy list. Add it. |
| `*_FILENAME` constants (`FINANCIAL_STATEMENT_FILENAME` etc.) | **Dead.** Artifacts of `v3`'s CSV/ZIP download endpoints. Drop. |

### 8.4 Response-type exceptions to the `List[Dict]` contract

Brief 3.6 fixes "stay `List[Dict]`-shaped at runtime." That is **verified correct for 276 of 276**
documented example responses — every single one parses as a JSON array of objects. Strong result.

Two endpoints need verification before the contract is assumed universal:

- **`financial-reports-xlsx`** — its documented example response is a **byte-for-byte copy of
  `financial-reports-json`'s example**, which cannot be right for an endpoint whose entire
  purpose is to return a spreadsheet. This almost certainly returns `application/vnd.openxmlformats…`
  binary. **Action: verify with a real key. If it returns binary, this method returns `bytes` and
  is the one documented exception to the response contract** — do not try to force it into
  `List[Dict]`, and do not silently return an unparsed error dict (that is the exact class of bug
  the rewrite exists to fix).
- **The 18 `*-bulk` endpoints** — every numeric value in every bulk example is quoted as a
  **string** (`"revenue": "33644000000"`, `"open": "2.67"`, `"discountedCashFlowScore": "5"`).
  That is the signature of a CSV serialization rendered as JSON for the docs. FMP's bulk product
  has historically been `text/csv`. **Action: verify with a real key.** If bulk returns CSV, the
  `bulk` group needs its own return contract (`List[Dict[str, str]]` parsed from CSV, or raw
  `bytes`), decided once for all 18 rather than per method.

Neither of these is a reason to abandon the `List[Dict]` decision. Both are reasons to make the
exceptions explicit and typed rather than discovering them in production.

### 8.5 Documentation reliability — a positive finding

All 276 REST sections were checked for disagreement between the example URL and the parameter
table (parameters present in one but not the other). **Exactly one discrepancy exists:**

- `senate-net-worth` — example URL is `?senateID=P000197&page=0&limit=250` but the parameter
  table lists only `senateID*`.

**Resolution:** support `page` and `limit` on `senate_net_worth`. FMP's own example is stronger
evidence than an omission in a generated table, and the parameters are harmless if ignored.

The broader point: FMP's parameter tables are **99.6% internally consistent** with their example
URLs. They can be trusted as the basis for method signatures. This is worth stating because the
brief's 3.3 discipline ("test before trusting the docs") is correct in principle but, applied to
parameter tables specifically, the evidence says the docs are reliable. Reserve live testing for
the two response-type questions in §8.4 and the two suspected typos in §8.6.

### 8.6 Two suspected doc typos requiring live verification

- **`sec-profile`** documents a parameter literally named **`cik-A`**. A hyphenated query
  parameter name would be unique in the entire API. Almost certainly `cik`. **Verify with a
  key**; implement as `cik` unless testing says otherwise, and note the doc oddity in a comment.
- **`symbol-change`** documents a parameter named **`invalid`** with example value `false`.
  Presumably "include invalid/delisted symbol changes." The name is real (it appears nowhere
  else, so it is not a template artifact), but the semantics are undocumented. **Verify
  behaviour**; document what it actually does rather than guessing in the docstring.

### 8.7 Parameter names reused with unrelated meanings

- **`extended`** — on `historical-chart/*` it means extended-hours trading data; on
  `available-exchanges` it means return a richer record. Same name, unrelated meaning.
- **`nonadjusted`** — on `historical-chart/*` it means split-unadjusted prices; on
  `tipranks-pit-symbol` / `tipranks-pit-analyst` / `tipranks-search` it means something else
  entirely (unadjusted ratings history).
- **`date`** — variously a snapshot date (`sector-performance-snapshot`), a filing date filter
  (`insider-trading/latest`), a bulk extraction date (`eod-bulk`), and a point-in-time cursor
  (`tipranks-pit-*`).

**Resolution:** no shared parameter-object or global validator across endpoints. Per-endpoint
signatures with per-endpoint docstrings. Do not build a generic "common params" mixin that
assumes `date` or `extended` means one thing.

### 8.8 `limit` defaults vary by two orders of magnitude

FMP's example `limit` values range from `1` to `2000`, clustered at `5` (18 endpoints), `100`
(30), `20` (10), `50`, `1000`, `250`, `300`, `500`. There is no global default.

**Resolution:** never send `limit` unless the caller passes it. Do not invent a package-wide
default — FMP's server-side defaults differ per endpoint and are not documented. Passing nothing
gets the caller FMP's intended default; passing our invented default silently changes behaviour.
Same for `page`.

---

## 9. Deliberate deviations from mechanical URL translation

Listed so the maintainer can audit exactly where judgment was applied. **Everything not on this
list is a mechanical transformation.**

| # | Deviation | Why | Risk if reversed |
|---|---|---|---|
| **9.1** | `historical-chart/{6 intervals}` collapsed into one `historical_chart(timeframe=…)` method | §5.3 — FMP itself names this token set as a query-parameter value (`timeframe`) on 9 other endpoints. We use FMP's vocabulary, not an invented one. | Low. Reversing gives 6 flat methods and costs nothing but ergonomics. **This is the deviation most deserving explicit sign-off.** |
| **9.2** | 276 doc sections deduplicated to 243 unique endpoints | §4 — 13 paths are documented up to 5× by FMP, once per asset-class chapter. Identical paths, parameters, and response shapes. | None. Not deduplicating would ship 5 methods issuing identical HTTP requests. |
| **9.3** | Full-path naming instead of bare-leaf-plus-collision-qualifier | §2.3 — bare-leaf produces `extract()`, `dates()`, `holdings()`, `stock()`, `search()`, `sma()`. Full-path makes collisions structurally impossible instead of test-detected. | None; every name the brief explicitly specifies is unchanged. |
| **9.4** | 5 alias-group renames (`Senate`→`congress`, `Partners`→`tipranks`, `Form13F`→`institutional_ownership`, `EtfAndMutualFunds`→`funds`, `DiscountedCashFlow`→`dcf`) | §3.2 — one is factually wrong, one names a business relationship, three stutter. Aliases are explicitly non-breaking sugar (brief 3.2), so this is the cheapest possible place to apply judgment. | None. Aliases can be renamed freely. |
| **9.5** | `from`/`to` → `from_date`/`to_date` as Python parameter names | `from` is a Python keyword. Forced by the language. | None; no alternative exists. |
| **9.6** | `historical_chart` carries the **union** of parameters documented across its 5 doc copies | §4.2 — the asset-class chapters omit `nonadjusted`/`extended`; the server accepts them regardless. | Low. Under-declaring would make equity users unable to reach real functionality. |
| **9.7** | `senate_net_worth` supports `page`/`limit` despite the parameter table omitting them | §8.5 — FMP's own example URL passes them. | Negligible. |

### 9.8 Deliberate NON-deviations

Places where a "cleaner" SDK is achievable and is being declined on purpose. Recorded so nobody
re-opens them as oversights:

- Not normalizing `historical-` prefix vs. `-historical` suffix (§7.1).
- Not normalizing `-latest` suffix vs. `latest-` prefix (§7.2).
- Not normalizing `-list` singular/plural drift (§7.6).
- Not moving `market-capitalization-batch` into the `batch-*` naming shape (§7.7).
- Not giving `acquisition_of_beneficial_ownership` or `insider_trading_transaction_type` an
  invented `insider_trading_` prefix to match their conceptual family (§7.4).
- Not word-splitting `standarddeviation`, `dowjones`, `mutualfund` (§2.5).
- Not renaming `house_trades_by_id`'s `senate_id` parameter (§7.5).
- Not collapsing index constituents, batch-quotes-by-asset-class, news-by-category, or
  senate/house (§5.4).

In every case the reason is the same: §2.4's round-trip property is worth more than local
tidiness, and the alias layer plus the generated cross-reference table absorb the cost.

---

## 10. Review of the design brief

The brief is sound and its major decisions hold up under the full catalog. Five items need the
maintainer's and the implementing model's joint attention before implementation starts. **These
are flagged, not overruled.**

### 10.1 The bare-leaf naming default (brief §3.3, §3.5) does not scale — HIGH

**Concern:** the brief's collision rule reads as "use the bare leaf name; qualify with the
enclosing path segment only where a collision exists." That is fine on the four endpoints the
brief examines and produces `extract()`, `dates()`, `disclosure()`, `holdings()`, `stock()`,
`search()`, `sma()` across the full catalog. It also makes collision-freedom a property that must
be *re-tested* every time FMP ships an endpoint, rather than a property of the naming rule.

**Proposed resolution (§2.1):** apply the brief's own qualifier unconditionally — full-path
naming. Every name the brief explicitly specifies (`insider_trading_latest`,
`institutional_ownership_latest`, `sec_filings_search_cik`, `sec_filings_company_search_cik`) is
produced unchanged. **This is a strengthening of 3.3, not a rejection of it**, but it is a
change to the stated rule and needs sign-off.

### 10.2 `PERIOD_VALUES` carry-forward is invalid (brief §3.6) — HIGH

**Concern:** brief 3.6 says to carry forward the legacy constant lists "re-verified against
current docs." The re-verification result is that `PERIOD_VALUES = ["annual", "quarter"]` is
correct for 7 of the 25 endpoints that take `period`, and
`TECHNICAL_INDICATORS_TIME_DELTA_VALUES` contains a dead `v3` token (`daily`, now `1day`).

If these are carried forward as validators, the SDK will reject valid FMP input on 18 endpoints —
a new, self-inflicted version of the exact failure mode (silent wrongness that looks like
correctness) the rewrite exists to eliminate. See §8.1–§8.3 for the corrected constants.

> **Resolved:** corrected constants (§8.1–§8.3) accepted, including the industries/sectors
> hybrid (static fallback constant, live endpoint as source of truth).

### 10.3 The `List[Dict]` response contract has at least one real exception (brief §3.6) — MEDIUM

**Concern:** the contract is verified correct for all 276 documented examples, which is a strong
result. But `financial-reports-xlsx` almost certainly returns binary (its documented example is a
copy-paste of the JSON endpoint's), and the 18 `*-bulk` endpoints show every numeric value quoted
as a string, the signature of a CSV payload rendered as JSON for the docs.

**Ask:** decide the bulk return contract **once, before implementation**, not per-method, and
decide it after a keyed live test. Nineteen methods is 8% of the surface — too many to leave to
per-method improvisation. See §8.4.

> **Resolved:** deferred to implementation — the two live calls needed (one bulk endpoint, one
> `financial-reports-xlsx` call) happen when those methods are built, per the session's live-testing
> discipline. Not an abstract decision to make in advance.

### 10.4 The catalog is 243 endpoints, not ~360 (brief §1, §2, §4) — MEDIUM

**Concern:** the brief repeatedly says "~360 documented `stable` endpoints." The live document
contains 287 sections, 276 of which are REST endpoints with a `stable/` URL, resolving to **243
unique paths**. The remaining 11 are WebSocket message schemas already scoped out.

This is not a coverage gap — nothing is missing. But it materially changes the scope estimate,
the number of scaffolded tests (brief 3.6), and the size of the generated cross-reference table.
Worth correcting in the brief so nobody later thinks 117 endpoints went missing.

> **Resolved:** correction accepted. 243 unique endpoints / 238 canonical methods is the scope
> going forward.

### 10.5 The §3.3 false-positive list appears to be stale — LOW

**Concern:** brief 3.3 reports live-testing 8 collision candidates and finding that bare
`williams`, `press-releases`, `holdings`, `holder-performance-summary`, and `industry-summary`
"are listed in FMP's own docs" but 404. Those bare slugs **do not appear anywhere in the current
`api-docs.md`** — only the nested forms (`technical-indicators/williams`,
`news/press-releases`, `etf/holdings`, `institutional-ownership/holder-performance-summary`,
`institutional-ownership/industry-summary`) are documented, each exactly once.

The scan was probably run against sidebar/nav labels rather than the endpoint URLs. The
*discipline* the brief draws from it ("test before trusting the docs") is right and is applied
throughout this spec. The specific finding should just be marked stale so it is not cited later
as evidence that the docs list phantom endpoints — on the evidence of §8.5, they do not.

Note the genuine collisions are confirmed exactly as the brief states: three leaf names
(`latest`, `cik`, `symbol`) across six endpoints, in two families
(`insider-trading` / `institutional-ownership`, and `sec-filings-search` /
`sec-filings-company-search`). No other leaf name is reused anywhere in the catalog.

> **Resolved:** correction accepted, marked stale. Moot in practice now that §2.1's unconditional
> full-path rule (§10.1) makes the bare-leaf question itself moot.

### 10.6 "One test file mirrors one method-group" needs the primary-group rule — LOW

**Concern:** brief 3.6 wants the structure to make "one test file mirrors one method-group"
straightforward. Ten methods live in more than one group (§4.3), so "which file tests
`quote`?" is ambiguous without a rule.

**Proposed resolution (§3.4):** every method has exactly one **primary** group; tests live with
the primary. Cross-listings get one shared identity assertion
(`assert client.crypto.quote is client.quote.quote`) rather than duplicated behavioural tests.

Also note the group sizes are lopsided: `statements` (27) and `bulk` (18) will produce large test
files while `commodity`, `crypto`, and `forex` produce nearly empty ones. Acceptable, but plan
for it rather than discovering it.

> **Resolved:** primary-group + shared identity-assertion rule accepted as proposed.

### 10.7 Things the brief got right that are worth confirming explicitly

- **Flat-canonical + thin aliases** is the correct call, and §7.4 and §7.10 are the evidence:
  FMP's namespace is 78% flat, and its conceptual families repeatedly do not match its path
  families. Only a two-layer design can be faithful to the paths *and* coherent for users.
- **Typed exceptions over silent `None`/error-dicts** — §8.4 shows why. Two endpoints in the
  catalog will return something that is not a JSON array, and the old design would have handed
  the caller a `dict` that looks like data. That is issue #60 all over again.
- **Header auth** — correct and, incidentally, avoids leaking the key into the `from`/`to` query
  strings that 60+ endpoints use, which tend to end up in logs.
- **The 402-message wording ("request", not "endpoint")** — confirmed necessary: many endpoints
  in this catalog are gated per-symbol or per-plan-tier rather than wholesale.

---

## 11. Implied package layout

Nothing here contradicts brief 3.6; it is the structure that falls out of §2–§5.

```
fmpsdk/
    __init__.py            Client, exception hierarchy, version.
    client.py              Client class. Owns api_key (mutable), session, timeouts, retry
                           policy, the single request/response/error-mapping path.
                           All 238 canonical methods are defined on it or mixed into it.
    exceptions.py          FMPError hierarchy (brief 3.6, unchanged).
    constants.py           PERIOD_ANNUAL_QUARTER / PERIOD_FISCAL / PERIOD_ANY,
                           TIMEFRAME_INTRADAY / TIMEFRAME_TECHNICAL,
                           INDUSTRY_VALUES, SECTOR_VALUES, ECONOMIC_INDICATOR_VALUES (+1),
                           TECHNICAL_INDICATOR_NAMES.  (§8.1-§8.3)
    endpoints/             One module per alias group, 29 modules. Each defines the canonical
        search.py          methods for its PRIMARY members only. Mixed into Client.
        directory.py       Module name == group name == test file stem.
        ...                (statements.py is the largest at 27; commodity/crypto/forex are 1.)
    groups.py              The 29 alias group objects. Pure attribute binding to bound methods
                           on the client, including the 10 cross-listings (§4.3). No logic.
    types/                 TypedDicts, generated from api-docs.md example responses. Amended
                           2026-08-23: originally a single types.py per this section as
                           written; split into a package (one module per alias group,
                           mirroring endpoints/) once it passed ~2900 lines / 155 types
                           across 27 groups. The split is mechanical and lossless — no
                           TypedDict is used by more than one group's endpoints/<group>.py,
                           so group ownership falls out of the existing import graph, not a
                           judgment call. types/__init__.py re-exports every name, so
                           `from ..types import X` in every endpoints/<group>.py is
                           unchanged; nothing outside this package needs to know the split
                           exists. Same file-per-group convention as endpoints/.
    _crossref.py           Generated FMP-path <-> method-name table (§2.4). Regenerable from
                           api-docs.md in one pass; feeds the README table required by brief 3.2.
tests/
    unit/test_<group>.py   Mocked. One file per alias group, matching endpoints/<group>.py.
    live/test_<group>.py   Free-tier-reachable.
    ultimate/              Gated, deferred.
    test_aliases.py        Identity assertions for all 10 cross-listings + a check that every
                           canonical method is reachable from at least one group.
```

**Two invariants worth enforcing in CI**, because they are what keeps the design from eroding:

1. **Name/path round-trip.** For every canonical method, `name == path.replace("/", "_").replace("-", "_")`.
   Exactly one documented exception: `historical_chart` (§5.3). A test that asserts this over the
   whole surface catches naming drift the moment it is introduced.
2. **Alias identity.** For every cross-listing, `getattr(group_a, n) is getattr(group_b, n)`.
   This is the mechanical guarantee that the alias layer never becomes a second implementation
   (brief 3.2).

---

## 12. Open items requiring a live API key

Consolidated so they can be run in one pass. None of them block starting implementation; all of
them should be resolved before the affected methods are finalized.

| # | Question | Affects | Fallback if untested |
|---|---|---|---|
| 1 | Does `financial-reports-xlsx` return binary or JSON? | 1 method's return type | Implement as `bytes`, document the uncertainty |
| 2 | Do the 18 `*-bulk` endpoints return CSV or JSON? | 18 methods' return contract | Content-type sniff at the JSON boundary; decide once |
| 3 | Is `sec-profile`'s second parameter `cik` or `cik-A`? | 1 parameter name | Implement `cik` |
| 4 | What does `symbol-change`'s `invalid` parameter do? | 1 docstring | Pass through, document as "undocumented by FMP" |
| 5 | Does `historical-chart/*` accept `nonadjusted`/`extended` for non-equity symbols? | §4.2 union decision | Send them; FMP ignores unknown params |
| 6 | Does `senate-net-worth` honour `page`/`limit`? | §8.5 | Support them |
| 7 | Do `INDUSTRY_VALUES` / `SECTOR_VALUES` still match `available-industries` / `available-sectors`? | 2 constants | Prefer the live endpoints as source of truth |
