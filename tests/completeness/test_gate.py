# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""Tests for the data-completeness window-closure gate."""
from datetime import datetime

from greenroute.completeness.gate import (
    evaluate_window_closure,
    emit_gate_metric,
    BLOCKED_METRIC,
    OVERRIDDEN_METRIC,
)


def test_gate_blocks_when_one_of_three_sources_is_still_open():
    window_end = datetime(2026, 3, 1, 0, 0, 0)
    source_watermarks = {
        "bronze_booking_cancellations": 48,
        "bronze_technician_checkins": 6,
        "bronze_payment_events": 24,
    }
    # bronze_booking_cancellations closes at window_end + 48h = Mar 3 00:00.
    # "now" is only 30h past window_end, so that source is still open.
    now = datetime(2026, 3, 2, 6, 0, 0)

    result = evaluate_window_closure(source_watermarks, window_end, now)

    assert result.allowed is False
    assert result.blocking_sources == ["bronze_booking_cancellations"]


def test_gate_opens_once_every_source_has_closed():
    window_end = datetime(2026, 3, 1, 0, 0, 0)
    source_watermarks = {
        "bronze_booking_cancellations": 48,
        "bronze_technician_checkins": 6,
    }
    now = datetime(2026, 3, 3, 0, 0, 1)

    result = evaluate_window_closure(source_watermarks, window_end, now)

    assert result.allowed is True
    assert result.blocking_sources == []


def test_blocked_gate_emits_a_metric_naming_the_blocking_source():
    window_end = datetime(2026, 3, 1, 0, 0, 0)
    source_watermarks = {"bronze_booking_cancellations": 48}
    now = datetime(2026, 3, 1, 6, 0, 0)

    result = evaluate_window_closure(source_watermarks, window_end, now)
    events = emit_gate_metric(result, window_end)

    assert len(events) == 1
    assert events[0]["metric"] == BLOCKED_METRIC
    assert events[0]["tags"]["source"] == "bronze_booking_cancellations"


def test_override_allows_publish_and_emits_a_distinct_metric_with_reason():
    window_end = datetime(2026, 3, 1, 0, 0, 0)
    source_watermarks = {"bronze_booking_cancellations": 48}
    now = datetime(2026, 3, 1, 6, 0, 0)

    result = evaluate_window_closure(
        source_watermarks, window_end, now,
        override_reason="exec asked for early publish for board meeting",
    )
    events = emit_gate_metric(result, window_end)

    assert result.allowed is True
    assert result.overridden is True
    assert len(events) == 1
    assert events[0]["metric"] == OVERRIDDEN_METRIC
    assert events[0]["metric"] != BLOCKED_METRIC
    assert events[0]["tags"]["reason"]
