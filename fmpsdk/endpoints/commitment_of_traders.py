"""client.commitment_of_traders — CFTC Commitment-of-Traders reports and
analysis (REWRITE_ARCHITECTURE.md §6, ``client.commitment_of_traders``).
3 canonical methods, no cross-listings. Unlike most of the catalog,
``symbol`` is optional here — FMP's own docs don't mark it required for
either the report or the analysis endpoint.
"""

from __future__ import annotations

from typing import cast

from ..types import (
    CommitmentOfTradersAnalysisResult,
    CommitmentOfTradersListResult,
    CommitmentOfTradersReportResult,
)


class CommitmentOfTradersEndpoints:
    """Mixed into :class:`fmpsdk.client.Client`. Each method issues one GET
    against its ``stable/`` path via ``self._get`` (defined on ``Client``).
    """

    def commitment_of_traders_report(
        self,
        symbol: str | None = None,
        from_: str | None = None,
        to: str | None = None,
    ) -> list[CommitmentOfTradersReportResult]:
        """``GET commitment-of-traders-report`` — the raw CFTC COT report:
        long/short/spread positions by trader category, open interest,
        concentration ratios.

        :param symbol: futures/commodity symbol, e.g. ``"NG"`` (optional —
            omit for the full market).
        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        """
        return cast(
            "list[CommitmentOfTradersReportResult]",
            self._get(
                "commitment-of-traders-report", {"symbol": symbol, "from": from_, "to": to}
            ),
        )

    def commitment_of_traders_analysis(
        self,
        symbol: str | None = None,
        from_: str | None = None,
        to: str | None = None,
    ) -> list[CommitmentOfTradersAnalysisResult]:
        """``GET commitment-of-traders-analysis`` — derived sentiment
        analysis (bullish/bearish market situation, net position change,
        reversal-trend flag) built on top of the raw report.

        :param symbol: futures/commodity symbol, e.g. ``"NG"`` (optional —
            omit for the full market).
        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        """
        return cast(
            "list[CommitmentOfTradersAnalysisResult]",
            self._get(
                "commitment-of-traders-analysis", {"symbol": symbol, "from": from_, "to": to}
            ),
        )

    def commitment_of_traders_list(self) -> list[CommitmentOfTradersListResult]:
        """``GET commitment-of-traders-list`` — every symbol a COT report
        is available for. No parameters."""
        return cast(
            "list[CommitmentOfTradersListResult]", self._get("commitment-of-traders-list", {})
        )
