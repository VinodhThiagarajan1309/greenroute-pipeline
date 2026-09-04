# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""Tests for the data-completeness capability: watermarks and orphan-row checks."""
from greenroute.completeness.watermarks import (
    derive_watermark_hours,
    watermark_has_headroom,
    watermark_closes_at,
    CANCELLATION_WATERMARK_HOURS,
    BOOKING_CANCELLATION_LATENESS_MINUTES,
)


def gold_rows_missing_bronze_source(gold_schedule_events, bronze_source_ids):
    """Completeness check: every gold_schedule_events row must trace back to
    a bronze source row. Returns the offending gold row ids, never a bool --
    a count with no ids tells an on-call engineer nothing.
    """
    bronze_ids = set(bronze_source_ids)
    return [
        row["schedule_event_id"]
        for row in gold_schedule_events
        if row["bronze_source_id"] not in bronze_ids
    ]


def test_cancellation_watermark_is_48_hours():
    assert CANCELLATION_WATERMARK_HOURS == 48


def test_watermark_clears_measured_p99_and_max():
    assert watermark_has_headroom(
        CANCELLATION_WATERMARK_HOURS,
        BOOKING_CANCELLATION_LATENESS_MINUTES["p99"],
        BOOKING_CANCELLATION_LATENESS_MINUTES["max"],
    )


def test_derive_watermark_rounds_measured_max_up_to_next_boundary():
    # 30h measured max rounds up to the next 12h boundary: 36h.
    assert derive_watermark_hours(30 * 60) == 36


def test_no_orphan_rows_when_every_gold_row_has_a_bronze_source():
    gold_rows = [
        {"schedule_event_id": "se-1", "bronze_source_id": "bk-1"},
        {"schedule_event_id": "se-2", "bronze_source_id": "bk-2"},
    ]
    bronze_ids = ["bk-1", "bk-2", "bk-3"]
    assert gold_rows_missing_bronze_source(gold_rows, bronze_ids) == []


def test_flags_gold_row_with_no_matching_bronze_source():
    gold_rows = [
        {"schedule_event_id": "se-1", "bronze_source_id": "bk-1"},
        {"schedule_event_id": "se-2", "bronze_source_id": "bk-missing"},
    ]
    bronze_ids = ["bk-1"]
    assert gold_rows_missing_bronze_source(gold_rows, bronze_ids) == ["se-2"]
