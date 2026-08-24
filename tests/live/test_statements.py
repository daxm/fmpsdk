"""Live tests for client.statements against the real FMP API — the subset
of the group actually reachable on the free tier. One fixed cheap call
per method, per the rewrite's live-testing discipline.

income_statement_ttm, balance_sheet_statement_ttm, cash_flow_statement_ttm,
and latest_financial_statements 402 on the free tier — see
tests/ultimate/test_statements.py.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.live


def test_income_statement(live_client):
    result = live_client.income_statement(symbol="AAPL", limit=1)
    assert result[0]["symbol"] == "AAPL"


def test_income_statement_as_reported(live_client):
    result = live_client.income_statement_as_reported(symbol="AAPL", period="annual")
    assert result[0]["symbol"] == "AAPL"


def test_income_statement_growth(live_client):
    result = live_client.income_statement_growth(symbol="AAPL", limit=1)
    assert result[0]["symbol"] == "AAPL"


def test_balance_sheet_statement(live_client):
    result = live_client.balance_sheet_statement(symbol="AAPL", limit=1)
    assert result[0]["symbol"] == "AAPL"


def test_balance_sheet_statement_as_reported(live_client):
    result = live_client.balance_sheet_statement_as_reported(
        symbol="AAPL", period="annual"
    )
    assert result[0]["symbol"] == "AAPL"


def test_balance_sheet_statement_growth(live_client):
    result = live_client.balance_sheet_statement_growth(symbol="AAPL", limit=1)
    assert result[0]["symbol"] == "AAPL"


def test_cash_flow_statement(live_client):
    result = live_client.cash_flow_statement(symbol="AAPL", limit=1)
    assert result[0]["symbol"] == "AAPL"


def test_cash_flow_statement_as_reported(live_client):
    result = live_client.cash_flow_statement_as_reported(symbol="AAPL", period="annual")
    assert result[0]["symbol"] == "AAPL"


def test_cash_flow_statement_growth(live_client):
    result = live_client.cash_flow_statement_growth(symbol="AAPL", limit=1)
    assert result[0]["symbol"] == "AAPL"


def test_financial_statement_full_as_reported(live_client):
    result = live_client.financial_statement_full_as_reported(
        symbol="AAPL", period="annual"
    )
    assert result[0]["symbol"] == "AAPL"


def test_key_metrics(live_client):
    result = live_client.key_metrics(symbol="AAPL", limit=1)
    assert result[0]["symbol"] == "AAPL"


def test_key_metrics_ttm(live_client):
    result = live_client.key_metrics_ttm(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"


def test_ratios(live_client):
    result = live_client.ratios(symbol="AAPL", limit=1)
    assert result[0]["symbol"] == "AAPL"


def test_ratios_ttm(live_client):
    result = live_client.ratios_ttm(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"


def test_financial_scores(live_client):
    result = live_client.financial_scores(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"


def test_owner_earnings(live_client):
    result = live_client.owner_earnings(symbol="AAPL", limit=1)
    assert result[0]["symbol"] == "AAPL"


def test_enterprise_values(live_client):
    result = live_client.enterprise_values(symbol="AAPL", limit=1)
    assert result[0]["symbol"] == "AAPL"


def test_financial_growth(live_client):
    result = live_client.financial_growth(symbol="AAPL", limit=1)
    assert result[0]["symbol"] == "AAPL"


def test_financial_reports_dates(live_client):
    result = live_client.financial_reports_dates(symbol="AAPL")
    assert len(result) > 0
    assert "fiscalYear" in result[0]


def test_financial_reports_json(live_client):
    # Not array-wrapped in the real response, unlike everything else in
    # the catalog — verified live, contradicting FMP's own docs (§8.4).
    result = live_client.financial_reports_json(symbol="AAPL", year="2022", period="FY")
    assert result["symbol"] == "AAPL"
    assert "Cover Page" in result


def test_financial_reports_xlsx(live_client):
    result = live_client.financial_reports_xlsx(symbol="AAPL", year="2022", period="FY")
    assert isinstance(result, bytes)
    assert result[:4] == b"PK\x03\x04"


def test_revenue_product_segmentation(live_client):
    result = live_client.revenue_product_segmentation(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"


def test_revenue_geographic_segmentation(live_client):
    result = live_client.revenue_geographic_segmentation(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"


def test_income_statement_ttm(live_client):
    result = live_client.income_statement_ttm(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"


def test_balance_sheet_statement_ttm(live_client):
    result = live_client.balance_sheet_statement_ttm(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"


def test_cash_flow_statement_ttm(live_client):
    result = live_client.cash_flow_statement_ttm(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"


def test_latest_financial_statements(live_client):
    result = live_client.latest_financial_statements(page=0, limit=10)
    assert len(result) > 0
    assert "symbol" in result[0]
