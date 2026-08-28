"""Catalog introspection: it must see every fmpsdk method, fully described."""

from __future__ import annotations

from fmpsdk_mcp import catalog

CAT = catalog.build_catalog()
VALID_TIERS = {"Free", "Starter", "Premium", "Ultimate", "Add-on"}


def test_sees_all_238_methods():
    assert len(CAT) == 238


def test_every_endpoint_is_fully_described():
    for e in CAT:
        assert e.http_method == "GET", e.name
        assert e.wire_path, e.name
        assert e.summary, e.name
        assert e.return_type, e.name
        assert e.tier in VALID_TIERS, (e.name, e.tier)


def test_tiers_json_covers_exactly_the_catalog():
    assert set(catalog._TIERS) == {e.name for e in CAT}
    assert set(catalog._TIERS.values()) <= VALID_TIERS


def test_known_tier_verdicts():
    tier = lambda n: catalog.by_name(n).tier  # noqa: E731
    assert tier("quote") == "Free"
    assert tier("search_symbol") == "Free"
    assert tier("company_screener") == "Starter"
    assert tier("commitment_of_traders_report") == "Premium"
    assert tier("income_statement_ttm") == "Ultimate"
    assert tier("tipranks_search") == "Add-on"


def test_summaries_are_plain_text():
    for e in CAT:
        assert ":meth:" not in e.summary, e.name
        assert "``" not in e.summary, e.name


def test_by_name():
    assert catalog.by_name("income_statement").group == "statements"
    assert catalog.by_name("not_a_real_method") is None


def test_search():
    assert catalog.search("") == list(CAT)
    hits = catalog.search("senate")
    assert hits
    assert all(
        "senate" in (h.name + " " + h.group + " " + h.summary).lower() for h in hits
    )


def test_signature_render():
    assert (
        catalog.by_name("income_statement").signature
        == "income_statement(symbol, limit=None, period=None)"
    )
