"""Mocked unit tests for client.congress — mirrors
fmpsdk/endpoints/congress.py.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.unit

BASE = "https://financialmodelingprep.com/stable/"

_TRADE_ROW = {
    "symbol": "AAPL",
    "senateID": "P000197",
    "disclosureDate": "2026-08-01",
    "transactionDate": "2026-07-15",
    "firstName": "Jane",
    "lastName": "Doe",
    "office": "California",
    "district": "12",
    "owner": "Self",
    "assetDescription": "Apple Inc. Common Stock",
    "assetType": "Stock",
    "type": "Purchase",
    "amount": "$1,001 - $15,000",
    "capitalGainsOver200USD": None,
    "comment": None,
    "link": "https://example.com/disclosure",
}

_SENATE_PROFILE_ROW = {
    "senateID": "P000197",
    "firstName": "Jane",
    "lastName": "Doe",
    "birthDate": "1960-01-01",
    "latestParty": "Democrat",
    "latestState": "CA",
    "latestPosition": "Senator",
    "image": "https://example.com/img.png",
    "active": True,
    "yearsActive": 12.0,
}

_SENATE_POSITION_ROW = {
    "senateID": "P000197",
    "congressNumber": 118,
    "startDate": "2023-01-03",
    "endDate": None,
    "party": "Democrat",
    "position": "Senator",
    "state": "CA",
    "yearsInTerm": 2.0,
}

_SENATE_NET_WORTH_ROW = {
    "senateID": "P000197",
    "formType": "Annual",
    "year": 2025,
    "filingDate": "2026-05-15",
    "section": "Assets",
    "category": "Stock",
    "name": "Apple Inc.",
    "assetType": "Stock",
    "incomeType": None,
    "owner": "Self",
    "comment": None,
    "debtDetails": None,
    "valueRange": None,
    "value": 50000.0,
    "incomeRange": None,
    "income": None,
    "link": "https://example.com/disclosure",
}

_SENATE_NET_WORTH_AGG_ROW = {
    "senateID": "P000197",
    "year": 2025,
    "total": 500000.0,
    "realEstateLiabilities": 0.0,
    "cashAndCashEquivalents": 100000.0,
    "businessAndSelfEmployment": 0.0,
    "realEstate": 0.0,
    "ownershipInterest": 0.0,
    "stock": 400000.0,
    "options": 0.0,
    "revolvingAndCreditLines": 0.0,
    "assetBackedSecurities": 0.0,
    "businessLiabilities": 0.0,
    "mutualFundsAndETFs": 0.0,
}


def test_house_latest(client, requests_mock):
    requests_mock.get(BASE + "house-latest", json=[_TRADE_ROW])
    result = client.house_latest(page=0, limit=50)
    assert result[0]["symbol"] == "AAPL"
    sent = requests_mock.last_request.qs
    assert sent["page"] == ["0"]
    assert sent["limit"] == ["50"]


def test_house_trades(client, requests_mock):
    requests_mock.get(BASE + "house-trades", json=[_TRADE_ROW])
    result = client.house_trades(symbol="AAPL")
    assert result[0]["type"] == "Purchase"
    assert requests_mock.last_request.qs["symbol"] == ["aapl"]


def test_house_trades_by_id(client, requests_mock):
    requests_mock.get(BASE + "house-trades-by-id", json=[_TRADE_ROW])
    result = client.house_trades_by_id(senate_id="P000197")
    assert result[0]["senateID"] == "P000197"
    # §7.5's bug, mirrored: the wire param is senateID even on this House method.
    assert requests_mock.last_request.qs["senateid"] == ["p000197"]


def test_house_trades_by_name(client, requests_mock):
    requests_mock.get(BASE + "house-trades-by-name", json=[_TRADE_ROW])
    result = client.house_trades_by_name(name="James")
    assert result[0]["firstName"] == "Jane"
    assert requests_mock.last_request.qs["name"] == ["james"]


def test_senate_latest(client, requests_mock):
    requests_mock.get(BASE + "senate-latest", json=[_TRADE_ROW])
    result = client.senate_latest(page=0, limit=50)
    assert result[0]["symbol"] == "AAPL"


def test_senate_trades(client, requests_mock):
    requests_mock.get(BASE + "senate-trades", json=[_TRADE_ROW])
    result = client.senate_trades(symbol="AAPL")
    assert result[0]["assetType"] == "Stock"
    assert requests_mock.last_request.qs["symbol"] == ["aapl"]


def test_senate_trades_by_id(client, requests_mock):
    requests_mock.get(BASE + "senate-trades-by-id", json=[_TRADE_ROW])
    result = client.senate_trades_by_id(senate_id="P000197")
    assert result[0]["senateID"] == "P000197"
    assert requests_mock.last_request.qs["senateid"] == ["p000197"]


def test_senate_trades_by_name(client, requests_mock):
    requests_mock.get(BASE + "senate-trades-by-name", json=[_TRADE_ROW])
    result = client.senate_trades_by_name(name="Jerry")
    assert result[0]["lastName"] == "Doe"


def test_senate_profile(client, requests_mock):
    requests_mock.get(BASE + "senate-profile", json=[_SENATE_PROFILE_ROW])
    result = client.senate_profile(senate_id="P000197", active=True)
    assert result[0]["latestParty"] == "Democrat"
    sent = requests_mock.last_request.qs
    assert sent["senateid"] == ["p000197"]
    assert sent["active"] == ["true"]


def test_senate_positions(client, requests_mock):
    requests_mock.get(BASE + "senate-positions", json=[_SENATE_POSITION_ROW])
    result = client.senate_positions(senate_id="P000197")
    assert result[0]["congressNumber"] == 118
    assert requests_mock.last_request.qs["senateid"] == ["p000197"]


def test_senate_net_worth(client, requests_mock):
    requests_mock.get(BASE + "senate-net-worth", json=[_SENATE_NET_WORTH_ROW])
    result = client.senate_net_worth(senate_id="P000197")
    assert result[0]["value"] == 50000.0
    assert requests_mock.last_request.qs["senateid"] == ["p000197"]


def test_senate_net_worth_aggregated(client, requests_mock):
    requests_mock.get(
        BASE + "senate-net-worth-aggregated", json=[_SENATE_NET_WORTH_AGG_ROW]
    )
    result = client.senate_net_worth_aggregated(senate_id="P000197")
    assert result[0]["total"] == 500000.0
    assert requests_mock.last_request.qs["senateid"] == ["p000197"]
