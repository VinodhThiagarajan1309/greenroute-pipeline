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


def derive_watermark_hours(measured_max_minutes, round_to_hours=12):
    """Derive a watermark from a MEASURED max lateness, never an assumed one.

    Round the measured max lateness up to the next `round_to_hours` boundary.
    For bronze_booking_cancellations the measured max was 36h12m; rounded up
    to the next 12h boundary that is 48h, which is also comfortably above the
    measured p99 of 11h.
    """
    hours = measured_max_minutes / 60.0
    boundaries = int(hours // round_to_hours)
    if hours % round_to_hours:
        boundaries += 1
    return round_to_hours * boundaries


def watermark_has_headroom(watermark_hours, measured_p99_minutes, measured_max_minutes):
    """A watermark must clear both the measured p99 and the measured max."""
    watermark_minutes = watermark_hours * 60
    return watermark_minutes > measured_p99_minutes and watermark_minutes >= measured_max_minutes


# Derived from BOOKING_CANCELLATION_LATENESS_MINUTES above: measured p99 was
# 11h, measured max was 36h12m -- caused by the mobile app queueing offline
# cancellations in dead zones (Circle C worst) until the phone regains
# signal. 48h is the observed max rounded up to the next 12h boundary.
CANCELLATION_WATERMARK_HOURS = derive_watermark_hours(
    BOOKING_CANCELLATION_LATENESS_MINUTES["max"]
)

assert CANCELLATION_WATERMARK_HOURS == 48
assert watermark_has_headroom(
    CANCELLATION_WATERMARK_HOURS,
    BOOKING_CANCELLATION_LATENESS_MINUTES["p99"],
    BOOKING_CANCELLATION_LATENESS_MINUTES["max"],
)
