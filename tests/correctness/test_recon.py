# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""Tests for the data-correctness incremental/batch parity check.

A check that cannot fail is not a check: these tests start from a seeded
mismatch, not just a happy-path match.
"""
from greenroute.correctness.recon import compare_rows, run_recon


def test_seeded_mismatch_is_detected():
    incremental_rows = [
        {"schedule_event_id": "se-1", "status": "completed"},
        {"schedule_event_id": "se-2", "status": "cancelled"},
    ]
    # Seed a mismatch: the batch recompute disagrees on se-2's status.
    batch_rows = [
        {"schedule_event_id": "se-1", "status": "completed"},
        {"schedule_event_id": "se-2", "status": "completed"},
    ]

    mismatches = compare_rows(
        incremental_rows, batch_rows,
        key_fields=["schedule_event_id"], value_fields=["status"],
    )

    assert len(mismatches) == 1
    assert mismatches[0]["key"] == ("se-2",)
    assert mismatches[0]["diffs"]["status"] == {"incremental": "cancelled", "batch": "completed"}


def test_matching_rows_produce_no_mismatches():
    rows = [{"schedule_event_id": "se-1", "status": "completed"}]
    assert compare_rows(rows, rows, ["schedule_event_id"], ["status"]) == []


def test_row_missing_from_batch_is_reported_by_kind():
    incremental_rows = [{"schedule_event_id": "se-1", "status": "completed"}]
    batch_rows = []

    mismatches = compare_rows(incremental_rows, batch_rows, ["schedule_event_id"], ["status"])

    assert mismatches == [{"key": ("se-1",), "kind": "missing_from_batch", "diffs": None}]


def test_run_recon_reports_row_counts_alongside_mismatches():
    incremental_rows = [{"schedule_event_id": "se-1", "status": "completed"}]
    batch_rows = [{"schedule_event_id": "se-1", "status": "cancelled"}]

    result = run_recon(
        "gold_schedule_events", incremental_rows, batch_rows,
        ["schedule_event_id"], ["status"],
    )

    assert result["mismatch_count"] == 1
    assert result["incremental_row_count"] == 1
    assert result["batch_row_count"] == 1
