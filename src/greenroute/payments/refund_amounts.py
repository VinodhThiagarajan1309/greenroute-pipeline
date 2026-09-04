# -*- coding: utf-8 -*-
"""payments: refund amount bookkeeping.

Total refunded for a capture may never exceed the amount captured. Partial
refund amounts are stored explicitly on each refund row -- never inferred
by subtracting from the capture amount at read time.
"""


def remaining_refundable_cents(capture_amount_cents, already_refunded_cents):
    """Pure: how much of a capture is still refundable."""
    return capture_amount_cents - already_refunded_cents


def validate_refund_amount(capture_amount_cents, already_refunded_cents, requested_amount_cents):
    """Reject a refund that would push total refunded past the captured amount.

    Returns the validated amount (stored explicitly on the refund row) on
    success; raises ValueError otherwise.
    """
    if requested_amount_cents <= 0:
        raise ValueError("refund amount must be positive")
    remaining = remaining_refundable_cents(capture_amount_cents, already_refunded_cents)
    if requested_amount_cents > remaining:
        raise ValueError(
            "refund of %d cents exceeds remaining refundable %d cents on this capture"
            % (requested_amount_cents, remaining)
        )
    return requested_amount_cents
