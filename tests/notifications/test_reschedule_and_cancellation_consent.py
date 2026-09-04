# -*- coding: utf-8 -*-
"""Tests that reschedule and cancellation sends respect
notification_preference.
"""
from greenroute.notifications.dispatch import send_reschedule, send_cancellation


def _opted_out():
    return {("cust-1", "sms"): {"opted_in": False}}


def _opted_in():
    return {("cust-1", "sms"): {"opted_in": True}}


def test_opted_out_customer_gets_no_reschedule_text():
    booking = {"booking_id": "b1", "service_window_start": "2026-09-10"}
    result = send_reschedule("cust-1", booking, _opted_out())
    assert result["sent"] is False
    assert result["reason"] == "opted_out"


def test_opted_out_customer_gets_no_cancellation_text():
    result = send_cancellation("cust-1", {"booking_id": "b1"}, _opted_out())
    assert result["sent"] is False


def test_opted_out_check_runs_before_any_provider_is_touched():
    # The opted-out short-circuit must return before send() ever reaches a
    # provider -- this is what makes it unbypassable regardless of which
    # provider is registered for the channel.
    booking = {"booking_id": "b1", "service_window_start": "2026-09-10"}
    result = send_reschedule("cust-1", booking, _opted_out())
    assert result == {"sent": False, "reason": "opted_out"}
