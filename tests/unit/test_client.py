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
