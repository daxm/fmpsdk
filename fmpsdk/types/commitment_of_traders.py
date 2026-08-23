"""TypedDicts for ``client.commitment_of_traders`` response shapes (REWRITE_ARCHITECTURE.md §6, ``client.commitment_of_traders``).

Split out of the former single ``types.py`` for size — see
``fmpsdk/types/__init__.py`` for the shared conventions (naming,
when shapes are/aren't reused, the functional-TypedDict-form cases)
and the re-export barrel that keeps ``from fmpsdk.types import X``
working unchanged for every caller.
"""

from __future__ import annotations

from typing import TypedDict

# --- client.commitment_of_traders -----------------------------------------


class CommitmentOfTradersReportResult(TypedDict):
    """CFTC COT report, one row per market per date. ~140 fields — kept
    fully typed per the project's response-typing contract (§8.4) rather
    than collapsed to a looser type; field names are verbatim from the
    documented example, including its two `Spead`/`Spread` inconsistencies
    (not our typo to fix)."""

    symbol: str
    date: str
    name: str
    sector: str
    marketAndExchangeNames: str
    cftcContractMarketCode: str
    cftcMarketCode: str
    cftcRegionCode: str
    cftcCommodityCode: str
    openInterestAll: int
    noncommPositionsLongAll: int
    noncommPositionsShortAll: int
    noncommPositionsSpreadAll: int
    commPositionsLongAll: int
    commPositionsShortAll: int
    totReptPositionsLongAll: int
    totReptPositionsShortAll: int
    nonreptPositionsLongAll: int
    nonreptPositionsShortAll: int
    openInterestOld: int
    noncommPositionsLongOld: int
    noncommPositionsShortOld: int
    noncommPositionsSpreadOld: int
    commPositionsLongOld: int
    commPositionsShortOld: int
    totReptPositionsLongOld: int
    totReptPositionsShortOld: int
    nonreptPositionsLongOld: int
    nonreptPositionsShortOld: int
    openInterestOther: int
    noncommPositionsLongOther: int
    noncommPositionsShortOther: int
    noncommPositionsSpreadOther: int
    commPositionsLongOther: int
    commPositionsShortOther: int
    totReptPositionsLongOther: int
    totReptPositionsShortOther: int
    nonreptPositionsLongOther: int
    nonreptPositionsShortOther: int
    changeInOpenInterestAll: int
    changeInNoncommLongAll: int
    changeInNoncommShortAll: int
    changeInNoncommSpeadAll: int
    changeInCommLongAll: int
    changeInCommShortAll: int
    changeInTotReptLongAll: int
    changeInTotReptShortAll: int
    changeInNonreptLongAll: int
    changeInNonreptShortAll: int
    pctOfOpenInterestAll: float
    pctOfOiNoncommLongAll: float
    pctOfOiNoncommShortAll: float
    pctOfOiNoncommSpreadAll: float
    pctOfOiCommLongAll: float
    pctOfOiCommShortAll: float
    pctOfOiTotReptLongAll: float
    pctOfOiTotReptShortAll: float
    pctOfOiNonreptLongAll: float
    pctOfOiNonreptShortAll: float
    pctOfOpenInterestOl: float
    pctOfOiNoncommLongOl: float
    pctOfOiNoncommShortOl: float
    pctOfOiNoncommSpreadOl: float
    pctOfOiCommLongOl: float
    pctOfOiCommShortOl: float
    pctOfOiTotReptLongOl: float
    pctOfOiTotReptShortOl: float
    pctOfOiNonreptLongOl: float
    pctOfOiNonreptShortOl: float
    pctOfOpenInterestOther: float
    pctOfOiNoncommLongOther: float
    pctOfOiNoncommShortOther: float
    pctOfOiNoncommSpreadOther: float
    pctOfOiCommLongOther: float
    pctOfOiCommShortOther: float
    pctOfOiTotReptLongOther: float
    pctOfOiTotReptShortOther: float
    pctOfOiNonreptLongOther: float
    pctOfOiNonreptShortOther: float
    tradersTotAll: int
    tradersNoncommLongAll: int
    tradersNoncommShortAll: int
    tradersNoncommSpreadAll: int
    tradersCommLongAll: int
    tradersCommShortAll: int
    tradersTotReptLongAll: int
    tradersTotReptShortAll: int
    tradersTotOl: int
    tradersNoncommLongOl: int
    tradersNoncommShortOl: int
    tradersNoncommSpeadOl: int
    tradersCommLongOl: int
    tradersCommShortOl: int
    tradersTotReptLongOl: int
    tradersTotReptShortOl: int
    tradersTotOther: int
    tradersNoncommLongOther: int
    tradersNoncommShortOther: int
    tradersNoncommSpreadOther: int
    tradersCommLongOther: int
    tradersCommShortOther: int
    tradersTotReptLongOther: int
    tradersTotReptShortOther: int
    concGrossLe4TdrLongAll: float
    concGrossLe4TdrShortAll: float
    concGrossLe8TdrLongAll: float
    concGrossLe8TdrShortAll: float
    concNetLe4TdrLongAll: float
    concNetLe4TdrShortAll: float
    concNetLe8TdrLongAll: float
    concNetLe8TdrShortAll: float
    concGrossLe4TdrLongOl: float
    concGrossLe4TdrShortOl: float
    concGrossLe8TdrLongOl: float
    concGrossLe8TdrShortOl: float
    concNetLe4TdrLongOl: float
    concNetLe4TdrShortOl: float
    concNetLe8TdrLongOl: float
    concNetLe8TdrShortOl: float
    concGrossLe4TdrLongOther: float
    concGrossLe4TdrShortOther: float
    concGrossLe8TdrLongOther: float
    concGrossLe8TdrShortOther: float
    concNetLe4TdrLongOther: float
    concNetLe4TdrShortOther: float
    concNetLe8TdrLongOther: float
    concNetLe8TdrShortOther: float
    contractUnits: str


class CommitmentOfTradersAnalysisResult(TypedDict):
    symbol: str
    date: str
    name: str
    sector: str
    exchange: str
    currentLongMarketSituation: float
    currentShortMarketSituation: float
    marketSituation: str
    previousLongMarketSituation: float
    previousShortMarketSituation: float
    previousMarketSituation: str
    netPostion: int  # Verbatim from FMP's documented example — not our typo to fix.
    previousNetPosition: int
    changeInNetPosition: float
    marketSentiment: str
    reversalTrend: bool


class CommitmentOfTradersListResult(TypedDict):
    symbol: str
    name: str
