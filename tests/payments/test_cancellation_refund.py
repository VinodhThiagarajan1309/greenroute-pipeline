# -*- coding: utf-8 -*-
"""Tests for auto-refund-on-cancellation matching scheduling's threshold (payments)."""
from greenroute.payments.cancellation_refund import decide_auto_refund, is_free_cancellation
from greenroute.payments.scheduling_client import parse_cancellation_threshold_row


def test_cancellation_before_threshold_is_free():
    # scheduling's threshold is T-2h, not payments' old hardcoded T-4h
    assert is_free_cancellation(hours_before_service=3.0, threshold_hours=2.0) is True


def test_cancellation_after_threshold_is_chargeable():
    assert is_free_cancellation(hours_before_service=1.5, threshold_hours=2.0) is False


def test_cancellation_exactly_on_threshold_is_free():
    assert is_free_cancellation(hours_before_service=2.0, threshold_hours=2.0) is True


def test_decide_auto_refund_matches_scheduling_free_determination():
    result = decide_auto_refund(capture_amount_cents=8000, hours_before_service=3.0, threshold_hours=2.0)
    assert result["refund_amount_cents"] == 8000
    assert result["reason"] == "free_cancellation"


def test_parse_cancellation_threshold_row():
    row = {"config_key": "cancellation_threshold_hours", "config_value": "2"}
    assert parse_cancellation_threshold_row(row) == 2.0
