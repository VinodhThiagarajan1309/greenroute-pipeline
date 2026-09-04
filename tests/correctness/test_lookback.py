# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""Tests for the data-correctness incremental lookback window."""
from datetime import datetime, timedelta

from greenroute.correctness.lookback import (
    lookback_window,
    rows_in_window,
    lookback_is_wider_than_watermark,
    RECON_LOOKBACK_HOURS,
)
from greenroute.completeness.watermarks import CANCELLATION_WATERMARK_HOURS


def test_lookback_is_strictly_wider_than_the_completeness_watermark():
    assert RECON_LOOKBACK_HOURS > CANCELLATION_WATERMARK_HOURS
    assert lookback_is_wider_than_watermark()


def test_recon_and_completeness_agree_at_the_48h_boundary():
    now = datetime(2026, 3, 3, 0, 0, 0)
    window_start, window_end = lookback_window(now, RECON_LOOKBACK_HOURS)

    # A row that just barely closed its completeness watermark (exactly 48h
    # before "now") must still fall inside recon's lookback window, or the
    # two checks disagree about whether that row is in scope.
    boundary_row = {
        "schedule_event_id": "se-1",
        "event_time": now - timedelta(hours=CANCELLATION_WATERMARK_HOURS),
    }

    assert rows_in_window([boundary_row], window_start, window_end, "event_time") == [boundary_row]


def test_row_outside_the_lookback_window_is_excluded():
    now = datetime(2026, 3, 3, 0, 0, 0)
    window_start, window_end = lookback_window(now, RECON_LOOKBACK_HOURS)

    ancient_row = {
        "schedule_event_id": "se-old",
        "event_time": now - timedelta(hours=RECON_LOOKBACK_HOURS + 10),
    }

    assert rows_in_window([ancient_row], window_start, window_end, "event_time") == []
