"""Mocked unit tests for client.analyst — mirrors fmpsdk/endpoints/analyst.py."""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.unit

BASE = "https://financialmodelingprep.com/stable/"


def test_analyst_estimates(client, requests_mock):
    requests_mock.get(
        BASE + "analyst-estimates",
        json=[
            {
                "symbol": "AAPL",
                "date": "2030-09-27",
                "revenueLow": 648228509004,
                "revenueHigh": 735022980353,
                "revenueAvg": 679000000000,
                "ebitdaLow": 233968328102,
                "ebitdaHigh": 265295486763,
                "ebitdaAvg": 245074834838,
                "ebitLow": 217109092822,
                "ebitHigh": 246178886382,
                "ebitAvg": 227415289483,
                "netIncomeLow": 191547261069,
                "netIncomeHigh": 225370398908,
                "netIncomeAvg": 203538714818,
                "sgaExpenseLow": 41721580524,
                "sgaExpenseHigh": 47307886087,
                "sgaExpenseAvg": 43702109337,
                "epsAvg": 13.565,
                "epsHigh": 15.01999,
                "epsLow": 12.76582,
                "numAnalystsRevenue": 16,
                "numAnalystsEps": 7,
            }
        ],
    )
    result = client.analyst_estimates(symbol="AAPL", period="annual", page=0, limit=10)
    assert result[0]["numAnalystsEps"] == 7
    sent = requests_mock.last_request.qs
    assert sent["symbol"] == ["aapl"]
    assert sent["period"] == ["annual"]
    assert sent["page"] == ["0"]
    assert sent["limit"] == ["10"]


def test_analyst_estimates_omits_unset_optional_params(client, requests_mock):
    requests_mock.get(BASE + "analyst-estimates", json=[])
    client.analyst_estimates(symbol="AAPL", period="quarter")
    sent = requests_mock.last_request.qs
    assert "page" not in sent
    assert "limit" not in sent


def test_ratings_snapshot(client, requests_mock):
    requests_mock.get(
        BASE + "ratings-snapshot",
        json=[
            {
                "symbol": "AAPL",
                "rating": "B",
                "overallScore": 3,
                "discountedCashFlowScore": 3,
                "returnOnEquityScore": 5,
                "returnOnAssetsScore": 5,
                "debtToEquityScore": 1,
                "priceToEarningsScore": 2,
                "priceToBookScore": 1,
            }
        ],
    )
    result = client.ratings_snapshot(symbol="AAPL")
    assert result[0]["rating"] == "B"


def test_ratings_historical(client, requests_mock):
    requests_mock.get(
        BASE + "ratings-historical",
        json=[
            {
                "symbol": "AAPL",
                "date": "2026-07-30",
                "rating": "B",
                "overallScore": 3,
                "discountedCashFlowScore": 3,
                "returnOnEquityScore": 5,
                "returnOnAssetsScore": 5,
                "debtToEquityScore": 1,
                "priceToEarningsScore": 2,
                "priceToBookScore": 1,
            }
        ],
    )
    result = client.ratings_historical(symbol="AAPL", limit=1)
    assert result[0]["date"] == "2026-07-30"
    assert requests_mock.last_request.qs["limit"] == ["1"]


def test_price_target_summary(client, requests_mock):
    requests_mock.get(
        BASE + "price-target-summary",
        json=[
            {
                "symbol": "AAPL",
                "lastMonthCount": 8,
                "lastMonthAvgPriceTarget": 333.75,
                "lastQuarterCount": 20,
                "lastQuarterAvgPriceTarget": 332.95,
                "lastYearCount": 67,
                "lastYearAvgPriceTarget": 304.86,
                "allTimeCount": 254,
                "allTimeAvgPriceTarget": 230.51,
                "publishers": '["StreetInsider","TheFly"]',
            }
        ],
    )
    result = client.price_target_summary(symbol="AAPL")
    assert result[0]["allTimeCount"] == 254


def test_price_target_consensus(client, requests_mock):
    requests_mock.get(
        BASE + "price-target-consensus",
        json=[{"symbol": "AAPL", "targetHigh": 400, "targetLow": 250, "targetConsensus": 337.67, "targetMedian": 340}],
    )
    result = client.price_target_consensus(symbol="AAPL")
    assert result[0]["targetMedian"] == 340


def test_grades(client, requests_mock):
    requests_mock.get(
        BASE + "grades",
        json=[
            {
                "symbol": "AAPL",
                "date": "2026-07-23",
                "gradingCompany": "Morgan Stanley",
                "previousGrade": "Overweight",
                "newGrade": "Overweight",
                "action": "maintain",
            }
        ],
    )
    result = client.grades(symbol="AAPL")
    assert result[0]["gradingCompany"] == "Morgan Stanley"


def test_grades_historical(client, requests_mock):
    requests_mock.get(
        BASE + "grades-historical",
        json=[
            {
                "symbol": "AAPL",
                "date": "2026-07-01",
                "analystRatingsStrongBuy": 6,
                "analystRatingsBuy": 23,
                "analystRatingsHold": 17,
                "analystRatingsSell": 2,
                "analystRatingsStrongSell": 2,
            }
        ],
    )
    result = client.grades_historical(symbol="AAPL", limit=100)
    assert result[0]["analystRatingsBuy"] == 23


def test_grades_consensus(client, requests_mock):
    requests_mock.get(
        BASE + "grades-consensus",
        json=[
            {
                "symbol": "AAPL",
                "strongBuy": 1,
                "buy": 70,
                "hold": 32,
                "sell": 8,
                "strongSell": 0,
                "consensus": "Buy",
            }
        ],
    )
    result = client.grades_consensus(symbol="AAPL")
    assert result[0]["consensus"] == "Buy"
