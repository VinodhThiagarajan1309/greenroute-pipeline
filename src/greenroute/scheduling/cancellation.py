# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""scheduling capability: the cancellation window."""

from datetime import timedelta

CANCELLATION_THRESHOLD_HOURS = 2
# The single configured cancellation threshold. This is the only place it
# is defined - no other capability (e.g. payments) may hold its own copy
# of this value. They must call get_cancellation_threshold_hours() below.


def get_cancellation_threshold_hours():
    """Read accessor for the cancellation threshold. Other capabilities
    must call this rather than copying the number into a constant of
    their own, so they never drift from scheduling's real value."""
    return CANCELLATION_THRESHOLD_HOURS


def is_chargeable_cancellation(cancelled_at, service_window_start, threshold_hours=None):
    """A cancellation received at or after (service_window_start - threshold)
    is CHARGEABLE. A cancellation received earlier than that is free.

    The boundary itself (cancelled_at == service_window_start - threshold)
    is CHARGEABLE, not free - this is a closed lower bound.
    """
    if threshold_hours is None:
        threshold_hours = CANCELLATION_THRESHOLD_HOURS
    cutoff = service_window_start - timedelta(hours=threshold_hours)
    return cancelled_at >= cutoff
