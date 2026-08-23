"""client.esg — ESG disclosures, ratings, and benchmarks
(REWRITE_ARCHITECTURE.md §6, ``client.esg``). 3 canonical methods, no
cross-listings. Named by the workflow doc's original pricing-tier audit
as a likely Bucket 2 (FMP-Ultimate-gated) category — confirm live rather
than assume.
"""

from __future__ import annotations

from typing import cast

from ..types import EsgBenchmarkResult, EsgDisclosuresResult, EsgRatingsResult


class EsgEndpoints:
    """Mixed into :class:`fmpsdk.client.Client`. Each method issues one GET
    against its ``stable/`` path via ``self._get`` (defined on ``Client``).
    """

    def esg_disclosures(self, symbol: str) -> list[EsgDisclosuresResult]:
        """``GET esg-disclosures`` — per-filing environmental/social/
        governance scores from SEC disclosures.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        """
        return cast(
            "list[EsgDisclosuresResult]",
            self._get("esg-disclosures", {"symbol": symbol}),
        )

    def esg_ratings(self, symbol: str) -> list[EsgRatingsResult]:
        """``GET esg-ratings`` — current ESG risk rating and industry rank
        for one company.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        """
        return cast(
            "list[EsgRatingsResult]", self._get("esg-ratings", {"symbol": symbol})
        )

    def esg_benchmark(self, year: str | None = None) -> list[EsgBenchmarkResult]:
        """``GET esg-benchmark`` — average ESG scores by sector, for
        cross-company benchmarking.

        :param year: fiscal year, e.g. ``"2023"``.
        """
        return cast(
            "list[EsgBenchmarkResult]", self._get("esg-benchmark", {"year": year})
        )
