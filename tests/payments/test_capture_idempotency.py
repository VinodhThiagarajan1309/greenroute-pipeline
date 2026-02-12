# -*- coding: utf-8 -*-
"""Tests for write-time capture idempotency (payments).

Only the pure decision functions are exercised here -- write_capture itself
wraps Spark I/O and is never imported at call time by these tests.
"""
from greenroute.payments.capture import capture_already_applied, decide_capture_write
from greenroute.payments.remediation_2024q2_duplicate_captures import collapse_duplicate_captures


def test_duplicate_webhook_delivery_is_not_captured_twice():
    existing = set(["evt_1"])
    assert capture_already_applied("evt_1", existing) is True
    assert capture_already_applied("evt_2", existing) is False


def test_decide_capture_write_rejects_duplicate_provider_event_id():
    existing = set(["evt_1"])
    result = decide_capture_write({"provider_event_id": "evt_1", "capture_id": "cap_1"}, existing)
    assert result["applied"] is False
    assert "duplicate" in result["reason"]


def test_decide_capture_write_applies_new_provider_event_id():
    existing = set()
    result = decide_capture_write({"provider_event_id": "evt_9", "capture_id": "cap_9"}, existing)
    assert result["applied"] is True
    assert result["capture_row"]["capture_id"] == "cap_9"


def test_collapse_duplicate_captures_keeps_earliest_and_flags_rest():
    events = [
        {"provider_event_id": "evt_a", "capture_id": "cap_1", "event_ts": "2024-04-01T10:00:00"},
        {"provider_event_id": "evt_a", "capture_id": "cap_1", "event_ts": "2024-04-01T10:00:05"},
    ]
    kept, reversed_rows = collapse_duplicate_captures(events)
    assert len(kept) == 1
    assert len(reversed_rows) == 1
    assert reversed_rows[0]["reversal_of"] == "cap_1"
