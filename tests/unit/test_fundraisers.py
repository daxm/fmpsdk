"""Mocked unit tests for client.fundraisers — mirrors fmpsdk/endpoints/fundraisers.py."""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.unit

BASE = "https://financialmodelingprep.com/stable/"

_CROWDFUNDING_ROW = {
    "cik": "0001916078",
    "companyName": "Enotap LLC",
    "date": None,
    "filingDate": "2026-03-04",
    "acceptedDate": "2026-03-04T16:00:00-05:00",
    "formType": "C",
    "formSignification": "Offering Statement",
    "nameOfIssuer": "Enotap LLC",
    "legalStatusForm": "Limited Liability Company",
    "jurisdictionOrganization": "DE",
    "issuerStreet": "123 Main St",
    "issuerCity": "Austin",
    "issuerStateOrCountry": "TX",
    "issuerZipCode": "78701",
    "issuerWebsite": "https://enotap.com",
    "intermediaryCompanyName": "Wefunder Portal LLC",
    "intermediaryCommissionCik": "0001670254",
    "intermediaryCommissionFileNumber": "007-00033",
    "compensationAmount": "6% of amount raised",
    "financialInterest": None,
    "securityOfferedType": "Simple Agreement for Future Equity",
    "securityOfferedOtherDescription": None,
    "numberOfSecurityOffered": 100000,
    "offeringPrice": 1.0,
    "offeringAmount": 100000.0,
    "overSubscriptionAccepted": "Y",
    "overSubscriptionAllocationType": "First-come, first-served basis",
    "maximumOfferingAmount": 5000000.0,
    "offeringDeadlineDate": "2026-06-01",
    "currentNumberOfEmployees": 4,
    "totalAssetMostRecentFiscalYear": 50000.0,
    "totalAssetPriorFiscalYear": 20000.0,
    "cashAndCashEquiValentMostRecentFiscalYear": 10000.0,
    "cashAndCashEquiValentPriorFiscalYear": 5000.0,
    "accountsReceivableMostRecentFiscalYear": 0.0,
    "accountsReceivablePriorFiscalYear": 0.0,
    "shortTermDebtMostRecentFiscalYear": 0.0,
    "shortTermDebtPriorFiscalYear": 0.0,
    "longTermDebtMostRecentFiscalYear": 0.0,
    "longTermDebtPriorFiscalYear": 0.0,
    "revenueMostRecentFiscalYear": 12000.0,
    "revenuePriorFiscalYear": 4000.0,
    "costGoodsSoldMostRecentFiscalYear": 3000.0,
    "costGoodsSoldPriorFiscalYear": 1000.0,
    "taxesPaidMostRecentFiscalYear": 0.0,
    "taxesPaidPriorFiscalYear": 0.0,
    "netIncomeMostRecentFiscalYear": -20000.0,
    "netIncomePriorFiscalYear": -15000.0,
}

_FUNDRAISING_ROW = {
    "cik": "0001547416",
    "companyName": "Example Ventures Inc.",
    "date": "2026-02-10",
    "filingDate": "2026-02-10",
    "acceptedDate": "2026-02-10T14:22:00-05:00",
    "formType": "D",
    "formSignification": "New Notice",
    "entityName": "Example Ventures Inc.",
    "issuerStreet": "1 Market St",
    "issuerCity": "San Francisco",
    "issuerStateOrCountry": "CA",
    "issuerStateOrCountryDescription": "CALIFORNIA",
    "issuerZipCode": "94105",
    "issuerPhoneNumber": "415-555-0100",
    "jurisdictionOfIncorporation": "DE",
    "entityType": "Corporation",
    "incorporatedWithinFiveYears": True,
    "yearOfIncorporation": "2023",
    "relatedPersonFirstName": "Jane",
    "relatedPersonLastName": "Doe",
    "relatedPersonStreet": "1 Market St",
    "relatedPersonCity": "San Francisco",
    "relatedPersonStateOrCountry": "CA",
    "relatedPersonStateOrCountryDescription": "CALIFORNIA",
    "relatedPersonZipCode": "94105",
    "relatedPersonRelationship": "Executive Officer",
    "industryGroupType": "Technology",
    "revenueRange": "No Revenue",
    "federalExemptionsExclusions": "06b",
    "isAmendment": False,
    "dateOfFirstSale": "2026-01-15",
    "durationOfOfferingIsMoreThanYear": False,
    "securitiesOfferedAreOfEquityType": True,
    "isBusinessCombinationTransaction": False,
    "minimumInvestmentAccepted": 25000.0,
    "totalOfferingAmount": 5000000.0,
    "totalAmountSold": 3200000.0,
    "totalAmountRemaining": 1800000.0,
    "hasNonAccreditedInvestors": False,
    "totalNumberAlreadyInvested": 12,
    "salesCommissions": 0.0,
    "findersFees": 0.0,
    "grossProceedsUsed": 0.0,
}


def test_crowdfunding_offerings(client, requests_mock):
    requests_mock.get(BASE + "crowdfunding-offerings", json=[_CROWDFUNDING_ROW])
    result = client.crowdfunding_offerings(cik="0001916078")
    assert result[0]["nameOfIssuer"] == "Enotap LLC"
    assert requests_mock.last_request.qs["cik"] == ["0001916078"]


def test_crowdfunding_offerings_latest(client, requests_mock):
    requests_mock.get(BASE + "crowdfunding-offerings-latest", json=[_CROWDFUNDING_ROW])
    client.crowdfunding_offerings_latest(page=0, limit=50)
    sent = requests_mock.last_request.qs
    assert sent["page"] == ["0"]
    assert sent["limit"] == ["50"]


def test_crowdfunding_offerings_latest_omits_unset_optional_params(
    client, requests_mock
):
    requests_mock.get(BASE + "crowdfunding-offerings-latest", json=[])
    client.crowdfunding_offerings_latest()
    assert requests_mock.last_request.qs == {}


def test_crowdfunding_offerings_search(client, requests_mock):
    requests_mock.get(
        BASE + "crowdfunding-offerings-search",
        json=[{"cik": "0001916078", "name": "Enotap LLC", "date": None}],
    )
    result = client.crowdfunding_offerings_search(name="enotap")
    assert result[0]["cik"] == "0001916078"
    assert requests_mock.last_request.qs["name"] == ["enotap"]


def test_fundraising(client, requests_mock):
    requests_mock.get(BASE + "fundraising", json=[_FUNDRAISING_ROW])
    result = client.fundraising(cik="0001547416")
    assert result[0]["entityName"] == "Example Ventures Inc."
    assert requests_mock.last_request.qs["cik"] == ["0001547416"]


def test_fundraising_latest(client, requests_mock):
    requests_mock.get(BASE + "fundraising-latest", json=[_FUNDRAISING_ROW])
    client.fundraising_latest(page=0, limit=50, cik="0001547416")
    sent = requests_mock.last_request.qs
    assert sent["page"] == ["0"]
    assert sent["limit"] == ["50"]
    assert sent["cik"] == ["0001547416"]


def test_fundraising_search(client, requests_mock):
    requests_mock.get(
        BASE + "fundraising-search",
        json=[{"cik": "0001547416", "name": "NJOY", "date": "2026-01-01"}],
    )
    result = client.fundraising_search(name="NJOY")
    assert result[0]["name"] == "NJOY"
    assert requests_mock.last_request.qs["name"] == ["njoy"]
