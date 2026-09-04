# -*- coding: utf-8 -*-
"""
Message templates for the customer-notifications capability: reschedule
and cancellation.
"""


def render_cancellation_template(booking):
    """Render the cancellation SMS body for a booking.

    Handles bookings with zero add-ons: the add-ons clause is simply
    omitted rather than rendering an empty "and:" fragment.
    """
    add_ons = booking.get("add_ons") or []
    base = "Your GreenRoute booking %s on %s has been cancelled." % (
        booking.get("booking_id"),
        booking.get("service_window_start"),
    )
    if not add_ons:
        return base
    return base + " This also cancels: %s." % ", ".join(add_ons)


def render_reschedule_template(booking, new_service_window_start):
    """Render the reschedule SMS body for a booking."""
    add_ons = booking.get("add_ons") or []
    base = "Your GreenRoute booking %s has been rescheduled from %s to %s." % (
        booking.get("booking_id"),
        booking.get("service_window_start"),
        new_service_window_start,
    )
    if not add_ons:
        return base
    return base + " Add-ons carried over: %s." % ", ".join(add_ons)
