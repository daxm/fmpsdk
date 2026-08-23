"""client.commodity — Commodity instrument reference list. 1 primary
method; ``quote``, ``quote_short``, ``batch_commodity_quotes``,
``historical_chart``, ``historical_price_eod_full``, and
``historical_price_eod_light`` are also reachable here from
``client.quote``/``client.chart``.
"""

from __future__ import annotations

from typing import cast

from ..types import CommoditiesListResult


class CommodityEndpoints:
    """Mixed into :class:`fmpsdk.client.Client`. Issues one GET against
    ``stable/`` via ``self._get`` (defined on ``Client``).
    """

    def commodities_list(self) -> list[CommoditiesListResult]:
        """``GET commodities-list`` — every tradable commodity FMP tracks,
        with symbol, trade month, and currency. No parameters."""
        return cast("list[CommoditiesListResult]", self._get("commodities-list", {}))
