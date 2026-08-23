"""client.chart — Historical price series, end-of-day and intraday, for
any symbol FMP covers (stocks, indexes, commodities, crypto, forex). 5
methods. ``historical_chart``, ``historical_price_eod_full``, and
``historical_price_eod_light`` are also reachable from
``client.indexes``/``commodity``/``crypto``/``forex``.
"""

from __future__ import annotations

from typing import cast

from ..types import (
    HistoricalChartResult,
    HistoricalPriceEodDividendAdjustedResult,
    HistoricalPriceEodFullResult,
    HistoricalPriceEodLightResult,
    HistoricalPriceEodNonSplitAdjustedResult,
)


class ChartEndpoints:
    """Mixed into :class:`fmpsdk.client.Client`. Each method issues one GET
    against its ``stable/`` path via ``self._get`` (defined on ``Client``).
    """

    def historical_chart(
        self,
        symbol: str,
        timeframe: str,
        from_: str | None = None,
        to: str | None = None,
        nonadjusted: bool | None = None,
        extended: bool | None = None,
    ) -> list[HistoricalChartResult]:
        """``GET historical-chart/{timeframe}`` — intraday OHLCV bars, one
        method covering all 6 intraday intervals FMP documents
        separately.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param timeframe: one of ``constants.TIMEFRAME_INTRADAY``
            (``"1min"``, ``"5min"``, ``"15min"``, ``"30min"``, ``"1hour"``,
            ``"4hour"``). There's no ``"1day"`` here — for daily bars use
            ``historical_price_eod_full`` instead.
        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        :param nonadjusted: return split-unadjusted prices.
        :param extended: include extended-hours bars.
        """
        return cast(
            "list[HistoricalChartResult]",
            self._get(
                f"historical-chart/{timeframe}",
                {
                    "symbol": symbol,
                    "from": from_,
                    "to": to,
                    "nonadjusted": nonadjusted,
                    "extended": extended,
                },
            ),
        )

    def historical_price_eod_light(
        self, symbol: str, from_: str | None = None, to: str | None = None
    ) -> list[HistoricalPriceEodLightResult]:
        """``GET historical-price-eod/light`` — daily close price and
        volume only, no OHLC.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        """
        return cast(
            "list[HistoricalPriceEodLightResult]",
            self._get(
                "historical-price-eod/light",
                {"symbol": symbol, "from": from_, "to": to},
            ),
        )

    def historical_price_eod_full(
        self, symbol: str, from_: str | None = None, to: str | None = None
    ) -> list[HistoricalPriceEodFullResult]:
        """``GET historical-price-eod/full`` — full daily OHLCV plus
        change and VWAP.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        """
        return cast(
            "list[HistoricalPriceEodFullResult]",
            self._get(
                "historical-price-eod/full", {"symbol": symbol, "from": from_, "to": to}
            ),
        )

    def historical_price_eod_non_split_adjusted(
        self, symbol: str, from_: str | None = None, to: str | None = None
    ) -> list[HistoricalPriceEodNonSplitAdjustedResult]:
        """``GET historical-price-eod/non-split-adjusted`` — daily OHLC as
        originally reported, without retroactive split adjustment.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        """
        return cast(
            "list[HistoricalPriceEodNonSplitAdjustedResult]",
            self._get(
                "historical-price-eod/non-split-adjusted",
                {"symbol": symbol, "from": from_, "to": to},
            ),
        )

    def historical_price_eod_dividend_adjusted(
        self, symbol: str, from_: str | None = None, to: str | None = None
    ) -> list[HistoricalPriceEodDividendAdjustedResult]:
        """``GET historical-price-eod/dividend-adjusted`` — daily OHLC
        adjusted for dividend payouts, for total-return analysis.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        """
        return cast(
            "list[HistoricalPriceEodDividendAdjustedResult]",
            self._get(
                "historical-price-eod/dividend-adjusted",
                {"symbol": symbol, "from": from_, "to": to},
            ),
        )
