"""Mocked unit tests for client.esg — mirrors fmpsdk/endpoints/esg.py."""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.unit

BASE = "https://financialmodelingprep.com/stable/"


def test_esg_disclosures(client, requests_mock):
    requests_mock.get(
        BASE + "esg-disclosures",
        json=[
            {
                "date": "2026-03-28",
                "acceptedDate": "2026-04-30",
                "symbol": "AAPL",
                "cik": "0000320193",
                "companyName": "Apple Inc.",
                "formType": "8-K",
                "environmentalScore": 66.29,
                "socialScore": 45.21,
                "governanceScore": 58.87,
                "ESGScore": 56.79,
                "url": "https://www.sec.gov/x",
            }
        ],
    )
    result = client.esg_disclosures(symbol="AAPL")
    assert result[0]["ESGScore"] == 56.79


def test_esg_ratings(client, requests_mock):
    requests_mock.get(
        BASE + "esg-ratings",
        json=[
            {
                "symbol": "AAPL",
                "cik": "0000320193",
                "companyName": "Apple Inc.",
                "industry": "CONSUMER ELECTRONICS",
                "fiscalYear": 2025,
                "ESGRiskRating": "B",
                "industryRank": "17 out of 20",
            }
        ],
    )
    result = client.esg_ratings(symbol="AAPL")
    assert result[0]["ESGRiskRating"] == "B"


def test_esg_benchmark(client, requests_mock):
    requests_mock.get(
        BASE + "esg-benchmark",
        json=[
            {
                "fiscalYear": 2023,
                "sector": "APPAREL RETAIL",
                "environmentalScore": 61.36,
                "socialScore": 67.44,
                "governanceScore": 68.1,
                "ESGScore": 65.63,
            }
        ],
    )
    result = client.esg_benchmark(year="2023")
    assert result[0]["sector"] == "APPAREL RETAIL"
    assert requests_mock.last_request.qs["year"] == ["2023"]


def test_esg_benchmark_omits_unset_optional_param(client, requests_mock):
    requests_mock.get(BASE + "esg-benchmark", json=[])
    client.esg_benchmark()
    assert "year" not in requests_mock.last_request.qs
