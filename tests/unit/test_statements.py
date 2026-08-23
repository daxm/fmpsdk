"""Mocked unit tests for client.statements — mirrors
fmpsdk/endpoints/statements.py.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.unit

BASE = "https://financialmodelingprep.com/stable/"

_INCOME_STATEMENT_JSON = {
    "date": "2025-09-27",
    "symbol": "AAPL",
    "reportedCurrency": "USD",
    "cik": "0000320193",
    "filingDate": "2025-10-31",
    "acceptedDate": "2025-10-31 06:01:26",
    "fiscalYear": "2025",
    "period": "FY",
    "revenue": 416161000000,
    "netIncome": 112010000000,
    "eps": 7.49,
}

_BALANCE_SHEET_JSON = {
    "date": "2025-09-27",
    "symbol": "AAPL",
    "reportedCurrency": "USD",
    "fiscalYear": "2025",
    "period": "FY",
    "totalAssets": 359241000000,
    "totalLiabilities": 285508000000,
}

_CASH_FLOW_JSON = {
    "date": "2025-09-27",
    "symbol": "AAPL",
    "reportedCurrency": "USD",
    "fiscalYear": "2025",
    "period": "FY",
    "netIncome": 112010000000,
    "freeCashFlow": 98767000000,
}


def test_income_statement(client, requests_mock):
    requests_mock.get(BASE + "income-statement", json=[_INCOME_STATEMENT_JSON])
    result = client.income_statement(symbol="AAPL", limit=5, period="FY")
    assert result[0]["revenue"] == 416161000000
    sent = requests_mock.last_request.qs
    assert sent["symbol"] == ["aapl"]
    assert sent["limit"] == ["5"]
    assert sent["period"] == ["fy"]


def test_income_statement_omits_unset_optional_params(client, requests_mock):
    requests_mock.get(BASE + "income-statement", json=[])
    client.income_statement(symbol="AAPL")
    sent = requests_mock.last_request.qs
    assert "limit" not in sent
    assert "period" not in sent


def test_income_statement_ttm(client, requests_mock):
    requests_mock.get(BASE + "income-statement-ttm", json=[_INCOME_STATEMENT_JSON])
    result = client.income_statement_ttm(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"


def test_income_statement_as_reported(client, requests_mock):
    requests_mock.get(
        BASE + "income-statement-as-reported",
        json=[
            {
                "symbol": "AAPL",
                "fiscalYear": 2025,
                "period": "FY",
                "reportedCurrency": "USD",
                "date": "2025-09-26",
                "data": {"revenuefromcontractwithcustomerexcludingassessedtax": 416161000000},
            }
        ],
    )
    result = client.income_statement_as_reported(symbol="AAPL", period="annual")
    assert result[0]["data"]["revenuefromcontractwithcustomerexcludingassessedtax"] == 416161000000
    assert requests_mock.last_request.qs["period"] == ["annual"]


def test_income_statement_growth(client, requests_mock):
    requests_mock.get(
        BASE + "income-statement-growth",
        json=[{"symbol": "AAPL", "date": "2025-09-27", "fiscalYear": "2025", "period": "FY", "reportedCurrency": "USD", "growthRevenue": 0.064}],
    )
    result = client.income_statement_growth(symbol="AAPL")
    assert result[0]["growthRevenue"] == 0.064


def test_balance_sheet_statement(client, requests_mock):
    requests_mock.get(BASE + "balance-sheet-statement", json=[_BALANCE_SHEET_JSON])
    result = client.balance_sheet_statement(symbol="AAPL", limit=5, period="FY")
    assert result[0]["totalAssets"] == 359241000000


def test_balance_sheet_statement_ttm(client, requests_mock):
    requests_mock.get(BASE + "balance-sheet-statement-ttm", json=[_BALANCE_SHEET_JSON])
    result = client.balance_sheet_statement_ttm(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"


def test_balance_sheet_statement_as_reported(client, requests_mock):
    requests_mock.get(
        BASE + "balance-sheet-statement-as-reported",
        json=[
            {
                "symbol": "AAPL",
                "fiscalYear": 2025,
                "period": "FY",
                "reportedCurrency": "USD",
                "date": "2025-09-26",
                "data": {"assets": 359241000000},
            }
        ],
    )
    result = client.balance_sheet_statement_as_reported(symbol="AAPL", period="annual")
    assert result[0]["data"]["assets"] == 359241000000


def test_balance_sheet_statement_growth(client, requests_mock):
    requests_mock.get(
        BASE + "balance-sheet-statement-growth",
        json=[{"symbol": "AAPL", "date": "2025-09-27", "fiscalYear": "2025", "period": "FY", "reportedCurrency": "USD", "growthTotalAssets": -0.0157}],
    )
    result = client.balance_sheet_statement_growth(symbol="AAPL")
    assert result[0]["growthTotalAssets"] == -0.0157


def test_cash_flow_statement(client, requests_mock):
    requests_mock.get(BASE + "cash-flow-statement", json=[_CASH_FLOW_JSON])
    result = client.cash_flow_statement(symbol="AAPL", limit=5, period="FY")
    assert result[0]["freeCashFlow"] == 98767000000


def test_cash_flow_statement_ttm(client, requests_mock):
    requests_mock.get(BASE + "cash-flow-statement-ttm", json=[_CASH_FLOW_JSON])
    result = client.cash_flow_statement_ttm(symbol="AAPL")
    assert result[0]["symbol"] == "AAPL"


def test_cash_flow_statement_as_reported(client, requests_mock):
    requests_mock.get(
        BASE + "cash-flow-statement-as-reported",
        json=[
            {
                "symbol": "AAPL",
                "fiscalYear": 2025,
                "period": "FY",
                "reportedCurrency": "USD",
                "date": "2025-09-26",
                "data": {"netincomeloss": 112010000000},
            }
        ],
    )
    result = client.cash_flow_statement_as_reported(symbol="AAPL", period="annual")
    assert result[0]["data"]["netincomeloss"] == 112010000000


def test_cash_flow_statement_growth(client, requests_mock):
    requests_mock.get(
        BASE + "cash-flow-statement-growth",
        json=[{"symbol": "AAPL", "date": "2025-09-27", "fiscalYear": "2025", "period": "FY", "reportedCurrency": "USD", "growthFreeCashFlow": -0.092}],
    )
    result = client.cash_flow_statement_growth(symbol="AAPL")
    assert result[0]["growthFreeCashFlow"] == -0.092


def test_financial_statement_full_as_reported(client, requests_mock):
    requests_mock.get(
        BASE + "financial-statement-full-as-reported",
        json=[
            {
                "symbol": "AAPL",
                "fiscalYear": 2025,
                "period": "FY",
                "reportedCurrency": "USD",
                "date": "2025-09-26",
                "data": {"documenttype": "10-K", "documentannualreport": "true", "entityaddresspostalzipcode": 95014},
            }
        ],
    )
    result = client.financial_statement_full_as_reported(symbol="AAPL", period="annual")
    assert result[0]["data"]["documenttype"] == "10-K"


def test_latest_financial_statements(client, requests_mock):
    requests_mock.get(
        BASE + "latest-financial-statements",
        json=[{"symbol": "UFPI", "calendarYear": 2026, "period": "Q2", "date": "2026-06-27", "dateAdded": "2026-07-30 13:17:26"}],
    )
    result = client.latest_financial_statements(page=0, limit=250)
    assert result[0]["symbol"] == "UFPI"
    sent = requests_mock.last_request.qs
    assert sent["limit"] == ["250"]


def test_key_metrics(client, requests_mock):
    requests_mock.get(
        BASE + "key-metrics",
        json=[{"symbol": "AAPL", "date": "2025-09-27", "fiscalYear": "2025", "period": "FY", "reportedCurrency": "USD", "marketCap": 3818743810000, "returnOnEquity": 1.519}],
    )
    result = client.key_metrics(symbol="AAPL", limit=5, period="FY")
    assert result[0]["returnOnEquity"] == 1.519


def test_key_metrics_ttm(client, requests_mock):
    requests_mock.get(
        BASE + "key-metrics-ttm",
        json=[{"symbol": "AAPL", "marketCap": 4874072686740, "enterpriseValueTTM": 4922455686740}],
    )
    result = client.key_metrics_ttm(symbol="AAPL")
    assert result[0]["enterpriseValueTTM"] == 4922455686740


def test_ratios(client, requests_mock):
    requests_mock.get(
        BASE + "ratios",
        json=[{"symbol": "AAPL", "date": "2025-09-27", "fiscalYear": "2025", "period": "FY", "reportedCurrency": "USD", "currentRatio": 0.893}],
    )
    result = client.ratios(symbol="AAPL", limit=5, period="FY")
    assert result[0]["currentRatio"] == 0.893


def test_ratios_ttm(client, requests_mock):
    requests_mock.get(
        BASE + "ratios-ttm",
        json=[{"symbol": "AAPL", "currentRatioTTM": 1.070}],
    )
    result = client.ratios_ttm(symbol="AAPL")
    assert result[0]["currentRatioTTM"] == 1.070


def test_financial_scores(client, requests_mock):
    requests_mock.get(
        BASE + "financial-scores",
        json=[{"symbol": "AAPL", "reportedCurrency": "USD", "altmanZScore": 14.04, "piotroskiScore": 9, "workingCapital": 9473000000, "totalAssets": 371082000000, "retainedEarnings": 12359000000, "ebit": 147722000000, "marketCap": 5042169135511, "totalLiabilities": 264591000000, "revenue": 451442000000}],
    )
    result = client.financial_scores(symbol="AAPL")
    assert result[0]["piotroskiScore"] == 9


def test_owner_earnings(client, requests_mock):
    requests_mock.get(
        BASE + "owner-earnings",
        json=[{"symbol": "AAPL", "reportedCurrency": "USD", "fiscalYear": "2026", "period": "Q2", "date": "2026-03-28", "averagePPE": 0.13466, "maintenanceCapex": 159994500, "ownersEarnings": 28861994500, "growthCapex": -2130994500, "ownersEarningsPerShare": 1.95}],
    )
    result = client.owner_earnings(symbol="AAPL", limit=5)
    assert result[0]["ownersEarningsPerShare"] == 1.95


def test_enterprise_values(client, requests_mock):
    requests_mock.get(
        BASE + "enterprise-values",
        json=[{"symbol": "AAPL", "date": "2025-09-27", "stockPrice": 255.46, "numberOfShares": 14948500000, "marketCapitalization": 3818743810000, "minusCashAndCashEquivalents": 35934000000, "addTotalDebt": 112377000000, "enterpriseValue": 3895186810000}],
    )
    result = client.enterprise_values(symbol="AAPL", limit=5, period="FY")
    assert result[0]["enterpriseValue"] == 3895186810000


def test_financial_growth(client, requests_mock):
    requests_mock.get(
        BASE + "financial-growth",
        json=[{"symbol": "AAPL", "date": "2025-09-27", "fiscalYear": "2025", "period": "FY", "reportedCurrency": "USD", "revenueGrowth": 0.064}],
    )
    result = client.financial_growth(symbol="AAPL", limit=5, period="FY")
    assert result[0]["revenueGrowth"] == 0.064


def test_financial_reports_dates(client, requests_mock):
    requests_mock.get(
        BASE + "financial-reports-dates",
        json=[
            {
                "symbol": "AAPL",
                "fiscalYear": 2026,
                "period": "Q2",
                "linkJson": "https://financialmodelingprep.com/stable/financial-reports-json?symbol=AAPL&year=2026&period=Q2",
                "linkXlsx": "https://financialmodelingprep.com/stable/financial-reports-xlsx?symbol=AAPL&year=2026&period=Q2",
            }
        ],
    )
    result = client.financial_reports_dates(symbol="AAPL")
    assert result[0]["fiscalYear"] == 2026


def test_financial_reports_json(client, requests_mock):
    # Real FMP responses for this endpoint are a single bare object, not
    # array-wrapped like everything else in the catalog — verified live
    # (§8.4). The mock reflects the real shape, not the docs' example.
    requests_mock.get(
        BASE + "financial-reports-json",
        json={"symbol": "AAPL", "period": "FY", "year": "2022", "Cover Page": [{"items": ["Sep. 24, 2022"]}]},
    )
    result = client.financial_reports_json(symbol="AAPL", year="2022", period="FY")
    assert result["symbol"] == "AAPL"
    assert "Cover Page" in result
    sent = requests_mock.last_request.qs
    assert sent["year"] == ["2022"]
    assert sent["period"] == ["fy"]


def test_financial_reports_xlsx_returns_raw_bytes(client, requests_mock):
    # Real FMP responses for this endpoint are binary XLSX (ZIP-container)
    # despite an application/json content-type header — verified live
    # (§8.4). The mock exercises that _get_bytes bypasses JSON parsing
    # entirely rather than trying to reproduce the real content-type lie.
    xlsx_magic_bytes = b"PK\x03\x04" + b"\x00" * 20
    requests_mock.get(
        BASE + "financial-reports-xlsx",
        content=xlsx_magic_bytes,
        headers={"Content-Type": "application/json; charset=utf-8"},
    )
    result = client.financial_reports_xlsx(symbol="AAPL", year="2022", period="FY")
    assert isinstance(result, bytes)
    assert result.startswith(b"PK\x03\x04")


def test_revenue_product_segmentation(client, requests_mock):
    requests_mock.get(
        BASE + "revenue-product-segmentation",
        json=[
            {
                "symbol": "AAPL",
                "fiscalYear": 2025,
                "period": "FY",
                "reportedCurrency": "USD",
                "date": "2025-09-27",
                "data": {"iPhone": 209586000000, "Mac": 33708000000},
            }
        ],
    )
    result = client.revenue_product_segmentation(symbol="AAPL", period="annual", structure="flat")
    assert result[0]["data"]["iPhone"] == 209586000000
    assert requests_mock.last_request.qs["structure"] == ["flat"]


def test_revenue_geographic_segmentation(client, requests_mock):
    requests_mock.get(
        BASE + "revenue-geographic-segmentation",
        json=[
            {
                "symbol": "AAPL",
                "fiscalYear": 2025,
                "period": "FY",
                "reportedCurrency": "USD",
                "date": "2025-09-27",
                "data": {"Americas Segment": 178353000000},
            }
        ],
    )
    result = client.revenue_geographic_segmentation(symbol="AAPL")
    assert result[0]["data"]["Americas Segment"] == 178353000000
