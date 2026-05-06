# -*- coding: utf-8 -*-
"""Tests reconciling zone_registry against the DAB CSV and ops' spreadsheet."""
from greenroute.expansion.zone_registry import find_source_disagreements, zone_for_zip

# Round Rock / Pflugerville seam zips -- exactly where GreenRoute is expanding.
SEAM_ZIPS = ["78660", "78664", "78665", "78681"]


def test_reconciliation_finds_the_four_seam_disagreements():
    registry_by_zip = {
        "78664": {"zone": "round_rock"},
        "78665": {"zone": "pflugerville"},
        "78681": {"zone": "round_rock"},
        "78660": {"zone": "round_rock"},
        "78701": {"zone": "zilker"},
    }
    ops_spreadsheet_by_zip = {
        "78664": "pflugerville",
        "78665": "round_rock",
        "78681": "pflugerville",
        "78660": "pflugerville",
        "78701": "zilker",
    }
    disagreements = find_source_disagreements(registry_by_zip, ops_spreadsheet_by_zip)
    disagreeing_zips = sorted(d["zip"] for d in disagreements)
    assert disagreeing_zips == sorted(SEAM_ZIPS)
    assert len(disagreements) == 4


def test_no_disagreement_when_sources_match():
    registry_by_zip = {"78701": {"zone": "zilker"}}
    other = {"78701": "zilker"}
    assert find_source_disagreements(registry_by_zip, other) == []


def test_zone_for_zip_returns_none_for_unregistered_zip():
    assert zone_for_zip("99999", {}) is None
