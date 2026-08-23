"""Response shapes returned by ``client.institutional_ownership`` methods."""

from __future__ import annotations

from typing import TypedDict

# --- client.institutional_ownership --------------------------------------


class InstitutionalOwnershipLatestResult(TypedDict):
    """One recent Form 13F filing, across all institutional investors. Returned by `institutional_ownership_latest()`."""

    cik: str
    name: str
    date: str
    filingDate: str
    acceptedDate: str
    formType: str
    link: str
    finalLink: str


class InstitutionalOwnershipExtractResult(TypedDict):
    """One security in one filer's Form 13F holdings for one quarter. Returned by `institutional_ownership_extract()`."""

    date: str
    filingDate: str
    acceptedDate: str
    cik: str
    securityCusip: str
    symbol: str
    nameOfIssuer: str
    shares: int
    titleOfClass: str
    sharesType: str
    putCallShare: str
    value: float
    link: str
    finalLink: str


class InstitutionalOwnershipDatesResult(TypedDict):
    """One fiscal year/quarter one filer has a Form 13F on file for. Returned by `institutional_ownership_dates()`."""

    date: str
    year: int
    quarter: int


class InstitutionalOwnershipExtractAnalyticsHolderResult(TypedDict):
    """Per-holder analytics for one security: weight, market value and share-count changes, ownership percentage, holding period. Returned by `institutional_ownership_extract_analytics_holder()`."""

    date: str
    cik: str
    filingDate: str
    investorName: str
    symbol: str
    securityName: str
    typeOfSecurity: str
    securityCusip: str
    sharesType: str
    putCallShare: str
    investmentDiscretion: str
    industryTitle: str
    weight: float
    lastWeight: float
    changeInWeight: float
    changeInWeightPercentage: float
    marketValue: float
    lastMarketValue: float
    changeInMarketValue: float
    changeInMarketValuePercentage: float
    sharesNumber: int
    lastSharesNumber: int
    changeInSharesNumber: int
    changeInSharesNumberPercentage: float
    quarterEndPrice: float
    avgPricePaid: float
    isNew: bool
    isSoldOut: bool
    ownership: float
    lastOwnership: float
    changeInOwnership: float
    changeInOwnershipPercentage: float
    holdingPeriod: int
    firstAdded: str
    performance: float
    performancePercentage: float
    lastPerformance: float
    changeInPerformance: float
    isCountedForPerformance: bool


class InstitutionalOwnershipHolderPerformanceSummaryResult(TypedDict):
    """One filer's portfolio performance, including S&P 500-relative returns over 1/3/5 years and since inception. Returned by `institutional_ownership_holder_performance_summary()`."""

    date: str
    cik: str
    investorName: str
    portfolioSize: int
    securitiesAdded: int
    securitiesRemoved: int
    marketValue: float
    previousMarketValue: float
    changeInMarketValue: float
    changeInMarketValuePercentage: float
    averageHoldingPeriod: int
    averageHoldingPeriodTop10: int
    averageHoldingPeriodTop20: int
    turnover: float
    turnoverAlternateSell: float
    turnoverAlternateBuy: float
    performance: float
    performancePercentage: float
    lastPerformance: float
    changeInPerformance: float
    performance1year: float
    performancePercentage1year: float
    performance3year: float
    performancePercentage3year: float
    performance5year: float
    performancePercentage5year: float
    performanceSinceInception: float
    performanceSinceInceptionPercentage: float
    performanceRelativeToSP500Percentage: float
    performance1yearRelativeToSP500Percentage: float
    performance3yearRelativeToSP500Percentage: float
    performance5yearRelativeToSP500Percentage: float
    performanceSinceInceptionRelativeToSP500Percentage: float


class InstitutionalOwnershipHolderIndustryBreakdownResult(TypedDict):
    """One filer's portfolio weight and performance for one industry. Returned by `institutional_ownership_holder_industry_breakdown()`."""

    date: str
    cik: str
    investorName: str
    industryTitle: str
    weight: float
    lastWeight: float
    changeInWeight: float
    changeInWeightPercentage: float
    performance: float
    performancePercentage: float
    lastPerformance: float
    changeInPerformance: float


class InstitutionalOwnershipSymbolPositionsSummaryResult(TypedDict):
    """Aggregate institutional positioning in one security: investor count, share/value totals, new/increased/reduced/closed position counts, put/call ratio. Returned by `institutional_ownership_symbol_positions_summary()`."""

    symbol: str
    cik: str
    date: str
    investorsHolding: int
    lastInvestorsHolding: int
    investorsHoldingChange: int
    numberOf13Fshares: int
    lastNumberOf13Fshares: int
    numberOf13FsharesChange: int
    totalInvested: float
    lastTotalInvested: float
    totalInvestedChange: float
    ownershipPercent: float
    lastOwnershipPercent: float
    ownershipPercentChange: float
    newPositions: int
    lastNewPositions: int
    newPositionsChange: int
    increasedPositions: int
    lastIncreasedPositions: int
    increasedPositionsChange: int
    closedPositions: int
    lastClosedPositions: int
    closedPositionsChange: int
    reducedPositions: int
    lastReducedPositions: int
    reducedPositionsChange: int
    totalCalls: int
    lastTotalCalls: int
    totalCallsChange: int
    totalPuts: int
    lastTotalPuts: int
    totalPutsChange: int
    putCallRatio: float
    lastPutCallRatio: float
    putCallRatioChange: float


class InstitutionalOwnershipIndustrySummaryResult(TypedDict):
    """Total institutional investment value for one industry, market-wide. Returned by `institutional_ownership_industry_summary()`."""

    industryTitle: str
    industryValue: float
    date: str
