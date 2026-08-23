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


class DirectoryGroup:
    """``client.directory`` — 10 primary methods. 1 cross-listed from
    ``client.earnings_transcript`` (``earnings_transcript_list``, §4.3 —
    FMP documents this path under both "Directory" and
    "EarningsTranscript")."""

    def __init__(self, bind: _MethodBinder) -> None:
        self.actively_trading_list = bind("actively_trading_list")
        self.available_countries = bind("available_countries")
        self.available_exchanges = bind("available_exchanges")
        self.available_industries = bind("available_industries")
        self.available_sectors = bind("available_sectors")
        self.cik_list = bind("cik_list")
        self.etf_list = bind("etf_list")
        self.financial_statement_symbol_list = bind("financial_statement_symbol_list")
        self.stock_list = bind("stock_list")
        self.symbol_change = bind("symbol_change")
        # Cross-listed from client.earnings_transcript (§4.3).
        self.earnings_transcript_list = bind("earnings_transcript_list")


class AnalystGroup:
    """``client.analyst`` — 8 primary methods, no cross-listings."""

    def __init__(self, bind: _MethodBinder) -> None:
        self.analyst_estimates = bind("analyst_estimates")
        self.grades = bind("grades")
        self.grades_consensus = bind("grades_consensus")
        self.grades_historical = bind("grades_historical")
        self.price_target_consensus = bind("price_target_consensus")
        self.price_target_summary = bind("price_target_summary")
        self.ratings_historical = bind("ratings_historical")
        self.ratings_snapshot = bind("ratings_snapshot")


class CalendarGroup:
    """``client.calendar`` — 9 primary methods, no cross-listings."""

    def __init__(self, bind: _MethodBinder) -> None:
        self.dividends = bind("dividends")
        self.dividends_calendar = bind("dividends_calendar")
        self.earnings = bind("earnings")
        self.earnings_calendar = bind("earnings_calendar")
        self.ipos_calendar = bind("ipos_calendar")
        self.ipos_disclosure = bind("ipos_disclosure")
        self.ipos_prospectus = bind("ipos_prospectus")
        self.splits = bind("splits")
        self.splits_calendar = bind("splits_calendar")


class ChartGroup:
    """``client.chart`` — 5 primary methods. 3 of them
    (``historical_chart``, ``historical_price_eod_full``,
    ``historical_price_eod_light``) are also cross-listed into
    ``indexes``/``commodity``/``crypto``/``forex`` once those groups exist."""

    def __init__(self, bind: _MethodBinder) -> None:
        self.historical_chart = bind("historical_chart")
        self.historical_price_eod_dividend_adjusted = bind(
            "historical_price_eod_dividend_adjusted"
        )
        self.historical_price_eod_full = bind("historical_price_eod_full")
        self.historical_price_eod_light = bind("historical_price_eod_light")
        self.historical_price_eod_non_split_adjusted = bind(
            "historical_price_eod_non_split_adjusted"
        )


class CompanyGroup:
    """``client.company`` — 17 primary methods, no cross-listings."""

    def __init__(self, bind: _MethodBinder) -> None:
        self.company_notes = bind("company_notes")
        self.delisted_companies = bind("delisted_companies")
        self.employee_count = bind("employee_count")
        self.executive_compensation_benchmark = bind("executive_compensation_benchmark")
        self.governance_executive_compensation = bind(
            "governance_executive_compensation"
        )
        self.historical_employee_count = bind("historical_employee_count")
        self.historical_market_capitalization = bind("historical_market_capitalization")
        self.key_executives = bind("key_executives")
        self.market_capitalization = bind("market_capitalization")
        self.market_capitalization_batch = bind("market_capitalization_batch")
        self.mergers_acquisitions_latest = bind("mergers_acquisitions_latest")
        self.mergers_acquisitions_search = bind("mergers_acquisitions_search")
        self.profile = bind("profile")
        self.profile_cik = bind("profile_cik")
        self.shares_float = bind("shares_float")
        self.shares_float_all = bind("shares_float_all")
        self.stock_peers = bind("stock_peers")


class CommitmentOfTradersGroup:
    """``client.commitment_of_traders`` — 3 primary methods, no cross-listings."""

    def __init__(self, bind: _MethodBinder) -> None:
        self.commitment_of_traders_analysis = bind("commitment_of_traders_analysis")
        self.commitment_of_traders_list = bind("commitment_of_traders_list")
        self.commitment_of_traders_report = bind("commitment_of_traders_report")


class DcfGroup:
    """``client.dcf`` — 4 primary methods, no cross-listings."""

    def __init__(self, bind: _MethodBinder) -> None:
        self.custom_discounted_cash_flow = bind("custom_discounted_cash_flow")
        self.custom_levered_discounted_cash_flow = bind(
            "custom_levered_discounted_cash_flow"
        )
        self.discounted_cash_flow = bind("discounted_cash_flow")
        self.levered_discounted_cash_flow = bind("levered_discounted_cash_flow")


class EconomicsGroup:
    """``client.economics`` — 4 primary methods, no cross-listings."""

    def __init__(self, bind: _MethodBinder) -> None:
        self.economic_calendar = bind("economic_calendar")
        self.economic_indicators = bind("economic_indicators")
        self.market_risk_premium = bind("market_risk_premium")
        self.treasury_rates = bind("treasury_rates")


class EsgGroup:
    """``client.esg`` — 3 primary methods, no cross-listings."""

    def __init__(self, bind: _MethodBinder) -> None:
        self.esg_benchmark = bind("esg_benchmark")
        self.esg_disclosures = bind("esg_disclosures")
        self.esg_ratings = bind("esg_ratings")


class FundsGroup:
    """``client.funds`` — 9 primary methods, no cross-listings."""

    def __init__(self, bind: _MethodBinder) -> None:
        self.etf_asset_exposure = bind("etf_asset_exposure")
        self.etf_country_weightings = bind("etf_country_weightings")
        self.etf_holdings = bind("etf_holdings")
        self.etf_info = bind("etf_info")
        self.etf_sector_weightings = bind("etf_sector_weightings")
        self.funds_disclosure = bind("funds_disclosure")
        self.funds_disclosure_dates = bind("funds_disclosure_dates")
        self.funds_disclosure_holders_latest = bind("funds_disclosure_holders_latest")
        self.funds_disclosure_holders_search = bind("funds_disclosure_holders_search")


class StatementsGroup:
    """``client.statements`` — 27 primary methods, no cross-listings."""

    def __init__(self, bind: _MethodBinder) -> None:
        self.balance_sheet_statement = bind("balance_sheet_statement")
        self.balance_sheet_statement_as_reported = bind(
            "balance_sheet_statement_as_reported"
        )
        self.balance_sheet_statement_growth = bind("balance_sheet_statement_growth")
        self.balance_sheet_statement_ttm = bind("balance_sheet_statement_ttm")
        self.cash_flow_statement = bind("cash_flow_statement")
        self.cash_flow_statement_as_reported = bind("cash_flow_statement_as_reported")
        self.cash_flow_statement_growth = bind("cash_flow_statement_growth")
        self.cash_flow_statement_ttm = bind("cash_flow_statement_ttm")
        self.enterprise_values = bind("enterprise_values")
        self.financial_growth = bind("financial_growth")
        self.financial_reports_dates = bind("financial_reports_dates")
        self.financial_reports_json = bind("financial_reports_json")
        self.financial_reports_xlsx = bind("financial_reports_xlsx")
        self.financial_scores = bind("financial_scores")
        self.financial_statement_full_as_reported = bind(
            "financial_statement_full_as_reported"
        )
        self.income_statement = bind("income_statement")
        self.income_statement_as_reported = bind("income_statement_as_reported")
        self.income_statement_growth = bind("income_statement_growth")
        self.income_statement_ttm = bind("income_statement_ttm")
        self.key_metrics = bind("key_metrics")
        self.key_metrics_ttm = bind("key_metrics_ttm")
        self.latest_financial_statements = bind("latest_financial_statements")
        self.owner_earnings = bind("owner_earnings")
        self.ratios = bind("ratios")
        self.ratios_ttm = bind("ratios_ttm")
        self.revenue_geographic_segmentation = bind("revenue_geographic_segmentation")
        self.revenue_product_segmentation = bind("revenue_product_segmentation")


class InstitutionalOwnershipGroup:
    """``client.institutional_ownership`` — 8 primary methods, no cross-listings."""

    def __init__(self, bind: _MethodBinder) -> None:
        self.institutional_ownership_dates = bind("institutional_ownership_dates")
        self.institutional_ownership_extract = bind("institutional_ownership_extract")
        self.institutional_ownership_extract_analytics_holder = bind(
            "institutional_ownership_extract_analytics_holder"
        )
        self.institutional_ownership_holder_industry_breakdown = bind(
            "institutional_ownership_holder_industry_breakdown"
        )
        self.institutional_ownership_holder_performance_summary = bind(
            "institutional_ownership_holder_performance_summary"
        )
        self.institutional_ownership_industry_summary = bind(
            "institutional_ownership_industry_summary"
        )
        self.institutional_ownership_latest = bind("institutional_ownership_latest")
        self.institutional_ownership_symbol_positions_summary = bind(
            "institutional_ownership_symbol_positions_summary"
        )


class IndexesGroup:
    """``client.indexes`` — 7 primary methods. 3 cross-listed from
    ``client.chart`` (``historical_chart``, ``historical_price_eod_full``,
    ``historical_price_eod_light``) and 3 from ``client.quote`` (``quote``,
    ``quote_short``, ``batch_index_quotes``) — all 6 per §4.3."""

    def __init__(self, bind: _MethodBinder) -> None:
        self.dowjones_constituent = bind("dowjones_constituent")
        self.historical_dowjones_constituent = bind("historical_dowjones_constituent")
        self.historical_nasdaq_constituent = bind("historical_nasdaq_constituent")
        self.historical_sp500_constituent = bind("historical_sp500_constituent")
        self.index_list = bind("index_list")
        self.nasdaq_constituent = bind("nasdaq_constituent")
        self.sp500_constituent = bind("sp500_constituent")
        # Cross-listed from client.chart (§4.3).
        self.historical_chart = bind("historical_chart")
        self.historical_price_eod_full = bind("historical_price_eod_full")
        self.historical_price_eod_light = bind("historical_price_eod_light")
        # Cross-listed from client.quote (§4.3).
        self.quote = bind("quote")
        self.quote_short = bind("quote_short")
        self.batch_index_quotes = bind("batch_index_quotes")


class CommodityGroup:
    """``client.commodity`` — 1 primary method. 3 cross-listed from
    ``client.chart`` and 3 from ``client.quote`` (``quote``,
    ``quote_short``, ``batch_commodity_quotes``) — all 6 per §4.3."""

    def __init__(self, bind: _MethodBinder) -> None:
        self.commodities_list = bind("commodities_list")
        # Cross-listed from client.chart (§4.3).
        self.historical_chart = bind("historical_chart")
        self.historical_price_eod_full = bind("historical_price_eod_full")
        self.historical_price_eod_light = bind("historical_price_eod_light")
        # Cross-listed from client.quote (§4.3).
        self.quote = bind("quote")
        self.quote_short = bind("quote_short")
        self.batch_commodity_quotes = bind("batch_commodity_quotes")


class CryptoGroup:
    """``client.crypto`` — 1 primary method. 3 cross-listed from
    ``client.chart`` and 3 from ``client.quote`` (``quote``,
    ``quote_short``, ``batch_crypto_quotes``) — all 6 per §4.3."""

    def __init__(self, bind: _MethodBinder) -> None:
        self.cryptocurrency_list = bind("cryptocurrency_list")
        # Cross-listed from client.chart (§4.3).
        self.historical_chart = bind("historical_chart")
        self.historical_price_eod_full = bind("historical_price_eod_full")
        self.historical_price_eod_light = bind("historical_price_eod_light")
        # Cross-listed from client.quote (§4.3).
        self.quote = bind("quote")
        self.quote_short = bind("quote_short")
        self.batch_crypto_quotes = bind("batch_crypto_quotes")


class FundraisersGroup:
    """``client.fundraisers`` — 6 primary methods, no cross-listings."""

    def __init__(self, bind: _MethodBinder) -> None:
        self.crowdfunding_offerings = bind("crowdfunding_offerings")
        self.crowdfunding_offerings_latest = bind("crowdfunding_offerings_latest")
        self.crowdfunding_offerings_search = bind("crowdfunding_offerings_search")
        self.fundraising = bind("fundraising")
        self.fundraising_latest = bind("fundraising_latest")
        self.fundraising_search = bind("fundraising_search")


class ForexGroup:
    """``client.forex`` — 1 primary method. 3 cross-listed from
    ``client.chart`` and 3 from ``client.quote`` (``quote``,
    ``quote_short``, ``batch_forex_quotes``) — all 6 per §4.3."""

    def __init__(self, bind: _MethodBinder) -> None:
        self.forex_list = bind("forex_list")
        # Cross-listed from client.chart (§4.3).
        self.historical_chart = bind("historical_chart")
        self.historical_price_eod_full = bind("historical_price_eod_full")
        self.historical_price_eod_light = bind("historical_price_eod_light")
        # Cross-listed from client.quote (§4.3).
        self.quote = bind("quote")
        self.quote_short = bind("quote_short")
        self.batch_forex_quotes = bind("batch_forex_quotes")


class InsiderTradesGroup:
    """``client.insider_trades`` — 6 primary methods, no cross-listings."""

    def __init__(self, bind: _MethodBinder) -> None:
        self.acquisition_of_beneficial_ownership = bind(
            "acquisition_of_beneficial_ownership"
        )
        self.insider_trading_latest = bind("insider_trading_latest")
        self.insider_trading_reporting_name = bind("insider_trading_reporting_name")
        self.insider_trading_search = bind("insider_trading_search")
        self.insider_trading_statistics = bind("insider_trading_statistics")
        self.insider_trading_transaction_type = bind("insider_trading_transaction_type")


class MarketPerformanceGroup:
    """``client.market_performance`` — 11 primary methods, no
    cross-listings."""

    def __init__(self, bind: _MethodBinder) -> None:
        self.biggest_gainers = bind("biggest_gainers")
        self.biggest_losers = bind("biggest_losers")
        self.historical_industry_pe = bind("historical_industry_pe")
        self.historical_industry_performance = bind("historical_industry_performance")
        self.historical_sector_pe = bind("historical_sector_pe")
        self.historical_sector_performance = bind("historical_sector_performance")
        self.industry_pe_snapshot = bind("industry_pe_snapshot")
        self.industry_performance_snapshot = bind("industry_performance_snapshot")
        self.most_actives = bind("most_actives")
        self.sector_pe_snapshot = bind("sector_pe_snapshot")
        self.sector_performance_snapshot = bind("sector_performance_snapshot")


class MarketHoursGroup:
    """``client.market_hours`` — 3 primary methods, no cross-listings."""

    def __init__(self, bind: _MethodBinder) -> None:
        self.all_exchange_market_hours = bind("all_exchange_market_hours")
        self.exchange_market_hours = bind("exchange_market_hours")
        self.holidays_by_exchange = bind("holidays_by_exchange")


class TechnicalIndicatorsGroup:
    """``client.technical_indicators`` — 9 primary methods, no
    cross-listings."""

    def __init__(self, bind: _MethodBinder) -> None:
        self.technical_indicators_adx = bind("technical_indicators_adx")
        self.technical_indicators_dema = bind("technical_indicators_dema")
        self.technical_indicators_ema = bind("technical_indicators_ema")
        self.technical_indicators_rsi = bind("technical_indicators_rsi")
        self.technical_indicators_sma = bind("technical_indicators_sma")
        self.technical_indicators_standarddeviation = bind(
            "technical_indicators_standarddeviation"
        )
        self.technical_indicators_tema = bind("technical_indicators_tema")
        self.technical_indicators_williams = bind("technical_indicators_williams")
        self.technical_indicators_wma = bind("technical_indicators_wma")


class NewsGroup:
    """``client.news`` — 10 primary methods, no cross-listings."""

    def __init__(self, bind: _MethodBinder) -> None:
        self.fmp_articles = bind("fmp_articles")
        self.news_crypto = bind("news_crypto")
        self.news_crypto_latest = bind("news_crypto_latest")
        self.news_forex = bind("news_forex")
        self.news_forex_latest = bind("news_forex_latest")
        self.news_general_latest = bind("news_general_latest")
        self.news_press_releases = bind("news_press_releases")
        self.news_press_releases_latest = bind("news_press_releases_latest")
        self.news_stock = bind("news_stock")
        self.news_stock_latest = bind("news_stock_latest")


class QuoteGroup:
    """``client.quote`` — 16 primary methods. 6 are cross-listed out into
    ``indexes``/``commodity``/``crypto``/``forex`` (§4.3, see those
    groups' own docstrings)."""

    def __init__(self, bind: _MethodBinder) -> None:
        self.aftermarket_quote = bind("aftermarket_quote")
        self.aftermarket_trade = bind("aftermarket_trade")
        self.batch_aftermarket_quote = bind("batch_aftermarket_quote")
        self.batch_aftermarket_trade = bind("batch_aftermarket_trade")
        self.batch_commodity_quotes = bind("batch_commodity_quotes")
        self.batch_crypto_quotes = bind("batch_crypto_quotes")
        self.batch_etf_quotes = bind("batch_etf_quotes")
        self.batch_exchange_quote = bind("batch_exchange_quote")
        self.batch_forex_quotes = bind("batch_forex_quotes")
        self.batch_index_quotes = bind("batch_index_quotes")
        self.batch_mutualfund_quotes = bind("batch_mutualfund_quotes")
        self.batch_quote = bind("batch_quote")
        self.batch_quote_short = bind("batch_quote_short")
        self.quote = bind("quote")
        self.quote_short = bind("quote_short")
        self.stock_price_change = bind("stock_price_change")


class SecFilingsGroup:
    """``client.sec_filings`` — 12 primary methods, no cross-listings."""

    def __init__(self, bind: _MethodBinder) -> None:
        self.all_industry_classification = bind("all_industry_classification")
        self.industry_classification_search = bind("industry_classification_search")
        self.sec_filings_8k = bind("sec_filings_8k")
        self.sec_filings_company_search_cik = bind("sec_filings_company_search_cik")
        self.sec_filings_company_search_name = bind("sec_filings_company_search_name")
        self.sec_filings_company_search_symbol = bind(
            "sec_filings_company_search_symbol"
        )
        self.sec_filings_financials = bind("sec_filings_financials")
        self.sec_filings_search_cik = bind("sec_filings_search_cik")
        self.sec_filings_search_form_type = bind("sec_filings_search_form_type")
        self.sec_filings_search_symbol = bind("sec_filings_search_symbol")
        self.sec_profile = bind("sec_profile")
        self.standard_industrial_classification_list = bind(
            "standard_industrial_classification_list"
        )


class EarningsTranscriptGroup:
    """``client.earnings_transcript`` — 4 primary methods. 1
    (``earnings_transcript_list``) is also cross-listed into
    ``client.directory`` (§4.3, see that group's docstring)."""

    def __init__(self, bind: _MethodBinder) -> None:
        self.earning_call_transcript = bind("earning_call_transcript")
        self.earning_call_transcript_dates = bind("earning_call_transcript_dates")
        self.earning_call_transcript_latest = bind("earning_call_transcript_latest")
        self.earnings_transcript_list = bind("earnings_transcript_list")


class CongressGroup:
    """``client.congress`` — 12 primary methods, no cross-listings."""

    def __init__(self, bind: _MethodBinder) -> None:
        self.house_latest = bind("house_latest")
        self.house_trades = bind("house_trades")
        self.house_trades_by_id = bind("house_trades_by_id")
        self.house_trades_by_name = bind("house_trades_by_name")
        self.senate_latest = bind("senate_latest")
        self.senate_net_worth = bind("senate_net_worth")
        self.senate_net_worth_aggregated = bind("senate_net_worth_aggregated")
        self.senate_positions = bind("senate_positions")
        self.senate_profile = bind("senate_profile")
        self.senate_trades = bind("senate_trades")
        self.senate_trades_by_id = bind("senate_trades_by_id")
        self.senate_trades_by_name = bind("senate_trades_by_name")


class BulkGroup:
    """``client.bulk`` — 18 primary methods, no cross-listings."""

    def __init__(self, bind: _MethodBinder) -> None:
        self.balance_sheet_statement_bulk = bind("balance_sheet_statement_bulk")
        self.balance_sheet_statement_growth_bulk = bind(
            "balance_sheet_statement_growth_bulk"
        )
        self.cash_flow_statement_bulk = bind("cash_flow_statement_bulk")
        self.cash_flow_statement_growth_bulk = bind("cash_flow_statement_growth_bulk")
        self.dcf_bulk = bind("dcf_bulk")
        self.earnings_surprises_bulk = bind("earnings_surprises_bulk")
        self.eod_bulk = bind("eod_bulk")
        self.etf_holder_bulk = bind("etf_holder_bulk")
        self.income_statement_bulk = bind("income_statement_bulk")
        self.income_statement_growth_bulk = bind("income_statement_growth_bulk")
        self.key_metrics_ttm_bulk = bind("key_metrics_ttm_bulk")
        self.peers_bulk = bind("peers_bulk")
        self.price_target_summary_bulk = bind("price_target_summary_bulk")
        self.profile_bulk = bind("profile_bulk")
        self.rating_bulk = bind("rating_bulk")
        self.ratios_ttm_bulk = bind("ratios_ttm_bulk")
        self.scores_bulk = bind("scores_bulk")
        self.upgrades_downgrades_consensus_bulk = bind(
            "upgrades_downgrades_consensus_bulk"
        )


class TipranksGroup:
    """``client.tipranks`` — 7 primary methods, no cross-listings."""

    def __init__(self, bind: _MethodBinder) -> None:
        self.tipranks_analyst_summary = bind("tipranks_analyst_summary")
        self.tipranks_analysts = bind("tipranks_analysts")
        self.tipranks_firm_summary = bind("tipranks_firm_summary")
        self.tipranks_pit_analyst = bind("tipranks_pit_analyst")
        self.tipranks_pit_symbol = bind("tipranks_pit_symbol")
        self.tipranks_search = bind("tipranks_search")
        self.tipranks_symbol_summary = bind("tipranks_symbol_summary")


def attach_groups(client: "Client") -> None:
    """Attach every alias-group namespace to ``client``.

    Called once from ``Client.__init__``. This is the single place group
    wiring happens — extend it as each new group's endpoint module and
    ``*Group`` class are added. All groups share one ``_MethodBinder`` so
    cross-listed methods stay identity-equal across groups.
    """
    bind = _MethodBinder(client)
    client.search = SearchGroup(bind)
    client.directory = DirectoryGroup(bind)
    client.analyst = AnalystGroup(bind)
    client.calendar = CalendarGroup(bind)
    client.chart = ChartGroup(bind)
    client.company = CompanyGroup(bind)
    client.commitment_of_traders = CommitmentOfTradersGroup(bind)
    client.dcf = DcfGroup(bind)
    client.economics = EconomicsGroup(bind)
    client.esg = EsgGroup(bind)
    client.funds = FundsGroup(bind)
    client.statements = StatementsGroup(bind)
    client.institutional_ownership = InstitutionalOwnershipGroup(bind)
    client.indexes = IndexesGroup(bind)
    client.commodity = CommodityGroup(bind)
    client.crypto = CryptoGroup(bind)
    client.fundraisers = FundraisersGroup(bind)
    client.forex = ForexGroup(bind)
    client.insider_trades = InsiderTradesGroup(bind)
    client.market_performance = MarketPerformanceGroup(bind)
    client.market_hours = MarketHoursGroup(bind)
    client.technical_indicators = TechnicalIndicatorsGroup(bind)
    client.news = NewsGroup(bind)
    client.quote = QuoteGroup(bind)
    client.sec_filings = SecFilingsGroup(bind)
    client.earnings_transcript = EarningsTranscriptGroup(bind)
    client.congress = CongressGroup(bind)
    client.bulk = BulkGroup(bind)
    client.tipranks = TipranksGroup(bind)
