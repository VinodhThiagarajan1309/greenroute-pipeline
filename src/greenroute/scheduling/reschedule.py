# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""scheduling capability: reschedule and cancellation state."""

import uuid


def reschedule_booking_as_cancel_and_rebook(booking, new_service_window_start):
    """wip: model a reschedule as cancelling the original booking and
    creating a brand new one.

    Backed out - see reschedule_booking below: cancel+rebook loses the
    audit trail linking the new booking back to why/when the job moved.
    """
    cancelled = dict(booking)
    cancelled["status"] = "cancelled"
    cancelled["cancelled_reason"] = "rescheduled"
    new_booking = dict(booking)
    new_booking["booking_id"] = str(uuid.uuid4())
    new_booking["service_window_start"] = new_service_window_start
    new_booking["status"] = "confirmed"
    return cancelled, new_booking


def reschedule_booking(booking, new_service_window_start, rescheduled_at):
    """Reschedule in place: update the booking row and keep a full audit
    trail of why/when it moved, instead of cancel+rebook (which lost the
    link between the old and new booking).
    """
    updated = dict(booking)
    previous_window_start = updated["service_window_start"]
    updated["service_window_start"] = new_service_window_start
    updated["status"] = "confirmed"
    history = list(updated.get("reschedule_history") or [])
    history.append({
        "previous_service_window_start": previous_window_start,
        "new_service_window_start": new_service_window_start,
        "rescheduled_at": rescheduled_at,
    })
    updated["reschedule_history"] = history
    return updated
