"""Ultimate-tier (Bucket 2) live tests for client.chart.

Discovered live, not predicted by REWRITE_ARCHITECTURE.md's group
directory (which lists no Bucket 2 flag on `chart`): `historical_chart`
(all 6 intraday timeframes, one method per §5.3's collapse) 402s on the
free tier, while all 4 `historical_price_eod_*` (daily) methods work fine.
Skipped by default (`-m "not ultimate"` / excluded unless explicitly
selected); run for real only during a deliberately-timed FMP Ultimate
month, per the rewrite workflow.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.ultimate


def test_historical_chart(live_client):
    result = live_client.historical_chart(symbol="AAPL", timeframe="1hour")
    assert len(result) > 0
    assert "close" in result[0]
