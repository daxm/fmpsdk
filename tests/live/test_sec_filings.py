"""Live tests for client.sec_filings against the real FMP API. One
fixed cheap call per method. 10 of 12 are free-tier reachable;
`industry_classification_search` and `all_industry_classification` 402
on the free tier, confirmed live 2026-08-23 — see
`tests/ultimate/test_sec_filings.py`.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.live

_FROM = "2026-08-01"
_TO = "2026-08-20"


def test_sec_filings_8k(live_client):
    result = live_client.sec_filings_8k(from_=_FROM, to=_TO, limit=1)
    assert len(result) > 0
    assert "cik" in result[0]


def test_sec_filings_financials(live_client):
    result = live_client.sec_filings_financials(from_=_FROM, to=_TO, limit=1)
    assert len(result) > 0
    assert "cik" in result[0]


def test_sec_filings_search_form_type(live_client):
    result = live_client.sec_filings_search_form_type(
        form_type="8-K", from_=_FROM, to=_TO, limit=1
    )
    assert len(result) > 0
    assert "cik" in result[0]


def test_sec_filings_search_symbol(live_client):
    result = live_client.sec_filings_search_symbol(symbol="AAPL", from_=_FROM, to=_TO)
    assert isinstance(result, list)


def test_sec_filings_search_cik(live_client):
    result = live_client.sec_filings_search_cik(cik="0000320193", from_=_FROM, to=_TO)
    assert isinstance(result, list)


def test_sec_filings_company_search_name(live_client):
    result = live_client.sec_filings_company_search_name(company="Apple")
    assert len(result) > 0
    assert "cik" in result[0]


def test_sec_filings_company_search_symbol(live_client):
    result = live_client.sec_filings_company_search_symbol(symbol="AAPL")
    assert len(result) > 0
    assert result[0]["symbol"] == "AAPL"


def test_sec_filings_company_search_cik(live_client):
    result = live_client.sec_filings_company_search_cik(cik="0000320193")
    assert len(result) > 0
    assert result[0]["cik"] == "0000320193"


def test_sec_profile(live_client):
    result = live_client.sec_profile(symbol="AAPL")
    assert len(result) > 0
    assert result[0]["symbol"] == "AAPL"


def test_standard_industrial_classification_list(live_client):
    result = live_client.standard_industrial_classification_list(sic_code="7372")
    assert isinstance(result, list)
