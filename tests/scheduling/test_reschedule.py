# -*- coding: utf-8 -*-
from datetime import datetime

from greenroute.scheduling.reschedule import reschedule_booking_and_invalidate_route


def test_reschedule_invalidates_original_route_assignment():
    booking = {"booking_id": "bk-1", "service_window_start": datetime(2026, 3, 12, 9, 0)}
    route_assignment = {"booking_id": "bk-1", "zone_id": "zilker", "status": "assigned"}
    updated_booking, invalidated = reschedule_booking_and_invalidate_route(
        booking, route_assignment, datetime(2026, 3, 13, 9, 0), datetime(2026, 3, 12, 16, 0)
    )
    assert updated_booking["service_window_start"] == datetime(2026, 3, 13, 9, 0)
    assert invalidated["status"] == "invalidated"


def test_reschedule_after_dispatch_cutoff_on_original_day_still_invalidates_route():
    # Dispatch for the original day had already gone out (afternoon of the
    # original service day) - the route assignment must still be
    # invalidated so the crew doesn't drive out for a job that moved.
    booking = {"booking_id": "bk-2", "service_window_start": datetime(2026, 3, 12, 15, 0)}
    route_assignment = {
        "booking_id": "bk-2", "zone_id": "mueller", "status": "assigned",
        "dispatched_at": datetime(2026, 3, 12, 6, 0),
    }
    updated_booking, invalidated = reschedule_booking_and_invalidate_route(
        booking, route_assignment, datetime(2026, 3, 14, 9, 0), datetime(2026, 3, 12, 14, 45)
    )
    assert invalidated is not None
    assert invalidated["invalidated_reason"] == "booking_rescheduled"
    assert updated_booking["reschedule_history"][-1]["rescheduled_at"] == datetime(2026, 3, 12, 14, 45)
