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
- `[x] ultimate-pending` — implemented and unit-tested; live verification blocked on the
  one-month Ultimate subscription (Bucket 2 — see below)
- `[x] done` — implemented, unit-tested, live-verified, nothing left
- `[ ] blocked: <reason>` — attempted, hit something unexpected (e.g. a doc/reality
  mismatch worth flagging), not resolved yet

**Bucket note:** group-level Bucket 2 flags below are a best-effort carry-over from the
original pricing-tier audit earlier in this project, not verified per-method. The actual
live-testing discipline (attempt each method as it's built, one fixed cheap test case)
is the real source of truth — if a "Bucket 1" method 402s, mark it `ultimate-pending`
and move on; if a "Bucket 2" method turns out to work on the current key, even better.

**Progress: 109 / 238 methods done, 129 ultimate-pending, 0 left untested.** **This
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
per-group notes below). Nothing left to test — what remains is only the
`ultimate-pending` methods' actual verification, deferred to a future paid Ultimate
month per the workflow doc.

---

## `client.search` — Identifier lookup (symbol/name/CIK/CUSIP/ISIN) and the screener.

7 methods.

> **Correction to the group directory's Bucket assignment:** not flagged as
> Bucket 2 in REWRITE_ARCHITECTURE.md §3.5, but live-testing found 4 of 7
> methods 402 on the free tier anyway. Reclassified below per the workflow
> doc's "if a Bucket 1 method 402s, mark it `ultimate-pending`" rule.

- [x] ultimate-pending `company_screener` — `company-screener` (402 on free tier)
- [x] done `search_cik` — `search-cik`
- [x] ultimate-pending `search_cusip` — `search-cusip` (402 on free tier)
- [x] ultimate-pending `search_exchange_variants` — `search-exchange-variants` (402 on free tier)
- [x] ultimate-pending `search_isin` — `search-isin` (402 on free tier)
- [x] done `search_name` — `search-name`
- [x] done `search_symbol` — `search-symbol`

## `client.directory` — Whole-universe reference lists: symbols, exchanges, sectors, industries, countries.

10 methods.

> **Correction to the group directory's Bucket assignment:** not flagged as
> Bucket 2 in REWRITE_ARCHITECTURE.md §3.5, but live-testing found all 10
> of 10 methods 402 on the free tier — the whole group, not a subset like
> `search`'s 4/7. Reclassified below per the workflow doc's "if a Bucket 1
> method 402s, mark it `ultimate-pending`" rule.

- [x] ultimate-pending `actively_trading_list` — `actively-trading-list` (402 on free tier)
- [x] ultimate-pending `available_countries` — `available-countries` (402 on free tier)
- [x] ultimate-pending `available_exchanges` — `available-exchanges` (402 on free tier)
- [x] ultimate-pending `available_industries` — `available-industries` (402 on free tier)
- [x] ultimate-pending `available_sectors` — `available-sectors` (402 on free tier)
- [x] ultimate-pending `cik_list` — `cik-list` (402 on free tier)
- [x] ultimate-pending `etf_list` — `etf-list` (402 on free tier)
- [x] ultimate-pending `financial_statement_symbol_list` — `financial-statement-symbol-list` (402 on free tier)
- [x] ultimate-pending `stock_list` — `stock-list` (402 on free tier)
- [x] ultimate-pending `symbol_change` — `symbol-change` (402 on free tier)

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
- [x] ultimate-pending `ipos_calendar` — `ipos-calendar` (402 on free tier)
- [x] ultimate-pending `ipos_disclosure` — `ipos-disclosure` (402 on free tier)
- [x] ultimate-pending `ipos_prospectus` — `ipos-prospectus` (402 on free tier)
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

- [x] ultimate-pending `historical_chart` — `historical-chart/{timeframe}` (402 on free tier)
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
- [x] ultimate-pending `executive_compensation_benchmark` — `executive-compensation-benchmark` (402 on free tier)
- [x] done `governance_executive_compensation` — `governance-executive-compensation`
- [x] done `historical_employee_count` — `historical-employee-count`
- [x] done `historical_market_capitalization` — `historical-market-capitalization`
- [x] done `key_executives` — `key-executives`
- [x] done `market_capitalization` — `market-capitalization`
- [x] done `market_capitalization_batch` — `market-capitalization-batch`
- [x] ultimate-pending `mergers_acquisitions_latest` — `mergers-acquisitions-latest` (402 on free tier)
- [x] ultimate-pending `mergers_acquisitions_search` — `mergers-acquisitions-search` (402 on free tier)
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

- [x] ultimate-pending `commitment_of_traders_analysis` — `commitment-of-traders-analysis` (402 on free tier)
- [x] ultimate-pending `commitment_of_traders_list` — `commitment-of-traders-list` (402 on free tier)
- [x] ultimate-pending `commitment_of_traders_report` — `commitment-of-traders-report` (402 on free tier)

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

- [x] ultimate-pending `economic_calendar` — `economic-calendar` (402 on free tier)
- [x] done `economic_indicators` — `economic-indicators`
- [x] done `market_risk_premium` — `market-risk-premium`
- [x] done `treasury_rates` — `treasury-rates`

## `client.esg` — ESG disclosures, ratings, and benchmarks.

> **Bucket 2 (Ultimate-gated), confirmed live:** the pricing-audit prediction held —
> all 3 methods 402 on the free tier. Tests live in `tests/ultimate/test_esg.py` only.

3 methods.

- [x] ultimate-pending `esg_benchmark` — `esg-benchmark` (402 on free tier)
- [x] ultimate-pending `esg_disclosures` — `esg-disclosures` (402 on free tier)
- [x] ultimate-pending `esg_ratings` — `esg-ratings` (402 on free tier)

## `client.funds` — ETF and mutual-fund composition, info, and N-PORT/13F-style disclosures.

9 methods.

> **Correction to the group directory's Bucket assignment:** not flagged as
> Bucket 2 in REWRITE_ARCHITECTURE.md §3.5, but live-testing found all 9
> methods 402 on the free tier. Reclassified below per the workflow doc's
> "if a Bucket 1 method 402s, mark it `ultimate-pending`" rule.

- [x] ultimate-pending `etf_asset_exposure` — `etf/asset-exposure` (402 on free tier)
- [x] ultimate-pending `etf_country_weightings` — `etf/country-weightings` (402 on free tier)
- [x] ultimate-pending `etf_holdings` — `etf/holdings` (402 on free tier)
- [x] ultimate-pending `etf_info` — `etf/info` (402 on free tier)
- [x] ultimate-pending `etf_sector_weightings` — `etf/sector-weightings` (402 on free tier)
- [x] ultimate-pending `funds_disclosure` — `funds/disclosure` (402 on free tier)
- [x] ultimate-pending `funds_disclosure_dates` — `funds/disclosure-dates` (402 on free tier)
- [x] ultimate-pending `funds_disclosure_holders_latest` — `funds/disclosure-holders-latest` (402 on free tier)
- [x] ultimate-pending `funds_disclosure_holders_search` — `funds/disclosure-holders-search` (402 on free tier)

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
- [x] ultimate-pending `balance_sheet_statement_ttm` — `balance-sheet-statement-ttm` (402 on free tier)
- [x] done `cash_flow_statement` — `cash-flow-statement`
- [x] done `cash_flow_statement_as_reported` — `cash-flow-statement-as-reported`
- [x] done `cash_flow_statement_growth` — `cash-flow-statement-growth`
- [x] ultimate-pending `cash_flow_statement_ttm` — `cash-flow-statement-ttm` (402 on free tier)
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
- [x] ultimate-pending `income_statement_ttm` — `income-statement-ttm` (402 on free tier)
- [x] done `key_metrics` — `key-metrics`
- [x] done `key_metrics_ttm` — `key-metrics-ttm`
- [x] ultimate-pending `latest_financial_statements` — `latest-financial-statements` (402 on free tier)
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

- [x] ultimate-pending `institutional_ownership_dates` — `institutional-ownership/dates` (402 on free tier)
- [x] ultimate-pending `institutional_ownership_extract` — `institutional-ownership/extract` (402 on free tier)
- [x] ultimate-pending `institutional_ownership_extract_analytics_holder` — `institutional-ownership/extract-analytics/holder` (402 on free tier)
- [x] ultimate-pending `institutional_ownership_holder_industry_breakdown` — `institutional-ownership/holder-industry-breakdown` (402 on free tier)
- [x] ultimate-pending `institutional_ownership_holder_performance_summary` — `institutional-ownership/holder-performance-summary` (402 on free tier)
- [x] ultimate-pending `institutional_ownership_industry_summary` — `institutional-ownership/industry-summary` (402 on free tier)
- [x] ultimate-pending `institutional_ownership_latest` — `institutional-ownership/latest` (402 on free tier)
- [x] ultimate-pending `institutional_ownership_symbol_positions_summary` — `institutional-ownership/symbol-positions-summary` (402 on free tier)

## `client.indexes` — Stock-market indexes, their quotes/charts, and their constituent lists.

7 methods.

> **Unit-tested and live-tested 2026-08-23.** Only `index_list` is
> free-tier reachable — the other 6 own methods all 402 despite no
> Bucket 2 flag in REWRITE_ARCHITECTURE.md §3.5. 3 cross-listed from
> `client.chart` (`historical_chart`, `historical_price_eod_full`,
> `historical_price_eod_light`) already hold the identity invariant —
> verified via `assert client.indexes.historical_chart is
> client.chart.historical_chart` at write time.

- [x] ultimate-pending `dowjones_constituent` — `dowjones-constituent` (402 on free tier)
- [x] ultimate-pending `historical_dowjones_constituent` — `historical-dowjones-constituent` (402 on free tier)
- [x] ultimate-pending `historical_nasdaq_constituent` — `historical-nasdaq-constituent` (402 on free tier)
- [x] ultimate-pending `historical_sp500_constituent` — `historical-sp500-constituent` (402 on free tier)
- [x] done `index_list` — `index-list`
- [x] ultimate-pending `nasdaq_constituent` — `nasdaq-constituent` (402 on free tier)
- [x] ultimate-pending `sp500_constituent` — `sp500-constituent` (402 on free tier)

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

- [x] ultimate-pending `acquisition_of_beneficial_ownership` — `acquisition-of-beneficial-ownership` (402 on free tier)
- [x] done `insider_trading_latest` — `insider-trading/latest`
- [x] ultimate-pending `insider_trading_reporting_name` — `insider-trading/reporting-name` (402 on free tier)
- [x] ultimate-pending `insider_trading_search` — `insider-trading/search` (402 on free tier)
- [x] ultimate-pending `insider_trading_statistics` — `insider-trading/statistics` (402 on free tier)
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

- [x] ultimate-pending `technical_indicators_adx` — `technical-indicators/adx` (402 on free tier)
- [x] ultimate-pending `technical_indicators_dema` — `technical-indicators/dema` (402 on free tier)
- [x] ultimate-pending `technical_indicators_ema` — `technical-indicators/ema` (402 on free tier)
- [x] ultimate-pending `technical_indicators_rsi` — `technical-indicators/rsi` (402 on free tier)
- [x] ultimate-pending `technical_indicators_sma` — `technical-indicators/sma` (402 on free tier)
- [x] ultimate-pending `technical_indicators_standarddeviation` — `technical-indicators/standarddeviation` (402 on free tier)
- [x] ultimate-pending `technical_indicators_tema` — `technical-indicators/tema` (402 on free tier)
- [x] ultimate-pending `technical_indicators_williams` — `technical-indicators/williams` (402 on free tier)
- [x] ultimate-pending `technical_indicators_wma` — `technical-indicators/wma` (402 on free tier)

## `client.news` — News, press releases, and FMP editorial articles.

10 methods.

> **Unit- and live-tested 2026-08-23.** Only `fmp_articles` is free-tier reachable —
> the other 9 methods (the whole `NewsArticleResult`-shaped family: general/
> press-releases/stock/crypto/forex, each with a "-latest" sibling) all 402'd, despite
> no Bucket 2 flag in REWRITE_ARCHITECTURE.md §3.5 → `ultimate-pending`.

- [x] done `fmp_articles` — `fmp-articles`
- [x] ultimate-pending `news_crypto` — `news/crypto` (402 on free tier)
- [x] ultimate-pending `news_crypto_latest` — `news/crypto-latest` (402 on free tier)
- [x] ultimate-pending `news_forex` — `news/forex` (402 on free tier)
- [x] ultimate-pending `news_forex_latest` — `news/forex-latest` (402 on free tier)
- [x] ultimate-pending `news_general_latest` — `news/general-latest` (402 on free tier)
- [x] ultimate-pending `news_press_releases` — `news/press-releases` (402 on free tier)
- [x] ultimate-pending `news_press_releases_latest` — `news/press-releases-latest` (402 on free tier)
- [x] ultimate-pending `news_stock` — `news/stock` (402 on free tier)
- [x] ultimate-pending `news_stock_latest` — `news/stock-latest` (402 on free tier)

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
- [x] ultimate-pending `batch_aftermarket_quote` — `batch-aftermarket-quote` (402 on free tier)
- [x] ultimate-pending `batch_aftermarket_trade` — `batch-aftermarket-trade` (402 on free tier)
- [x] ultimate-pending `batch_commodity_quotes` — `batch-commodity-quotes` (402 on free tier)
- [x] ultimate-pending `batch_crypto_quotes` — `batch-crypto-quotes` (402 on free tier)
- [x] ultimate-pending `batch_etf_quotes` — `batch-etf-quotes` (402 on free tier)
- [x] ultimate-pending `batch_exchange_quote` — `batch-exchange-quote` (402 on free tier)
- [x] ultimate-pending `batch_forex_quotes` — `batch-forex-quotes` (402 on free tier)
- [x] ultimate-pending `batch_index_quotes` — `batch-index-quotes` (402 on free tier)
- [x] ultimate-pending `batch_mutualfund_quotes` — `batch-mutualfund-quotes` (402 on free tier)
- [x] ultimate-pending `batch_quote` — `batch-quote` (402 on free tier)
- [x] ultimate-pending `batch_quote_short` — `batch-quote-short` (402 on free tier)
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

- [x] ultimate-pending `all_industry_classification` — `all-industry-classification` (402 on free tier)
- [x] ultimate-pending `industry_classification_search` — `industry-classification-search` (402 on free tier)
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

- [x] ultimate-pending `earning_call_transcript` — `earning-call-transcript` (402 on free tier)
- [x] ultimate-pending `earning_call_transcript_dates` — `earning-call-transcript-dates` (402 on free tier)
- [x] ultimate-pending `earning_call_transcript_latest` — `earning-call-transcript-latest` (402 on free tier)
- [x] ultimate-pending `earnings_transcript_list` — `earnings-transcript-list` (402 on free tier)

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
- [x] ultimate-pending `house_trades` — `house-trades` (402 on free tier)
- [x] ultimate-pending `house_trades_by_id` — `house-trades-by-id` (402 on free tier)
- [x] ultimate-pending `house_trades_by_name` — `house-trades-by-name` (402 on free tier)
- [x] done `senate_latest` — `senate-latest`
- [x] ultimate-pending `senate_net_worth` — `senate-net-worth` (402 on free tier)
- [x] ultimate-pending `senate_net_worth_aggregated` — `senate-net-worth-aggregated` (402 on free tier)
- [x] ultimate-pending `senate_positions` — `senate-positions` (402 on free tier)
- [x] ultimate-pending `senate_profile` — `senate-profile` (402 on free tier)
- [x] ultimate-pending `senate_trades` — `senate-trades` (402 on free tier)
- [x] ultimate-pending `senate_trades_by_id` — `senate-trades-by-id` (402 on free tier)
- [x] ultimate-pending `senate_trades_by_name` — `senate-trades-by-name` (402 on free tier)

## `client.bulk` — Whole-universe bulk downloads.

> **Confirmed Bucket 2 (Ultimate-gated), 2026-08-23:** all 18 methods 402'd, matching
> the original pricing audit's prediction — the whole group, not a subset. 17 of 18
> methods return every field as a JSON string, including semantically numeric/boolean
> fields — a real, documented quirk (see `types/bulk.py`'s module docstring), not a
> transcription choice. `profile_bulk` is the lone exception (real JSON types) and
> reuses `ProfileResult` directly rather than duplicating it, since its example
> response is field-for-field identical to `profile`/`profile_cik`'s.

18 methods.

- [x] ultimate-pending `balance_sheet_statement_bulk` — `balance-sheet-statement-bulk` (402 on free tier)
- [x] ultimate-pending `balance_sheet_statement_growth_bulk` — `balance-sheet-statement-growth-bulk` (402 on free tier)
- [x] ultimate-pending `cash_flow_statement_bulk` — `cash-flow-statement-bulk` (402 on free tier)
- [x] ultimate-pending `cash_flow_statement_growth_bulk` — `cash-flow-statement-growth-bulk` (402 on free tier)
- [x] ultimate-pending `dcf_bulk` — `dcf-bulk` (402 on free tier)
- [x] ultimate-pending `earnings_surprises_bulk` — `earnings-surprises-bulk` (402 on free tier)
- [x] ultimate-pending `eod_bulk` — `eod-bulk` (402 on free tier)
- [x] ultimate-pending `etf_holder_bulk` — `etf-holder-bulk` (402 on free tier)
- [x] ultimate-pending `income_statement_bulk` — `income-statement-bulk` (402 on free tier)
- [x] ultimate-pending `income_statement_growth_bulk` — `income-statement-growth-bulk` (402 on free tier)
- [x] ultimate-pending `key_metrics_ttm_bulk` — `key-metrics-ttm-bulk` (402 on free tier)
- [x] ultimate-pending `peers_bulk` — `peers-bulk` (402 on free tier)
- [x] ultimate-pending `price_target_summary_bulk` — `price-target-summary-bulk` (402 on free tier)
- [x] ultimate-pending `profile_bulk` — `profile-bulk` (402 on free tier)
- [x] ultimate-pending `rating_bulk` — `rating-bulk` (402 on free tier)
- [x] ultimate-pending `ratios_ttm_bulk` — `ratios-ttm-bulk` (402 on free tier)
- [x] ultimate-pending `scores_bulk` — `scores-bulk` (402 on free tier)
- [x] ultimate-pending `upgrades_downgrades_consensus_bulk` — `upgrades-downgrades-consensus-bulk` (402 on free tier)

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

- [x] ultimate-pending `tipranks_analyst_summary` — `tipranks-analyst-summary` (402 on free tier)
- [x] ultimate-pending `tipranks_analysts` — `tipranks-analysts` (402 on free tier)
- [x] ultimate-pending `tipranks_firm_summary` — `tipranks-firm-summary` (402 on free tier)
- [x] ultimate-pending `tipranks_pit_analyst` — `tipranks-pit-analyst` (402 on free tier)
- [x] ultimate-pending `tipranks_pit_symbol` — `tipranks-pit-symbol` (402 on free tier)
- [x] ultimate-pending `tipranks_search` — `tipranks-search` (402 on free tier)
- [x] ultimate-pending `tipranks_symbol_summary` — `tipranks-symbol-summary` (402 on free tier)
