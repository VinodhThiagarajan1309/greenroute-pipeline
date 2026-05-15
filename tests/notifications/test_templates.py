# -*- coding: utf-8 -*-
"""Tests for notification templates."""
from greenroute.notifications.templates import (
    render_cancellation_template,
    render_reschedule_template,
)


def test_cancellation_template_renders_correctly_with_zero_add_ons():
    booking = {"booking_id": "b1", "service_window_start": "2026-09-10", "add_ons": []}
    text = render_cancellation_template(booking)
    assert text == "Your GreenRoute booking b1 on 2026-09-10 has been cancelled."
    assert "This also cancels" not in text


def test_cancellation_template_lists_add_ons_when_present():
    booking = {"booking_id": "b2", "service_window_start": "2026-09-10", "add_ons": ["mulching"]}
    text = render_cancellation_template(booking)
    assert "This also cancels: mulching." in text


def test_cancellation_template_missing_add_ons_key_treated_as_zero():
    booking = {"booking_id": "b3", "service_window_start": "2026-09-10"}
    text = render_cancellation_template(booking)
    assert text == "Your GreenRoute booking b3 on 2026-09-10 has been cancelled."


def test_reschedule_template_includes_old_and_new_window():
    booking = {"booking_id": "b4", "service_window_start": "2026-09-10", "add_ons": []}
    text = render_reschedule_template(booking, "2026-09-15")
    assert "2026-09-10" in text
    assert "2026-09-15" in text
