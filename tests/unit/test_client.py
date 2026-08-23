"""Mocked unit tests for the Client core: auth header, error mapping, and
the non-retryable status codes. Retry/backoff behavior isn't tested here
yet — it depends on `_compute_backoff_delay`, which is still a TODO in
fmpsdk/client.py.
"""

from __future__ import annotations

import pytest

import fmpsdk

pytestmark = pytest.mark.unit

BASE = "https://financialmodelingprep.com/stable/"


def test_no_api_key_raises_authentication_error(monkeypatch):
    monkeypatch.delenv("FMP_API_KEY", raising=False)
    with pytest.raises(fmpsdk.FMPAuthenticationError):
        fmpsdk.Client()


def test_api_key_falls_back_to_env_var(monkeypatch):
    monkeypatch.setenv("FMP_API_KEY", "from-env")
    c = fmpsdk.Client()
    assert c.api_key == "from-env"


def test_sends_api_key_as_header_not_query_string(client, requests_mock):
    requests_mock.get(BASE + "search-symbol", json=[])
    client.search_symbol(query="AAPL")
    request = requests_mock.last_request
    assert request.headers["apikey"] == "unit-test-key"
    assert "apikey" not in request.qs


@pytest.mark.parametrize(
    "status_code,exception_cls",
    [
        (400, fmpsdk.FMPValidationError),
        (401, fmpsdk.FMPAuthenticationError),
        (402, fmpsdk.FMPPlanLimitError),
        (403, fmpsdk.FMPAuthenticationError),
        (404, fmpsdk.FMPNotFoundError),
    ],
)
def test_non_retryable_statuses_raise_immediately(client, requests_mock, status_code, exception_cls):
    requests_mock.get(BASE + "search-symbol", status_code=status_code, text="FMP says no")
    with pytest.raises(exception_cls):
        client.search_symbol(query="AAPL")
    # Exactly one request — none of these are retried (brief 3.6).
    assert requests_mock.call_count == 1


def test_plan_limit_error_message_says_request_not_endpoint(client, requests_mock):
    requests_mock.get(BASE + "search-symbol", status_code=402, text="FMP raw detail")
    with pytest.raises(fmpsdk.FMPPlanLimitError) as excinfo:
        client.search_symbol(query="AAPL")
    assert "request" in str(excinfo.value)
    assert "endpoint" not in str(excinfo.value)
    assert excinfo.value.response_text == "FMP raw detail"


def test_empty_response_body_returns_empty_list(client, requests_mock):
    requests_mock.get(BASE + "search-symbol", status_code=200, content=b"")
    assert client.search_symbol(query="NOPE") == []


@pytest.mark.parametrize("status_code,exception_cls", [(429, fmpsdk.FMPRateLimitError), (503, fmpsdk.FMPServerError)])
def test_retryable_statuses_retry_then_raise_after_max_retries(
    client, requests_mock, monkeypatch, status_code, exception_cls
):
    monkeypatch.setattr("fmpsdk.client.time.sleep", lambda _seconds: None)
    requests_mock.get(BASE + "search-symbol", status_code=status_code, text="try again later")
    with pytest.raises(exception_cls):
        client.search_symbol(query="AAPL")
    # 1 initial attempt + client.max_retries (default 3) retries.
    assert requests_mock.call_count == client.max_retries + 1


def test_retryable_status_succeeds_after_transient_failure(client, requests_mock, monkeypatch):
    monkeypatch.setattr("fmpsdk.client.time.sleep", lambda _seconds: None)
    requests_mock.get(
        BASE + "search-symbol",
        [
            {"status_code": 503, "text": "temporarily unavailable"},
            {"status_code": 200, "json": [{"symbol": "AAPL"}]},
        ],
    )
    result = client.search_symbol(query="AAPL")
    assert result == [{"symbol": "AAPL"}]
    assert requests_mock.call_count == 2
