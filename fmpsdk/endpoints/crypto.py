"""client.crypto — Cryptocurrency instrument reference list
(REWRITE_ARCHITECTURE.md §6, ``client.crypto``). 1 primary method.
``quote``, ``quote_short``, ``batch_crypto_quotes``, ``historical_chart``,
``historical_price_eod_full``, and ``historical_price_eod_light`` are
cross-listed in from ``client.quote``/``client.chart`` once those groups
exist — see §4.3 and the workflow note in ``groups.py``.
"""

from __future__ import annotations

from typing import cast

from ..types import CryptocurrencyListResult


class CryptoEndpoints:
    """Mixed into :class:`fmpsdk.client.Client`. Issues one GET against
    ``stable/`` via ``self._get`` (defined on ``Client``).
    """

    def cryptocurrency_list(self) -> list[CryptocurrencyListResult]:
        """``GET cryptocurrency-list`` — every cryptocurrency FMP tracks,
        with symbol, name, exchange, and supply data. No parameters."""
        return cast(
            "list[CryptocurrencyListResult]", self._get("cryptocurrency-list", {})
        )
