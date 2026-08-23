"""TypedDicts for ``client.news`` response shapes (REWRITE_ARCHITECTURE.md §6, ``client.news``).

Split out of the former single ``types.py`` for size — see
``fmpsdk/types/__init__.py`` for the shared conventions (naming,
when shapes are/aren't reused, the functional-TypedDict-form cases)
and the re-export barrel that keeps ``from fmpsdk.types import X``
working unchanged for every caller.
"""

from __future__ import annotations

from typing import TypedDict

# --- client.news ------------------------------------------------------------


class FmpArticlesResult(TypedDict):
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
