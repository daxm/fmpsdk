"""Mocked unit tests for client.crypto — mirrors fmpsdk/endpoints/crypto.py.

Only `cryptocurrency_list` is covered here. `historical_chart`,
`historical_price_eod_full`, `historical_price_eod_light`, `quote`,
`quote_short`, and `batch_crypto_quotes` are cross-listed in from
`client.chart`/`client.quote` (§4.3) — already covered there.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.unit

BASE = "https://financialmodelingprep.com/stable/"


def test_cryptocurrency_list(client, requests_mock):
    requests_mock.get(
        BASE + "cryptocurrency-list",
        json=[
            {
                "symbol": "BTCUSD",
                "name": "Bitcoin",
                "exchange": "CCC",
                "icoDate": "2009-01-03",
                "circulatingSupply": 19800000.0,
                "totalSupply": 21000000.0,
            }
        ],
    )
    result = client.cryptocurrency_list()
    assert result[0]["symbol"] == "BTCUSD"
    assert requests_mock.last_request.qs == {}
