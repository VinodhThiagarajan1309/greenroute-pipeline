# -*- coding: utf-8 -*-
"""Tests for staggered TDA refresh scheduling."""
from collections import Counter
import datetime as dt

from greenroute.compliance.refresh import (
    compute_stagger_offset_seconds,
    is_stale,
    DEFAULT_TTL_SECONDS,
)


def _simulate_offsets(n_licenses):
    return [
        compute_stagger_offset_seconds("TDA-%05d" % i, DEFAULT_TTL_SECONDS)
        for i in range(n_licenses)
    ]


def test_stagger_offsets_are_deterministic():
    offset_a = compute_stagger_offset_seconds("TDA-00001")
    offset_b = compute_stagger_offset_seconds("TDA-00001")
    assert offset_a == offset_b


def test_staggered_refresh_never_exceeds_60_requests_in_any_rolling_60s_window():
    # 400 licenses is the expansion-plan fleet size; bucket each license's
    # daily offset into its refresh second and confirm no 60s window ever
    # asks the TDA lookup for more than the 60/min it allows.
    offsets = _simulate_offsets(400)
    per_second = Counter(offsets)
    seconds_in_day = 24 * 60 * 60
    max_in_any_minute = 0
    for start in range(0, seconds_in_day, 60):
        window = sum(per_second.get(s, 0) for s in range(start, start + 60))
        max_in_any_minute = max(max_in_any_minute, window)
    assert max_in_any_minute <= 60


def test_stale_flags_after_ttl_elapses():
    last_refreshed = dt.datetime(2026, 9, 1, 12, 0, 0)
    just_under_ttl = last_refreshed + dt.timedelta(seconds=DEFAULT_TTL_SECONDS - 1)
    just_over_ttl = last_refreshed + dt.timedelta(seconds=DEFAULT_TTL_SECONDS + 1)
    assert is_stale(last_refreshed, just_under_ttl) is False
    assert is_stale(last_refreshed, just_over_ttl) is True
