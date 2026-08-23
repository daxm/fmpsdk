"""client.insider_trades — Form 4 insider transactions, statistics, and
beneficial-ownership acquisitions (REWRITE_ARCHITECTURE.md §6,
``client.insider_trades``). 6 canonical methods, no cross-listings.
"""

from __future__ import annotations

from typing import cast

from ..types import (
    AcquisitionOfBeneficialOwnershipResult,
    InsiderTradingReportingNameResult,
    InsiderTradingResult,
    InsiderTradingStatisticsResult,
    InsiderTradingTransactionTypeResult,
)


class InsiderTradesEndpoints:
    """Mixed into :class:`fmpsdk.client.Client`. Each method issues one GET
    against its ``stable/`` path via ``self._get`` (defined on ``Client``).
    """

    def insider_trading_latest(
        self,
        date: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> list[InsiderTradingResult]:
        """``GET insider-trading/latest`` — most recent Form 4 insider
        transactions across all companies, paginated.

        :param date: restrict to one filing date, ``YYYY-MM-DD``.
        :param page: zero-indexed page number.
        :param limit: max results per page.
        """
        return cast(
            "list[InsiderTradingResult]",
            self._get(
                "insider-trading/latest", {"date": date, "page": page, "limit": limit}
            ),
        )

    def insider_trading_search(
        self,
        symbol: str | None = None,
        page: int | None = None,
        limit: int | None = None,
        reporting_cik: str | None = None,
        company_cik: str | None = None,
        transaction_type: str | None = None,
    ) -> list[InsiderTradingResult]:
        """``GET insider-trading/search`` — Form 4 insider transactions
        filtered by symbol, filer, issuer, or transaction type.

        :param symbol: security ticker symbol, e.g. ``"AAPL"``.
        :param page: zero-indexed page number.
        :param limit: max results per page.
        :param reporting_cik: filter by the insider's own CIK.
        :param company_cik: filter by the issuer's CIK.
        :param transaction_type: filter by transaction code, e.g. ``"S-Sale"``.
        """
        return cast(
            "list[InsiderTradingResult]",
            self._get(
                "insider-trading/search",
                {
                    "symbol": symbol,
                    "page": page,
                    "limit": limit,
                    "reportingCik": reporting_cik,
                    "companyCik": company_cik,
                    "transactionType": transaction_type,
                },
            ),
        )

    def insider_trading_reporting_name(
        self, name: str
    ) -> list[InsiderTradingReportingNameResult]:
        """``GET insider-trading/reporting-name`` — insiders whose filed
        name matches a search string, resolving to a reporting CIK.

        :param name: reporting person/entity name to search for, e.g. ``"Zuckerberg"``.
        """
        return cast(
            "list[InsiderTradingReportingNameResult]",
            self._get("insider-trading/reporting-name", {"name": name}),
        )

    def insider_trading_transaction_type(
        self,
    ) -> list[InsiderTradingTransactionTypeResult]:
        """``GET insider-trading-transaction-type`` — every SEC Form 4
        transaction type code FMP recognizes. No parameters."""
        return cast(
            "list[InsiderTradingTransactionTypeResult]",
            self._get("insider-trading-transaction-type", {}),
        )

    def insider_trading_statistics(
        self, symbol: str
    ) -> list[InsiderTradingStatisticsResult]:
        """``GET insider-trading/statistics`` — quarterly insider buy/sell
        totals and acquired/disposed ratio for one company.

        :param symbol: security ticker symbol, e.g. ``"AAPL"``.
        """
        return cast(
            "list[InsiderTradingStatisticsResult]",
            self._get("insider-trading/statistics", {"symbol": symbol}),
        )

    def acquisition_of_beneficial_ownership(
        self, symbol: str, limit: int | None = None
    ) -> list[AcquisitionOfBeneficialOwnershipResult]:
        """``GET acquisition-of-beneficial-ownership`` — Schedule 13D/13G
        beneficial-ownership changes for one company.

        :param symbol: security ticker symbol, e.g. ``"AAPL"``.
        :param limit: max results to return.
        """
        return cast(
            "list[AcquisitionOfBeneficialOwnershipResult]",
            self._get(
                "acquisition-of-beneficial-ownership",
                {"symbol": symbol, "limit": limit},
            ),
        )
