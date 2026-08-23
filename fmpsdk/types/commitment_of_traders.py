"""Response shapes returned by ``client.commitment_of_traders`` methods."""

from __future__ import annotations

from typing import TypedDict

# --- client.commitment_of_traders -----------------------------------------


class CommitmentOfTradersReportResult(TypedDict):
    """CFTC Commitment of Traders report, one row per market per date.
    ~140 fields, fully typed. Field names are verbatim from FMP's own
    response, including its `Spead`/`Spread` and `netPostion` typos —
    not corrected here, since fixing them would break parsing a real
    response."""

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
    """Derived sentiment analysis (bullish/bearish market situation, net
    position change, reversal-trend flag) built on top of the raw COT
    report. Returned by `commitment_of_traders_analysis()`."""

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
    """One symbol a COT report is available for. Returned by
    `commitment_of_traders_list()`."""

    symbol: str
    name: str
