"""Mocked unit tests for client.commodity — mirrors fmpsdk/endpoints/commodity.py.

Only `commodities_list` is covered here. `historical_chart`,
`historical_price_eod_full`, `historical_price_eod_light`, `quote`,
`quote_short`, and `batch_commodity_quotes` are cross-listed in from
`client.chart`/`client.quote` (§4.3) — already covered there.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.unit

BASE = "https://financialmodelingprep.com/stable/"


def test_commodities_list(client, requests_mock):
    requests_mock.get(
        BASE + "commodities-list",
        json=[
            {
                "symbol": "GCUSD",
                "name": "Gold Futures",
                "exchange": "COMEX",
                "tradeMonth": "2026-12",
                "currency": "USD",
            }
        ],
    )
    result = client.commodities_list()
    assert result[0]["symbol"] == "GCUSD"
    assert requests_mock.last_request.qs == {}
