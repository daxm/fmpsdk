"""Mocked unit tests for client.sec_filings — mirrors
fmpsdk/endpoints/sec_filings.py.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.unit

BASE = "https://financialmodelingprep.com/stable/"

_FILING_ROW = {
    "symbol": "AAPL",
    "cik": "0000320193",
    "filingDate": "2026-08-01",
    "acceptedDate": "2026-08-01T16:00:00-04:00",
    "formType": "8-K",
    "hasFinancials": True,
    "link": "https://sec.gov/filing",
    "finalLink": "https://sec.gov/filing-final",
}

_FILING_SEARCH_ROW = {
    "symbol": "AAPL",
    "cik": "0000320193",
    "filingDate": "2026-08-01",
    "acceptedDate": "2026-08-01T16:00:00-04:00",
    "formType": "8-K",
    "link": "https://sec.gov/filing",
    "finalLink": "https://sec.gov/filing-final",
}

_COMPANY_SEARCH_ROW = {
    "symbol": "AAPL",
    "name": "Apple Inc.",
    "cik": "0000320193",
    "sicCode": "3571",
    "industryTitle": "ELECTRONIC COMPUTERS",
    "businessAddress": "One Apple Park Way, Cupertino, CA",
    "phoneNumber": "(408) 996-1010",
}

_SEC_PROFILE_ROW = {
    "symbol": "AAPL",
    "cik": "0000320193",
    "registrantName": "Apple Inc.",
    "sicCode": "3571",
    "sicDescription": "ELECTRONIC COMPUTERS",
    "sicGroup": "Technology",
    "isin": "US0378331005",
    "businessAddress": "One Apple Park Way, Cupertino, CA",
    "mailingAddress": "One Apple Park Way, Cupertino, CA",
    "phoneNumber": "(408) 996-1010",
    "postalCode": "95014",
    "city": "Cupertino",
    "state": "CA",
    "country": "US",
    "description": "Apple Inc. designs...",
    "ceo": "Timothy D. Cook",
    "website": "https://www.apple.com",
    "exchange": "NASDAQ",
    "stateLocation": "CA",
    "stateOfIncorporation": "CA",
    "fiscalYearEnd": "0928",
    "ipoDate": "1980-12-12",
    "employees": "164000",
    "secFilingsUrl": "https://sec.gov/cgi-bin/browse-edgar?...",
    "taxIdentificationNumber": "94-2404110",
    "fiftyTwoWeekRange": "165.0-240.0",
    "isActive": True,
    "assetType": "Common Stock",
    "openFigiComposite": "BBG000B9XRY4",
    "priceCurrency": "USD",
    "marketSector": "Technology",
    "securityType": None,
    "isEtf": False,
    "isAdr": False,
    "isFund": False,
}

_SIC_ROW = {
    "office": "Office of Technology",
    "sicCode": "3571",
    "industryTitle": "ELECTRONIC COMPUTERS",
}

_INDUSTRY_CLASS_ROW = {
    "symbol": "AAPL",
    "name": "Apple Inc.",
    "cik": "0000320193",
    "sicCode": "3571",
    "industryTitle": "ELECTRONIC COMPUTERS",
    "businessAddress": "One Apple Park Way, Cupertino, CA",
    "phoneNumber": "(408) 996-1010",
}


def test_sec_filings_8k(client, requests_mock):
    requests_mock.get(BASE + "sec-filings-8k", json=[_FILING_ROW])
    result = client.sec_filings_8k(from_="2026-08-01", to="2026-08-20")
    assert result[0]["formType"] == "8-K"
    sent = requests_mock.last_request.qs
    assert sent["from"] == ["2026-08-01"]
    assert sent["to"] == ["2026-08-20"]


def test_sec_filings_financials(client, requests_mock):
    requests_mock.get(BASE + "sec-filings-financials", json=[_FILING_ROW])
    result = client.sec_filings_financials(from_="2026-08-01", to="2026-08-20")
    assert result[0]["hasFinancials"] is True


def test_sec_filings_search_form_type(client, requests_mock):
    requests_mock.get(BASE + "sec-filings-search/form-type", json=[_FILING_SEARCH_ROW])
    result = client.sec_filings_search_form_type(
        form_type="8-K", from_="2026-08-01", to="2026-08-20"
    )
    assert result[0]["formType"] == "8-K"
    assert requests_mock.last_request.qs["formtype"] == ["8-k"]


def test_sec_filings_search_symbol(client, requests_mock):
    requests_mock.get(BASE + "sec-filings-search/symbol", json=[_FILING_SEARCH_ROW])
    result = client.sec_filings_search_symbol(
        symbol="AAPL", from_="2026-08-01", to="2026-08-20"
    )
    assert result[0]["symbol"] == "AAPL"
    assert requests_mock.last_request.qs["symbol"] == ["aapl"]


def test_sec_filings_search_cik(client, requests_mock):
    requests_mock.get(BASE + "sec-filings-search/cik", json=[_FILING_SEARCH_ROW])
    result = client.sec_filings_search_cik(
        cik="0000320193", from_="2026-08-01", to="2026-08-20"
    )
    assert result[0]["cik"] == "0000320193"
    assert requests_mock.last_request.qs["cik"] == ["0000320193"]


def test_sec_filings_company_search_name(client, requests_mock):
    requests_mock.get(
        BASE + "sec-filings-company-search/name", json=[_COMPANY_SEARCH_ROW]
    )
    result = client.sec_filings_company_search_name(company="Apple")
    assert result[0]["cik"] == "0000320193"
    assert requests_mock.last_request.qs["company"] == ["apple"]


def test_sec_filings_company_search_symbol(client, requests_mock):
    requests_mock.get(
        BASE + "sec-filings-company-search/symbol", json=[_COMPANY_SEARCH_ROW]
    )
    result = client.sec_filings_company_search_symbol(symbol="AAPL")
    assert result[0]["sicCode"] == "3571"


def test_sec_filings_company_search_cik(client, requests_mock):
    requests_mock.get(
        BASE + "sec-filings-company-search/cik", json=[_COMPANY_SEARCH_ROW]
    )
    result = client.sec_filings_company_search_cik(cik="0000320193")
    assert result[0]["name"] == "Apple Inc."


def test_sec_profile(client, requests_mock):
    requests_mock.get(BASE + "sec-profile", json=[_SEC_PROFILE_ROW])
    result = client.sec_profile(symbol="AAPL", cik="0000320193")
    assert result[0]["registrantName"] == "Apple Inc."
    sent = requests_mock.last_request.qs
    assert sent["symbol"] == ["aapl"]
    assert sent["cik"] == ["0000320193"]


def test_standard_industrial_classification_list(client, requests_mock):
    requests_mock.get(BASE + "standard-industrial-classification-list", json=[_SIC_ROW])
    result = client.standard_industrial_classification_list(sic_code="3571")
    assert result[0]["industryTitle"] == "ELECTRONIC COMPUTERS"
    assert requests_mock.last_request.qs["siccode"] == ["3571"]


def test_industry_classification_search(client, requests_mock):
    requests_mock.get(
        BASE + "industry-classification-search", json=[_INDUSTRY_CLASS_ROW]
    )
    result = client.industry_classification_search(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"


def test_all_industry_classification(client, requests_mock):
    requests_mock.get(BASE + "all-industry-classification", json=[_INDUSTRY_CLASS_ROW])
    result = client.all_industry_classification(page=0, limit=100)
    assert result[0]["name"] == "Apple Inc."
    sent = requests_mock.last_request.qs
    assert sent["page"] == ["0"]
    assert sent["limit"] == ["100"]
