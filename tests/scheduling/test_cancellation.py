# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

from greenroute.scheduling.cancellation import (
    is_chargeable_cancellation,
    CANCELLATION_THRESHOLD_HOURS,
)


def test_cancel_exactly_on_the_boundary_is_chargeable():
    window_start = datetime(2026, 3, 10, 14, 0, 0)
    cancelled_at = window_start - timedelta(hours=CANCELLATION_THRESHOLD_HOURS)
    assert is_chargeable_cancellation(cancelled_at, window_start) is True


def test_cancel_before_the_boundary_is_free():
    window_start = datetime(2026, 3, 10, 14, 0, 0)
    cancelled_at = window_start - timedelta(hours=CANCELLATION_THRESHOLD_HOURS, minutes=1)
    assert is_chargeable_cancellation(cancelled_at, window_start) is False
