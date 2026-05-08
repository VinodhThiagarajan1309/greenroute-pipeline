# -*- coding: utf-8 -*-
"""Tests for backfill value-parity reconciliation (pipeline-orchestration)."""
from greenroute.orchestration.backfill_recon import (
    RECON_FAIL,
    RECON_INCONCLUSIVE,
    RECON_PASS,
    value_parity_check,
)


def test_seeded_value_corruption_with_unchanged_row_count_is_caught():
    before = [
        {"event_key": "evt_1", "zone_id": "zilker", "amount_cents": 5000},
        {"event_key": "evt_2", "zone_id": "mueller", "amount_cents": 3000},
    ]
    # same keys, same row count, but evt_2's amount was silently corrupted
    after = [
        {"event_key": "evt_1", "zone_id": "zilker", "amount_cents": 5000},
        {"event_key": "evt_2", "zone_id": "mueller", "amount_cents": 9999},
    ]
    assert len(before) == len(after)
    assert value_parity_check(before, after, "event_key", ["zone_id", "amount_cents"]) == RECON_FAIL


def test_identical_data_passes():
    records = [{"event_key": "evt_1", "zone_id": "zilker", "amount_cents": 5000}]
    assert value_parity_check(records, list(records), "event_key", ["zone_id", "amount_cents"]) == RECON_PASS


def test_empty_vs_empty_is_inconclusive_not_pass():
    assert value_parity_check([], [], "event_key", ["zone_id"]) == RECON_INCONCLUSIVE
