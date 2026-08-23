"""Response shapes returned by ``client.fundraisers`` methods."""

from __future__ import annotations

from typing import TypedDict

# --- client.fundraisers -------------------------------------------------------


class CrowdfundingOfferingResult(TypedDict):
    """Shape shared by `crowdfunding_offerings` (one issuer's campaigns by
    CIK) and `crowdfunding_offerings_latest` (market-wide, paginated) —
    identical fields in both documented examples."""

    cik: str
    companyName: str
    date: str | None
    filingDate: str
    acceptedDate: str
    formType: str
    formSignification: str
    nameOfIssuer: str
    legalStatusForm: str
    jurisdictionOrganization: str
    issuerStreet: str
    issuerCity: str
    issuerStateOrCountry: str
    issuerZipCode: str
    issuerWebsite: str | None
    intermediaryCompanyName: str
    intermediaryCommissionCik: str
    intermediaryCommissionFileNumber: str
    compensationAmount: str
    financialInterest: str | None
    securityOfferedType: str
    securityOfferedOtherDescription: str | None
    numberOfSecurityOffered: int
    offeringPrice: float
    offeringAmount: float
    overSubscriptionAccepted: str
    overSubscriptionAllocationType: str
    maximumOfferingAmount: float
    offeringDeadlineDate: str
    currentNumberOfEmployees: int
    totalAssetMostRecentFiscalYear: float
    totalAssetPriorFiscalYear: float
    cashAndCashEquiValentMostRecentFiscalYear: float
    cashAndCashEquiValentPriorFiscalYear: float
    accountsReceivableMostRecentFiscalYear: float
    accountsReceivablePriorFiscalYear: float
    shortTermDebtMostRecentFiscalYear: float
    shortTermDebtPriorFiscalYear: float
    longTermDebtMostRecentFiscalYear: float
    longTermDebtPriorFiscalYear: float
    revenueMostRecentFiscalYear: float
    revenuePriorFiscalYear: float
    costGoodsSoldMostRecentFiscalYear: float
    costGoodsSoldPriorFiscalYear: float
    taxesPaidMostRecentFiscalYear: float
    taxesPaidPriorFiscalYear: float
    netIncomeMostRecentFiscalYear: float
    netIncomePriorFiscalYear: float


class CrowdfundingOfferingSearchResult(TypedDict):
    """One issuer matching a Reg CF campaign name search, resolving to a CIK. Returned by `crowdfunding_offerings_search()`."""

    cik: str
    name: str
    date: str | None


class FundraisingResult(TypedDict):
    """Shape shared by `fundraising` (one issuer's Reg D filings by CIK)
    and `fundraising_latest` (market-wide, paginated) — identical fields
    in both documented examples."""

    cik: str
    companyName: str
    date: str
    filingDate: str
    acceptedDate: str
    formType: str
    formSignification: str
    entityName: str
    issuerStreet: str
    issuerCity: str
    issuerStateOrCountry: str
    issuerStateOrCountryDescription: str
    issuerZipCode: str
    issuerPhoneNumber: str
    jurisdictionOfIncorporation: str
    entityType: str
    incorporatedWithinFiveYears: bool | None
    yearOfIncorporation: str
    relatedPersonFirstName: str
    relatedPersonLastName: str
    relatedPersonStreet: str
    relatedPersonCity: str
    relatedPersonStateOrCountry: str
    relatedPersonStateOrCountryDescription: str
    relatedPersonZipCode: str
    relatedPersonRelationship: str
    industryGroupType: str
    revenueRange: str
    federalExemptionsExclusions: str
    isAmendment: bool
    dateOfFirstSale: str
    durationOfOfferingIsMoreThanYear: bool
    securitiesOfferedAreOfEquityType: bool
    isBusinessCombinationTransaction: bool
    minimumInvestmentAccepted: float
    totalOfferingAmount: float
    totalAmountSold: float
    totalAmountRemaining: float
    hasNonAccreditedInvestors: bool
    totalNumberAlreadyInvested: int
    salesCommissions: float
    findersFees: float
    grossProceedsUsed: float


class FundraisingSearchResult(TypedDict):
    """One issuer matching a Reg D/A company name search, resolving to a CIK. Returned by `fundraising_search()`."""

    cik: str
    name: str
    date: str | None
