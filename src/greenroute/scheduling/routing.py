# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""scheduling capability: zone-based route optimization.

NOTE: the original PR that started this module (this commit and the next)
was closed, not merged - its drive-time fix was later re-ported into the
merged scheduling-zone-routing-v2 change below.
"""

import math


def _haversine_km(lat1, lon1, lat2, lon2):
    """Great-circle distance - kept only for reference. Route ordering
    must NOT use this; see order_stops_by_distance below and its
    drive-time replacement further down."""
    r = 6371.0
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dlambda / 2) ** 2
    return 2 * r * math.asin(math.sqrt(a))


def order_stops_by_distance(stops):
    """wip: order stops by straight-line (haversine) distance from the
    previous stop. This is the buggy version - see the drive-time fix."""
    ordered = [stops[0]]
    remaining = list(stops[1:])
    while remaining:
        last = ordered[-1]
        remaining.sort(key=lambda s: _haversine_km(last["lat"], last["lon"], s["lat"], s["lon"]))
        ordered.append(remaining.pop(0))
    return ordered


def order_stops_by_drive_time(stops, drive_time_minutes):
    """Order stops using actual drive time between them (drive_time_minutes
    is a {(from_stop_id, to_stop_id): minutes} lookup from the routing
    provider), not haversine distance - straight-line distance ignores
    roads, one-ways and I-35 traffic and produced bad routes.
    """
    if not stops:
        return []
    ordered = [stops[0]]
    remaining = list(stops[1:])
    while remaining:
        last_id = ordered[-1]["stop_id"]
        remaining.sort(key=lambda s: drive_time_minutes[(last_id, s["stop_id"])])
        ordered.append(remaining.pop(0))
    return ordered
