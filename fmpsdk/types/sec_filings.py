"""TypedDicts for ``client.sec_filings`` response shapes (REWRITE_ARCHITECTURE.md §6, ``client.sec_filings``).

Split out of the former single ``types.py`` for size — see
``fmpsdk/types/__init__.py`` for the shared conventions (naming,
when shapes are/aren't reused, the functional-TypedDict-form cases)
and the re-export barrel that keeps ``from fmpsdk.types import X``
working unchanged for every caller.
"""

from __future__ import annotations

from typing import TypedDict

# --- client.sec_filings -------------------------------------------------------


class SecFilingResult(TypedDict):
    """Shape shared by `sec_filings_8k` and `sec_filings_financials` —
    identical fields, including `hasFinancials` (absent from the
    `sec_filings_search_*` family, see `SecFilingSearchResult`)."""

    symbol: str
    cik: str
    filingDate: str
    acceptedDate: str
    formType: str
    hasFinancials: bool | None
    link: str
    finalLink: str


class SecFilingSearchResult(TypedDict):
    """Shape shared by `sec_filings_search_form_type`,
    `sec_filings_search_symbol`, and `sec_filings_search_cik` — identical
    fields, one field short of `SecFilingResult` (no `hasFinancials`)."""

    symbol: str
    cik: str
    filingDate: str
    acceptedDate: str
    formType: str
    link: str
    finalLink: str


class SecFilingsCompanySearchResult(TypedDict):
    """Shape shared by `sec_filings_company_search_name`, `_symbol`, and
    `_cik` — identical fields. Structurally identical to
    `IndustryClassificationResult` but kept separate: different question
    (identify a company by a search term vs. list companies by industry
    classification), same rationale as §7.8's `profile`."""

    symbol: str
    name: str
    cik: str
    sicCode: str
    industryTitle: str
    businessAddress: str
    phoneNumber: str


class SecProfileResult(TypedDict):
    symbol: str
    cik: str
    registrantName: str
    sicCode: str
    sicDescription: str
    sicGroup: str
    isin: str
    businessAddress: str
    mailingAddress: str
    phoneNumber: str
    postalCode: str
    city: str
    state: str
    country: str
    description: str
    ceo: str
    website: str
    exchange: str
    stateLocation: str
    stateOfIncorporation: str
    fiscalYearEnd: str
    ipoDate: str
    employees: str
    secFilingsUrl: str
    taxIdentificationNumber: str
    fiftyTwoWeekRange: str
    isActive: bool
    assetType: str
    openFigiComposite: str
    priceCurrency: str
    marketSector: str
    securityType: str | None
    isEtf: bool
    isAdr: bool
    isFund: bool


class StandardIndustrialClassificationResult(TypedDict):
    office: str
    sicCode: str
    industryTitle: str


class IndustryClassificationResult(TypedDict):
    """Shape shared by `all_industry_classification` and
    `industry_classification_search` — same question (industry
    classification lookup) at different scope (whole universe vs.
    filtered by symbol/cik/sicCode). See `SecFilingsCompanySearchResult`
    for the structurally-identical-but-different-question sibling this is
    deliberately kept apart from."""

    symbol: str
    name: str
    cik: str
    sicCode: str
    industryTitle: str
    businessAddress: str
    phoneNumber: str
