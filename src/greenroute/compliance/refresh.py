# -*- coding: utf-8 -*-
"""
Per-license TTL and staggered refresh scheduling for TDA licensee
lookups, for the technician-compliance capability.

The TDA licensee lookup is ONE REQUEST PER LICENSE NUMBER, rate limited to
60/min, with no bulk endpoint and no SLA. At 47 licensed applicators today
a full refresh sweep is trivial; the expansion plan implies ~400 licenses,
which at one request per license would be 7+ minutes of sustained
requests if refreshed all at once. A per-license TTL with staggered
refresh keeps the fleet's lookups spread across the day instead of
stampeding the endpoint.
"""
import hashlib
import datetime as dt

REFRESH_WINDOW_SECONDS = 24 * 60 * 60


def compute_stagger_offset_seconds(license_number, window_seconds=REFRESH_WINDOW_SECONDS):
    """Deterministically spread a license's refresh across `window_seconds`.

    Hashing license_number gives a stable, evenly distributed offset so
    the same license refreshes at roughly the same time each day, and
    different licenses land at different times with no coordination
    between them.
    """
    digest = hashlib.sha256(license_number.encode("utf-8")).hexdigest()
    return int(digest, 16) % window_seconds


DEFAULT_TTL_SECONDS = 24 * 60 * 60


def compute_next_refresh_at(license_number, last_refreshed_at, ttl_seconds=DEFAULT_TTL_SECONDS):
    """Next time this license is due for a TDA refresh.

    Combines the per-license TTL with the staggered offset so refreshes
    for different licenses don't clump even if they were all last
    refreshed at the same moment (e.g. after a backfill).
    """
    offset = compute_stagger_offset_seconds(license_number, ttl_seconds)
    day_start = last_refreshed_at.replace(hour=0, minute=0, second=0, microsecond=0)
    candidate = day_start + dt.timedelta(seconds=offset)
    if candidate <= last_refreshed_at:
        candidate += dt.timedelta(seconds=ttl_seconds)
    return candidate
