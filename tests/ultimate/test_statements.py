"""Ultimate-tier (Bucket 2) live tests for client.statements.

Discovered live, not predicted by REWRITE_ARCHITECTURE.md's group
directory (which lists no Bucket 2 flag on `statements`): these 4 of 27
methods 402 on the free tier, while the other 23 work fine. Skipped by
default (`-m "not ultimate"` / excluded unless explicitly selected); run
for real only during a deliberately-timed FMP Ultimate month, per the
rewrite workflow.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.ultimate


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
