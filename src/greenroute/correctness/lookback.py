# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""data-correctness: bound the incremental/batch parity lookback window.

Recon must not rescan full history on every run. Bound it to a lookback
window instead -- but the lookback must stay strictly wider than the
data-completeness watermark, or the two checks disagree with each other:
recon would compare a window completeness hasn't even finished publishing.
"""
from __future__ import annotations

from datetime import timedelta


def lookback_window(now, lookback_hours):
    """The [start, end) window recon should scan, bounded to `lookback_hours`."""
    start = now - timedelta(hours=lookback_hours)
    return start, now


def rows_in_window(rows, window_start, window_end, timestamp_field):
    """Filter rows to those whose `timestamp_field` falls in [window_start, window_end)."""
    return [
        row for row in rows
        if window_start <= row[timestamp_field] < window_end
    ]
