"""Response shapes returned by ``client.institutional_ownership`` methods."""

from __future__ import annotations

from typing import TypedDict

# --- client.institutional_ownership --------------------------------------


class InstitutionalOwnershipLatestResult(TypedDict):
    cik: str
    name: str
    date: str
    filingDate: str
    acceptedDate: str
    formType: str
    link: str
    finalLink: str


class InstitutionalOwnershipExtractResult(TypedDict):
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
    date: str
    year: int
    quarter: int


class InstitutionalOwnershipExtractAnalyticsHolderResult(TypedDict):
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
    industryTitle: str
    industryValue: float
    date: str
