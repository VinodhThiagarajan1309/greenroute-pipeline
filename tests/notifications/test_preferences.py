# -*- coding: utf-8 -*-
"""Tests that an opted-out customer gets no SMS on confirmation, reminder,
or cancellation.
"""
from greenroute.notifications.dispatch import (
    send_confirmation,
    send_reminder,
    send_cancellation,
)


def _prefs(opted_in):
    return {("cust-1", "sms"): {"opted_in": opted_in}}


def test_opted_out_customer_blocked_on_confirmation():
    result = send_confirmation("cust-1", {"booking_id": "b1"}, _prefs(False))
    assert result["sent"] is False
    assert result["reason"] == "opted_out"


def test_opted_out_customer_blocked_on_reminder():
    result = send_reminder(
        "cust-1", {"booking_id": "b1", "service_window_start": "2026-09-10"}, _prefs(False)
    )
    assert result["sent"] is False


def test_opted_out_customer_blocked_on_cancellation():
    result = send_cancellation("cust-1", {"booking_id": "b1"}, _prefs(False))
    assert result["sent"] is False


def test_unknown_customer_defaults_to_not_opted_in():
    result = send_confirmation("cust-9", {"booking_id": "b2"}, {})
    assert result["sent"] is False
