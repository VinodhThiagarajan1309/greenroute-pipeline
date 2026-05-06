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


# wip: end-to-end zip onboarding


def assign_pricing_tier(zone, service, pricing_tier_by_zone_and_service):
    """Pricing tier hangs off zone, never zip -- this is the only pricing
    lookup onboarding needs once a zone exists.
    """
    return pricing_tier_by_zone_and_service.get((zone, service))


def onboard_zone(zone, zips, effective_date, pricing_by_service):
    """wip: draft end-to-end onboarding -- register zips and stage
    pricing. Technician coverage gating and verification land in the next
    two commits.
    """
    registry_rows = [
        {"zip": z, "zone": zone, "effective_date": effective_date, "source_note": "onboarding"}
        for z in zips
    ]
    pricing_rows = [
        {"zone": zone, "service": service, "tier": tier}
        for service, tier in pricing_by_service.items()
    ]
    return {"registry_rows": registry_rows, "pricing_rows": pricing_rows}
