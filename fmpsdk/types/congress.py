"""TypedDicts for ``client.congress`` response shapes (REWRITE_ARCHITECTURE.md §6, ``client.congress``).

Split out of the former single ``types.py`` for size — see
``fmpsdk/types/__init__.py`` for the shared conventions (naming,
when shapes are/aren't reused, the functional-TypedDict-form cases)
and the re-export barrel that keeps ``from fmpsdk.types import X``
working unchanged for every caller.
"""

from __future__ import annotations

from typing import TypedDict

# --- client.congress -----------------------------------------------------------


# Functional form is not needed here (no field name collides with a
# keyword or starts with a digit), but the wire field is genuinely
# `senateID` even on the 4 House methods that share this shape (§7.5) —
# not a typo, mirrored as-is.
class CongressionalTradeResult(TypedDict):
    """Shape shared by 8 `client.congress` methods: `house_latest`,
    `house_trades`, `house_trades_by_id`, `house_trades_by_name`,
    `senate_latest`, `senate_trades`, `senate_trades_by_id`,
    `senate_trades_by_name` — identical fields in every documented
    example. One disclosure record, whether from a Senate or House
    filing; FMP's own `senateID` field name is used on House rows too
    (§7.5's parameter-naming bug, mirrored here as the response field is
    genuinely spelled this way on both chambers' endpoints)."""

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
