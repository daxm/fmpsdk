"""Response shapes returned by ``client.congress`` methods."""

from __future__ import annotations

from typing import TypedDict

# --- client.congress -----------------------------------------------------------


class CongressionalTradeResult(TypedDict):
    """One financial disclosure record, from either a House or Senate
    filing. Shared by `house_latest`, `house_trades`,
    `house_trades_by_id`, `house_trades_by_name`, `senate_latest`,
    `senate_trades`, `senate_trades_by_id`, `senate_trades_by_name`.
    Note the `senateID` field is used on House rows too — that's FMP's
    own naming, not a typo in this SDK."""

    symbol: str
    senateID: str
    disclosureDate: str
    transactionDate: str
    firstName: str
    lastName: str
    office: str
    district: str
    owner: str
    assetDescription: str
    assetType: str
    type: str
    amount: str
    capitalGainsOver200USD: str | None
    comment: str | None
    link: str


class SenateProfileResult(TypedDict):
    senateID: str
    firstName: str
    lastName: str
    birthDate: str
    latestParty: str
    latestState: str
    latestPosition: str
    image: str
    active: bool
    yearsActive: float


class SenatePositionResult(TypedDict):
    senateID: str
    congressNumber: int
    startDate: str
    endDate: str | None
    party: str
    position: str
    state: str
    yearsInTerm: float


class SenateNetWorthResult(TypedDict):
    senateID: str
    formType: str
    year: int
    filingDate: str
    section: str
    category: str
    name: str
    assetType: str
    incomeType: str | None
    owner: str
    comment: str | None
    debtDetails: dict[str, object] | None
    valueRange: dict[str, object] | None
    value: float | None
    incomeRange: dict[str, object] | None
    income: float | None
    link: str


class SenateNetWorthAggregatedResult(TypedDict):
    senateID: str
    year: int
    total: float
    realEstateLiabilities: float
    cashAndCashEquivalents: float
    businessAndSelfEmployment: float
    realEstate: float
    ownershipInterest: float
    stock: float
    options: float
    revolvingAndCreditLines: float
    assetBackedSecurities: float
    businessLiabilities: float
    mutualFundsAndETFs: float
