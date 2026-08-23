"""Response shapes returned by ``client.tipranks`` methods."""

from __future__ import annotations

from typing import TypedDict


class TipranksRecommendationBreakdown(TypedDict):
    """Nested shape of the 3 summary types' ``recommendations`` field."""

    buy: int
    hold: int
    sell: int


class TipranksAnalystActionBreakdown(TypedDict):
    """Nested shape of the 3 summary types' ``analystAction`` field."""

    initiated: int
    maintained: int
    upgraded: int
    downgraded: int
    reiterated: int
    resumed: int


class TipranksRatingResult(TypedDict):
    symbol: str
    date: str
    recommendationDate: str
    expertUID: str
    analystName: str
    firmName: str
    recommendation: str
    analystAction: str
    articleTitle: str
    articleSite: str
    priceTarget: float | None
    priceTargetCurrency: str | None
    url: str


class TipranksPointInTimeResult(TypedDict):
    """Shape shared by `tipranks_pit_symbol` and `tipranks_pit_analyst` —
    same question (a point-in-time analyst rating snapshot) at different
    scope (one symbol's coverage panel vs. one analyst's book), identical
    fields in both documented examples."""

    symbol: str
    date: str
    expertUID: str
    analystName: str
    stockSuccessRate: float | None
    firmName: str
    lastRecommendation: str
    lastRecommendationDate: str
    articleTitle: str
    articleSite: str
    priceTarget: float | None
    priceTargetCurrency: str | None
    url: str
    lastAnalystAction: str
    stockReturn: float | None
    beatTarget: bool | None


# Functional form, not class syntax: all 3 summary shapes have a field
# literally named `from`, which collides with the Python keyword (same
# reason as `DividendResult` in types/calendar.py).
TipranksSymbolSummaryResult = TypedDict(
    "TipranksSymbolSummaryResult",
    {
        "symbol": str,
        "from": str,
        "to": str,
        "totalRecommendations": int,
        "distinctSymbols": int,
        "distinctAnalysts": int,
        "validPriceTargets": int,
        "recommendations": TipranksRecommendationBreakdown,
        "analystAction": TipranksAnalystActionBreakdown,
        "comparedPriceTargets": int,
        "beats": int,
        "misses": int,
        "averageReturn": float,
        "topReturn": float,
        "worstReturn": float,
    },
)


TipranksAnalystSummaryResult = TypedDict(
    "TipranksAnalystSummaryResult",
    {
        "expertUID": str,
        "from": str,
        "to": str,
        "totalRecommendations": int,
        "distinctSymbols": int,
        "distinctAnalysts": int,
        "validPriceTargets": int,
        "recommendations": TipranksRecommendationBreakdown,
        "analystAction": TipranksAnalystActionBreakdown,
        "comparedPriceTargets": int,
        "beats": int,
        "misses": int,
        "averageReturn": float,
        "topReturn": float,
        "worstReturn": float,
    },
)


TipranksFirmSummaryResult = TypedDict(
    "TipranksFirmSummaryResult",
    {
        "firmName": str,
        "from": str,
        "to": str,
        "totalRecommendations": int,
        "distinctSymbols": int,
        "distinctAnalysts": int,
        "validPriceTargets": int,
        "recommendations": TipranksRecommendationBreakdown,
        "analystAction": TipranksAnalystActionBreakdown,
        "comparedPriceTargets": int,
        "beats": int,
        "misses": int,
        "averageReturn": float,
        "topReturn": float,
        "worstReturn": float,
    },
)


class TipranksAnalystDirectoryResult(TypedDict):
    expertUID: str
    analystName: str
    firmName: str
    successRate: float
    excessReturn: float
    totalRecommendations: int
    goodRecommendations: int
    analystRank: int
    numOfStars: int
