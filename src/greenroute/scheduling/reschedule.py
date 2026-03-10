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


def reschedule_booking_and_invalidate_route(booking, route_assignment, new_service_window_start, rescheduled_at):
    """Reschedule a booking AND invalidate its derived route-assignment
    state.

    fix: the sprint-5 bug was that reschedule updated only the booking row
    and left the old route_assignment row in place, so a crew was still
    dispatched for a job that had moved (two crews drove to Zilker for a
    job moved to Thursday). Route assignment is derived state - any
    reschedule must explicitly invalidate it, not just update the booking.
    """
    updated_booking = reschedule_booking(booking, new_service_window_start, rescheduled_at)
    invalidated_route_assignment = None
    if route_assignment is not None and route_assignment.get("status") == "assigned" \
            and route_assignment.get("booking_id") == booking["booking_id"]:
        invalidated_route_assignment = dict(route_assignment)
        invalidated_route_assignment["status"] = "invalidated"
        invalidated_route_assignment["invalidated_reason"] = "booking_rescheduled"
        invalidated_route_assignment["invalidated_at"] = rescheduled_at
    return updated_booking, invalidated_route_assignment
