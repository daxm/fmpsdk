"""client.technical_indicators — Computed technical indicator series
(REWRITE_ARCHITECTURE.md §6, ``client.technical_indicators``). 9 canonical
methods, no cross-listings. All 9 share an identical ``symbol*``,
``periodLength*``, ``timeframe*``, ``from``, ``to`` param set — factored
into one private builder (same pattern as ``endpoints/dcf.py``'s
``_custom_dcf_params``). The response shapes are NOT shared despite
sharing the same 6 OHLCV+date base fields: each indicator's value lives
under a key literally named after the indicator (``sma``, ``rsi``, ...),
so the 9 result types stay separate (see ``types.py``'s note on this).
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
