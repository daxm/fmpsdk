"""client.forex — FX pair reference list (REWRITE_ARCHITECTURE.md §6,
``client.forex``). 1 primary method. ``quote``, ``quote_short``,
``batch_forex_quotes``, ``historical_chart``, ``historical_price_eod_full``,
and ``historical_price_eod_light`` are cross-listed in from
``client.quote``/``client.chart`` once those groups exist — see §4.3 and
the workflow note in ``groups.py``.
"""

from __future__ import annotations

from typing import cast

from ..types import ForexListResult


class ForexEndpoints:
    """Mixed into :class:`fmpsdk.client.Client`. Issues one GET against
    ``stable/`` via ``self._get`` (defined on ``Client``).
    """

    def forex_list(self) -> list[ForexListResult]:
        """``GET forex-list`` — every currency pair FMP tracks, with
        symbol and the base/counter currency names. No parameters."""
        return cast("list[ForexListResult]", self._get("forex-list", {}))
