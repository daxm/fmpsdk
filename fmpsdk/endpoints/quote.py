"""client.quote — Real-time and aftermarket quotes, single and batch. 16
methods. ``quote``, ``quote_short``, ``batch_index_quotes``,
``batch_commodity_quotes``, ``batch_crypto_quotes``, and
``batch_forex_quotes`` are also reachable from ``client.indexes``/
``client.commodity``/``client.crypto``/``client.forex`` respectively.

The 5 single-symbol methods (``quote``, ``quote_short``,
``aftermarket_quote``, ``aftermarket_trade``, ``stock_price_change``)
work on the free tier. ``batch_quote``, ``batch_quote_short``,
``batch_aftermarket_quote``, and ``batch_aftermarket_trade`` require an
FMP Starter-tier plan or higher. The remaining 7 ``batch_*`` methods
(``batch_exchange_quote`` and the 6 whole-asset-class ones —
``batch_etf_quotes``, ``batch_mutualfund_quotes``,
``batch_commodity_quotes``, ``batch_crypto_quotes``,
``batch_forex_quotes``, ``batch_index_quotes``) require an FMP
Ultimate-tier plan (402 on free, Starter, and Premium; confirmed
working on Ultimate 2026-08-24).
"""

from __future__ import annotations

from typing import cast

from ..types import (
    AftermarketQuoteResult,
    AftermarketTradeResult,
    QuoteResult,
    QuoteShortResult,
    StockPriceChangeResult,
)


class QuoteEndpoints:
    """Mixed into :class:`fmpsdk.client.Client`. Each method issues one GET
    against its ``stable/`` path via ``self._get`` (defined on ``Client``).
    """

    def quote(self, symbol: str) -> list[QuoteResult]:
        """``GET quote`` — full real-time quote for one symbol (equity,
        index, commodity, crypto, or forex pair — the path is generic).

        :param symbol: ticker symbol, e.g. ``"AAPL"`` or ``"^VIX"``.
        """
        return cast("list[QuoteResult]", self._get("quote", {"symbol": symbol}))

    def quote_short(self, symbol: str) -> list[QuoteShortResult]:
        """``GET quote-short`` — condensed real-time quote (price, change,
        volume only) for one symbol.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        """
        return cast(
            "list[QuoteShortResult]", self._get("quote-short", {"symbol": symbol})
        )

    def aftermarket_quote(self, symbol: str) -> list[AftermarketQuoteResult]:
        """``GET aftermarket-quote`` — post-market bid/ask quote for one
        symbol.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        """
        return cast(
            "list[AftermarketQuoteResult]",
            self._get("aftermarket-quote", {"symbol": symbol}),
        )

    def aftermarket_trade(self, symbol: str) -> list[AftermarketTradeResult]:
        """``GET aftermarket-trade`` — post-market trade prints for one
        symbol.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        """
        return cast(
            "list[AftermarketTradeResult]",
            self._get("aftermarket-trade", {"symbol": symbol}),
        )

    def stock_price_change(self, symbol: str) -> list[StockPriceChangeResult]:
        """``GET stock-price-change`` — percentage price change over
        fixed lookback windows (1D through max) for one symbol.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        """
        return cast(
            "list[StockPriceChangeResult]",
            self._get("stock-price-change", {"symbol": symbol}),
        )

    def batch_quote(self, symbols: str) -> list[QuoteResult]:
        """``GET batch-quote`` — full real-time quotes for several
        symbols in one call.

        :param symbols: comma-separated ticker symbols, e.g. ``"AAPL,MSFT"``.
        """
        return cast("list[QuoteResult]", self._get("batch-quote", {"symbols": symbols}))

    def batch_quote_short(self, symbols: str) -> list[QuoteShortResult]:
        """``GET batch-quote-short`` — condensed real-time quotes for
        several symbols in one call.

        :param symbols: comma-separated ticker symbols, e.g. ``"AAPL,MSFT"``.
        """
        return cast(
            "list[QuoteShortResult]",
            self._get("batch-quote-short", {"symbols": symbols}),
        )

    def batch_aftermarket_quote(self, symbols: str) -> list[AftermarketQuoteResult]:
        """``GET batch-aftermarket-quote`` — post-market bid/ask quotes
        for several symbols in one call.

        :param symbols: comma-separated ticker symbols, e.g. ``"AAPL,MSFT"``.
        """
        return cast(
            "list[AftermarketQuoteResult]",
            self._get("batch-aftermarket-quote", {"symbols": symbols}),
        )

    def batch_aftermarket_trade(self, symbols: str) -> list[AftermarketTradeResult]:
        """``GET batch-aftermarket-trade`` — post-market trade prints for
        several symbols in one call.

        :param symbols: comma-separated ticker symbols, e.g. ``"AAPL,MSFT"``.
        """
        return cast(
            "list[AftermarketTradeResult]",
            self._get("batch-aftermarket-trade", {"symbols": symbols}),
        )

    def batch_exchange_quote(
        self, exchange: str, short: bool | None = None
    ) -> list[QuoteShortResult]:
        """``GET batch-exchange-quote`` — condensed quotes for every
        symbol listed on one exchange.

        :param exchange: exchange code, e.g. ``"NASDAQ"``.
        :param short: unused by the response shape today (already
            condensed) but accepted by FMP; passed through as documented.
        """
        return cast(
            "list[QuoteShortResult]",
            self._get("batch-exchange-quote", {"exchange": exchange, "short": short}),
        )

    def batch_etf_quotes(self, short: bool | None = None) -> list[QuoteShortResult]:
        """``GET batch-etf-quotes`` — condensed quotes for every ETF FMP
        tracks. No scope parameter — whole asset class.

        :param short: passed through as documented by FMP.
        """
        return cast(
            "list[QuoteShortResult]", self._get("batch-etf-quotes", {"short": short})
        )

    def batch_mutualfund_quotes(
        self, short: bool | None = None
    ) -> list[QuoteShortResult]:
        """``GET batch-mutualfund-quotes`` — condensed quotes for every
        mutual fund FMP tracks. No scope parameter — whole asset class.

        :param short: passed through as documented by FMP.
        """
        return cast(
            "list[QuoteShortResult]",
            self._get("batch-mutualfund-quotes", {"short": short}),
        )

    def batch_commodity_quotes(
        self, short: bool | None = None
    ) -> list[QuoteShortResult]:
        """``GET batch-commodity-quotes`` — condensed quotes for every
        commodity FMP tracks. No scope parameter — whole asset class.
        Also reachable from ``client.commodity``.

        :param short: passed through as documented by FMP.
        """
        return cast(
            "list[QuoteShortResult]",
            self._get("batch-commodity-quotes", {"short": short}),
        )

    def batch_crypto_quotes(self, short: bool | None = None) -> list[QuoteShortResult]:
        """``GET batch-crypto-quotes`` — condensed quotes for every
        cryptocurrency FMP tracks. No scope parameter — whole asset
        class. Also reachable from ``client.crypto``.

        :param short: passed through as documented by FMP.
        """
        return cast(
            "list[QuoteShortResult]",
            self._get("batch-crypto-quotes", {"short": short}),
        )

    def batch_forex_quotes(self, short: bool | None = None) -> list[QuoteShortResult]:
        """``GET batch-forex-quotes`` — condensed quotes for every
        currency pair FMP tracks. No scope parameter — whole asset
        class. Also reachable from ``client.forex``.

        :param short: passed through as documented by FMP.
        """
        return cast(
            "list[QuoteShortResult]", self._get("batch-forex-quotes", {"short": short})
        )

    def batch_index_quotes(self, short: bool | None = None) -> list[QuoteShortResult]:
        """``GET batch-index-quotes`` — condensed quotes for every stock
        market index FMP tracks. No scope parameter — whole asset
        class. Also reachable from ``client.indexes``.

        :param short: passed through as documented by FMP.
        """
        return cast(
            "list[QuoteShortResult]", self._get("batch-index-quotes", {"short": short})
        )
