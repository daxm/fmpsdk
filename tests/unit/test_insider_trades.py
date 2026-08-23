"""Mocked unit tests for client.insider_trades — mirrors fmpsdk/endpoints/insider_trades.py."""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.unit

BASE = "https://financialmodelingprep.com/stable/"

_TRADE_ROW = {
    "symbol": "AAPL",
    "filingDate": "2026-08-01",
    "transactionDate": "2026-07-30",
    "reportingCik": "0001214156",
    "companyCik": "0000320193",
    "transactionType": "S-Sale",
    "securitiesOwned": 1200000.0,
    "reportingName": "COOK TIMOTHY D",
    "typeOfOwner": "officer: Chief Executive Officer",
    "acquisitionOrDisposition": "D",
    "directOrIndirect": "D",
    "formType": "4",
    "securitiesTransacted": 50000.0,
    "price": 227.5,
    "securityName": "Common Stock",
    "url": "https://www.sec.gov/x",
}


def test_insider_trading_latest(client, requests_mock):
    requests_mock.get(BASE + "insider-trading/latest", json=[_TRADE_ROW])
    client.insider_trading_latest(date="2026-08-01", page=0, limit=100)
    sent = requests_mock.last_request.qs
    assert sent["date"] == ["2026-08-01"]
    assert sent["page"] == ["0"]
    assert sent["limit"] == ["100"]


def test_insider_trading_latest_omits_unset_optional_params(client, requests_mock):
    requests_mock.get(BASE + "insider-trading/latest", json=[])
    client.insider_trading_latest()
    assert requests_mock.last_request.qs == {}


def test_insider_trading_search(client, requests_mock):
    requests_mock.get(BASE + "insider-trading/search", json=[_TRADE_ROW])
    client.insider_trading_search(
        symbol="AAPL",
        page=0,
        limit=100,
        reporting_cik="0001214156",
        company_cik="0000320193",
        transaction_type="S-Sale",
    )
    sent = requests_mock.last_request.qs
    assert sent["symbol"] == ["aapl"]
    assert sent["reportingcik"] == ["0001214156"]
    assert sent["companycik"] == ["0000320193"]
    assert sent["transactiontype"] == ["s-sale"]


def test_insider_trading_reporting_name(client, requests_mock):
    requests_mock.get(
        BASE + "insider-trading/reporting-name",
        json=[{"reportingCik": "0001548760", "reportingName": "Zuckerberg Mark"}],
    )
    result = client.insider_trading_reporting_name(name="Zuckerberg")
    assert result[0]["reportingCik"] == "0001548760"
    assert requests_mock.last_request.qs["name"] == ["zuckerberg"]


def test_insider_trading_transaction_type(client, requests_mock):
    requests_mock.get(
        BASE + "insider-trading-transaction-type",
        json=[{"transactionType": "S-Sale"}, {"transactionType": "P-Purchase"}],
    )
    result = client.insider_trading_transaction_type()
    assert len(result) == 2
    assert requests_mock.last_request.qs == {}


def test_insider_trading_statistics(client, requests_mock):
    requests_mock.get(
        BASE + "insider-trading/statistics",
        json=[
            {
                "symbol": "AAPL",
                "cik": "0000320193",
                "year": 2026,
                "quarter": 2,
                "acquiredTransactions": 3,
                "disposedTransactions": 14,
                "acquiredDisposedRatio": 0.176,
                "totalAcquired": 40000.0,
                "totalDisposed": 227000.0,
                "averageAcquired": 13333.3,
                "averageDisposed": 16214.3,
                "totalPurchases": 3,
                "totalSales": 14,
            }
        ],
    )
    result = client.insider_trading_statistics(symbol="AAPL")
    assert result[0]["totalSales"] == 14
    assert requests_mock.last_request.qs["symbol"] == ["aapl"]


def test_acquisition_of_beneficial_ownership(client, requests_mock):
    requests_mock.get(
        BASE + "acquisition-of-beneficial-ownership",
        json=[
            {
                "cik": "0000320193",
                "symbol": "AAPL",
                "filingDate": "2026-02-14",
                "acceptedDate": "2026-02-14T16:30:00-05:00",
                "cusip": "037833100",
                "nameOfReportingPerson": "The Vanguard Group",
                "citizenshipOrPlaceOfOrganization": "Pennsylvania",
                "soleVotingPower": "0",
                "sharedVotingPower": "184000000",
                "soleDispositivePower": "1450000000",
                "sharedDispositivePower": "184000000",
                "amountBeneficiallyOwned": "1634000000",
                "percentOfClass": "8.4",
                "typeOfReportingPerson": "IA",
                "url": "https://www.sec.gov/x",
            }
        ],
    )
    result = client.acquisition_of_beneficial_ownership(symbol="AAPL", limit=10)
    assert result[0]["nameOfReportingPerson"] == "The Vanguard Group"
    assert requests_mock.last_request.qs["limit"] == ["10"]
