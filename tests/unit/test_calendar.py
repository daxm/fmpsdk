"""Mocked unit tests for client.calendar — mirrors fmpsdk/endpoints/calendar.py."""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.unit

BASE = "https://financialmodelingprep.com/stable/"


def test_dividends(client, requests_mock):
    requests_mock.get(
        BASE + "dividends",
        json=[
            {
                "symbol": "AAPL",
                "date": "2026-05-11",
                "recordDate": "2026-05-11",
                "paymentDate": "2026-05-14",
                "declarationDate": "2026-04-30",
                "adjDividend": 0.27,
                "dividend": 0.27,
                "yield": 0.3587535875358754,
                "frequency": "Quarterly",
            }
        ],
    )
    result = client.dividends(symbol="AAPL", limit=100)
    assert result[0]["frequency"] == "Quarterly"
    assert requests_mock.last_request.qs["limit"] == ["100"]


def test_dividends_calendar(client, requests_mock):
    requests_mock.get(
        BASE + "dividends-calendar",
        json=[
            {
                "symbol": "5871.TW",
                "date": "2026-07-29",
                "recordDate": "2026-07-30",
                "paymentDate": "2026-09-01",
                "declarationDate": "",
                "adjDividend": 5.8,
                "dividend": 5.916,
                "yield": 5.155555555555556,
                "frequency": "Annual",
            }
        ],
    )
    result = client.dividends_calendar(from_="2026-03-06", to="2026-06-06", page=0)
    assert result[0]["symbol"] == "5871.TW"
    sent = requests_mock.last_request.qs
    assert sent["from"] == ["2026-03-06"]
    assert sent["to"] == ["2026-06-06"]
    assert sent["page"] == ["0"]


def test_dividends_calendar_omits_unset_optional_params(client, requests_mock):
    requests_mock.get(BASE + "dividends-calendar", json=[])
    client.dividends_calendar()
    sent = requests_mock.last_request.qs
    assert "from" not in sent
    assert "to" not in sent
    assert "page" not in sent


def test_earnings(client, requests_mock):
    requests_mock.get(
        BASE + "earnings",
        json=[
            {
                "symbol": "AAPL",
                "date": "2026-07-30",
                "epsActual": None,
                "epsEstimated": 1.88,
                "revenueActual": None,
                "revenueEstimated": 109038900000,
                "lastUpdated": "2026-07-30",
            }
        ],
    )
    result = client.earnings(symbol="AAPL", limit=100, include_report_times=False)
    assert result[0]["epsEstimated"] == 1.88
    sent = requests_mock.last_request.qs
    assert sent["includereporttimes"] == ["false"]


def test_earnings_calendar(client, requests_mock):
    requests_mock.get(
        BASE + "earnings-calendar",
        json=[
            {
                "symbol": "GRG.L",
                "date": "2026-07-29",
                "epsActual": 0.549,
                "epsEstimated": 0.501,
                "revenueActual": 1101500000,
                "revenueEstimated": 1086300000,
                "lastUpdated": "2026-07-30",
            }
        ],
    )
    result = client.earnings_calendar(from_="2026-03-06", to="2026-06-06")
    assert result[0]["symbol"] == "GRG.L"


def test_ipos_calendar(client, requests_mock):
    requests_mock.get(
        BASE + "ipos-calendar",
        json=[
            {
                "symbol": "IMC",
                "date": "2026-07-29",
                "daa": "2026-07-29T04:00:00.000Z",
                "company": "IMC Rare Earths Ltd",
                "exchange": "NYSE",
                "actions": "Priced",
                "shares": None,
                "priceRange": None,
                "marketCap": None,
            }
        ],
    )
    result = client.ipos_calendar(from_="2026-03-06", to="2026-06-06")
    assert result[0]["company"] == "IMC Rare Earths Ltd"


def test_ipos_disclosure(client, requests_mock):
    requests_mock.get(
        BASE + "ipos-disclosure",
        json=[
            {
                "symbol": "QTJA",
                "filingDate": "2026-07-30",
                "acceptedDate": "2026-07-30",
                "effectivenessDate": "2026-07-30",
                "cik": "0001415726",
                "form": "CERT",
                "url": "https://www.sec.gov/Archives/edgar/data/1415726/x.pdf",
            }
        ],
    )
    result = client.ipos_disclosure(from_="2026-03-06", to="2026-06-06")
    assert result[0]["form"] == "CERT"


def test_ipos_prospectus(client, requests_mock):
    requests_mock.get(
        BASE + "ipos-prospectus",
        json=[
            {
                "symbol": "FTW-WT",
                "acceptedDate": "2026-07-29",
                "filingDate": "2026-07-30",
                "ipoDate": "2026-07-28",
                "cik": "0002083125",
                "pricePublicPerShare": 1,
                "pricePublicTotal": 434,
                "discountsAndCommissionsPerShare": 0,
                "discountsAndCommissionsTotal": 82251,
                "proceedsBeforeExpensesPerShare": 1,
                "proceedsBeforeExpensesTotal": 82251,
                "form": "S-1",
                "url": "https://www.sec.gov/Archives/edgar/data/2083125/x.htm",
            }
        ],
    )
    result = client.ipos_prospectus(from_="2026-03-06", to="2026-06-06")
    assert result[0]["form"] == "S-1"


def test_splits(client, requests_mock):
    requests_mock.get(
        BASE + "splits",
        json=[
            {"symbol": "AAPL", "date": "2020-08-31", "numerator": 4, "denominator": 1, "splitType": "stock-split"}
        ],
    )
    result = client.splits(symbol="AAPL", limit=100)
    assert result[0]["numerator"] == 4


def test_splits_calendar(client, requests_mock):
    requests_mock.get(
        BASE + "splits-calendar",
        json=[
            {"symbol": "WHLR", "date": "2026-07-28", "numerator": 1, "denominator": 5, "splitType": "stock-split"}
        ],
    )
    result = client.splits_calendar(from_="2026-03-06", to="2026-06-06", page=0)
    assert result[0]["symbol"] == "WHLR"
