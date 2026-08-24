"""Mocked unit tests for client.bulk — mirrors fmpsdk/endpoints/bulk.py.

Every bulk endpoint's real response is CSV (``text/csv``), not JSON —
confirmed live 2026-08-24 against an FMP Ultimate-tier key, including
``profile_bulk`` (previously assumed to be the one exception returning
real JSON). Mocks below use ``text=`` with a CSV header row plus one
data row, trimmed to a few representative columns each — the TypedDict
cast isn't runtime-checked, so a full-fidelity mock buys nothing a
partial one doesn't. Every field comes back as a `str`, per
types/bulk.py's module docstring.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.unit

BASE = "https://financialmodelingprep.com/stable/"


def test_profile_bulk(client, requests_mock):
    requests_mock.get(
        BASE + "profile-bulk",
        text='"symbol","companyName","price"\n"AAPL","Apple Inc.","230.5"\n',
    )
    result = client.profile_bulk(part="0")
    assert result[0]["symbol"] == "AAPL"
    assert requests_mock.last_request.qs["part"] == ["0"]


def test_rating_bulk(client, requests_mock):
    requests_mock.get(
        BASE + "rating-bulk",
        text=(
            '"symbol","date","rating","discountedCashFlowScore"\n'
            '"AAPL","2026-08-20","A-","5"\n'
        ),
    )
    result = client.rating_bulk()
    assert result[0]["rating"] == "A-"
    assert requests_mock.last_request.qs == {}


def test_dcf_bulk(client, requests_mock):
    requests_mock.get(
        BASE + "dcf-bulk",
        text='"symbol","date","dcf","Stock Price"\n"AAPL","2026-08-20","220.5","230.5"\n',
    )
    result = client.dcf_bulk()
    assert result[0]["dcf"] == "220.5"


def test_scores_bulk(client, requests_mock):
    requests_mock.get(
        BASE + "scores-bulk",
        text=(
            '"symbol","reportedCurrency","altmanZScore","piotroskiScore"\n'
            '"AAPL","USD","8.1","7"\n'
        ),
    )
    result = client.scores_bulk()
    assert result[0]["piotroskiScore"] == "7"


def test_price_target_summary_bulk(client, requests_mock):
    requests_mock.get(
        BASE + "price-target-summary-bulk",
        text=(
            '"symbol","lastMonthCount","lastMonthAvgPriceTarget"\n'
            '"AAPL","5","240.0"\n'
        ),
    )
    result = client.price_target_summary_bulk()
    assert result[0]["lastMonthCount"] == "5"


def test_etf_holder_bulk(client, requests_mock):
    requests_mock.get(
        BASE + "etf-holder-bulk",
        text=(
            '"symbol","name","sharesNumber","lastUpdated"\n'
            '"SPY","Apple Inc.","12345","2026-08-20"\n'
        ),
    )
    result = client.etf_holder_bulk(part="1")
    assert result[0]["name"] == "Apple Inc."
    assert requests_mock.last_request.qs["part"] == ["1"]


def test_upgrades_downgrades_consensus_bulk(client, requests_mock):
    requests_mock.get(
        BASE + "upgrades-downgrades-consensus-bulk",
        text='"symbol","strongBuy","buy","consensus"\n"AAPL","10","20","Buy"\n',
    )
    result = client.upgrades_downgrades_consensus_bulk()
    assert result[0]["consensus"] == "Buy"


def test_key_metrics_ttm_bulk(client, requests_mock):
    requests_mock.get(
        BASE + "key-metrics-ttm-bulk",
        text=(
            '"symbol","marketCap","enterpriseValueTTM"\n'
            '"AAPL","3500000000000","3550000000000"\n'
        ),
    )
    result = client.key_metrics_ttm_bulk()
    assert result[0]["marketCap"] == "3500000000000"


def test_ratios_ttm_bulk(client, requests_mock):
    requests_mock.get(
        BASE + "ratios-ttm-bulk",
        text='"symbol","grossProfitMarginTTM","currentRatioTTM"\n"AAPL","0.46","1.1"\n',
    )
    result = client.ratios_ttm_bulk()
    assert result[0]["currentRatioTTM"] == "1.1"


def test_peers_bulk(client, requests_mock):
    requests_mock.get(
        BASE + "peers-bulk",
        text='"symbol","peers"\n"AAPL","MSFT,GOOG,AMZN"\n',
    )
    result = client.peers_bulk()
    assert result[0]["peers"] == "MSFT,GOOG,AMZN"


def test_earnings_surprises_bulk(client, requests_mock):
    requests_mock.get(
        BASE + "earnings-surprises-bulk",
        text=(
            '"symbol","date","epsActual","epsEstimated"\n'
            '"AAPL","2026-07-31","0.3631","0.35"\n'
        ),
    )
    result = client.earnings_surprises_bulk(year="2026")
    assert result[0]["epsActual"] == "0.3631"
    assert requests_mock.last_request.qs["year"] == ["2026"]


def test_income_statement_bulk(client, requests_mock):
    requests_mock.get(
        BASE + "income-statement-bulk",
        text='"date","symbol","period","revenue"\n"2026-06-30","AAPL","Q3","90000000000"\n',
    )
    result = client.income_statement_bulk(year="2026", period="Q3")
    assert result[0]["revenue"] == "90000000000"
    sent = requests_mock.last_request.qs
    assert sent["year"] == ["2026"]
    assert sent["period"] == ["q3"]


def test_income_statement_growth_bulk(client, requests_mock):
    requests_mock.get(
        BASE + "income-statement-growth-bulk",
        text='"symbol","date","period","growthRevenue"\n"AAPL","2026-06-30","Q3","0.05"\n',
    )
    result = client.income_statement_growth_bulk(year="2026", period="Q3")
    assert result[0]["growthRevenue"] == "0.05"


def test_balance_sheet_statement_bulk(client, requests_mock):
    requests_mock.get(
        BASE + "balance-sheet-statement-bulk",
        text='"date","symbol","period","totalAssets"\n"2026-06-30","AAPL","Q3","350000000000"\n',
    )
    result = client.balance_sheet_statement_bulk(year="2026", period="Q3")
    assert result[0]["totalAssets"] == "350000000000"


def test_balance_sheet_statement_growth_bulk(client, requests_mock):
    requests_mock.get(
        BASE + "balance-sheet-statement-growth-bulk",
        text='"symbol","date","period","growthTotalAssets"\n"AAPL","2026-06-30","Q3","0.02"\n',
    )
    result = client.balance_sheet_statement_growth_bulk(year="2026", period="Q3")
    assert result[0]["growthTotalAssets"] == "0.02"


def test_cash_flow_statement_bulk(client, requests_mock):
    requests_mock.get(
        BASE + "cash-flow-statement-bulk",
        text='"date","symbol","period","freeCashFlow"\n"2026-06-30","AAPL","Q3","25000000000"\n',
    )
    result = client.cash_flow_statement_bulk(year="2026", period="Q3")
    assert result[0]["freeCashFlow"] == "25000000000"


def test_cash_flow_statement_growth_bulk(client, requests_mock):
    requests_mock.get(
        BASE + "cash-flow-statement-growth-bulk",
        text=(
            '"symbol","date","period","growthNetCashProvidedByOperatingActivites"\n'
            '"AAPL","2026-06-30","Q3","0.03"\n'
        ),
    )
    result = client.cash_flow_statement_growth_bulk(year="2026", period="Q3")
    assert result[0]["growthNetCashProvidedByOperatingActivites"] == "0.03"


def test_eod_bulk(client, requests_mock):
    requests_mock.get(
        BASE + "eod-bulk",
        text='"symbol","date","open","close"\n"AAPL","2026-08-20","228.0","230.5"\n',
    )
    result = client.eod_bulk(date="2026-08-20")
    assert result[0]["close"] == "230.5"
    assert requests_mock.last_request.qs["date"] == ["2026-08-20"]
