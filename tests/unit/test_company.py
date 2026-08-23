"""Mocked unit tests for client.company — mirrors fmpsdk/endpoints/company.py."""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.unit

BASE = "https://financialmodelingprep.com/stable/"

_PROFILE_JSON = {
    "symbol": "AAPL",
    "price": 331.85501,
    "marketCap": 4874072686740,
    "beta": 1.097,
    "lastDividend": 1.05,
    "range": "201.5-344.57",
    "change": -6.33498,
    "changePercentage": -1.8732,
    "volume": 28718014,
    "averageVolume": 55309000,
    "companyName": "Apple Inc.",
    "currency": "USD",
    "cik": "0000320193",
    "isin": "US0378331005",
    "cusip": "037833100",
    "exchangeFullName": "NASDAQ Global Select",
    "exchange": "NASDAQ",
    "industry": "Consumer Electronics",
    "website": "https://www.apple.com",
    "description": "Apple Inc. designs, manufactures...",
    "ceo": "Timothy D. Cook",
    "sector": "Technology",
    "country": "US",
    "fullTimeEmployees": "166000",
    "phone": "(408) 996-1010",
    "address": "One Apple Park Way",
    "city": "Cupertino",
    "state": "CA",
    "zip": "95014",
    "image": "https://images.financialmodelingprep.com/symbol/AAPL.png",
    "ipoDate": "1980-12-12",
    "defaultImage": False,
    "isEtf": False,
    "isActivelyTrading": True,
    "isAdr": False,
    "isFund": False,
}


def test_profile(client, requests_mock):
    requests_mock.get(BASE + "profile", json=[_PROFILE_JSON])
    result = client.profile(symbol="AAPL")
    assert result[0]["ceo"] == "Timothy D. Cook"
    assert requests_mock.last_request.qs["symbol"] == ["aapl"]


def test_profile_cik(client, requests_mock):
    requests_mock.get(BASE + "profile-cik", json=[_PROFILE_JSON])
    result = client.profile_cik(cik="320193")
    assert result[0]["cik"] == "0000320193"
    assert requests_mock.last_request.qs["cik"] == ["320193"]


def test_company_notes(client, requests_mock):
    requests_mock.get(
        BASE + "company-notes",
        json=[{"cik": "0000320193", "symbol": "AAPL", "title": "0.000% Notes due 2025", "exchange": "NASDAQ"}],
    )
    result = client.company_notes(symbol="AAPL")
    assert result[0]["title"] == "0.000% Notes due 2025"


def test_stock_peers(client, requests_mock):
    requests_mock.get(
        BASE + "stock-peers",
        json=[{"symbol": "GOOGL", "companyName": "Alphabet Inc.", "price": 333.84, "mktCap": 4040168831718}],
    )
    result = client.stock_peers(symbol="AAPL")
    assert result[0]["symbol"] == "GOOGL"


def test_delisted_companies(client, requests_mock):
    requests_mock.get(
        BASE + "delisted-companies",
        json=[
            {
                "symbol": "CCIX",
                "companyName": "Churchill Capital Corp IX Ordinary Shares",
                "exchange": "NASDAQ",
                "ipoDate": "2007-03-01",
                "delistedDate": "2026-07-28",
            }
        ],
    )
    result = client.delisted_companies(page=0, limit=100)
    assert result[0]["symbol"] == "CCIX"
    sent = requests_mock.last_request.qs
    assert sent["page"] == ["0"]
    assert sent["limit"] == ["100"]


def test_employee_count(client, requests_mock):
    requests_mock.get(
        BASE + "employee-count",
        json=[
            {
                "symbol": "AAPL",
                "cik": "0000320193",
                "acceptanceTime": "2025-10-31 06:01:26",
                "periodOfReport": "2025-09-27",
                "companyName": "Apple Inc.",
                "formType": "10-K",
                "filingDate": "2025-10-31",
                "employeeCount": 166000,
                "source": "https://www.sec.gov/x",
            }
        ],
    )
    result = client.employee_count(symbol="AAPL", limit=100)
    assert result[0]["employeeCount"] == 166000


def test_historical_employee_count(client, requests_mock):
    requests_mock.get(
        BASE + "historical-employee-count",
        json=[
            {
                "symbol": "AAPL",
                "cik": "0000320193",
                "acceptanceTime": "2025-10-31 06:01:26",
                "periodOfReport": "2025-09-27",
                "companyName": "Apple Inc.",
                "formType": "10-K",
                "filingDate": "2025-10-31",
                "employeeCount": 166000,
                "source": "https://www.sec.gov/x",
            }
        ],
    )
    result = client.historical_employee_count(symbol="AAPL")
    assert result[0]["formType"] == "10-K"


def test_market_capitalization(client, requests_mock):
    requests_mock.get(
        BASE + "market-capitalization",
        json=[{"symbol": "AAPL", "date": "2026-07-30", "marketCap": 4874072686740}],
    )
    result = client.market_capitalization(symbol="AAPL")
    assert result[0]["marketCap"] == 4874072686740


def test_market_capitalization_batch(client, requests_mock):
    requests_mock.get(
        BASE + "market-capitalization-batch",
        json=[{"symbol": "AAPL", "date": "2026-07-30", "marketCap": 4874072686740}],
    )
    result = client.market_capitalization_batch(symbols="AAPL,MSFT,GOOG")
    assert result[0]["symbol"] == "AAPL"
    assert requests_mock.last_request.qs["symbols"] == ["aapl,msft,goog"]


def test_historical_market_capitalization(client, requests_mock):
    requests_mock.get(
        BASE + "historical-market-capitalization",
        json=[{"symbol": "AAPL", "date": "2026-07-30", "marketCap": 4879177245542}],
    )
    result = client.historical_market_capitalization(
        symbol="AAPL", limit=100, from_="2026-04-16", to="2026-07-16"
    )
    assert result[0]["marketCap"] == 4879177245542
    sent = requests_mock.last_request.qs
    assert sent["from"] == ["2026-04-16"]
    assert sent["to"] == ["2026-07-16"]


def test_shares_float(client, requests_mock):
    requests_mock.get(
        BASE + "shares-float",
        json=[
            {
                "symbol": "AAPL",
                "date": "2026-07-30 15:48:00",
                "freeFloat": 99.83,
                "floatShares": 14662387495,
                "outstandingShares": 14687356000,
                "source": "https://www.sec.gov/x",
            }
        ],
    )
    result = client.shares_float(symbol="AAPL")
    assert result[0]["floatShares"] == 14662387495


def test_shares_float_all(client, requests_mock):
    requests_mock.get(
        BASE + "shares-float-all",
        json=[
            {
                "symbol": "000001.SZ",
                "date": "2026-07-29 14:23:30",
                "freeFloat": 41.409,
                "floatShares": 8035796667,
                "outstandingShares": 19405918198,
            }
        ],
    )
    result = client.shares_float_all(limit=1000, page=0)
    assert result[0]["symbol"] == "000001.SZ"


def test_mergers_acquisitions_latest(client, requests_mock):
    requests_mock.get(
        BASE + "mergers-acquisitions-latest",
        json=[
            {
                "symbol": "AGH",
                "companyName": "Aureus Greenway Holdings Inc",
                "cik": "0002009312",
                "targetedCompanyName": "Aureus Greenway Holdings, Inc.",
                "targetedCik": "0002009312",
                "targetedSymbol": "PUSA",
                "transactionDate": "2026-07-29",
                "acceptedDate": "2026-07-29 16:00:46",
                "link": "https://www.sec.gov/x",
            }
        ],
    )
    result = client.mergers_acquisitions_latest(page=0, limit=100)
    assert result[0]["targetedSymbol"] == "PUSA"


def test_mergers_acquisitions_search(client, requests_mock):
    requests_mock.get(
        BASE + "mergers-acquisitions-search",
        json=[
            {
                "symbol": "PEGY",
                "companyName": "Pineapple Energy Inc.",
                "cik": "0000022701",
                "targetedCompanyName": "Communications Systems, Inc.",
                "targetedCik": "0000022701",
                "targetedSymbol": "JCS",
                "transactionDate": "2021-11-12",
                "acceptedDate": "2021-11-12 09:54:22",
                "link": "https://www.sec.gov/x",
            }
        ],
    )
    result = client.mergers_acquisitions_search(name="Apple")
    assert result[0]["symbol"] == "PEGY"
    assert requests_mock.last_request.qs["name"] == ["apple"]


def test_key_executives(client, requests_mock):
    requests_mock.get(
        BASE + "key-executives",
        json=[
            {
                "title": "Vice President of Worldwide Communications",
                "name": "Kristin Huguet Quayle",
                "pay": None,
                "currencyPay": "USD",
                "gender": "female",
                "yearBorn": None,
                "titleSince": None,
                "active": True,
            }
        ],
    )
    result = client.key_executives(symbol="AAPL")
    assert result[0]["gender"] == "female"


def test_governance_executive_compensation(client, requests_mock):
    requests_mock.get(
        BASE + "governance-executive-compensation",
        json=[
            {
                "cik": "0000320193",
                "symbol": "AAPL",
                "companyName": "Apple Inc.",
                "filingDate": "2026-01-08",
                "acceptedDate": "2026-01-08 16:31:36",
                "nameAndPosition": "Luca Maestri Former SVP, CFO",
                "year": 2025,
                "salary": 819231,
                "bonus": 0,
                "stockAward": 13003031,
                "optionAward": 0,
                "incentivePlanCompensation": 1638462,
                "allOtherCompensation": 22204,
                "total": 15482928,
                "link": "https://www.sec.gov/x",
            }
        ],
    )
    result = client.governance_executive_compensation(symbol="AAPL")
    assert result[0]["total"] == 15482928


def test_executive_compensation_benchmark(client, requests_mock):
    requests_mock.get(
        BASE + "executive-compensation-benchmark",
        json=[
            {
                "industryTitle": "ABRASIVE, ASBESTOS & MISC NONMETALLIC MINERAL PRODS",
                "year": 2024,
                "averageCompensation": 784407.5555555555,
            }
        ],
    )
    result = client.executive_compensation_benchmark(year="2024")
    assert result[0]["year"] == 2024
    assert requests_mock.last_request.qs["year"] == ["2024"]


def test_executive_compensation_benchmark_omits_unset_optional_param(client, requests_mock):
    requests_mock.get(BASE + "executive-compensation-benchmark", json=[])
    client.executive_compensation_benchmark()
    assert "year" not in requests_mock.last_request.qs
