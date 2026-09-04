# -*- coding: utf-8 -*-
"""payments: auto-refund decision on booking cancellation.

Reads scheduling's cancellation threshold rather than holding a private
copy. The sprint-5 bug: payments hardcoded a T-4h auto-refund threshold
while scheduling used T-2h, so a customer cancelling at T-3h was told "no
charge" by scheduling and then charged by payments. That private T-4h
constant is gone; the threshold now always comes from scheduling_client.
"""


def is_free_cancellation(hours_before_service, threshold_hours):
    """True if a cancellation this far before the service window is free.

    ``threshold_hours`` must come from scheduling (see scheduling_client.py)
    -- payments does not define its own threshold.
    """
    return hours_before_service >= threshold_hours


def decide_auto_refund(capture_amount_cents, hours_before_service, threshold_hours):
    """Pure decision: how much (if anything) to auto-refund on cancellation."""
    if is_free_cancellation(hours_before_service, threshold_hours):
        return {"refund_amount_cents": capture_amount_cents, "reason": "free_cancellation"}
    return {"refund_amount_cents": 0, "reason": "chargeable_cancellation"}
