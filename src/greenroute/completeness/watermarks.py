# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""data-completeness: per-source watermarks tracking maximum observed lateness.

Every source that feeds a gold partition declares a maximum expected lateness.
That number is derived from measurement of how late records for that source
have actually arrived historically -- never assumed or picked as a round
number.
"""
from __future__ import annotations

from datetime import timedelta


# Measured lateness distribution for bronze_booking_cancellations, in minutes.
# The tail is caused by the mobile app queueing offline actions: technicians
# cancel on-site in dead zones (Circle C is the worst offender) and the app
# only syncs the cancellation once the phone regains signal.
BOOKING_CANCELLATION_LATENESS_MINUTES = {
    "p50": 4,
    "p90": 51,
    "p99": 660,      # 11h
    "max": 2172,     # 36h12m
}


def watermark_table_row(source, measured_lateness_minutes, watermark_hours):
    """Build one row of the watermark table: max observed lateness per source.

    This is the row that gates gold publish -- see completeness/gate.py.
    """
    return {
        "source": source,
        "measured_p50_minutes": measured_lateness_minutes["p50"],
        "measured_p90_minutes": measured_lateness_minutes["p90"],
        "measured_p99_minutes": measured_lateness_minutes["p99"],
        "measured_max_minutes": measured_lateness_minutes["max"],
        "watermark_hours": watermark_hours,
    }


def watermark_closes_at(window_end, watermark_hours):
    """The instant a source's watermark for a window closes."""
    return window_end + timedelta(hours=watermark_hours)
