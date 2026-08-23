"""Mocked unit tests for client.funds — mirrors fmpsdk/endpoints/funds.py."""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.unit

BASE = "https://financialmodelingprep.com/stable/"


def test_etf_holdings(client, requests_mock):
    requests_mock.get(
        BASE + "etf/holdings",
        json=[
            {
                "symbol": "SPY",
                "asset": "AAPL",
                "name": "APPLE INC",
                "isin": "US0378331005",
                "securityCusip": "037833100",
                "sharesNumber": 181418073,
                "weightPercentage": 7.79997012,
                "marketValue": 61679458958,
                "updatedAt": "2026-07-30 08:07:21",
            }
        ],
    )
    result = client.etf_holdings(symbol="SPY")
    assert result[0]["asset"] == "AAPL"
    assert requests_mock.last_request.qs["symbol"] == ["spy"]


def test_etf_info(client, requests_mock):
    requests_mock.get(
        BASE + "etf/info",
        json=[
            {
                "symbol": "SPY",
                "name": "State Street SPDR S&P 500 ETF",
                "description": "SPY is the best-recognized...",
                "isin": "US78462F1030",
                "assetClass": "Equity",
                "securityCusip": "78462F103",
                "domicile": "US",
                "website": "https://www.ssga.com/x",
                "etfCompany": "SPDR",
                "expenseRatio": 0.09,
                "assetsUnderManagement": 777349860000,
                "avgVolume": 52093933,
                "inceptionDate": "1993-01-22",
                "nav": 729.27,
                "navCurrency": "USD",
                "holdingsCount": 504,
                "isActivelyTrading": True,
                "updatedAt": "2026-07-30T16:00:20.049Z",
                "sectorsList": [{"industry": "Basic Materials", "exposure": 1.6916311902850854}],
            }
        ],
    )
    result = client.etf_info(symbol="SPY")
    assert result[0]["holdingsCount"] == 504
    assert result[0]["sectorsList"][0]["industry"] == "Basic Materials"


def test_etf_country_weightings(client, requests_mock):
    requests_mock.get(
        BASE + "etf/country-weightings",
        json=[{"country": "United States", "weightPercentage": "97.26%"}],
    )
    result = client.etf_country_weightings(symbol="SPY")
    assert result[0]["weightPercentage"] == "97.26%"


def test_etf_asset_exposure(client, requests_mock):
    requests_mock.get(
        BASE + "etf/asset-exposure",
        json=[
            {
                "symbol": "ZWT-T.TO",
                "asset": "AAPL",
                "sharesNumber": 42372,
                "weightPercentage": 10.100000000000001,
                "marketValue": 20141231.66,
            }
        ],
    )
    result = client.etf_asset_exposure(symbol="AAPL")
    assert result[0]["symbol"] == "ZWT-T.TO"


def test_etf_sector_weightings(client, requests_mock):
    requests_mock.get(
        BASE + "etf/sector-weightings",
        json=[{"symbol": "SPY", "sector": "Basic Materials", "weightPercentage": 1.6916311902850854}],
    )
    result = client.etf_sector_weightings(symbol="SPY")
    assert result[0]["sector"] == "Basic Materials"


def test_funds_disclosure(client, requests_mock):
    requests_mock.get(
        BASE + "funds/disclosure",
        json=[
            {
                "cik": "0000857489",
                "date": "2023-10-31",
                "acceptedDate": "2023-12-28 09:26:13",
                "symbol": "000089.SZ",
                "name": "Shenzhen Airport Co Ltd",
                "lei": "3003009W045RIKRBZI44",
                "title": "SHENZ AIRPORT-A",
                "cusip": "N/A",
                "isin": "CNE000000VK1",
                "balance": 2438784,
                "units": "NS",
                "cur_cd": "CNY",
                "valUsd": 2255873.6,
                "pctVal": 0.0023838966190458206,
                "payoffProfile": "Long",
                "assetCat": "EC",
                "issuerCat": "CORP",
                "invCountry": "CN",
                "isRestrictedSec": "N",
                "fairValLevel": "2",
                "isCashCollateral": "N",
                "isNonCashCollateral": "N",
                "isLoanByFund": "N",
            }
        ],
    )
    result = client.funds_disclosure(symbol="VWO", year="2023", quarter="4", cik="0000857489")
    assert result[0]["assetCat"] == "EC"
    sent = requests_mock.last_request.qs
    assert sent["year"] == ["2023"]
    assert sent["quarter"] == ["4"]
    assert sent["cik"] == ["0000857489"]


def test_funds_disclosure_omits_unset_optional_cik(client, requests_mock):
    requests_mock.get(BASE + "funds/disclosure", json=[])
    client.funds_disclosure(symbol="VWO", year="2023", quarter="4")
    assert "cik" not in requests_mock.last_request.qs


def test_funds_disclosure_dates(client, requests_mock):
    requests_mock.get(
        BASE + "funds/disclosure-dates", json=[{"date": "2026-04-30", "year": 2026, "quarter": 2}]
    )
    result = client.funds_disclosure_dates(symbol="VWO")
    assert result[0]["quarter"] == 2


def test_funds_disclosure_holders_latest(client, requests_mock):
    requests_mock.get(
        BASE + "funds/disclosure-holders-latest",
        json=[
            {
                "cik": "0000866256",
                "holder": "PARNASSUS INCOME FUNDS",
                "securityCusip": "037833100",
                "shares": 3638451,
                "dateReported": "2026-06-30",
                "change": -316881,
                "weightPercent": 4.06607721,
            }
        ],
    )
    result = client.funds_disclosure_holders_latest(symbol="AAPL")
    assert result[0]["holder"] == "PARNASSUS INCOME FUNDS"


def test_funds_disclosure_holders_search(client, requests_mock):
    requests_mock.get(
        BASE + "funds/disclosure-holders-search",
        json=[
            {
                "symbol": "FGOAX",
                "cik": "0000355691",
                "classId": "C000024574",
                "seriesId": "S000009042",
                "entityName": "Federated Hermes Government Income Securities, Inc.",
                "entityOrgType": "30",
                "seriesName": "Federated Hermes Government Income Securities, Inc.",
                "className": "Class A Shares",
                "reportingFileNumber": "811-03266",
                "address": "4000 ERICSSON DRIVE",
                "city": "WARRENDALE",
                "zipCode": "15086-7561",
                "state": "PA",
            }
        ],
    )
    result = client.funds_disclosure_holders_search(name="Federated Hermes")
    assert result[0]["symbol"] == "FGOAX"
