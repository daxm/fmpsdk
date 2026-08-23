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

**Progress: 42 / 238 methods done** (28 more implemented + unit-tested, pending
Ultimate verification).

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

- [ ] `etf_asset_exposure` — `etf/asset-exposure`
- [ ] `etf_country_weightings` — `etf/country-weightings`
- [ ] `etf_holdings` — `etf/holdings`
- [ ] `etf_info` — `etf/info`
- [ ] `etf_sector_weightings` — `etf/sector-weightings`
- [ ] `funds_disclosure` — `funds/disclosure`
- [ ] `funds_disclosure_dates` — `funds/disclosure-dates`
- [ ] `funds_disclosure_holders_latest` — `funds/disclosure-holders-latest`
- [ ] `funds_disclosure_holders_search` — `funds/disclosure-holders-search`

## `client.statements` — Financial statements and everything computed directly from them.

27 methods.

- [ ] `balance_sheet_statement` — `balance-sheet-statement`
- [ ] `balance_sheet_statement_as_reported` — `balance-sheet-statement-as-reported`
- [ ] `balance_sheet_statement_growth` — `balance-sheet-statement-growth`
- [ ] `balance_sheet_statement_ttm` — `balance-sheet-statement-ttm`
- [ ] `cash_flow_statement` — `cash-flow-statement`
- [ ] `cash_flow_statement_as_reported` — `cash-flow-statement-as-reported`
- [ ] `cash_flow_statement_growth` — `cash-flow-statement-growth`
- [ ] `cash_flow_statement_ttm` — `cash-flow-statement-ttm`
- [ ] `enterprise_values` — `enterprise-values`
- [ ] `financial_growth` — `financial-growth`
- [ ] `financial_reports_dates` — `financial-reports-dates`
- [ ] `financial_reports_json` — `financial-reports-json`
- [ ] `financial_reports_xlsx` — `financial-reports-xlsx`
- [ ] `financial_scores` — `financial-scores`
- [ ] `financial_statement_full_as_reported` — `financial-statement-full-as-reported`
- [ ] `income_statement` — `income-statement`
- [ ] `income_statement_as_reported` — `income-statement-as-reported`
- [ ] `income_statement_growth` — `income-statement-growth`
- [ ] `income_statement_ttm` — `income-statement-ttm`
- [ ] `key_metrics` — `key-metrics`
- [ ] `key_metrics_ttm` — `key-metrics-ttm`
- [ ] `latest_financial_statements` — `latest-financial-statements`
- [ ] `owner_earnings` — `owner-earnings`
- [ ] `ratios` — `ratios`
- [ ] `ratios_ttm` — `ratios-ttm`
- [ ] `revenue_geographic_segmentation` — `revenue-geographic-segmentation`
- [ ] `revenue_product_segmentation` — `revenue-product-segmentation`

## `client.institutional_ownership` — Form 13F institutional holdings, holders, and derived analytics.

> **Likely Bucket 2 (Ultimate-gated):** Confirmed Ultimate-only in the pricing audit (Form 13F).

8 methods.

- [ ] `institutional_ownership_dates` — `institutional-ownership/dates`
- [ ] `institutional_ownership_extract` — `institutional-ownership/extract`
- [ ] `institutional_ownership_extract_analytics_holder` — `institutional-ownership/extract-analytics/holder`
- [ ] `institutional_ownership_holder_industry_breakdown` — `institutional-ownership/holder-industry-breakdown`
- [ ] `institutional_ownership_holder_performance_summary` — `institutional-ownership/holder-performance-summary`
- [ ] `institutional_ownership_industry_summary` — `institutional-ownership/industry-summary`
- [ ] `institutional_ownership_latest` — `institutional-ownership/latest`
- [ ] `institutional_ownership_symbol_positions_summary` — `institutional-ownership/symbol-positions-summary`

## `client.indexes` — Stock-market indexes, their quotes/charts, and their constituent lists.

7 methods.

- [ ] `dowjones_constituent` — `dowjones-constituent`
- [ ] `historical_dowjones_constituent` — `historical-dowjones-constituent`
- [ ] `historical_nasdaq_constituent` — `historical-nasdaq-constituent`
- [ ] `historical_sp500_constituent` — `historical-sp500-constituent`
- [ ] `index_list` — `index-list`
- [ ] `nasdaq_constituent` — `nasdaq-constituent`
- [ ] `sp500_constituent` — `sp500-constituent`

## `client.commodity` — Commodity instruments: list, quotes, charts.

1 methods.

- [ ] `commodities_list` — `commodities-list`

## `client.crypto` — Cryptocurrency instruments: list, quotes, charts.

1 methods.

- [ ] `cryptocurrency_list` — `cryptocurrency-list`

## `client.fundraisers` — Reg CF crowdfunding and Reg D/A equity offerings.

6 methods.

- [ ] `crowdfunding_offerings` — `crowdfunding-offerings`
- [ ] `crowdfunding_offerings_latest` — `crowdfunding-offerings-latest`
- [ ] `crowdfunding_offerings_search` — `crowdfunding-offerings-search`
- [ ] `fundraising` — `fundraising`
- [ ] `fundraising_latest` — `fundraising-latest`
- [ ] `fundraising_search` — `fundraising-search`

## `client.forex` — FX pairs: list, quotes, charts.

1 methods.

- [ ] `forex_list` — `forex-list`

## `client.insider_trades` — Form 4 insider transactions, statistics, and beneficial-ownership acquisitions.

6 methods.

- [ ] `acquisition_of_beneficial_ownership` — `acquisition-of-beneficial-ownership`
- [ ] `insider_trading_latest` — `insider-trading/latest`
- [ ] `insider_trading_reporting_name` — `insider-trading/reporting-name`
- [ ] `insider_trading_search` — `insider-trading/search`
- [ ] `insider_trading_statistics` — `insider-trading/statistics`
- [ ] `insider_trading_transaction_type` — `insider-trading-transaction-type`

## `client.market_performance` — Sector/industry performance and P/E, snapshot and historical, plus market leaders.

11 methods.

- [ ] `biggest_gainers` — `biggest-gainers`
- [ ] `biggest_losers` — `biggest-losers`
- [ ] `historical_industry_pe` — `historical-industry-pe`
- [ ] `historical_industry_performance` — `historical-industry-performance`
- [ ] `historical_sector_pe` — `historical-sector-pe`
- [ ] `historical_sector_performance` — `historical-sector-performance`
- [ ] `industry_pe_snapshot` — `industry-pe-snapshot`
- [ ] `industry_performance_snapshot` — `industry-performance-snapshot`
- [ ] `most_actives` — `most-actives`
- [ ] `sector_pe_snapshot` — `sector-pe-snapshot`
- [ ] `sector_performance_snapshot` — `sector-performance-snapshot`

## `client.market_hours` — Exchange trading sessions and holiday calendars.

3 methods.

- [ ] `all_exchange_market_hours` — `all-exchange-market-hours`
- [ ] `exchange_market_hours` — `exchange-market-hours`
- [ ] `holidays_by_exchange` — `holidays-by-exchange`

## `client.technical_indicators` — Computed technical indicator series.

9 methods.

- [ ] `technical_indicators_adx` — `technical-indicators/adx`
- [ ] `technical_indicators_dema` — `technical-indicators/dema`
- [ ] `technical_indicators_ema` — `technical-indicators/ema`
- [ ] `technical_indicators_rsi` — `technical-indicators/rsi`
- [ ] `technical_indicators_sma` — `technical-indicators/sma`
- [ ] `technical_indicators_standarddeviation` — `technical-indicators/standarddeviation`
- [ ] `technical_indicators_tema` — `technical-indicators/tema`
- [ ] `technical_indicators_williams` — `technical-indicators/williams`
- [ ] `technical_indicators_wma` — `technical-indicators/wma`

## `client.news` — News, press releases, and FMP editorial articles.

10 methods.

- [ ] `fmp_articles` — `fmp-articles`
- [ ] `news_crypto` — `news/crypto`
- [ ] `news_crypto_latest` — `news/crypto-latest`
- [ ] `news_forex` — `news/forex`
- [ ] `news_forex_latest` — `news/forex-latest`
- [ ] `news_general_latest` — `news/general-latest`
- [ ] `news_press_releases` — `news/press-releases`
- [ ] `news_press_releases_latest` — `news/press-releases-latest`
- [ ] `news_stock` — `news/stock`
- [ ] `news_stock_latest` — `news/stock-latest`

## `client.quote` — Real-time and aftermarket quotes, single and batch.

16 methods.

- [ ] `aftermarket_quote` — `aftermarket-quote`
- [ ] `aftermarket_trade` — `aftermarket-trade`
- [ ] `batch_aftermarket_quote` — `batch-aftermarket-quote`
- [ ] `batch_aftermarket_trade` — `batch-aftermarket-trade`
- [ ] `batch_commodity_quotes` — `batch-commodity-quotes`
- [ ] `batch_crypto_quotes` — `batch-crypto-quotes`
- [ ] `batch_etf_quotes` — `batch-etf-quotes`
- [ ] `batch_exchange_quote` — `batch-exchange-quote`
- [ ] `batch_forex_quotes` — `batch-forex-quotes`
- [ ] `batch_index_quotes` — `batch-index-quotes`
- [ ] `batch_mutualfund_quotes` — `batch-mutualfund-quotes`
- [ ] `batch_quote` — `batch-quote`
- [ ] `batch_quote_short` — `batch-quote-short`
- [ ] `quote` — `quote`
- [ ] `quote_short` — `quote-short`
- [ ] `stock_price_change` — `stock-price-change`

## `client.sec_filings` — SEC filing search, SEC company identity, and SIC industry classification.

12 methods.

- [ ] `all_industry_classification` — `all-industry-classification`
- [ ] `industry_classification_search` — `industry-classification-search`
- [ ] `sec_filings_8k` — `sec-filings-8k`
- [ ] `sec_filings_company_search_cik` — `sec-filings-company-search/cik`
- [ ] `sec_filings_company_search_name` — `sec-filings-company-search/name`
- [ ] `sec_filings_company_search_symbol` — `sec-filings-company-search/symbol`
- [ ] `sec_filings_financials` — `sec-filings-financials`
- [ ] `sec_filings_search_cik` — `sec-filings-search/cik`
- [ ] `sec_filings_search_form_type` — `sec-filings-search/form-type`
- [ ] `sec_filings_search_symbol` — `sec-filings-search/symbol`
- [ ] `sec_profile` — `sec-profile`
- [ ] `standard_industrial_classification_list` — `standard-industrial-classification-list`

## `client.earnings_transcript` — Earnings-call transcripts and their availability metadata.

> **Likely Bucket 2 (Ultimate-gated):** Confirmed Ultimate-only in the pricing audit.

4 methods.

- [ ] `earning_call_transcript` — `earning-call-transcript`
- [ ] `earning_call_transcript_dates` — `earning-call-transcript-dates`
- [ ] `earning_call_transcript_latest` — `earning-call-transcript-latest`
- [ ] `earnings_transcript_list` — `earnings-transcript-list`

## `client.congress` — U.S. Senate and House financial disclosures, trades, and member profiles.

12 methods.

- [ ] `house_latest` — `house-latest`
- [ ] `house_trades` — `house-trades`
- [ ] `house_trades_by_id` — `house-trades-by-id`
- [ ] `house_trades_by_name` — `house-trades-by-name`
- [ ] `senate_latest` — `senate-latest`
- [ ] `senate_net_worth` — `senate-net-worth`
- [ ] `senate_net_worth_aggregated` — `senate-net-worth-aggregated`
- [ ] `senate_positions` — `senate-positions`
- [ ] `senate_profile` — `senate-profile`
- [ ] `senate_trades` — `senate-trades`
- [ ] `senate_trades_by_id` — `senate-trades-by-id`
- [ ] `senate_trades_by_name` — `senate-trades-by-name`

## `client.bulk` — Whole-universe bulk downloads.

> **Likely Bucket 2 (Ultimate-gated):** Confirmed Ultimate-only in the pricing audit.

18 methods.

- [ ] `balance_sheet_statement_bulk` — `balance-sheet-statement-bulk`
- [ ] `balance_sheet_statement_growth_bulk` — `balance-sheet-statement-growth-bulk`
- [ ] `cash_flow_statement_bulk` — `cash-flow-statement-bulk`
- [ ] `cash_flow_statement_growth_bulk` — `cash-flow-statement-growth-bulk`
- [ ] `dcf_bulk` — `dcf-bulk`
- [ ] `earnings_surprises_bulk` — `earnings-surprises-bulk`
- [ ] `eod_bulk` — `eod-bulk`
- [ ] `etf_holder_bulk` — `etf-holder-bulk`
- [ ] `income_statement_bulk` — `income-statement-bulk`
- [ ] `income_statement_growth_bulk` — `income-statement-growth-bulk`
- [ ] `key_metrics_ttm_bulk` — `key-metrics-ttm-bulk`
- [ ] `peers_bulk` — `peers-bulk`
- [ ] `price_target_summary_bulk` — `price-target-summary-bulk`
- [ ] `profile_bulk` — `profile-bulk`
- [ ] `rating_bulk` — `rating-bulk`
- [ ] `ratios_ttm_bulk` — `ratios-ttm-bulk`
- [ ] `scores_bulk` — `scores-bulk`
- [ ] `upgrades_downgrades_consensus_bulk` — `upgrades-downgrades-consensus-bulk`

## `client.tipranks` — TipRanks partner analyst data.

> **Likely Bucket 2 (Ultimate-gated):** Not in the original pricing audit by name (found later via docs), but licensed partner data — treat as Ultimate-only until proven otherwise.

7 methods.

- [ ] `tipranks_analyst_summary` — `tipranks-analyst-summary`
- [ ] `tipranks_analysts` — `tipranks-analysts`
- [ ] `tipranks_firm_summary` — `tipranks-firm-summary`
- [ ] `tipranks_pit_analyst` — `tipranks-pit-analyst`
- [ ] `tipranks_pit_symbol` — `tipranks-pit-symbol`
- [ ] `tipranks_search` — `tipranks-search`
- [ ] `tipranks_symbol_summary` — `tipranks-symbol-summary`
