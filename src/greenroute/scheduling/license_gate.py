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

LICENSE_REQUIRED_SERVICES = frozenset({"pesticide_application"})

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


def gate_licensed_service_booking(service_type, technician_license_status, license_service_reachable,
                                  renewal_filed_date=None, expiry_date=None, booking_date=None):
    """Decide whether a booking may be confirmed.

    Blocks confirmation of a licensed service unless the technician's
    license_status is "active", or is "pending_renewal" inside the TDA
    grace window.

    OPEN QUESTION (deliberately unresolved): if the TDA license service is
    unreachable at write time this FAILS OPEN. Product/legal has not
    decided fail-open vs fail-closed. Do not change silently.
    """
    if service_type not in LICENSE_REQUIRED_SERVICES:
        return True, "service_not_licensed"
    if not license_service_reachable:
        return True, "license_service_unreachable_failed_open"
    if technician_license_status == "active":
        return True, "license_active"
    if technician_license_status == "pending_renewal" and within_renewal_grace(
            renewal_filed_date, expiry_date, booking_date):
        return True, "license_pending_renewal_grace"
    return False, "license_not_active"
