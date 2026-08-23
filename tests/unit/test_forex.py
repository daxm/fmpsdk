"""Mocked unit tests for client.forex — mirrors fmpsdk/endpoints/forex.py.

Only `forex_list` is covered here. `historical_chart`,
`historical_price_eod_full`, `historical_price_eod_light`, `quote`,
`quote_short`, and `batch_forex_quotes` are cross-listed in from
`client.chart`/`client.quote` (§4.3) — already covered there.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.unit

BASE = "https://financialmodelingprep.com/stable/"


def test_forex_list(client, requests_mock):
    requests_mock.get(
        BASE + "forex-list",
        json=[
            {
                "symbol": "EURUSD",
                "fromCurrency": "EUR",
                "toCurrency": "USD",
                "fromName": "Euro",
                "toName": "United States Dollar",
            }
        ],
    )
    result = client.forex_list()
    assert result[0]["symbol"] == "EURUSD"
    assert requests_mock.last_request.qs == {}
