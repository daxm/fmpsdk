"""Mocked unit tests for client.commitment_of_traders — mirrors
fmpsdk/endpoints/commitment_of_traders.py.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.unit

BASE = "https://financialmodelingprep.com/stable/"

# Trimmed to the fields exercised by assertions — the real response has
# ~140 fields (see types.py's CommitmentOfTradersReportResult), but the
# mock only needs to round-trip correctly, not reproduce every field.
_REPORT_JSON = {
    "symbol": "VX",
    "date": "2024-02-27 00:00:00",
    "name": "CBOE VIX (VX)",
    "sector": "INDICES",
    "marketAndExchangeNames": "VIX FUTURES - CBOE FUTURES EXCHANGE",
    "cftcContractMarketCode": "1170E1",
    "cftcMarketCode": "E",
    "cftcRegionCode": "0",
    "cftcCommodityCode": "117",
    "openInterestAll": 361331,
    "contractUnits": "($1000 X INDEX)",
}


def test_commitment_of_traders_report(client, requests_mock):
    requests_mock.get(BASE + "commitment-of-traders-report", json=[_REPORT_JSON])
    result = client.commitment_of_traders_report(symbol="VX", from_="2024-01-01", to="2024-03-01")
    assert result[0]["openInterestAll"] == 361331
    sent = requests_mock.last_request.qs
    assert sent["symbol"] == ["vx"]
    assert sent["from"] == ["2024-01-01"]
    assert sent["to"] == ["2024-03-01"]


def test_commitment_of_traders_report_symbol_is_optional(client, requests_mock):
    requests_mock.get(BASE + "commitment-of-traders-report", json=[])
    client.commitment_of_traders_report()
    sent = requests_mock.last_request.qs
    assert "symbol" not in sent
    assert "from" not in sent
    assert "to" not in sent


def test_commitment_of_traders_analysis(client, requests_mock):
    requests_mock.get(
        BASE + "commitment-of-traders-analysis",
        json=[
            {
                "symbol": "PA",
                "date": "2024-02-27 00:00:00",
                "name": "Palladium (PA)",
                "sector": "METALS",
                "exchange": "PALLADIUM - NEW YORK MERCANTILE EXCHANGE",
                "currentLongMarketSituation": 20.87,
                "currentShortMarketSituation": 79.13,
                "marketSituation": "Bearish",
                "previousLongMarketSituation": 20.88,
                "previousShortMarketSituation": 79.12,
                "previousMarketSituation": "Bearish",
                "netPostion": -12315,
                "previousNetPosition": -12453,
                "changeInNetPosition": 1.11,
                "marketSentiment": "Increasing Bullish",
                "reversalTrend": True,
            }
        ],
    )
    result = client.commitment_of_traders_analysis(symbol="PA")
    assert result[0]["marketSituation"] == "Bearish"
    assert result[0]["reversalTrend"] is True


def test_commitment_of_traders_list(client, requests_mock):
    requests_mock.get(
        BASE + "commitment-of-traders-list", json=[{"symbol": "NG", "name": "Natural Gas (NG)"}]
    )
    result = client.commitment_of_traders_list()
    assert result[0]["symbol"] == "NG"
    assert requests_mock.last_request.qs == {}
