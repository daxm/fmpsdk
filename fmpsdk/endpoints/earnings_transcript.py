"""client.earnings_transcript — Earnings-call transcripts and their
availability metadata. 4 methods. ``earnings_transcript_list`` is also
reachable as ``client.directory.earnings_transcript_list``. Requires an
FMP Ultimate-tier plan — every method here 402s on the free tier.
"""

from __future__ import annotations

from typing import cast

from ..types import (
    EarningCallTranscriptDatesResult,
    EarningCallTranscriptLatestResult,
    EarningCallTranscriptResult,
    EarningsTranscriptListResult,
)


class EarningsTranscriptEndpoints:
    """Mixed into :class:`fmpsdk.client.Client`. Each method issues one GET
    against its ``stable/`` path via ``self._get`` (defined on ``Client``).
    """

    def earning_call_transcript(
        self, symbol: str, year: str, quarter: str, limit: int | None = None
    ) -> list[EarningCallTranscriptResult]:
        """``GET earning-call-transcript`` — full text of one company's
        earnings call for one fiscal quarter.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        :param year: fiscal year, e.g. ``"2020"``.
        :param quarter: fiscal quarter, e.g. ``"3"``.
        :param limit: max results to return.
        """
        return cast(
            "list[EarningCallTranscriptResult]",
            self._get(
                "earning-call-transcript",
                {"symbol": symbol, "year": year, "quarter": quarter, "limit": limit},
            ),
        )

    def earning_call_transcript_dates(
        self, symbol: str
    ) -> list[EarningCallTranscriptDatesResult]:
        """``GET earning-call-transcript-dates`` — every fiscal
        year/quarter one company has an earnings-call transcript on file
        for.

        :param symbol: ticker symbol, e.g. ``"AAPL"``.
        """
        return cast(
            "list[EarningCallTranscriptDatesResult]",
            self._get("earning-call-transcript-dates", {"symbol": symbol}),
        )

    def earning_call_transcript_latest(
        self, limit: int | None = None, page: int | None = None
    ) -> list[EarningCallTranscriptLatestResult]:
        """``GET earning-call-transcript-latest`` — most recent
        earnings-call transcripts across all companies, paginated.

        :param limit: max results per page.
        :param page: zero-indexed page number.
        """
        return cast(
            "list[EarningCallTranscriptLatestResult]",
            self._get("earning-call-transcript-latest", {"limit": limit, "page": page}),
        )

    def earnings_transcript_list(self) -> list[EarningsTranscriptListResult]:
        """``GET earnings-transcript-list`` — every company with at least
        one earnings-call transcript on file, with the transcript count.
        No parameters."""
        return cast(
            "list[EarningsTranscriptListResult]",
            self._get("earnings-transcript-list", {}),
        )
