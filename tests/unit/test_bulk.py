"""Mocked unit tests for client.bulk — mirrors fmpsdk/endpoints/bulk.py.

Response rows are trimmed to a few representative fields each — the
TypedDict cast isn't runtime-checked, so a full-fidelity mock buys
nothing a partial one doesn't. Per types/bulk.py's module docstring,
every field below is a JSON string in the real API except
`profile_bulk`'s.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.unit

BASE = "https://financialmodelingprep.com/stable/"


def test_profile_bulk(client, requests_mock):
    requests_mock.get(
        BASE + "profile-bulk",
        json=[{"symbol": "AAPL", "companyName": "Apple Inc.", "price": 230.5}],
    )
    result = client.profile_bulk(part="0")
    assert result[0]["symbol"] == "AAPL"
    assert requests_mock.last_request.qs["part"] == ["0"]


def test_rating_bulk(client, requests_mock):
    requests_mock.get(
        BASE + "rating-bulk",
        json=[
            {
                "symbol": "AAPL",
                "date": "2026-08-20",
                "rating": "A-",
                "discountedCashFlowScore": "5",
            }
        ],
    )
    result = client.rating_bulk()
    assert result[0]["rating"] == "A-"
    assert requests_mock.last_request.qs == {}


def test_dcf_bulk(client, requests_mock):
    requests_mock.get(
        BASE + "dcf-bulk",
        json=[
            {
                "symbol": "AAPL",
                "date": "2026-08-20",
                "dcf": "220.5",
                "Stock Price": "230.5",
            }
        ],
    )
    result = client.dcf_bulk()
    assert result[0]["dcf"] == "220.5"


def test_scores_bulk(client, requests_mock):
    requests_mock.get(
        BASE + "scores-bulk",
        json=[
            {
                "symbol": "AAPL",
                "reportedCurrency": "USD",
                "altmanZScore": "8.1",
                "piotroskiScore": "7",
            }
        ],
    )
    result = client.scores_bulk()
    assert result[0]["piotroskiScore"] == "7"


def test_price_target_summary_bulk(client, requests_mock):
    requests_mock.get(
        BASE + "price-target-summary-bulk",
        json=[
            {
                "symbol": "AAPL",
                "lastMonthCount": "5",
                "lastMonthAvgPriceTarget": "240.0",
            }
        ],
    )
    result = client.price_target_summary_bulk()
    assert result[0]["lastMonthCount"] == "5"


def test_etf_holder_bulk(client, requests_mock):
    requests_mock.get(
        BASE + "etf-holder-bulk",
        json=[
            {
                "symbol": "SPY",
                "name": "Apple Inc.",
                "sharesNumber": "12345",
                "lastUpdated": "2026-08-20",
            }
        ],
    )
    result = client.etf_holder_bulk(part="1")
    assert result[0]["name"] == "Apple Inc."
    assert requests_mock.last_request.qs["part"] == ["1"]


def test_upgrades_downgrades_consensus_bulk(client, requests_mock):
    requests_mock.get(
        BASE + "upgrades-downgrades-consensus-bulk",
        json=[{"symbol": "AAPL", "strongBuy": "10", "buy": "20", "consensus": "Buy"}],
    )
    result = client.upgrades_downgrades_consensus_bulk()
    assert result[0]["consensus"] == "Buy"


def test_key_metrics_ttm_bulk(client, requests_mock):
    requests_mock.get(
        BASE + "key-metrics-ttm-bulk",
        json=[
            {
                "symbol": "AAPL",
                "marketCap": "3500000000000",
                "enterpriseValueTTM": "3550000000000",
            }
        ],
    )
    result = client.key_metrics_ttm_bulk()
    assert result[0]["marketCap"] == "3500000000000"


def test_ratios_ttm_bulk(client, requests_mock):
    requests_mock.get(
        BASE + "ratios-ttm-bulk",
        json=[
            {"symbol": "AAPL", "grossProfitMarginTTM": "0.46", "currentRatioTTM": "1.1"}
        ],
    )
    result = client.ratios_ttm_bulk()
    assert result[0]["currentRatioTTM"] == "1.1"


def test_peers_bulk(client, requests_mock):
    requests_mock.get(
        BASE + "peers-bulk", json=[{"symbol": "AAPL", "peers": "MSFT,GOOG,AMZN"}]
    )
    result = client.peers_bulk()
    assert result[0]["peers"] == "MSFT,GOOG,AMZN"


def test_earnings_surprises_bulk(client, requests_mock):
    requests_mock.get(
        BASE + "earnings-surprises-bulk",
        json=[
            {
                "symbol": "AAPL",
                "date": "2026-07-31",
                "epsActual": "0.3631",
                "epsEstimated": "0.35",
            }
        ],
    )
    result = client.earnings_surprises_bulk(year="2026")
    assert result[0]["epsActual"] == "0.3631"
    assert requests_mock.last_request.qs["year"] == ["2026"]


def test_income_statement_bulk(client, requests_mock):
    requests_mock.get(
        BASE + "income-statement-bulk",
        json=[
            {
                "date": "2026-06-30",
                "symbol": "AAPL",
                "period": "Q3",
                "revenue": "90000000000",
            }
        ],
    )
    result = client.income_statement_bulk(year="2026", period="Q3")
    assert result[0]["revenue"] == "90000000000"
    sent = requests_mock.last_request.qs
    assert sent["year"] == ["2026"]
    assert sent["period"] == ["q3"]


def test_income_statement_growth_bulk(client, requests_mock):
    requests_mock.get(
        BASE + "income-statement-growth-bulk",
        json=[
            {
                "symbol": "AAPL",
                "date": "2026-06-30",
                "period": "Q3",
                "growthRevenue": "0.05",
            }
        ],
    )
    result = client.income_statement_growth_bulk(year="2026", period="Q3")
    assert result[0]["growthRevenue"] == "0.05"


def test_balance_sheet_statement_bulk(client, requests_mock):
    requests_mock.get(
        BASE + "balance-sheet-statement-bulk",
        json=[
            {
                "date": "2026-06-30",
                "symbol": "AAPL",
                "period": "Q3",
                "totalAssets": "350000000000",
            }
        ],
    )
    result = client.balance_sheet_statement_bulk(year="2026", period="Q3")
    assert result[0]["totalAssets"] == "350000000000"


def test_balance_sheet_statement_growth_bulk(client, requests_mock):
    requests_mock.get(
        BASE + "balance-sheet-statement-growth-bulk",
        json=[
            {
                "symbol": "AAPL",
                "date": "2026-06-30",
                "period": "Q3",
                "growthTotalAssets": "0.02",
            }
        ],
    )
    result = client.balance_sheet_statement_growth_bulk(year="2026", period="Q3")
    assert result[0]["growthTotalAssets"] == "0.02"


def test_cash_flow_statement_bulk(client, requests_mock):
    requests_mock.get(
        BASE + "cash-flow-statement-bulk",
        json=[
            {
                "date": "2026-06-30",
                "symbol": "AAPL",
                "period": "Q3",
                "freeCashFlow": "25000000000",
            }
        ],
    )
    result = client.cash_flow_statement_bulk(year="2026", period="Q3")
    assert result[0]["freeCashFlow"] == "25000000000"


def test_cash_flow_statement_growth_bulk(client, requests_mock):
    requests_mock.get(
        BASE + "cash-flow-statement-growth-bulk",
        json=[
            {
                "symbol": "AAPL",
                "date": "2026-06-30",
                "period": "Q3",
                "growthNetCashProvidedByOperatingActivites": "0.03",
            }
        ],
    )
    result = client.cash_flow_statement_growth_bulk(year="2026", period="Q3")
    assert result[0]["growthNetCashProvidedByOperatingActivites"] == "0.03"


def test_eod_bulk(client, requests_mock):
    requests_mock.get(
        BASE + "eod-bulk",
        json=[
            {"symbol": "AAPL", "date": "2026-08-20", "open": "228.0", "close": "230.5"}
        ],
    )
    result = client.eod_bulk(date="2026-08-20")
    assert result[0]["close"] == "230.5"
    assert requests_mock.last_request.qs["date"] == ["2026-08-20"]
