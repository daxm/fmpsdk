"""Response shapes returned by ``client.insider_trades`` methods."""

from __future__ import annotations

from typing import TypedDict

# --- client.insider_trades -----------------------------------------------------


class InsiderTradingResult(TypedDict):
    """Shape shared by `insider_trading_latest` and
    `insider_trading_search` — identical fields in both documented
    examples."""

    symbol: str
    filingDate: str
    transactionDate: str
    reportingCik: str
    companyCik: str
    transactionType: str
    securitiesOwned: float
    reportingName: str
    typeOfOwner: str
    acquisitionOrDisposition: str
    directOrIndirect: str
    formType: str
    securitiesTransacted: float
    price: float
    securityName: str
    url: str


class InsiderTradingReportingNameResult(TypedDict):
    """One insider matching a filed-name search, resolving to a reporting CIK. Returned by `insider_trading_reporting_name()`."""

    reportingCik: str
    reportingName: str


class InsiderTradingTransactionTypeResult(TypedDict):
    """One SEC Form 4 transaction type code FMP recognizes. Returned by `insider_trading_transaction_type()`."""

    transactionType: str


class InsiderTradingStatisticsResult(TypedDict):
    """Quarterly insider buy/sell totals and acquired/disposed ratio for one company. Returned by `insider_trading_statistics()`."""

    symbol: str
    cik: str
    year: int
    quarter: int
    acquiredTransactions: int
    disposedTransactions: int
    acquiredDisposedRatio: float
    totalAcquired: float
    totalDisposed: float
    averageAcquired: float
    averageDisposed: float
    totalPurchases: int
    totalSales: int


class AcquisitionOfBeneficialOwnershipResult(TypedDict):
    """One Schedule 13D/13G beneficial-ownership change for one company. Returned by `acquisition_of_beneficial_ownership()`."""

    cik: str
    symbol: str
    filingDate: str
    acceptedDate: str
    cusip: str
    nameOfReportingPerson: str
    citizenshipOrPlaceOfOrganization: str
    soleVotingPower: str
    sharedVotingPower: str
    soleDispositivePower: str
    sharedDispositivePower: str
    amountBeneficiallyOwned: str
    percentOfClass: str
    typeOfReportingPerson: str
    url: str
