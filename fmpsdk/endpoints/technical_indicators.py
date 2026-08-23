"""client.technical_indicators — Computed technical indicator series
(SMA, EMA, WMA, DEMA, TEMA, RSI, standard deviation, Williams %R, ADX).
9 methods, all taking the same ``symbol``/``period_length``/
``timeframe``/``from``/``to`` parameters. Requires an FMP Starter-tier
plan or higher — every method here 402s on the free tier.
"""

from __future__ import annotations

from typing import cast

from ..types import (
    AdxResult,
    DemaResult,
    EmaResult,
    RsiResult,
    SmaResult,
    StandardDeviationResult,
    TemaResult,
    WilliamsResult,
    WmaResult,
)


def _technical_indicator_params(
    symbol: str,
    period_length: int,
    timeframe: str,
    from_: str | None,
    to: str | None,
) -> dict:
    """Shared query-param assembly for all 9 ``technical-indicators/*``
    methods. ``timeframe`` accepts ``constants.TIMEFRAME_TECHNICAL``."""
    return {
        "symbol": symbol,
        "periodLength": period_length,
        "timeframe": timeframe,
        "from": from_,
        "to": to,
    }


class TechnicalIndicatorsEndpoints:
    """Mixed into :class:`fmpsdk.client.Client`. Each method issues one GET
    against its ``stable/`` path via ``self._get`` (defined on ``Client``).
    """

    def technical_indicators_sma(
        self,
        symbol: str,
        period_length: int,
        timeframe: str,
        from_: str | None = None,
        to: str | None = None,
    ) -> list[SmaResult]:
        """``GET technical-indicators/sma`` — simple moving average series.

        :param symbol: security ticker symbol, e.g. ``"AAPL"``.
        :param period_length: look-back window length, e.g. ``10``.
        :param timeframe: bar interval, one of ``constants.TIMEFRAME_TECHNICAL``.
        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        """
        return cast(
            "list[SmaResult]",
            self._get(
                "technical-indicators/sma",
                _technical_indicator_params(
                    symbol, period_length, timeframe, from_, to
                ),
            ),
        )

    def technical_indicators_ema(
        self,
        symbol: str,
        period_length: int,
        timeframe: str,
        from_: str | None = None,
        to: str | None = None,
    ) -> list[EmaResult]:
        """``GET technical-indicators/ema`` — exponential moving average
        series.

        :param symbol: security ticker symbol, e.g. ``"AAPL"``.
        :param period_length: look-back window length, e.g. ``10``.
        :param timeframe: bar interval, one of ``constants.TIMEFRAME_TECHNICAL``.
        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        """
        return cast(
            "list[EmaResult]",
            self._get(
                "technical-indicators/ema",
                _technical_indicator_params(
                    symbol, period_length, timeframe, from_, to
                ),
            ),
        )

    def technical_indicators_wma(
        self,
        symbol: str,
        period_length: int,
        timeframe: str,
        from_: str | None = None,
        to: str | None = None,
    ) -> list[WmaResult]:
        """``GET technical-indicators/wma`` — weighted moving average
        series.

        :param symbol: security ticker symbol, e.g. ``"AAPL"``.
        :param period_length: look-back window length, e.g. ``10``.
        :param timeframe: bar interval, one of ``constants.TIMEFRAME_TECHNICAL``.
        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        """
        return cast(
            "list[WmaResult]",
            self._get(
                "technical-indicators/wma",
                _technical_indicator_params(
                    symbol, period_length, timeframe, from_, to
                ),
            ),
        )

    def technical_indicators_dema(
        self,
        symbol: str,
        period_length: int,
        timeframe: str,
        from_: str | None = None,
        to: str | None = None,
    ) -> list[DemaResult]:
        """``GET technical-indicators/dema`` — double exponential moving
        average series.

        :param symbol: security ticker symbol, e.g. ``"AAPL"``.
        :param period_length: look-back window length, e.g. ``10``.
        :param timeframe: bar interval, one of ``constants.TIMEFRAME_TECHNICAL``.
        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        """
        return cast(
            "list[DemaResult]",
            self._get(
                "technical-indicators/dema",
                _technical_indicator_params(
                    symbol, period_length, timeframe, from_, to
                ),
            ),
        )

    def technical_indicators_tema(
        self,
        symbol: str,
        period_length: int,
        timeframe: str,
        from_: str | None = None,
        to: str | None = None,
    ) -> list[TemaResult]:
        """``GET technical-indicators/tema`` — triple exponential moving
        average series.

        :param symbol: security ticker symbol, e.g. ``"AAPL"``.
        :param period_length: look-back window length, e.g. ``10``.
        :param timeframe: bar interval, one of ``constants.TIMEFRAME_TECHNICAL``.
        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        """
        return cast(
            "list[TemaResult]",
            self._get(
                "technical-indicators/tema",
                _technical_indicator_params(
                    symbol, period_length, timeframe, from_, to
                ),
            ),
        )

    def technical_indicators_rsi(
        self,
        symbol: str,
        period_length: int,
        timeframe: str,
        from_: str | None = None,
        to: str | None = None,
    ) -> list[RsiResult]:
        """``GET technical-indicators/rsi`` — relative strength index
        series.

        :param symbol: security ticker symbol, e.g. ``"AAPL"``.
        :param period_length: look-back window length, e.g. ``10``.
        :param timeframe: bar interval, one of ``constants.TIMEFRAME_TECHNICAL``.
        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        """
        return cast(
            "list[RsiResult]",
            self._get(
                "technical-indicators/rsi",
                _technical_indicator_params(
                    symbol, period_length, timeframe, from_, to
                ),
            ),
        )

    def technical_indicators_standarddeviation(
        self,
        symbol: str,
        period_length: int,
        timeframe: str,
        from_: str | None = None,
        to: str | None = None,
    ) -> list[StandardDeviationResult]:
        """``GET technical-indicators/standarddeviation`` — rolling
        standard deviation series.

        :param symbol: security ticker symbol, e.g. ``"AAPL"``.
        :param period_length: look-back window length, e.g. ``10``.
        :param timeframe: bar interval, one of ``constants.TIMEFRAME_TECHNICAL``.
        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        """
        return cast(
            "list[StandardDeviationResult]",
            self._get(
                "technical-indicators/standarddeviation",
                _technical_indicator_params(
                    symbol, period_length, timeframe, from_, to
                ),
            ),
        )

    def technical_indicators_williams(
        self,
        symbol: str,
        period_length: int,
        timeframe: str,
        from_: str | None = None,
        to: str | None = None,
    ) -> list[WilliamsResult]:
        """``GET technical-indicators/williams`` — Williams %R series.

        :param symbol: security ticker symbol, e.g. ``"AAPL"``.
        :param period_length: look-back window length, e.g. ``10``.
        :param timeframe: bar interval, one of ``constants.TIMEFRAME_TECHNICAL``.
        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        """
        return cast(
            "list[WilliamsResult]",
            self._get(
                "technical-indicators/williams",
                _technical_indicator_params(
                    symbol, period_length, timeframe, from_, to
                ),
            ),
        )

    def technical_indicators_adx(
        self,
        symbol: str,
        period_length: int,
        timeframe: str,
        from_: str | None = None,
        to: str | None = None,
    ) -> list[AdxResult]:
        """``GET technical-indicators/adx`` — average directional index
        series.

        :param symbol: security ticker symbol, e.g. ``"AAPL"``.
        :param period_length: look-back window length, e.g. ``10``.
        :param timeframe: bar interval, one of ``constants.TIMEFRAME_TECHNICAL``.
        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        """
        return cast(
            "list[AdxResult]",
            self._get(
                "technical-indicators/adx",
                _technical_indicator_params(
                    symbol, period_length, timeframe, from_, to
                ),
            ),
        )
