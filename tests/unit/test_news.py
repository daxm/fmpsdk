"""Mocked unit tests for client.news — mirrors fmpsdk/endpoints/news.py."""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.unit

BASE = "https://financialmodelingprep.com/stable/"

_ARTICLE_ROW = {
    "symbol": "AAPL",
    "publishedDate": "2026-08-20 09:00:00",
    "publisher": "Reuters",
    "title": "Apple announces new product",
    "image": "https://example.com/img.png",
    "site": "reuters.com",
    "text": "Apple today announced...",
    "url": "https://example.com/article",
}


def test_fmp_articles(client, requests_mock):
    requests_mock.get(
        BASE + "fmp-articles",
        json=[
            {
                "title": "Market wrap",
                "date": "2026-08-20",
                "content": "...",
                "tickers": "AAPL,MSFT",
                "image": "https://example.com/img.png",
                "link": "https://example.com/article",
                "author": "Jane Doe",
                "site": "financialmodelingprep.com",
            }
        ],
    )
    result = client.fmp_articles(page=0, limit=10)
    assert result[0]["title"] == "Market wrap"
    sent = requests_mock.last_request.qs
    assert sent["page"] == ["0"]
    assert sent["limit"] == ["10"]


def test_news_general_latest(client, requests_mock):
    requests_mock.get(BASE + "news/general-latest", json=[_ARTICLE_ROW])
    result = client.news_general_latest(from_="2026-08-01", to="2026-08-20")
    assert result[0]["publisher"] == "Reuters"
    sent = requests_mock.last_request.qs
    assert sent["from"] == ["2026-08-01"]
    assert sent["to"] == ["2026-08-20"]


def test_news_press_releases(client, requests_mock):
    requests_mock.get(BASE + "news/press-releases", json=[_ARTICLE_ROW])
    result = client.news_press_releases(symbols="AAPL")
    assert result[0]["symbol"] == "AAPL"
    assert requests_mock.last_request.qs["symbols"] == ["aapl"]


def test_news_press_releases_latest(client, requests_mock):
    requests_mock.get(BASE + "news/press-releases-latest", json=[_ARTICLE_ROW])
    result = client.news_press_releases_latest()
    assert result[0]["title"] == "Apple announces new product"
    assert requests_mock.last_request.qs == {}


def test_news_stock(client, requests_mock):
    requests_mock.get(BASE + "news/stock", json=[_ARTICLE_ROW])
    result = client.news_stock(symbols="AAPL")
    assert result[0]["symbol"] == "AAPL"
    assert requests_mock.last_request.qs["symbols"] == ["aapl"]


def test_news_stock_latest(client, requests_mock):
    requests_mock.get(BASE + "news/stock-latest", json=[_ARTICLE_ROW])
    result = client.news_stock_latest()
    assert result[0]["site"] == "reuters.com"
    assert requests_mock.last_request.qs == {}


def test_news_crypto(client, requests_mock):
    requests_mock.get(BASE + "news/crypto", json=[_ARTICLE_ROW])
    result = client.news_crypto(symbols="BTCUSD")
    assert result[0]["publisher"] == "Reuters"
    assert requests_mock.last_request.qs["symbols"] == ["btcusd"]


def test_news_crypto_latest(client, requests_mock):
    requests_mock.get(BASE + "news/crypto-latest", json=[_ARTICLE_ROW])
    result = client.news_crypto_latest()
    assert result[0]["url"] == "https://example.com/article"
    assert requests_mock.last_request.qs == {}


def test_news_forex(client, requests_mock):
    requests_mock.get(BASE + "news/forex", json=[_ARTICLE_ROW])
    result = client.news_forex(symbols="EURUSD")
    assert result[0]["publisher"] == "Reuters"
    assert requests_mock.last_request.qs["symbols"] == ["eurusd"]


def test_news_forex_latest(client, requests_mock):
    requests_mock.get(BASE + "news/forex-latest", json=[_ARTICLE_ROW])
    result = client.news_forex_latest()
    assert result[0]["text"] == "Apple today announced..."
    assert requests_mock.last_request.qs == {}
