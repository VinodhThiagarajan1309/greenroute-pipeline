# -*- coding: utf-8 -*-
"""
Hard gate for the technician-compliance capability: scheduling refuses to
confirm a booking for a TDA-licensed service unless the assigned
technician currently has an active license.
"""





def build_license_gate_blocked_metric(technician_id, service_type, reason):
    """Pure metric payload for when the license gate blocks a booking.

    Anything that gates or blocks must emit a metric saying it fired --
    this is that metric for the pesticide-license hard gate.
    """
    return {
        "metric": "license_gate_blocked",
        "technician_id": technician_id,
        "service_type": service_type,
        "reason": reason,
    }


def evaluate_booking_and_metric(service_type, technician_id, technician_license_status, license_service_reachable):
    """Convenience wrapper: gate decision plus the metric payload to emit
    if the booking is blocked.
    """
    allowed, reason = gate_licensed_service_booking(
        service_type, technician_license_status, license_service_reachable
    )
    metric = None
    if not allowed:
        metric = build_license_gate_blocked_metric(technician_id, service_type, reason)
    return allowed, reason, metric


"""
Hard gate for the technician-compliance capability: scheduling refuses to
confirm a booking for a TDA-licensed service unless the assigned
technician currently has an active license -- or, since sprint 7, a
pending renewal that TDA still honours.
"""
import datetime as dt


# TDA keeps an applicator legal for this long after expiry, provided the
# renewal was filed on or before the expiry date.
TDA_RENEWAL_GRACE_DAYS = 30


def within_renewal_grace(renewal_filed_date, expiry_date, booking_date):
    """True when a pending renewal is still inside the TDA grace window.

    Good THROUGH day 30 after expiry, blocked from day 31. A renewal filed
    after the licence expired never qualifies.
    """
    if renewal_filed_date is None or expiry_date is None or booking_date is None:
        return False
    if renewal_filed_date > expiry_date:
        return False
    return booking_date <= expiry_date + dt.timedelta(days=TDA_RENEWAL_GRACE_DAYS)


LICENSE_REQUIRED_SERVICES = frozenset({
    # Kept only as the fallback for callers that still pass a bare
    # service_type_id string. The gate reads the catalog row's
    # license_required flag whenever it is given the row.
    "pesticide_application",
    "herbicide_application",
    "fertilizer_application",
})


def _license_required(service_type):
    if isinstance(service_type, dict):
        return bool(service_type.get("license_required"))
    return service_type in LICENSE_REQUIRED_SERVICES


def gate_licensed_service_booking(service_type, technician_license_status, license_service_reachable,
                                  renewal_filed_date=None, expiry_date=None, booking_date=None):
    """Decide whether a booking may be confirmed.

    `service_type` is a catalog row (preferred) or a service_type_id. The
    gate reads the row's license_required flag; it does not know service
    names. Blocks unless license_status is "active", or "pending_renewal"
    inside the TDA grace window.

    OPEN QUESTION (deliberately unresolved): an unreachable TDA lookup
    FAILS OPEN. Product/legal has not decided. Do not change silently.
    """
    if not _license_required(service_type):
        return True, "service_not_licensed"
    if not license_service_reachable:
        return True, "license_service_unreachable_failed_open"
    if technician_license_status == "active":
        return True, "license_active"
    if technician_license_status == "pending_renewal" and within_renewal_grace(
            renewal_filed_date, expiry_date, booking_date):
        return True, "license_pending_renewal_grace"
    return False, "license_not_active"
