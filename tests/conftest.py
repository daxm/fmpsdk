"""Shared pytest fixtures.

`live` and `ultimate`-marked tests need a real FMP API key. They skip
automatically when ``FMP_API_KEY`` isn't set — e.g. in CI, or a session
with no ``.env`` — rather than failing, per the tiering in
REWRITE_ARCHITECTURE.md §11 / the rewrite workflow notes.
"""

from __future__ import annotations

import os

import pytest
from dotenv import load_dotenv

import fmpsdk

load_dotenv()


@pytest.fixture
def client() -> fmpsdk.Client:
    """A Client with a fake key, for `unit` tests — never makes a real call."""
    return fmpsdk.Client(api_key="unit-test-key")


@pytest.fixture
def live_client() -> fmpsdk.Client:
    """A Client with the real key from FMP_API_KEY, for `live` tests."""
    api_key = os.environ.get("FMP_API_KEY")
    if not api_key:
        pytest.skip("FMP_API_KEY not set — skipping live test")
    return fmpsdk.Client(api_key=api_key)
