"""Response shapes returned by ``client.quote`` methods."""

from __future__ import annotations

from typing import TypedDict

# --- client.quote ------------------------------------------------------------


class QuoteResult(TypedDict):
    """Shape shared by `quote` and `batch_quote` — identical fields."""

    symbol: str
    name: str
    price: float
    changePercentage: float
    change: float
    volume: int
    dayLow: float
    dayHigh: float
    yearHigh: float
    yearLow: float
    marketCap: float | None
    priceAvg50: float
    priceAvg200: float
    exchange: str
    open: float
    previousClose: float
    timestamp: int


class QuoteShortResult(TypedDict):
    """Condensed quote shape (price/change/volume only) shared by
    `quote_short` and every `batch_*` quote method: `batch_quote_short`,
    `batch_exchange_quote`, `batch_etf_quotes`, `batch_mutualfund_quotes`,
    `batch_commodity_quotes`, `batch_crypto_quotes`, `batch_forex_quotes`,
    `batch_index_quotes`."""

    symbol: str
    price: float
    change: float
    volume: int


class AftermarketTradeResult(TypedDict):
    """Shape shared by `aftermarket_trade` and `batch_aftermarket_trade`."""

    symbol: str
    price: float
    tradeSize: int
    timestamp: int


class AftermarketQuoteResult(TypedDict):
    """Shape shared by `aftermarket_quote` and `batch_aftermarket_quote`."""

    symbol: str
    bidSize: int
    bidPrice: float
    askSize: int
    askPrice: float
    volume: int
    timestamp: int


# Functional form, not class syntax: several fields (`1D`, `5D`, `1M`, `3M`,
# `6M`, `1Y`, `3Y`, `5Y`, `10Y`) start with a digit, which is not a legal
# Python identifier.
StockPriceChangeResult = TypedDict(
    "StockPriceChangeResult",
    {
        "symbol": str,
        "1D": float,
        "5D": float,
        "1M": float,
        "3M": float,
        "6M": float,
        "ytd": float,
        "1Y": float,
        "3Y": float,
        "5Y": float,
        "10Y": float,
        "max": float,
    },
)
