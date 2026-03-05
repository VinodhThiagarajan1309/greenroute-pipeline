# -*- coding: utf-8 -*-
"""payments: refund state transitions.

A refund references the CAPTURE it reverses, never the booking directly --
a booking can have several captures (rescheduled jobs, add-ons billed
separately).
"""

REFUND_STATE_REQUESTED = "requested"
REFUND_STATE_SUCCEEDED = "succeeded"
REFUND_STATE_FAILED = "failed"

ALLOWED_REFUND_TRANSITIONS = {
    None: set([REFUND_STATE_REQUESTED]),
    REFUND_STATE_REQUESTED: set([REFUND_STATE_SUCCEEDED, REFUND_STATE_FAILED]),
    REFUND_STATE_FAILED: set([REFUND_STATE_REQUESTED]),  # a failed refund can be retried
}


def transition_refund_state(current_state, next_state):
    """Pure state-machine check. Raises ValueError on an illegal transition."""
    allowed = ALLOWED_REFUND_TRANSITIONS.get(current_state, set())
    if next_state not in allowed:
        raise ValueError("illegal refund transition: %r -> %r" % (current_state, next_state))
    return next_state


def build_refund_record(capture_id, amount_cents, state):
    """A refund record always references the capture_id it reverses, never a booking_id."""
    return {"capture_id": capture_id, "amount_cents": amount_cents, "state": state}
