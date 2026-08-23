"""client.dcf — Discounted-cash-flow valuations, standard and custom-input
(REWRITE_ARCHITECTURE.md §6, ``client.dcf``). 4 canonical methods, no
cross-listings. The two custom-input methods share an identical 18-param
assumption set (all optional overrides on top of FMP's own model
defaults) — factored into one private builder so it's defined once.
"""

from __future__ import annotations

from typing import cast

from ..types import (
    CustomDiscountedCashFlowResult,
    CustomLeveredDiscountedCashFlowResult,
    DiscountedCashFlowResult,
    LeveredDiscountedCashFlowResult,
)


def _custom_dcf_params(
    symbol: str,
    revenue_growth_pct: float | None,
    ebitda_pct: float | None,
    depreciation_and_amortization_pct: float | None,
    cash_and_short_term_investments_pct: float | None,
    receivables_pct: float | None,
    inventories_pct: float | None,
    payable_pct: float | None,
    ebit_pct: float | None,
    capital_expenditure_pct: float | None,
    operating_cash_flow_pct: float | None,
    selling_general_and_administrative_expenses_pct: float | None,
    tax_rate: float | None,
    long_term_growth_rate: float | None,
    cost_of_debt: float | None,
    cost_of_equity: float | None,
    market_risk_premium: float | None,
    beta: float | None,
    risk_free_rate: float | None,
) -> dict:
    """Shared query-param assembly for both custom-DCF methods — same 18
    optional assumption overrides, same ``symbol*``, on two different
    response shapes (unlevered vs. levered)."""
    return {
        "symbol": symbol,
        "revenueGrowthPct": revenue_growth_pct,
        "ebitdaPct": ebitda_pct,
        "depreciationAndAmortizationPct": depreciation_and_amortization_pct,
        "cashAndShortTermInvestmentsPct": cash_and_short_term_investments_pct,
        "receivablesPct": receivables_pct,
        "inventoriesPct": inventories_pct,
        "payablePct": payable_pct,
        "ebitPct": ebit_pct,
        "capitalExpenditurePct": capital_expenditure_pct,
        "operatingCashFlowPct": operating_cash_flow_pct,
        "sellingGeneralAndAdministrativeExpensesPct": (
            selling_general_and_administrative_expenses_pct
        ),
        "taxRate": tax_rate,
        "longTermGrowthRate": long_term_growth_rate,
        "costOfDebt": cost_of_debt,
        "costOfEquity": cost_of_equity,
        "marketRiskPremium": market_risk_premium,
        "beta": beta,
        "riskFreeRate": risk_free_rate,
    }


class DcfEndpoints:
    """Mixed into :class:`fmpsdk.client.Client`. Each method issues one GET
    against its ``stable/`` path via ``self._get`` (defined on ``Client``).
    """

    def discounted_cash_flow(self, symbol: str) -> list[DiscountedCashFlowResult]:
        """``GET discounted-cash-flow`` — unlevered DCF valuation using
        FMP's own model assumptions.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        """
        return cast(
            "list[DiscountedCashFlowResult]",
            self._get("discounted-cash-flow", {"symbol": symbol}),
        )

    def levered_discounted_cash_flow(self, symbol: str) -> list[LeveredDiscountedCashFlowResult]:
        """``GET levered-discounted-cash-flow`` — DCF valuation net of
        debt, using FMP's own model assumptions.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        """
        return cast(
            "list[LeveredDiscountedCashFlowResult]",
            self._get("levered-discounted-cash-flow", {"symbol": symbol}),
        )

    def custom_discounted_cash_flow(
        self,
        symbol: str,
        revenue_growth_pct: float | None = None,
        ebitda_pct: float | None = None,
        depreciation_and_amortization_pct: float | None = None,
        cash_and_short_term_investments_pct: float | None = None,
        receivables_pct: float | None = None,
        inventories_pct: float | None = None,
        payable_pct: float | None = None,
        ebit_pct: float | None = None,
        capital_expenditure_pct: float | None = None,
        operating_cash_flow_pct: float | None = None,
        selling_general_and_administrative_expenses_pct: float | None = None,
        tax_rate: float | None = None,
        long_term_growth_rate: float | None = None,
        cost_of_debt: float | None = None,
        cost_of_equity: float | None = None,
        market_risk_premium: float | None = None,
        beta: float | None = None,
        risk_free_rate: float | None = None,
    ) -> list[CustomDiscountedCashFlowResult]:
        """``GET custom-discounted-cash-flow`` — unlevered DCF with every
        model assumption overridable. Any parameter left unset falls back
        to FMP's own default for that assumption (§8.8 — we never invent
        one ourselves). Full year-by-year projection in the response:
        revenue/EBITDA/EBIT build-up, WACC components, terminal value,
        equity value per share.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param revenue_growth_pct: override for projected revenue growth rate.
        :param ebitda_pct: override for EBITDA margin.
        :param depreciation_and_amortization_pct: override for D&A as a % of revenue.
        :param cash_and_short_term_investments_pct: override for cash/STI as a % of revenue.
        :param receivables_pct: override for receivables as a % of revenue.
        :param inventories_pct: override for inventories as a % of revenue.
        :param payable_pct: override for payables as a % of revenue.
        :param ebit_pct: override for EBIT margin.
        :param capital_expenditure_pct: override for capex as a % of revenue.
        :param operating_cash_flow_pct: override for operating cash flow as a % of revenue.
        :param selling_general_and_administrative_expenses_pct: override for SG&A as a % of revenue.
        :param tax_rate: override for the effective tax rate.
        :param long_term_growth_rate: override for the terminal growth rate.
        :param cost_of_debt: override for pre-tax cost of debt.
        :param cost_of_equity: override for cost of equity.
        :param market_risk_premium: override for the market risk premium.
        :param beta: override for equity beta.
        :param risk_free_rate: override for the risk-free rate.
        """
        return cast(
            "list[CustomDiscountedCashFlowResult]",
            self._get(
                "custom-discounted-cash-flow",
                _custom_dcf_params(
                    symbol,
                    revenue_growth_pct,
                    ebitda_pct,
                    depreciation_and_amortization_pct,
                    cash_and_short_term_investments_pct,
                    receivables_pct,
                    inventories_pct,
                    payable_pct,
                    ebit_pct,
                    capital_expenditure_pct,
                    operating_cash_flow_pct,
                    selling_general_and_administrative_expenses_pct,
                    tax_rate,
                    long_term_growth_rate,
                    cost_of_debt,
                    cost_of_equity,
                    market_risk_premium,
                    beta,
                    risk_free_rate,
                ),
            ),
        )

    def custom_levered_discounted_cash_flow(
        self,
        symbol: str,
        revenue_growth_pct: float | None = None,
        ebitda_pct: float | None = None,
        depreciation_and_amortization_pct: float | None = None,
        cash_and_short_term_investments_pct: float | None = None,
        receivables_pct: float | None = None,
        inventories_pct: float | None = None,
        payable_pct: float | None = None,
        ebit_pct: float | None = None,
        capital_expenditure_pct: float | None = None,
        operating_cash_flow_pct: float | None = None,
        selling_general_and_administrative_expenses_pct: float | None = None,
        tax_rate: float | None = None,
        long_term_growth_rate: float | None = None,
        cost_of_debt: float | None = None,
        cost_of_equity: float | None = None,
        market_risk_premium: float | None = None,
        beta: float | None = None,
        risk_free_rate: float | None = None,
    ) -> list[CustomLeveredDiscountedCashFlowResult]:
        """``GET custom-levered-discounted-cash-flow`` — same 18
        overridable assumptions as :meth:`custom_discounted_cash_flow`,
        levered (net of debt): operating cash flow build-up instead of
        EBITDA/EBIT, free cash flow instead of unlevered FCF.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param revenue_growth_pct: override for projected revenue growth rate.
        :param ebitda_pct: override for EBITDA margin.
        :param depreciation_and_amortization_pct: override for D&A as a % of revenue.
        :param cash_and_short_term_investments_pct: override for cash/STI as a % of revenue.
        :param receivables_pct: override for receivables as a % of revenue.
        :param inventories_pct: override for inventories as a % of revenue.
        :param payable_pct: override for payables as a % of revenue.
        :param ebit_pct: override for EBIT margin.
        :param capital_expenditure_pct: override for capex as a % of revenue.
        :param operating_cash_flow_pct: override for operating cash flow as a % of revenue.
        :param selling_general_and_administrative_expenses_pct: override for SG&A as a % of revenue.
        :param tax_rate: override for the effective tax rate.
        :param long_term_growth_rate: override for the terminal growth rate.
        :param cost_of_debt: override for pre-tax cost of debt.
        :param cost_of_equity: override for cost of equity.
        :param market_risk_premium: override for the market risk premium.
        :param beta: override for equity beta.
        :param risk_free_rate: override for the risk-free rate.
        """
        return cast(
            "list[CustomLeveredDiscountedCashFlowResult]",
            self._get(
                "custom-levered-discounted-cash-flow",
                _custom_dcf_params(
                    symbol,
                    revenue_growth_pct,
                    ebitda_pct,
                    depreciation_and_amortization_pct,
                    cash_and_short_term_investments_pct,
                    receivables_pct,
                    inventories_pct,
                    payable_pct,
                    ebit_pct,
                    capital_expenditure_pct,
                    operating_cash_flow_pct,
                    selling_general_and_administrative_expenses_pct,
                    tax_rate,
                    long_term_growth_rate,
                    cost_of_debt,
                    cost_of_equity,
                    market_risk_premium,
                    beta,
                    risk_free_rate,
                ),
            ),
        )
