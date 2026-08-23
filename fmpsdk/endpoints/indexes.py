"""client.indexes — Stock-market indexes, their quotes/charts, and their
constituent lists. 7 primary methods; ``historical_chart``,
``historical_price_eod_full``, and ``historical_price_eod_light`` are
also reachable here from ``client.chart``. Only ``index_list`` works on
the free tier — the 3 constituent-list methods and their 3
``historical_*`` counterparts all require an FMP Ultimate-tier plan.
"""

from __future__ import annotations

from typing import cast

from ..types import (
    HistoricalIndexConstituentResult,
    IndexConstituentResult,
    IndexListResult,
)


class IndexesEndpoints:
    """Mixed into :class:`fmpsdk.client.Client`. Each method issues one GET
    against its ``stable/`` path via ``self._get`` (defined on ``Client``).
    """

    def index_list(self) -> list[IndexListResult]:
        """``GET index-list`` — every stock market index FMP tracks, with
        symbol, name, exchange, and currency. No parameters."""
        return cast("list[IndexListResult]", self._get("index-list", {}))

    def sp500_constituent(self) -> list[IndexConstituentResult]:
        """``GET sp500-constituent`` — current S&P 500 membership, one row
        per company. No parameters."""
        return cast("list[IndexConstituentResult]", self._get("sp500-constituent", {}))

    def nasdaq_constituent(self) -> list[IndexConstituentResult]:
        """``GET nasdaq-constituent`` — current Nasdaq membership, one row
        per company. No parameters."""
        return cast("list[IndexConstituentResult]", self._get("nasdaq-constituent", {}))

    def dowjones_constituent(self) -> list[IndexConstituentResult]:
        """``GET dowjones-constituent`` — current Dow Jones Industrial
        Average membership, one row per company. No parameters."""
        return cast(
            "list[IndexConstituentResult]", self._get("dowjones-constituent", {})
        )

    def historical_sp500_constituent(
        self,
    ) -> list[HistoricalIndexConstituentResult]:
        """``GET historical-sp500-constituent`` — every addition/removal
        to the S&P 500's membership, with the reason for each change. No
        parameters."""
        return cast(
            "list[HistoricalIndexConstituentResult]",
            self._get("historical-sp500-constituent", {}),
        )

    def historical_nasdaq_constituent(
        self,
    ) -> list[HistoricalIndexConstituentResult]:
        """``GET historical-nasdaq-constituent`` — every addition/removal
        to the Nasdaq's membership, with the reason for each change. No
        parameters."""
        return cast(
            "list[HistoricalIndexConstituentResult]",
            self._get("historical-nasdaq-constituent", {}),
        )

    def historical_dowjones_constituent(
        self,
    ) -> list[HistoricalIndexConstituentResult]:
        """``GET historical-dowjones-constituent`` — every addition/removal
        to the Dow Jones's membership, with the reason for each change. No
        parameters."""
        return cast(
            "list[HistoricalIndexConstituentResult]",
            self._get("historical-dowjones-constituent", {}),
        )
