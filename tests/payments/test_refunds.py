# -*- coding: utf-8 -*-
"""Tests for payments refund state transitions and amount limits."""
import pytest

from greenroute.payments.refunds import (
    REFUND_STATE_REQUESTED,
    REFUND_STATE_SUCCEEDED,
    transition_refund_state,
)
from greenroute.payments.refund_amounts import validate_refund_amount


def test_refund_transitions_requested_to_succeeded():
    assert transition_refund_state(REFUND_STATE_REQUESTED, REFUND_STATE_SUCCEEDED) == REFUND_STATE_SUCCEEDED


def test_illegal_refund_transition_rejected():
    with pytest.raises(ValueError):
        transition_refund_state(REFUND_STATE_SUCCEEDED, REFUND_STATE_REQUESTED)


def test_refund_exceeding_capture_is_rejected():
    with pytest.raises(ValueError):
        validate_refund_amount(capture_amount_cents=5000, already_refunded_cents=0, requested_amount_cents=5001)


def test_refund_within_captured_amount_is_accepted():
    assert (
        validate_refund_amount(capture_amount_cents=5000, already_refunded_cents=1000, requested_amount_cents=4000)
        == 4000
    )
