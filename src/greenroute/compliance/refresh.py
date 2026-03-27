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
