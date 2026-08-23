"""Response shapes returned by ``client.company`` methods."""

from __future__ import annotations

from typing import TypedDict


class ProfileResult(TypedDict):
    """Shape shared by `profile` (lookup by symbol) and `profile_cik`
    (lookup by CIK) — identical fields in both documented examples, and
    both answer the same question (the company profile record), just
    keyed differently."""

    symbol: str
    price: float
    marketCap: float
    beta: float
    lastDividend: float
    range: str
    change: float
    changePercentage: float
    volume: int
    averageVolume: int
    companyName: str
    currency: str
    cik: str
    isin: str
    cusip: str
    exchangeFullName: str
    exchange: str
    industry: str
    website: str
    description: str
    ceo: str
    sector: str
    country: str
    fullTimeEmployees: str
    phone: str
    address: str
    city: str
    state: str
    zip: str
    image: str
    ipoDate: str
    defaultImage: bool
    isEtf: bool
    isActivelyTrading: bool
    isAdr: bool
    isFund: bool


class CompanyNotesResult(TypedDict):
    """One corporate debt note the company has issued, with exchange
    listing. Returned by `company_notes()`."""

    cik: str
    symbol: str
    title: str
    exchange: str


class StockPeersResult(TypedDict):
    """One peer company: same exchange, sector, and market-cap range.
    Returned by `stock_peers()`."""

    symbol: str
    companyName: str
    price: float
    mktCap: float


class DelistedCompanyResult(TypedDict):
    """One company removed from public exchanges. Returned by
    `delisted_companies()`."""

    symbol: str
    companyName: str
    exchange: str
    ipoDate: str
    delistedDate: str


class EmployeeCountResult(TypedDict):
    """Shape shared by `employee_count` (latest filing) and
    `historical_employee_count` (full history) — identical fields in both
    documented examples, same question at different scope."""

    symbol: str
    cik: str
    acceptanceTime: str
    periodOfReport: str
    companyName: str
    formType: str
    filingDate: str
    employeeCount: int
    source: str


class MarketCapResult(TypedDict):
    """Shape shared by `market_capitalization` (one symbol, latest),
    `market_capitalization_batch` (many symbols, latest), and
    `historical_market_capitalization` (one symbol, date range) —
    identical fields in all three documented examples, same question at
    different scope."""

    symbol: str
    date: str
    marketCap: float


class SharesFloatResult(TypedDict):
    """Publicly tradable share count and free float percentage for one
    company. Returned by `shares_float()`."""

    symbol: str
    date: str
    freeFloat: float
    floatShares: int
    outstandingShares: int
    source: str


class SharesFloatAllResult(TypedDict):
    """Same as `SharesFloatResult` minus `source` — the market-wide
    listing's documented example doesn't include a per-row filing link."""

    symbol: str
    date: str
    freeFloat: float
    floatShares: int
    outstandingShares: int


class MergersAcquisitionsResult(TypedDict):
    """Shape shared by `mergers_acquisitions_latest` (recent, unfiltered)
    and `mergers_acquisitions_search` (filtered by company name) —
    identical fields in both documented examples, same question at
    different scope."""

    symbol: str
    companyName: str
    cik: str
    targetedCompanyName: str
    targetedCik: str
    targetedSymbol: str
    transactionDate: str
    acceptedDate: str
    link: str


class KeyExecutiveResult(TypedDict):
    """One member of company leadership: name, title, pay, and
    demographic detail. Returned by `key_executives()`."""

    title: str
    name: str
    pay: float | None
    currencyPay: str
    gender: str
    yearBorn: int | None
    # Type inferred, not verified: the documented example's only value is
    # `null`, so whether this is a date string, a year, or a timestamp is
    # unconfirmed. Flag for correction if a live response disagrees.
    titleSince: int | None
    active: bool


class ExecutiveCompensationResult(TypedDict):
    """One executive's detailed compensation filing: salary, bonus,
    stock/option awards, total. Returned by
    `governance_executive_compensation()`."""

    cik: str
    symbol: str
    companyName: str
    filingDate: str
    acceptedDate: str
    nameAndPosition: str
    year: int
    salary: float
    bonus: float
    stockAward: float
    optionAward: float
    incentivePlanCompensation: float
    allOtherCompensation: float
    total: float
    link: str


class ExecutiveCompensationBenchmarkResult(TypedDict):
    """Average executive compensation for one industry, for
    cross-company benchmarking. Returned by
    `executive_compensation_benchmark()`."""

    industryTitle: str
    year: int
    averageCompensation: float
