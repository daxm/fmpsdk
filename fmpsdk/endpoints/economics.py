"""client.economics — Macroeconomic series, treasury rates, economic
calendar, risk premium (REWRITE_ARCHITECTURE.md §6, ``client.economics``).
4 canonical methods, no cross-listings.
"""

from __future__ import annotations

from typing import cast

from ..types import (
    EconomicCalendarResult,
    EconomicIndicatorsResult,
    MarketRiskPremiumResult,
    TreasuryRatesResult,
)


class EconomicsEndpoints:
    """Mixed into :class:`fmpsdk.client.Client`. Each method issues one GET
    against its ``stable/`` path via ``self._get`` (defined on ``Client``).
    """

    def treasury_rates(
        self, from_: str | None = None, to: str | None = None
    ) -> list[TreasuryRatesResult]:
        """``GET treasury-rates`` — US Treasury yield curve (1-month
        through 30-year), one row per date.

        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        """
        return cast(
            "list[TreasuryRatesResult]", self._get("treasury-rates", {"from": from_, "to": to})
        )

    def economic_indicators(
        self, name: str, from_: str | None = None, to: str | None = None
    ) -> list[EconomicIndicatorsResult]:
        """``GET economic-indicators`` — one macroeconomic series (GDP,
        CPI, unemployment, etc.) over time.

        :param name: indicator name, one of ``constants.ECONOMIC_INDICATOR_VALUES``
            (e.g. ``"GDP"``).
        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        """
        return cast(
            "list[EconomicIndicatorsResult]",
            self._get("economic-indicators", {"name": name, "from": from_, "to": to}),
        )

    def economic_calendar(
        self,
        country: str | None = None,
        from_: str | None = None,
        to: str | None = None,
    ) -> list[EconomicCalendarResult]:
        """``GET economic-calendar`` — scheduled economic data releases,
        with prior/estimate/actual values once reported.

        :param country: ISO country code to filter by, e.g. ``"US"``.
        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        """
        return cast(
            "list[EconomicCalendarResult]",
            self._get("economic-calendar", {"country": country, "from": from_, "to": to}),
        )

    def market_risk_premium(self) -> list[MarketRiskPremiumResult]:
        """``GET market-risk-premium`` — country risk premium and total
        equity risk premium, one row per country. No parameters."""
        return cast(
            "list[MarketRiskPremiumResult]", self._get("market-risk-premium", {})
        )
