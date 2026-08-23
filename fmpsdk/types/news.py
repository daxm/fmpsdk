"""Response shapes returned by ``client.news`` methods."""

from __future__ import annotations

from typing import TypedDict

# --- client.news ------------------------------------------------------------


class FmpArticlesResult(TypedDict):
    """One of FMP's own editorial articles. Returned by
    `fmp_articles()`."""

    title: str
    date: str
    content: str
    tickers: str
    image: str
    link: str
    author: str
    site: str


class NewsArticleResult(TypedDict):
    """Shape shared by all 9 remaining `client.news` methods
    (`news_general_latest`, `news_press_releases`/`_latest`,
    `news_stock`/`_latest`, `news_crypto`/`_latest`, `news_forex`/
    `_latest`) — identical fields in every documented example; the
    `symbols*`-taking "search" variants and their "-latest" siblings
    answer the same question (a news article) at different scope
    (one symbol vs. market-wide)."""

    symbol: str | None
    publishedDate: str
    publisher: str
    title: str
    image: str
    site: str
    text: str
    url: str
