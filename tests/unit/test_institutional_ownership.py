"""Mocked unit tests for client.institutional_ownership — mirrors
fmpsdk/endpoints/institutional_ownership.py.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.unit

BASE = "https://financialmodelingprep.com/stable/"


def test_institutional_ownership_latest(client, requests_mock):
    requests_mock.get(
        BASE + "institutional-ownership/latest",
        json=[
            {
                "cik": "0001803005",
                "name": "WEALTH ADVISORS OF IOWA, LLC",
                "date": "2026-06-30",
                "filingDate": "2026-07-30 00:00:00",
                "acceptedDate": "2026-07-30 13:14:23",
                "formType": "13F-HR",
                "link": "https://www.sec.gov/x",
                "finalLink": "https://www.sec.gov/y",
            }
        ],
    )
    result = client.institutional_ownership_latest(page=0, limit=100)
    assert result[0]["formType"] == "13F-HR"
    sent = requests_mock.last_request.qs
    assert sent["page"] == ["0"]
    assert sent["limit"] == ["100"]


def test_institutional_ownership_extract(client, requests_mock):
    requests_mock.get(
        BASE + "institutional-ownership/extract",
        json=[
            {
                "date": "2023-09-30",
                "filingDate": "2023-11-13",
                "acceptedDate": "2023-11-13",
                "cik": "0001388838",
                "securityCusip": "674215207",
                "symbol": "CHRD",
                "nameOfIssuer": "CHORD ENERGY CORPORATION",
                "shares": 13280,
                "titleOfClass": "COM NEW",
                "sharesType": "SH",
                "putCallShare": "",
                "value": 2152290,
                "link": "https://www.sec.gov/x",
                "finalLink": "https://www.sec.gov/y",
            }
        ],
    )
    result = client.institutional_ownership_extract(cik="0001388838", year="2023", quarter="3")
    assert result[0]["symbol"] == "CHRD"
    sent = requests_mock.last_request.qs
    assert sent["cik"] == ["0001388838"]
    assert sent["year"] == ["2023"]
    assert sent["quarter"] == ["3"]


def test_institutional_ownership_dates(client, requests_mock):
    requests_mock.get(
        BASE + "institutional-ownership/dates",
        json=[{"date": "2026-03-31", "year": 2026, "quarter": 1}],
    )
    result = client.institutional_ownership_dates(cik="0001067983")
    assert result[0]["quarter"] == 1


def test_institutional_ownership_extract_analytics_holder(client, requests_mock):
    requests_mock.get(
        BASE + "institutional-ownership/extract-analytics/holder",
        json=[
            {
                "date": "2023-09-30",
                "cik": "0000102909",
                "filingDate": "2023-12-18",
                "investorName": "VANGUARD GROUP INC",
                "symbol": "AAPL",
                "securityName": "APPLE INC",
                "typeOfSecurity": "COM",
                "securityCusip": "037833100",
                "sharesType": "SH",
                "putCallShare": "Share",
                "investmentDiscretion": "SOLE",
                "industryTitle": "ELECTRONIC COMPUTERS",
                "weight": 5.4673,
                "lastWeight": 5.996,
                "changeInWeight": -0.5287,
                "changeInWeightPercentage": -8.8175,
                "marketValue": 222572509140,
                "lastMarketValue": 252876459509,
                "changeInMarketValue": -30303950369,
                "changeInMarketValuePercentage": -11.9837,
                "sharesNumber": 1299997133,
                "lastSharesNumber": 1303688506,
                "changeInSharesNumber": -3691373,
                "changeInSharesNumberPercentage": -0.2831,
                "quarterEndPrice": 171.21,
                "avgPricePaid": 20.65,
                "isNew": False,
                "isSoldOut": False,
                "ownership": 8.3336,
                "lastOwnership": 8.305,
                "changeInOwnership": 0.0286,
                "changeInOwnershipPercentage": 0.3445,
                "holdingPeriod": 75,
                "firstAdded": "2005-03-31",
                "performance": -29671950396,
                "performancePercentage": -11.7338,
                "lastPerformance": 38078179274,
                "changeInPerformance": -67750129670,
                "isCountedForPerformance": True,
            }
        ],
    )
    result = client.institutional_ownership_extract_analytics_holder(
        symbol="AAPL", year="2023", quarter="3", page=0, limit=10
    )
    assert result[0]["investorName"] == "VANGUARD GROUP INC"
    assert requests_mock.last_request.qs["limit"] == ["10"]


def test_institutional_ownership_holder_performance_summary(client, requests_mock):
    requests_mock.get(
        BASE + "institutional-ownership/holder-performance-summary",
        json=[
            {
                "date": "2026-03-31",
                "cik": "0001067983",
                "investorName": "BERKSHIRE HATHAWAY INC",
                "portfolioSize": 29,
                "securitiesAdded": 3,
                "securitiesRemoved": 16,
                "marketValue": 263095703570,
                "previousMarketValue": 274160086701,
                "changeInMarketValue": -11064383131,
                "changeInMarketValuePercentage": -4.0357,
                "averageHoldingPeriod": 19,
                "averageHoldingPeriodTop10": 32,
                "averageHoldingPeriodTop20": 25,
                "turnover": 0.6552,
                "turnoverAlternateSell": 9.1702,
                "turnoverAlternateBuy": 5.8198,
                "performance": -2243708176,
                "performancePercentage": -0.8184,
                "lastPerformance": 12155036983,
                "changeInPerformance": -14398745159,
                "performance1year": 28972527543,
                "performancePercentage1year": 11.3877,
                "performance3year": 118145912143,
                "performancePercentage3year": 45.9009,
                "performance5year": 146867544096,
                "performancePercentage5year": 63.1842,
                "performanceSinceInception": 267584180516,
                "performanceSinceInceptionPercentage": 203.9112,
                "performanceRelativeToSP500Percentage": 3.8118,
                "performance1yearRelativeToSP500Percentage": -4.9473,
                "performance3yearRelativeToSP500Percentage": -12.9708,
                "performance5yearRelativeToSP500Percentage": -1.1428,
                "performanceSinceInceptionRelativeToSP500Percentage": -114.003,
            }
        ],
    )
    result = client.institutional_ownership_holder_performance_summary(cik="0001067983", page=0)
    assert result[0]["investorName"] == "BERKSHIRE HATHAWAY INC"


def test_institutional_ownership_holder_industry_breakdown(client, requests_mock):
    requests_mock.get(
        BASE + "institutional-ownership/holder-industry-breakdown",
        json=[
            {
                "date": "2023-09-30",
                "cik": "0001067983",
                "investorName": "BERKSHIRE HATHAWAY INC",
                "industryTitle": "ELECTRONIC COMPUTERS",
                "weight": 49.7704,
                "lastWeight": 51.0035,
                "changeInWeight": -1.2332,
                "changeInWeightPercentage": -2.4178,
                "performance": -20838154294,
                "performancePercentage": -178.2938,
                "lastPerformance": 26615340304,
                "changeInPerformance": -47453494598,
            }
        ],
    )
    result = client.institutional_ownership_holder_industry_breakdown(
        cik="0001067983", year="2023", quarter="3"
    )
    assert result[0]["industryTitle"] == "ELECTRONIC COMPUTERS"


def test_institutional_ownership_symbol_positions_summary(client, requests_mock):
    requests_mock.get(
        BASE + "institutional-ownership/symbol-positions-summary",
        json=[
            {
                "symbol": "AAPL",
                "cik": "0000320193",
                "date": "2023-09-30",
                "investorsHolding": 4863,
                "lastInvestorsHolding": 4805,
                "investorsHoldingChange": 58,
                "numberOf13Fshares": 9139920744,
                "lastNumberOf13Fshares": 9360939709,
                "numberOf13FsharesChange": -221018965,
                "totalInvested": 1575774922899,
                "lastTotalInvested": 1820827010085,
                "totalInvestedChange": -245052087186,
                "ownershipPercent": 58.5914,
                "lastOwnershipPercent": 59.6329,
                "ownershipPercentChange": -1.0415,
                "newPositions": 162,
                "lastNewPositions": 191,
                "newPositionsChange": -29,
                "increasedPositions": 1941,
                "lastIncreasedPositions": 1789,
                "increasedPositionsChange": 152,
                "closedPositions": 158,
                "lastClosedPositions": 122,
                "closedPositionsChange": 36,
                "reducedPositions": 2408,
                "lastReducedPositions": 2543,
                "reducedPositionsChange": -135,
                "totalCalls": 173627138,
                "lastTotalCalls": 198895582,
                "totalCallsChange": -25268444,
                "totalPuts": 192913290,
                "lastTotalPuts": 177042062,
                "totalPutsChange": 15871228,
                "putCallRatio": 1.1111,
                "lastPutCallRatio": 0.8901,
                "putCallRatioChange": 22.0952,
            }
        ],
    )
    result = client.institutional_ownership_symbol_positions_summary(
        symbol="AAPL", year="2023", quarter="3"
    )
    assert result[0]["investorsHolding"] == 4863


def test_institutional_ownership_industry_summary(client, requests_mock):
    requests_mock.get(
        BASE + "institutional-ownership/industry-summary",
        json=[
            {
                "industryTitle": "ABRASIVE, ASBESTOS & MISC NONMETALLIC MINERAL PRODS",
                "industryValue": 11088059691,
                "date": "2023-09-30",
            }
        ],
    )
    result = client.institutional_ownership_industry_summary(year="2023", quarter="3")
    assert result[0]["industryValue"] == 11088059691
