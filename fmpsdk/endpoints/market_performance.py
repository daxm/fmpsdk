"""client.market_performance — Sector/industry performance and P/E,
snapshot and historical, plus market leaders (REWRITE_ARCHITECTURE.md §6,
``client.market_performance``). 11 canonical methods, no cross-listings.
"""

from __future__ import annotations

from typing import cast

from ..types import (
    IndustryPeResult,
    IndustryPerformanceResult,
    MarketMoverResult,
    SectorPeResult,
    SectorPerformanceResult,
)


class MarketPerformanceEndpoints:
    """Mixed into :class:`fmpsdk.client.Client`. Each method issues one GET
    against its ``stable/`` path via ``self._get`` (defined on ``Client``).
    """

    def biggest_gainers(self) -> list[MarketMoverResult]:
        """``GET biggest-gainers`` — stocks with the largest percentage
        price increase today. No parameters."""
        return cast("list[MarketMoverResult]", self._get("biggest-gainers", {}))

    def biggest_losers(self) -> list[MarketMoverResult]:
        """``GET biggest-losers`` — stocks with the largest percentage
        price decline today. No parameters."""
        return cast("list[MarketMoverResult]", self._get("biggest-losers", {}))

    def most_actives(self) -> list[MarketMoverResult]:
        """``GET most-actives`` — stocks with the highest trading volume
        today. No parameters."""
        return cast("list[MarketMoverResult]", self._get("most-actives", {}))

    def sector_performance_snapshot(
        self,
        date: str,
        exchange: str | None = None,
        sector: str | None = None,
    ) -> list[SectorPerformanceResult]:
        """``GET sector-performance-snapshot`` — average percentage change
        by sector on one date.

        :param date: snapshot date, ``YYYY-MM-DD``.
        :param exchange: restrict to one exchange, e.g. ``"NASDAQ"``.
        :param sector: restrict to one sector, one of ``constants.SECTOR_VALUES``.
        """
        return cast(
            "list[SectorPerformanceResult]",
            self._get(
                "sector-performance-snapshot",
                {"date": date, "exchange": exchange, "sector": sector},
            ),
        )

    def industry_performance_snapshot(
        self,
        date: str,
        exchange: str | None = None,
        industry: str | None = None,
    ) -> list[IndustryPerformanceResult]:
        """``GET industry-performance-snapshot`` — average percentage
        change by industry on one date.

        :param date: snapshot date, ``YYYY-MM-DD``.
        :param exchange: restrict to one exchange, e.g. ``"NASDAQ"``.
        :param industry: restrict to one industry, one of ``constants.INDUSTRY_VALUES``.
        """
        return cast(
            "list[IndustryPerformanceResult]",
            self._get(
                "industry-performance-snapshot",
                {"date": date, "exchange": exchange, "industry": industry},
            ),
        )

    def historical_sector_performance(
        self,
        sector: str,
        exchange: str | None = None,
        from_: str | None = None,
        to: str | None = None,
    ) -> list[SectorPerformanceResult]:
        """``GET historical-sector-performance`` — average percentage
        change by sector over a date range.

        :param sector: sector name, one of ``constants.SECTOR_VALUES``.
        :param exchange: restrict to one exchange, e.g. ``"NASDAQ"``.
        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        """
        return cast(
            "list[SectorPerformanceResult]",
            self._get(
                "historical-sector-performance",
                {"sector": sector, "exchange": exchange, "from": from_, "to": to},
            ),
        )

    def historical_industry_performance(
        self,
        industry: str,
        exchange: str | None = None,
        from_: str | None = None,
        to: str | None = None,
    ) -> list[IndustryPerformanceResult]:
        """``GET historical-industry-performance`` — average percentage
        change by industry over a date range.

        :param industry: industry name, one of ``constants.INDUSTRY_VALUES``.
        :param exchange: restrict to one exchange, e.g. ``"NASDAQ"``.
        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        """
        return cast(
            "list[IndustryPerformanceResult]",
            self._get(
                "historical-industry-performance",
                {"industry": industry, "exchange": exchange, "from": from_, "to": to},
            ),
        )

    def sector_pe_snapshot(
        self,
        date: str,
        exchange: str | None = None,
        sector: str | None = None,
    ) -> list[SectorPeResult]:
        """``GET sector-pe-snapshot`` — price-to-earnings ratio by sector
        on one date.

        :param date: snapshot date, ``YYYY-MM-DD``.
        :param exchange: restrict to one exchange, e.g. ``"NASDAQ"``.
        :param sector: restrict to one sector, one of ``constants.SECTOR_VALUES``.
        """
        return cast(
            "list[SectorPeResult]",
            self._get(
                "sector-pe-snapshot",
                {"date": date, "exchange": exchange, "sector": sector},
            ),
        )

    def industry_pe_snapshot(
        self,
        date: str,
        exchange: str | None = None,
        industry: str | None = None,
    ) -> list[IndustryPeResult]:
        """``GET industry-pe-snapshot`` — price-to-earnings ratio by
        industry on one date.

        :param date: snapshot date, ``YYYY-MM-DD``.
        :param exchange: restrict to one exchange, e.g. ``"NASDAQ"``.
        :param industry: restrict to one industry, one of ``constants.INDUSTRY_VALUES``.
        """
        return cast(
            "list[IndustryPeResult]",
            self._get(
                "industry-pe-snapshot",
                {"date": date, "exchange": exchange, "industry": industry},
            ),
        )

    def historical_sector_pe(
        self,
        sector: str,
        exchange: str | None = None,
        from_: str | None = None,
        to: str | None = None,
    ) -> list[SectorPeResult]:
        """``GET historical-sector-pe`` — price-to-earnings ratio by
        sector over a date range.

        :param sector: sector name, one of ``constants.SECTOR_VALUES``.
        :param exchange: restrict to one exchange, e.g. ``"NASDAQ"``.
        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        """
        return cast(
            "list[SectorPeResult]",
            self._get(
                "historical-sector-pe",
                {"sector": sector, "exchange": exchange, "from": from_, "to": to},
            ),
        )

    def historical_industry_pe(
        self,
        industry: str,
        exchange: str | None = None,
        from_: str | None = None,
        to: str | None = None,
    ) -> list[IndustryPeResult]:
        """``GET historical-industry-pe`` — price-to-earnings ratio by
        industry over a date range.

        :param industry: industry name, one of ``constants.INDUSTRY_VALUES``.
        :param exchange: restrict to one exchange, e.g. ``"NASDAQ"``.
        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        """
        return cast(
            "list[IndustryPeResult]",
            self._get(
                "historical-industry-pe",
                {"industry": industry, "exchange": exchange, "from": from_, "to": to},
            ),
        )
