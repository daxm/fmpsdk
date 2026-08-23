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
    """``client.directory`` — 10 primary methods, no cross-listings."""

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
        self.governance_executive_compensation = bind("governance_executive_compensation")
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
        self.custom_levered_discounted_cash_flow = bind("custom_levered_discounted_cash_flow")
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
