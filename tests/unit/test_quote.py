"""Mocked unit tests for client.quote — mirrors fmpsdk/endpoints/quote.py."""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.unit

BASE = "https://financialmodelingprep.com/stable/"

_QUOTE_ROW = {
    "symbol": "AAPL",
    "name": "Apple Inc.",
    "price": 230.5,
    "changePercentage": 1.2,
    "change": 2.75,
    "volume": 45000000,
    "dayLow": 227.1,
    "dayHigh": 231.0,
    "yearHigh": 240.0,
    "yearLow": 165.0,
    "marketCap": 3500000000000.0,
    "priceAvg50": 225.0,
    "priceAvg200": 210.0,
    "exchange": "NASDAQ",
    "open": 228.0,
    "previousClose": 227.75,
    "timestamp": 1755700000,
}

_QUOTE_SHORT_ROW = {
    "symbol": "AAPL",
    "price": 230.5,
    "change": 2.75,
    "volume": 45000000,
}

_AFTERMARKET_QUOTE_ROW = {
    "symbol": "AAPL",
    "bidSize": 100,
    "bidPrice": 230.4,
    "askSize": 100,
    "askPrice": 230.6,
    "volume": 12000,
    "timestamp": 1755700000,
}

_AFTERMARKET_TRADE_ROW = {
    "symbol": "AAPL",
    "price": 230.5,
    "tradeSize": 50,
    "timestamp": 1755700000,
}

_PRICE_CHANGE_ROW = {
    "symbol": "AAPL",
    "1D": 1.2,
    "5D": 2.5,
    "1M": 4.1,
    "3M": 8.0,
    "6M": 15.0,
    "ytd": 20.0,
    "1Y": 22.0,
    "3Y": 60.0,
    "5Y": 150.0,
    "10Y": 400.0,
    "max": 1000.0,
}


def test_quote(client, requests_mock):
    requests_mock.get(BASE + "quote", json=[_QUOTE_ROW])
    # client.quote is the QuoteGroup namespace (attach_groups shadows the
    # mixed-in `quote` method with it for this one name) — the method
    # itself is client.quote.quote, per groups.py's own docstring example.
    result = client.quote.quote(symbol="AAPL")
    assert result[0]["price"] == 230.5
    assert requests_mock.last_request.qs["symbol"] == ["aapl"]


def test_quote_short(client, requests_mock):
    requests_mock.get(BASE + "quote-short", json=[_QUOTE_SHORT_ROW])
    result = client.quote_short(symbol="AAPL")
    assert result[0]["price"] == 230.5


def test_aftermarket_quote(client, requests_mock):
    requests_mock.get(BASE + "aftermarket-quote", json=[_AFTERMARKET_QUOTE_ROW])
    result = client.aftermarket_quote(symbol="AAPL")
    assert result[0]["bidPrice"] == 230.4


def test_aftermarket_trade(client, requests_mock):
    requests_mock.get(BASE + "aftermarket-trade", json=[_AFTERMARKET_TRADE_ROW])
    result = client.aftermarket_trade(symbol="AAPL")
    assert result[0]["tradeSize"] == 50


def test_stock_price_change(client, requests_mock):
    requests_mock.get(BASE + "stock-price-change", json=[_PRICE_CHANGE_ROW])
    result = client.stock_price_change(symbol="AAPL")
    assert result[0]["ytd"] == 20.0


def test_batch_quote(client, requests_mock):
    requests_mock.get(BASE + "batch-quote", json=[_QUOTE_ROW])
    result = client.batch_quote(symbols="AAPL,MSFT")
    assert result[0]["symbol"] == "AAPL"
    assert requests_mock.last_request.qs["symbols"] == ["aapl,msft"]


def test_batch_quote_short(client, requests_mock):
    requests_mock.get(BASE + "batch-quote-short", json=[_QUOTE_SHORT_ROW])
    result = client.batch_quote_short(symbols="AAPL,MSFT")
    assert result[0]["volume"] == 45000000


def test_batch_aftermarket_quote(client, requests_mock):
    requests_mock.get(BASE + "batch-aftermarket-quote", json=[_AFTERMARKET_QUOTE_ROW])
    result = client.batch_aftermarket_quote(symbols="AAPL,MSFT")
    assert result[0]["askPrice"] == 230.6


def test_batch_aftermarket_trade(client, requests_mock):
    requests_mock.get(BASE + "batch-aftermarket-trade", json=[_AFTERMARKET_TRADE_ROW])
    result = client.batch_aftermarket_trade(symbols="AAPL,MSFT")
    assert result[0]["price"] == 230.5


def test_batch_exchange_quote(client, requests_mock):
    requests_mock.get(BASE + "batch-exchange-quote", json=[_QUOTE_SHORT_ROW])
    result = client.batch_exchange_quote(exchange="NASDAQ")
    assert result[0]["symbol"] == "AAPL"
    assert requests_mock.last_request.qs["exchange"] == ["nasdaq"]


def test_batch_etf_quotes(client, requests_mock):
    requests_mock.get(BASE + "batch-etf-quotes", json=[_QUOTE_SHORT_ROW])
    result = client.batch_etf_quotes()
    assert result[0]["symbol"] == "AAPL"
    assert requests_mock.last_request.qs == {}


def test_batch_mutualfund_quotes(client, requests_mock):
    requests_mock.get(BASE + "batch-mutualfund-quotes", json=[_QUOTE_SHORT_ROW])
    result = client.batch_mutualfund_quotes()
    assert result[0]["change"] == 2.75


def test_batch_commodity_quotes(client, requests_mock):
    requests_mock.get(BASE + "batch-commodity-quotes", json=[_QUOTE_SHORT_ROW])
    result = client.batch_commodity_quotes()
    assert result[0]["symbol"] == "AAPL"


def test_batch_crypto_quotes(client, requests_mock):
    requests_mock.get(BASE + "batch-crypto-quotes", json=[_QUOTE_SHORT_ROW])
    result = client.batch_crypto_quotes()
    assert result[0]["symbol"] == "AAPL"


def test_batch_forex_quotes(client, requests_mock):
    requests_mock.get(BASE + "batch-forex-quotes", json=[_QUOTE_SHORT_ROW])
    result = client.batch_forex_quotes()
    assert result[0]["symbol"] == "AAPL"


def test_batch_index_quotes(client, requests_mock):
    requests_mock.get(BASE + "batch-index-quotes", json=[_QUOTE_SHORT_ROW])
    result = client.batch_index_quotes()
    assert result[0]["symbol"] == "AAPL"
