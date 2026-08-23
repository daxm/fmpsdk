"""client.news — News, press releases, and FMP editorial articles
(REWRITE_ARCHITECTURE.md §6, ``client.news``). 10 canonical methods, no
cross-listings. 9 of the 10 share one response shape (``NewsArticleResult``)
— see ``types.py`` for which.
"""

from __future__ import annotations

from typing import cast

from ..types import FmpArticlesResult, NewsArticleResult


class NewsEndpoints:
    """Mixed into :class:`fmpsdk.client.Client`. Each method issues one GET
    against its ``stable/`` path via ``self._get`` (defined on ``Client``).
    """

    def fmp_articles(
        self, page: int | None = None, limit: int | None = None
    ) -> list[FmpArticlesResult]:
        """``GET fmp-articles`` — FMP's own editorial articles, most
        recent first.

        :param page: zero-indexed page number.
        :param limit: max results per page.
        """
        return cast(
            "list[FmpArticlesResult]",
            self._get("fmp-articles", {"page": page, "limit": limit}),
        )

    def news_general_latest(
        self,
        from_: str | None = None,
        to: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> list[NewsArticleResult]:
        """``GET news/general-latest`` — most recent general news
        articles across all sources, market-wide.

        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        :param page: zero-indexed page number.
        :param limit: max results per page.
        """
        return cast(
            "list[NewsArticleResult]",
            self._get(
                "news/general-latest",
                {"from": from_, "to": to, "page": page, "limit": limit},
            ),
        )

    def news_press_releases(
        self,
        symbols: str,
        from_: str | None = None,
        to: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> list[NewsArticleResult]:
        """``GET news/press-releases`` — official company press releases
        for one or more symbols.

        :param symbols: comma-separated ticker symbols, e.g. ``"AAPL"``.
        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        :param page: zero-indexed page number.
        :param limit: max results per page.
        """
        return cast(
            "list[NewsArticleResult]",
            self._get(
                "news/press-releases",
                {
                    "symbols": symbols,
                    "from": from_,
                    "to": to,
                    "page": page,
                    "limit": limit,
                },
            ),
        )

    def news_press_releases_latest(
        self,
        from_: str | None = None,
        to: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> list[NewsArticleResult]:
        """``GET news/press-releases-latest`` — most recent company press
        releases across all companies, market-wide.

        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        :param page: zero-indexed page number.
        :param limit: max results per page.
        """
        return cast(
            "list[NewsArticleResult]",
            self._get(
                "news/press-releases-latest",
                {"from": from_, "to": to, "page": page, "limit": limit},
            ),
        )

    def news_stock(
        self,
        symbols: str,
        from_: str | None = None,
        to: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> list[NewsArticleResult]:
        """``GET news/stock`` — stock market news for one or more symbols.

        :param symbols: comma-separated ticker symbols, e.g. ``"AAPL"``.
        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        :param page: zero-indexed page number.
        :param limit: max results per page.
        """
        return cast(
            "list[NewsArticleResult]",
            self._get(
                "news/stock",
                {
                    "symbols": symbols,
                    "from": from_,
                    "to": to,
                    "page": page,
                    "limit": limit,
                },
            ),
        )

    def news_stock_latest(
        self,
        from_: str | None = None,
        to: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> list[NewsArticleResult]:
        """``GET news/stock-latest`` — most recent stock market news
        across all companies, market-wide.

        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        :param page: zero-indexed page number.
        :param limit: max results per page.
        """
        return cast(
            "list[NewsArticleResult]",
            self._get(
                "news/stock-latest",
                {"from": from_, "to": to, "page": page, "limit": limit},
            ),
        )

    def news_crypto(
        self,
        symbols: str,
        from_: str | None = None,
        to: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> list[NewsArticleResult]:
        """``GET news/crypto`` — cryptocurrency news for one or more
        symbols.

        :param symbols: comma-separated crypto symbols, e.g. ``"BTCUSD"``.
        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        :param page: zero-indexed page number.
        :param limit: max results per page.
        """
        return cast(
            "list[NewsArticleResult]",
            self._get(
                "news/crypto",
                {
                    "symbols": symbols,
                    "from": from_,
                    "to": to,
                    "page": page,
                    "limit": limit,
                },
            ),
        )

    def news_crypto_latest(
        self,
        from_: str | None = None,
        to: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> list[NewsArticleResult]:
        """``GET news/crypto-latest`` — most recent cryptocurrency news
        across all coins, market-wide.

        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        :param page: zero-indexed page number.
        :param limit: max results per page.
        """
        return cast(
            "list[NewsArticleResult]",
            self._get(
                "news/crypto-latest",
                {"from": from_, "to": to, "page": page, "limit": limit},
            ),
        )

    def news_forex(
        self,
        symbols: str,
        from_: str | None = None,
        to: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> list[NewsArticleResult]:
        """``GET news/forex`` — foreign-exchange news for one or more
        currency pairs.

        :param symbols: comma-separated currency pairs, e.g. ``"EURUSD"``.
        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        :param page: zero-indexed page number.
        :param limit: max results per page.
        """
        return cast(
            "list[NewsArticleResult]",
            self._get(
                "news/forex",
                {
                    "symbols": symbols,
                    "from": from_,
                    "to": to,
                    "page": page,
                    "limit": limit,
                },
            ),
        )

    def news_forex_latest(
        self,
        from_: str | None = None,
        to: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> list[NewsArticleResult]:
        """``GET news/forex-latest`` — most recent foreign-exchange news
        across all pairs, market-wide.

        :param from_: start date, ``YYYY-MM-DD`` (``from`` is a Python keyword).
        :param to: end date, ``YYYY-MM-DD``.
        :param page: zero-indexed page number.
        :param limit: max results per page.
        """
        return cast(
            "list[NewsArticleResult]",
            self._get(
                "news/forex-latest",
                {"from": from_, "to": to, "page": page, "limit": limit},
            ),
        )
