# -*- coding: utf-8 -*-
"""
Onboarding workflow for the neighborhood-expansion capability: register
zips, assign pricing tier per service, confirm technician coverage,
verify.
"""
from greenroute.expansion.zone_registry import zone_for_zip


def requeue_quarantined_bookings(quarantined_bookings, registry_by_zip):
    """Re-run scheduling-baseline's zone-unresolvable quarantined bookings
    against zone_registry. Returns (resolved, still_quarantined) -- this
    is what finally lets bookings quarantined against un-onboarded
    subdivisions (e.g. the two Pflugerville subdivisions) get re-driven
    once their zips are registered.
    """
    resolved = []
    still_quarantined = []
    for booking in quarantined_bookings:
        zone = zone_for_zip(booking["zip"], registry_by_zip)
        if zone is None:
            still_quarantined.append(booking)
        else:
            resolved.append(dict(booking, zone=zone))
    return resolved, still_quarantined
