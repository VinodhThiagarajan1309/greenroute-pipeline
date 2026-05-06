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


MIN_TECHNICIANS_PER_ZONE = 2


def check_technician_coverage(zone, technician_count, min_technicians=MIN_TECHNICIANS_PER_ZONE):
    """Gate: a zone is not onboarding-complete without enough technician
    coverage. Emits a metric when it blocks, per house style.
    """
    if technician_count >= min_technicians:
        return True, None
    return False, build_coverage_gate_metric(zone, technician_count, min_technicians)


def build_coverage_gate_metric(zone, technician_count, min_technicians):
    return {
        "metric": "onboarding_blocked_insufficient_coverage",
        "zone": zone,
        "technician_count": technician_count,
        "min_technicians": min_technicians,
    }


def verify_zone_onboarded(zone, zips_registered, pricing_rows, technician_count, min_technicians=MIN_TECHNICIANS_PER_ZONE):
    """Final verify step: zips registered, pricing assigned for every
    service, and technician coverage confirmed.
    """
    coverage_ok, coverage_metric = check_technician_coverage(zone, technician_count, min_technicians)
    return {
        "zone": zone,
        "zips_registered": bool(zips_registered),
        "pricing_assigned": bool(pricing_rows),
        "technician_coverage_ok": coverage_ok,
        "onboarded": bool(zips_registered) and bool(pricing_rows) and coverage_ok,
        "coverage_metric": coverage_metric,
    }
