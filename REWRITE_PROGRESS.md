# fmpsdk Rewrite — Implementation Progress

Checklist of all 238 canonical methods from `REWRITE_ARCHITECTURE.md` §6.
Generated from that file — if the catalog changes, regenerate rather than hand-edit the list.

## How to use this file

Update the checkbox and status tag as each method is actually built and tested — this
file, not memory or conversation history, is the source of truth for "what's left."
Commit it alongside the method(s) it tracks, as its own line in the diff.

**Status tags** (append after the method name once it's past `[ ]`):
- `[x] unit` — implemented, mocked unit test passing, not yet live-verified
- `[x] live` — implemented, unit-tested, and live-verified against the real API (Bucket 1)
- `[x] ultimate-pending` — implemented and unit-tested; confirmed to 402 on every FMP tier
  tested so far (see the parenthetical after each line for exactly which tiers)
- `[x] done` — implemented, unit-tested, live-verified on some real tier, nothing left.
  Check the parenthetical: plain `done` with no tier note means free-tier; `(works on
  Starter tier; ...)` etc. means it needed that paid tier or higher
- `[ ] blocked: <reason>` — attempted, hit something unexpected (e.g. a doc/reality
  mismatch worth flagging), not resolved yet

**FMP's real pricing ladder is Free → Starter → Premium → Ultimate** (not just
Free/Ultimate as earlier notes in this project assumed) — see the dated entry below and
[[fmpsdk-rewrite-status]] for how that was discovered. The plan: whenever Dax upgrades to
the next paid tier, re-run `pytest tests/ultimate/ -m ultimate`, move whatever now passes
into `tests/live/`, and repeat at the next tier up. A method still `ultimate-pending` after
a tier's pass hasn't necessarily earned the name "needs Ultimate" — it just hasn't been
confirmed working yet at any tier tried so far; the parenthetical always says which tiers
it's actually been tested against and failed on.

**Bucket note:** group-level Bucket 2 flags below are a best-effort carry-over from the
original pricing-tier audit earlier in this project, not verified per-method. The actual
live-testing discipline (attempt each method as it's built, one fixed cheap test case)
is the real source of truth — if a "Bucket 1" method 402s, mark it `ultimate-pending`
and move on; if a "Bucket 2" method turns out to work on the current key, even better.

**Progress: 231 / 238 methods done, 7 ultimate-pending, 0 left untested.** **This
is the full 238/238 catalog now implemented in code, and every single method has now
been attempted at least once (unit-tested, and live-tested except where already
Bucket-2-confirmed)** — every canonical method in REWRITE_ARCHITECTURE.md §6 has a
Python implementation and a test result. 2026-08-23's second work session
unit-tested and live-tested all 45 `indexes`-through-`technical_indicators` methods
from the first code-only pass; a third session live-tested `market_performance`
(11/11, no 402s), wrote mocked unit tests for all 79 methods in `news`/`quote`/
`sec_filings`/`earnings_transcript`/`congress`/`bulk`/`tipranks` (268/268 unit tests
passing), then live-tested all 79 of those too — 19 more passed free-tier
(`fmp_articles`; `quote`/`quote_short`/`aftermarket_quote`/`aftermarket_trade`/
`stock_price_change`; 10 of 12 `sec_filings` methods; `house_latest`/
`senate_latest`), the remaining 60 402'd and moved to `ultimate-pending`
(`earnings_transcript`, `bulk`, and `tipranks` confirmed fully gated as their
pre-flagged Bucket 2 status predicted; `news`'s `batch_*` quote family and most of
`congress` turned out gated too, despite no Bucket 2 flag in §3.5 — see the
per-group notes below).

**2026-08-23, later — Dax upgraded Free → Starter.** Learned FMP's pricing ladder
actually has 4 tiers (Free/Starter/Premium/Ultimate), not the Free/Ultimate binary this
project assumed until now. Re-ran all 129 `ultimate-pending` methods' existing
`tests/ultimate/` test bodies (no new tests needed to write) against the Starter-tier
key: **51 now pass, 78 still 402.** All 51 moved into `tests/live/` (merged into each
group's existing live file, or a new one where the whole group had been gated), tagged
`done` with a "works on Starter tier" note below; the 78 still-gated stay
`ultimate-pending`, now annotated "402 on free tier and on Starter tier" so a future
Premium-tier pass knows exactly what's already been ruled out. Full groups that flipped
entirely to `done`: `directory` (10/10), `insider_trades` (4/4, closing that group out
completely), `technical_indicators` (9/9, closing that group out completely),
`sec_filings` (2/2, closing that group out completely — all 12 methods now done),
`calendar`'s IPOs (3/3), `chart`'s `historical_chart` (closing that group out
completely), `economics`'s `economic_calendar` (closing that group out completely),
`search`'s remaining 4 (closing that group out completely). Partial flips: `news` (7 of
9 402'd methods now pass — only the 2 press-releases methods still gated), `congress`
(6 of 10 — the symbol/name-scoped trade lookups now work, the 4 senate-profile-shaped
methods don't), `funds` (3 of 9 — the informational ETF endpoints work, the disclosure/
holdings ones don't), `company` (1 of 3 — `mergers_acquisitions_latest` only). Groups
that stayed **fully** gated even at Starter: `bulk` (18), `commitment_of_traders` (3),
`earnings_transcript` (4), `esg` (3), `institutional_ownership` (8), `tipranks` (7),
`indexes`'s constituent-list methods (6), `quote`'s `batch_*` family (11), `statements`'s
TTM/latest (4). Whole test suite re-run after the reorg: 268/268 unit, 160/160 live
(includes the 51 newly-moved), 78/78 ultimate still failing as expected — clean split,
no regressions. Docstrings for all affected methods/groups updated same session to state
the new Starter-tier facts, replacing flat "requires Ultimate" claims (never actually
verified against a real Ultimate key) with "requires FMP Premium or Ultimate, not yet
confirmed which" wherever a method was still gated.

**2026-08-23, same day, later still — Dax upgraded Starter → Premium** (750 calls/min at
this tier). Re-ran the remaining 78 `ultimate-pending` methods' existing `tests/ultimate/`
test bodies against the Premium-tier key: **21 now pass, 57 still 402.** Same
move/retag/docstring process as the Starter pass. Groups that flipped entirely to `done`:
`commitment_of_traders` (3/3), `company` (now 3/3, closing that group out completely —
`mergers_acquisitions_search` and `executive_compensation_benchmark` were the last 2),
`congress` (now 10/10 + the 2 free-tier `-latest` listings = 12/12, closing that group out
completely), `indexes` (all 6 constituent-list methods, closing that group out
completely), `news` (now 10/10, closing that group out completely — `news_press_releases`
and `news_press_releases_latest` were the last 2). Partial: `quote` (4 of the remaining 7
`batch_*` methods now pass — `batch_quote`, `batch_quote_short`,
`batch_aftermarket_quote`, `batch_aftermarket_trade`; the other 7, including
`batch_exchange_quote` and all 6 whole-asset-class ones, still gated). Groups that stayed
**fully** gated even at Premium: `bulk` (18), `earnings_transcript` (4), `esg` (3), `funds`
(6 remaining), `institutional_ownership` (8), `statements`'s TTM/latest (4), `tipranks`
(7) — these 57 now carry "402 on free, Starter, and Premium tiers" and await a future
Ultimate-tier pass (the last rung on FMP's ladder, so whatever's still gated there simply
*is* Ultimate-only — no more ambiguity to track past that point). Whole suite re-verified:
268/268 unit, 181/181 live, 57/57 ultimate still failing as expected — clean split, no
regressions. Docstrings updated same session for all 6 affected groups/methods.

**2026-08-24 — Dax upgraded Premium → Ultimate** (3000 calls/min at this tier — FMP's top
standard plan). Re-ran the remaining 57 `ultimate-pending` methods against the
Ultimate-tier key: **50 now pass, 7 still 402.** Along the way, running `bulk`'s tests for
the first time against a real 200 response (rather than an immediate 402) surfaced a real
bug that had nothing to do with plan tier: **every `client.bulk` method's real response is
CSV (`text/csv`), not JSON**, despite FMP's own docs showing JSON-looking examples — the
existing code called `Client._get`, which parses JSON and raised `JSONDecodeError` against
real bulk data. Fixed by adding `Client._get_csv` (shares the retry/error-mapping core via
`_request`, same pattern as `_get_bytes` for `financial_reports_xlsx`) and switching all 18
`bulk` methods to it. Field names/order in every existing `*BulkResult` TypedDict were
verified against real CSV headers and all matched exactly — the one exception was
`profile_bulk`, previously typed as the JSON-shaped `ProfileResult` on the (wrong) belief
that it was the one bulk method returning real JSON; it's CSV too, all-`str` like every
other bulk method, so a new `ProfileBulkResult` TypedDict replaces that reuse. `tests/unit/
test_bulk.py`'s 18 mocks switched from `json=` to `text=` CSV fixtures to match. See
[[fmpsdk-rewrite-status]] for the full account.

Groups that flipped entirely to `done`: `bulk` (all 18, once the CSV fix landed),
`earnings_transcript` (4/4), `esg` (3/3), `institutional_ownership` (8/8), `funds` (now
9/9, closing that group out completely), `quote` (now 16/16, closing that group out
completely — the remaining 7 `batch_*` methods), `statements` (now 27/27, closing that
group out completely — the TTM/`latest_financial_statements` quartet). **`tipranks`'s 7
methods still 402 even on Ultimate — but this is not a tier gap.** FMP's own error message
names the real cause: a separate paid add-on ("TipRanks data boost"), purchased
independently of the Free/Starter/Premium/Ultimate ladder via the dashboard's Add-ons tab.
Retagged accordingly below rather than left implying a 5th tier exists. Whole suite
re-verified: 268/268 unit, 231/231 live, 7/7 ultimate (tipranks) still failing as
expected — clean split, no regressions. Docstrings updated same session for all 7 affected
groups/methods (including a genuine mistake caught and fixed from the Premium-pass
session: `quote`'s module docstring had wrongly claimed 7 `batch_*` methods were
"confirmed working on Premium" when they'd actually still been gated at that tier).

**This closes out the entire standard-tier testing backlog — 231/238 done, with the
remaining 7 blocked on a separate product purchase (TipRanks add-on) rather than a plan
tier, and nothing left to re-test unless Dax buys that add-on.**

---

## `client.search` — Identifier lookup (symbol/name/CIK/CUSIP/ISIN) and the screener.

7 methods.

> **Correction to the group directory's Bucket assignment:** not flagged as
> Bucket 2 in REWRITE_ARCHITECTURE.md §3.5, but live-testing found 4 of 7
> methods 402 on the free tier anyway. Reclassified below per the workflow
> doc's "if a Bucket 1 method 402s, mark it `ultimate-pending`" rule.

- [x] done `company_screener` — `company-screener` (works on Starter tier; 402 on free tier)
- [x] done `search_cik` — `search-cik`
- [x] done `search_cusip` — `search-cusip` (works on Starter tier; 402 on free tier)
- [x] done `search_exchange_variants` — `search-exchange-variants` (works on Starter tier; 402 on free tier)
- [x] done `search_isin` — `search-isin` (works on Starter tier; 402 on free tier)
- [x] done `search_name` — `search-name`
- [x] done `search_symbol` — `search-symbol`

## `client.directory` — Whole-universe reference lists: symbols, exchanges, sectors, industries, countries.

10 methods.

> **Correction to the group directory's Bucket assignment:** not flagged as
> Bucket 2 in REWRITE_ARCHITECTURE.md §3.5, but live-testing found all 10
> of 10 methods 402 on the free tier — the whole group, not a subset like
> `search`'s 4/7. Reclassified below per the workflow doc's "if a Bucket 1
> method 402s, mark it `ultimate-pending`" rule.

- [x] done `actively_trading_list` — `actively-trading-list` (works on Starter tier; 402 on free tier)
- [x] done `available_countries` — `available-countries` (works on Starter tier; 402 on free tier)
- [x] done `available_exchanges` — `available-exchanges` (works on Starter tier; 402 on free tier)
- [x] done `available_industries` — `available-industries` (works on Starter tier; 402 on free tier)
- [x] done `available_sectors` — `available-sectors` (works on Starter tier; 402 on free tier)
- [x] done `cik_list` — `cik-list` (works on Starter tier; 402 on free tier)
- [x] done `etf_list` — `etf-list` (works on Starter tier; 402 on free tier)
- [x] done `financial_statement_symbol_list` — `financial-statement-symbol-list` (works on Starter tier; 402 on free tier)
- [x] done `stock_list` — `stock-list` (works on Starter tier; 402 on free tier)
- [x] done `symbol_change` — `symbol-change` (works on Starter tier; 402 on free tier)

## `client.analyst` — Sell-side estimates, ratings, price targets, grades.

8 methods.

- [x] done `analyst_estimates` — `analyst-estimates`
- [x] done `grades` — `grades`
- [x] done `grades_consensus` — `grades-consensus`
- [x] done `grades_historical` — `grades-historical`
- [x] done `price_target_consensus` — `price-target-consensus`
- [x] done `price_target_summary` — `price-target-summary`
- [x] done `ratings_historical` — `ratings-historical`
- [x] done `ratings_snapshot` — `ratings-snapshot`

## `client.calendar` — Date-driven corporate events: dividends, earnings, IPOs, splits.

9 methods.

> **Correction to the group directory's Bucket assignment:** not flagged as
> Bucket 2 in REWRITE_ARCHITECTURE.md §3.5, but live-testing found the 3
> `ipos_*` methods 402 on the free tier — the whole IPOs category, while
> dividends/earnings/splits are all free-tier reachable. Reclassified below
> per the workflow doc's "if a Bucket 1 method 402s, mark it
> `ultimate-pending`" rule.

- [x] done `dividends` — `dividends`
- [x] done `dividends_calendar` — `dividends-calendar`
- [x] done `earnings` — `earnings`
- [x] done `earnings_calendar` — `earnings-calendar`
- [x] done `ipos_calendar` — `ipos-calendar` (works on Starter tier; 402 on free tier)
- [x] done `ipos_disclosure` — `ipos-disclosure` (works on Starter tier; 402 on free tier)
- [x] done `ipos_prospectus` — `ipos-prospectus` (works on Starter tier; 402 on free tier)
- [x] done `splits` — `splits`
- [x] done `splits_calendar` — `splits-calendar`

## `client.chart` — Historical price series, EOD and intraday, for every asset class.

5 methods.

> **Correction to the group directory's Bucket assignment:** not flagged as
> Bucket 2 in REWRITE_ARCHITECTURE.md §3.5, but live-testing found
> `historical_chart` (all 6 intraday timeframes) 402s on the free tier
> while all 4 `historical_price_eod_*` daily methods work. Reclassified
> below per the workflow doc's "if a Bucket 1 method 402s, mark it
> `ultimate-pending`" rule.

- [x] done `historical_chart` — `historical-chart/{timeframe}` (works on Starter tier; 402 on free tier)
- [x] done `historical_price_eod_dividend_adjusted` — `historical-price-eod/dividend-adjusted`
- [x] done `historical_price_eod_full` — `historical-price-eod/full`
- [x] done `historical_price_eod_light` — `historical-price-eod/light`
- [x] done `historical_price_eod_non_split_adjusted` — `historical-price-eod/non-split-adjusted`

## `client.company` — Company-level reference and profile data, incl. market cap, float, executives, M&A.

17 methods.

> **Correction to the group directory's Bucket assignment:** not flagged as
> Bucket 2 in REWRITE_ARCHITECTURE.md §3.5, but live-testing found 3 of 17
> methods 402 on the free tier. Reclassified below per the workflow doc's
> "if a Bucket 1 method 402s, mark it `ultimate-pending`" rule.

- [x] done `company_notes` — `company-notes`
- [x] done `delisted_companies` — `delisted-companies`
- [x] done `employee_count` — `employee-count`
- [x] done `executive_compensation_benchmark` — `executive-compensation-benchmark` (works on Premium tier; 402 on free and Starter tiers)
- [x] done `governance_executive_compensation` — `governance-executive-compensation`
- [x] done `historical_employee_count` — `historical-employee-count`
- [x] done `historical_market_capitalization` — `historical-market-capitalization`
- [x] done `key_executives` — `key-executives`
- [x] done `market_capitalization` — `market-capitalization`
- [x] done `market_capitalization_batch` — `market-capitalization-batch`
- [x] done `mergers_acquisitions_latest` — `mergers-acquisitions-latest` (works on Starter tier; 402 on free tier)
- [x] done `mergers_acquisitions_search` — `mergers-acquisitions-search` (works on Premium tier; 402 on free and Starter tiers)
- [x] done `profile` — `profile`
- [x] done `profile_cik` — `profile-cik`
- [x] done `shares_float` — `shares-float`
- [x] done `shares_float_all` — `shares-float-all`
- [x] done `stock_peers` — `stock-peers`

## `client.commitment_of_traders` — CFTC Commitment-of-Traders reports and analysis.

3 methods.

> **Correction to the group directory's Bucket assignment:** not flagged as
> Bucket 2 in REWRITE_ARCHITECTURE.md §3.5, but live-testing found all 3
> methods 402 on the free tier. Reclassified below per the workflow doc's
> "if a Bucket 1 method 402s, mark it `ultimate-pending`" rule.

- [x] done `commitment_of_traders_analysis` — `commitment-of-traders-analysis` (works on Premium tier; 402 on free and Starter tiers)
- [x] done `commitment_of_traders_list` — `commitment-of-traders-list` (works on Premium tier; 402 on free and Starter tiers)
- [x] done `commitment_of_traders_report` — `commitment-of-traders-report` (works on Premium tier; 402 on free and Starter tiers)

## `client.dcf` — Discounted-cash-flow valuations, standard and custom-input.

4 methods.

- [x] done `custom_discounted_cash_flow` — `custom-discounted-cash-flow`
- [x] done `custom_levered_discounted_cash_flow` — `custom-levered-discounted-cash-flow`
- [x] done `discounted_cash_flow` — `discounted-cash-flow`
- [x] done `levered_discounted_cash_flow` — `levered-discounted-cash-flow`

## `client.economics` — Macroeconomic series, treasury rates, economic calendar, risk premium.

4 methods.

> **Correction to the group directory's Bucket assignment:** not flagged as
> Bucket 2 in REWRITE_ARCHITECTURE.md §3.5, but live-testing found
> `economic_calendar` 402s on the free tier while the other 3 work.
> Reclassified below per the workflow doc's "if a Bucket 1 method 402s,
> mark it `ultimate-pending`" rule.

- [x] done `economic_calendar` — `economic-calendar` (works on Starter tier; 402 on free tier)
- [x] done `economic_indicators` — `economic-indicators`
- [x] done `market_risk_premium` — `market-risk-premium`
- [x] done `treasury_rates` — `treasury-rates`

## `client.esg` — ESG disclosures, ratings, and benchmarks.

> **Bucket 2 (Ultimate-gated), confirmed live:** the pricing-audit prediction held —
> all 3 methods 402 on the free tier. Tests live in `tests/ultimate/test_esg.py` only.

3 methods.

- [x] done `esg_benchmark` — `esg-benchmark` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `esg_disclosures` — `esg-disclosures` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `esg_ratings` — `esg-ratings` (works on Ultimate tier; 402 on free, Starter, and Premium)

## `client.funds` — ETF and mutual-fund composition, info, and N-PORT/13F-style disclosures.

9 methods.

> **Correction to the group directory's Bucket assignment:** not flagged as
> Bucket 2 in REWRITE_ARCHITECTURE.md §3.5, but live-testing found all 9
> methods 402 on the free tier. Reclassified below per the workflow doc's
> "if a Bucket 1 method 402s, mark it `ultimate-pending`" rule.

- [x] done `etf_asset_exposure` — `etf/asset-exposure` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `etf_country_weightings` — `etf/country-weightings` (works on Starter tier; 402 on free tier)
- [x] done `etf_holdings` — `etf/holdings` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `etf_info` — `etf/info` (works on Starter tier; 402 on free tier)
- [x] done `etf_sector_weightings` — `etf/sector-weightings` (works on Starter tier; 402 on free tier)
- [x] done `funds_disclosure` — `funds/disclosure` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `funds_disclosure_dates` — `funds/disclosure-dates` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `funds_disclosure_holders_latest` — `funds/disclosure-holders-latest` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `funds_disclosure_holders_search` — `funds/disclosure-holders-search` (works on Ultimate tier; 402 on free, Starter, and Premium)

## `client.statements` — Financial statements and everything computed directly from them.

27 methods.

> **Correction to the group directory's Bucket assignment:** not flagged as
> Bucket 2 in REWRITE_ARCHITECTURE.md §3.5, but live-testing found 4 of 27
> methods 402 on the free tier. Reclassified below per the workflow doc's
> "if a Bucket 1 method 402s, mark it `ultimate-pending`" rule.
>
> **Two doc/reality mismatches found and resolved, not just noted:**
> `financial_reports_xlsx` really does return binary XLSX bytes (verified
> via ZIP magic bytes `PK\x03\x04`) despite a lying `application/json`
> content-type header and a docs example that's a copy-paste of the JSON
> endpoint's — exactly what REWRITE_ARCHITECTURE.md §8.4 predicted and
> flagged for live verification. `financial_reports_json` turned out to
> return a single bare object, **not** array-wrapped like the other 242
> endpoints in the catalog (contradicting FMP's own docs, which show it
> array-wrapped) — a second, previously-unflagged exception to the
> `List[Dict]` response contract. Both are implemented correctly (not
> forced into the wrong shape) — see `client.py`'s `_get_bytes()` and
> `financial_reports_json`'s return type in `endpoints/statements.py`.

- [x] done `balance_sheet_statement` — `balance-sheet-statement`
- [x] done `balance_sheet_statement_as_reported` — `balance-sheet-statement-as-reported`
- [x] done `balance_sheet_statement_growth` — `balance-sheet-statement-growth`
- [x] done `balance_sheet_statement_ttm` — `balance-sheet-statement-ttm` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `cash_flow_statement` — `cash-flow-statement`
- [x] done `cash_flow_statement_as_reported` — `cash-flow-statement-as-reported`
- [x] done `cash_flow_statement_growth` — `cash-flow-statement-growth`
- [x] done `cash_flow_statement_ttm` — `cash-flow-statement-ttm` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `enterprise_values` — `enterprise-values`
- [x] done `financial_growth` — `financial-growth`
- [x] done `financial_reports_dates` — `financial-reports-dates`
- [x] done `financial_reports_json` — `financial-reports-json` (returns a single dict, not array-wrapped — verified live, contradicts FMP's own docs)
- [x] done `financial_reports_xlsx` — `financial-reports-xlsx` (returns raw `bytes` — verified live per §8.4)
- [x] done `financial_scores` — `financial-scores`
- [x] done `financial_statement_full_as_reported` — `financial-statement-full-as-reported`
- [x] done `income_statement` — `income-statement`
- [x] done `income_statement_as_reported` — `income-statement-as-reported`
- [x] done `income_statement_growth` — `income-statement-growth`
- [x] done `income_statement_ttm` — `income-statement-ttm` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `key_metrics` — `key-metrics`
- [x] done `key_metrics_ttm` — `key-metrics-ttm`
- [x] done `latest_financial_statements` — `latest-financial-statements` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `owner_earnings` — `owner-earnings`
- [x] done `ratios` — `ratios`
- [x] done `ratios_ttm` — `ratios-ttm`
- [x] done `revenue_geographic_segmentation` — `revenue-geographic-segmentation`
- [x] done `revenue_product_segmentation` — `revenue-product-segmentation`

## `client.institutional_ownership` — Form 13F institutional holdings, holders, and derived analytics.

> **Bucket 2 (Ultimate-gated), confirmed live:** the pricing-audit prediction held —
> all 8 methods 402 on the free tier. Tests live in
> `tests/ultimate/test_institutional_ownership.py` only.

8 methods.

- [x] done `institutional_ownership_dates` — `institutional-ownership/dates` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `institutional_ownership_extract` — `institutional-ownership/extract` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `institutional_ownership_extract_analytics_holder` — `institutional-ownership/extract-analytics/holder` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `institutional_ownership_holder_industry_breakdown` — `institutional-ownership/holder-industry-breakdown` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `institutional_ownership_holder_performance_summary` — `institutional-ownership/holder-performance-summary` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `institutional_ownership_industry_summary` — `institutional-ownership/industry-summary` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `institutional_ownership_latest` — `institutional-ownership/latest` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `institutional_ownership_symbol_positions_summary` — `institutional-ownership/symbol-positions-summary` (works on Ultimate tier; 402 on free, Starter, and Premium)

## `client.indexes` — Stock-market indexes, their quotes/charts, and their constituent lists.

7 methods.

> **Unit-tested and live-tested 2026-08-23.** Only `index_list` is
> free-tier reachable — the other 6 own methods all 402 despite no
> Bucket 2 flag in REWRITE_ARCHITECTURE.md §3.5. 3 cross-listed from
> `client.chart` (`historical_chart`, `historical_price_eod_full`,
> `historical_price_eod_light`) already hold the identity invariant —
> verified via `assert client.indexes.historical_chart is
> client.chart.historical_chart` at write time.

- [x] done `dowjones_constituent` — `dowjones-constituent` (works on Premium tier; 402 on free and Starter tiers)
- [x] done `historical_dowjones_constituent` — `historical-dowjones-constituent` (works on Premium tier; 402 on free and Starter tiers)
- [x] done `historical_nasdaq_constituent` — `historical-nasdaq-constituent` (works on Premium tier; 402 on free and Starter tiers)
- [x] done `historical_sp500_constituent` — `historical-sp500-constituent` (works on Premium tier; 402 on free and Starter tiers)
- [x] done `index_list` — `index-list`
- [x] done `nasdaq_constituent` — `nasdaq-constituent` (works on Premium tier; 402 on free and Starter tiers)
- [x] done `sp500_constituent` — `sp500-constituent` (works on Premium tier; 402 on free and Starter tiers)

## `client.commodity` — Commodity instruments: list, quotes, charts.

1 methods.

> **Unit-tested and live-tested 2026-08-23.** `quote`/`quote_short`/
> `batch_commodity_quotes` will cross-list here once `client.quote` is
> built; the 3 `client.chart` cross-listings are already wired.

- [x] done `commodities_list` — `commodities-list`

## `client.crypto` — Cryptocurrency instruments: list, quotes, charts.

1 methods.

> **Unit-tested and live-tested 2026-08-23.** Same cross-listing note as
> `client.commodity` above.

- [x] done `cryptocurrency_list` — `cryptocurrency-list`

## `client.fundraisers` — Reg CF crowdfunding and Reg D/A equity offerings.

6 methods.

> **Unit-tested and live-tested 2026-08-23** — all 6 free-tier reachable.

- [x] done `crowdfunding_offerings` — `crowdfunding-offerings`
- [x] done `crowdfunding_offerings_latest` — `crowdfunding-offerings-latest`
- [x] done `crowdfunding_offerings_search` — `crowdfunding-offerings-search`
- [x] done `fundraising` — `fundraising`
- [x] done `fundraising_latest` — `fundraising-latest`
- [x] done `fundraising_search` — `fundraising-search`

## `client.forex` — FX pairs: list, quotes, charts.

1 methods.

> **Unit-tested and live-tested 2026-08-23.** Same cross-listing note as
> `client.commodity` above.

- [x] done `forex_list` — `forex-list`

## `client.insider_trades` — Form 4 insider transactions, statistics, and beneficial-ownership acquisitions.

6 methods.

> **Unit-tested and live-tested 2026-08-23.** Only `insider_trading_latest`
> and `insider_trading_transaction_type` are free-tier reachable — the
> other 4 all 402 despite no Bucket 2 flag in REWRITE_ARCHITECTURE.md §3.5.

- [x] done `acquisition_of_beneficial_ownership` — `acquisition-of-beneficial-ownership` (works on Starter tier; 402 on free tier)
- [x] done `insider_trading_latest` — `insider-trading/latest`
- [x] done `insider_trading_reporting_name` — `insider-trading/reporting-name` (works on Starter tier; 402 on free tier)
- [x] done `insider_trading_search` — `insider-trading/search` (works on Starter tier; 402 on free tier)
- [x] done `insider_trading_statistics` — `insider-trading/statistics` (works on Starter tier; 402 on free tier)
- [x] done `insider_trading_transaction_type` — `insider-trading-transaction-type`

## `client.market_performance` — Sector/industry performance and P/E, snapshot and historical, plus market leaders.

11 methods.

> **Unit- and live-tested 2026-08-23 — all 11 free-tier reachable, no 402s.**

- [x] done `biggest_gainers` — `biggest-gainers`
- [x] done `biggest_losers` — `biggest-losers`
- [x] done `historical_industry_pe` — `historical-industry-pe`
- [x] done `historical_industry_performance` — `historical-industry-performance`
- [x] done `historical_sector_pe` — `historical-sector-pe`
- [x] done `historical_sector_performance` — `historical-sector-performance`
- [x] done `industry_pe_snapshot` — `industry-pe-snapshot`
- [x] done `industry_performance_snapshot` — `industry-performance-snapshot`
- [x] done `most_actives` — `most-actives`
- [x] done `sector_pe_snapshot` — `sector-pe-snapshot`
- [x] done `sector_performance_snapshot` — `sector-performance-snapshot`

## `client.market_hours` — Exchange trading sessions and holiday calendars.

3 methods.

> **Unit-tested and live-tested 2026-08-23** — all 3 free-tier reachable.

- [x] done `all_exchange_market_hours` — `all-exchange-market-hours`
- [x] done `exchange_market_hours` — `exchange-market-hours`
- [x] done `holidays_by_exchange` — `holidays-by-exchange`

## `client.technical_indicators` — Computed technical indicator series.

9 methods.

> **Unit-tested and live-tested 2026-08-23** — all 9 402 on the free
> tier, the whole group gated, despite no Bucket 2 flag in
> REWRITE_ARCHITECTURE.md §3.5.

- [x] done `technical_indicators_adx` — `technical-indicators/adx` (works on Starter tier; 402 on free tier)
- [x] done `technical_indicators_dema` — `technical-indicators/dema` (works on Starter tier; 402 on free tier)
- [x] done `technical_indicators_ema` — `technical-indicators/ema` (works on Starter tier; 402 on free tier)
- [x] done `technical_indicators_rsi` — `technical-indicators/rsi` (works on Starter tier; 402 on free tier)
- [x] done `technical_indicators_sma` — `technical-indicators/sma` (works on Starter tier; 402 on free tier)
- [x] done `technical_indicators_standarddeviation` — `technical-indicators/standarddeviation` (works on Starter tier; 402 on free tier)
- [x] done `technical_indicators_tema` — `technical-indicators/tema` (works on Starter tier; 402 on free tier)
- [x] done `technical_indicators_williams` — `technical-indicators/williams` (works on Starter tier; 402 on free tier)
- [x] done `technical_indicators_wma` — `technical-indicators/wma` (works on Starter tier; 402 on free tier)

## `client.news` — News, press releases, and FMP editorial articles.

10 methods.

> **Unit- and live-tested 2026-08-23.** Only `fmp_articles` is free-tier reachable —
> the other 9 methods (the whole `NewsArticleResult`-shaped family: general/
> press-releases/stock/crypto/forex, each with a "-latest" sibling) all 402'd, despite
> no Bucket 2 flag in REWRITE_ARCHITECTURE.md §3.5 → `ultimate-pending`.

- [x] done `fmp_articles` — `fmp-articles`
- [x] done `news_crypto` — `news/crypto` (works on Starter tier; 402 on free tier)
- [x] done `news_crypto_latest` — `news/crypto-latest` (works on Starter tier; 402 on free tier)
- [x] done `news_forex` — `news/forex` (works on Starter tier; 402 on free tier)
- [x] done `news_forex_latest` — `news/forex-latest` (works on Starter tier; 402 on free tier)
- [x] done `news_general_latest` — `news/general-latest` (works on Starter tier; 402 on free tier)
- [x] done `news_press_releases` — `news/press-releases` (works on Premium tier; 402 on free and Starter tiers)
- [x] done `news_press_releases_latest` — `news/press-releases-latest` (works on Premium tier; 402 on free and Starter tiers)
- [x] done `news_stock` — `news/stock` (works on Starter tier; 402 on free tier)
- [x] done `news_stock_latest` — `news/stock-latest` (works on Starter tier; 402 on free tier)

## `client.quote` — Real-time and aftermarket quotes, single and batch.

16 methods.

> **Unit- and live-tested 2026-08-23.** Completes the full §4.3 cross-listing table:
> `quote`/`quote_short`/`batch_index_quotes`/`batch_commodity_quotes`/
> `batch_crypto_quotes`/`batch_forex_quotes` are wired into `client.indexes`/
> `commodity`/`crypto`/`forex` in `groups.py` — all 10 cross-listings in the whole
> rewrite are wired, identity-asserted at write time. The 5 single-symbol methods
> (`quote`, `quote_short`, `aftermarket_quote`, `aftermarket_trade`,
> `stock_price_change`) are free-tier reachable; all 11 `batch_*` methods 402'd — a
> clean split along §7.6's own singular/plural distinction.

- [x] done `aftermarket_quote` — `aftermarket-quote`
- [x] done `aftermarket_trade` — `aftermarket-trade`
- [x] done `batch_aftermarket_quote` — `batch-aftermarket-quote` (works on Premium tier; 402 on free and Starter tiers)
- [x] done `batch_aftermarket_trade` — `batch-aftermarket-trade` (works on Premium tier; 402 on free and Starter tiers)
- [x] done `batch_commodity_quotes` — `batch-commodity-quotes` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `batch_crypto_quotes` — `batch-crypto-quotes` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `batch_etf_quotes` — `batch-etf-quotes` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `batch_exchange_quote` — `batch-exchange-quote` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `batch_forex_quotes` — `batch-forex-quotes` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `batch_index_quotes` — `batch-index-quotes` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `batch_mutualfund_quotes` — `batch-mutualfund-quotes` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `batch_quote` — `batch-quote` (works on Premium tier; 402 on free and Starter tiers)
- [x] done `batch_quote_short` — `batch-quote-short` (works on Premium tier; 402 on free and Starter tiers)
- [x] done `quote` — `quote`
- [x] done `quote_short` — `quote-short`
- [x] done `stock_price_change` — `stock-price-change`

## `client.sec_filings` — SEC filing search, SEC company identity, and SIC industry classification.

12 methods.

> **Unit- and live-tested 2026-08-23.** 10 of 12 are free-tier reachable;
> `industry_classification_search` and `all_industry_classification` 402'd →
> `ultimate-pending`. `sec_profile`'s second parameter renders in FMP's own docs as
> `cik-A`, which reads like a table-rendering artifact rather than a real wire name —
> exposed here as plain `cik`; live-tested with `symbol` only (didn't spend an extra
> call probing the `cik-A` question), so that particular oddity is still unconfirmed
> either way.

- [x] done `all_industry_classification` — `all-industry-classification` (works on Starter tier; 402 on free tier)
- [x] done `industry_classification_search` — `industry-classification-search` (works on Starter tier; 402 on free tier)
- [x] done `sec_filings_8k` — `sec-filings-8k`
- [x] done `sec_filings_company_search_cik` — `sec-filings-company-search/cik`
- [x] done `sec_filings_company_search_name` — `sec-filings-company-search/name`
- [x] done `sec_filings_company_search_symbol` — `sec-filings-company-search/symbol`
- [x] done `sec_filings_financials` — `sec-filings-financials`
- [x] done `sec_filings_search_cik` — `sec-filings-search/cik`
- [x] done `sec_filings_search_form_type` — `sec-filings-search/form-type`
- [x] done `sec_filings_search_symbol` — `sec-filings-search/symbol`
- [x] done `sec_profile` — `sec-profile`
- [x] done `standard_industrial_classification_list` — `standard-industrial-classification-list`

## `client.earnings_transcript` — Earnings-call transcripts and their availability metadata.

> **Confirmed Bucket 2 (Ultimate-gated), 2026-08-23:** all 4 methods 402'd, matching
> the original pricing audit's prediction. `earnings_transcript_list` is cross-listed
> into `client.directory` (§4.3, itself fully gated) — consistent with this result.

4 methods.

- [x] done `earning_call_transcript` — `earning-call-transcript` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `earning_call_transcript_dates` — `earning-call-transcript-dates` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `earning_call_transcript_latest` — `earning-call-transcript-latest` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `earnings_transcript_list` — `earnings-transcript-list` (works on Ultimate tier; 402 on free, Starter, and Premium)

## `client.congress` — U.S. Senate and House financial disclosures, trades, and member profiles.

12 methods.

> **Unit- and live-tested 2026-08-23.** Only the parameterless `house_latest`/
> `senate_latest` listings are free-tier reachable — every symbol/id/name-scoped
> lookup (10 methods) 402'd. §7.5's parameter-naming bug mirrored as documented:
> `house_trades_by_id` and `senate_trades_by_id` (and every other `senateID`-taking
> method, including the House ones) expose the Python parameter `senate_id` — the
> wire name really is `senateID` even on House endpoints, called out loudly in
> `house_trades_by_id`'s own docstring so it doesn't read as our bug.

- [x] done `house_latest` — `house-latest`
- [x] done `house_trades` — `house-trades` (works on Starter tier; 402 on free tier)
- [x] done `house_trades_by_id` — `house-trades-by-id` (works on Starter tier; 402 on free tier)
- [x] done `house_trades_by_name` — `house-trades-by-name` (works on Starter tier; 402 on free tier)
- [x] done `senate_latest` — `senate-latest`
- [x] done `senate_net_worth` — `senate-net-worth` (works on Premium tier; 402 on free and Starter tiers)
- [x] done `senate_net_worth_aggregated` — `senate-net-worth-aggregated` (works on Premium tier; 402 on free and Starter tiers)
- [x] done `senate_positions` — `senate-positions` (works on Premium tier; 402 on free and Starter tiers)
- [x] done `senate_profile` — `senate-profile` (works on Premium tier; 402 on free and Starter tiers)
- [x] done `senate_trades` — `senate-trades` (works on Starter tier; 402 on free tier)
- [x] done `senate_trades_by_id` — `senate-trades-by-id` (works on Starter tier; 402 on free tier)
- [x] done `senate_trades_by_name` — `senate-trades-by-name` (works on Starter tier; 402 on free tier)

## `client.bulk` — Whole-universe bulk downloads.

> **Confirmed Bucket 2 (Ultimate-gated), 2026-08-23:** all 18 methods 402'd, matching
> the original pricing audit's prediction — the whole group, not a subset. 17 of 18
> methods return every field as a JSON string, including semantically numeric/boolean
> fields — a real, documented quirk (see `types/bulk.py`'s module docstring), not a
> transcription choice. `profile_bulk` is the lone exception (real JSON types) and
> reuses `ProfileResult` directly rather than duplicating it, since its example
> response is field-for-field identical to `profile`/`profile_cik`'s.

18 methods.

- [x] done `balance_sheet_statement_bulk` — `balance-sheet-statement-bulk` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `balance_sheet_statement_growth_bulk` — `balance-sheet-statement-growth-bulk` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `cash_flow_statement_bulk` — `cash-flow-statement-bulk` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `cash_flow_statement_growth_bulk` — `cash-flow-statement-growth-bulk` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `dcf_bulk` — `dcf-bulk` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `earnings_surprises_bulk` — `earnings-surprises-bulk` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `eod_bulk` — `eod-bulk` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `etf_holder_bulk` — `etf-holder-bulk` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `income_statement_bulk` — `income-statement-bulk` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `income_statement_growth_bulk` — `income-statement-growth-bulk` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `key_metrics_ttm_bulk` — `key-metrics-ttm-bulk` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `peers_bulk` — `peers-bulk` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `price_target_summary_bulk` — `price-target-summary-bulk` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `profile_bulk` — `profile-bulk` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `rating_bulk` — `rating-bulk` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `ratios_ttm_bulk` — `ratios-ttm-bulk` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `scores_bulk` — `scores-bulk` (works on Ultimate tier; 402 on free, Starter, and Premium)
- [x] done `upgrades_downgrades_consensus_bulk` — `upgrades-downgrades-consensus-bulk` (works on Ultimate tier; 402 on free, Starter, and Premium)

## `client.tipranks` — TipRanks partner analyst data.

> **Confirmed Bucket 2 (Ultimate-gated), 2026-08-23:** all 7 methods 402'd, matching
> the workflow doc's treat-as-Ultimate-until-proven-otherwise call — the whole group.
> `tipranks_pit_symbol` and `tipranks_pit_analyst` share one response type
> (`TipranksPointInTimeResult`) — identical fields in both documented examples. The 3
> summary methods (`tipranks_symbol_summary`/`tipranks_analyst_summary`/
> `tipranks_firm_summary`) each get their own top-level type (different identifying
> field: symbol/expertUID/firmName) but share two small nested breakdown types
> (`TipranksRecommendationBreakdown`, `TipranksAnalystActionBreakdown`).

7 methods.

- [x] ultimate-pending `tipranks_analyst_summary` — `tipranks-analyst-summary` (402 on every plan tier through Ultimate — requires FMP's separate TipRanks add-on, confirmed 2026-08-24)
- [x] ultimate-pending `tipranks_analysts` — `tipranks-analysts` (402 on every plan tier through Ultimate — requires FMP's separate TipRanks add-on, confirmed 2026-08-24)
- [x] ultimate-pending `tipranks_firm_summary` — `tipranks-firm-summary` (402 on every plan tier through Ultimate — requires FMP's separate TipRanks add-on, confirmed 2026-08-24)
- [x] ultimate-pending `tipranks_pit_analyst` — `tipranks-pit-analyst` (402 on every plan tier through Ultimate — requires FMP's separate TipRanks add-on, confirmed 2026-08-24)
- [x] ultimate-pending `tipranks_pit_symbol` — `tipranks-pit-symbol` (402 on every plan tier through Ultimate — requires FMP's separate TipRanks add-on, confirmed 2026-08-24)
- [x] ultimate-pending `tipranks_search` — `tipranks-search` (402 on every plan tier through Ultimate — requires FMP's separate TipRanks add-on, confirmed 2026-08-24)
- [x] ultimate-pending `tipranks_symbol_summary` — `tipranks-symbol-summary` (402 on every plan tier through Ultimate — requires FMP's separate TipRanks add-on, confirmed 2026-08-24)
