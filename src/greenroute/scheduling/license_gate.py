# -*- coding: utf-8 -*-
"""
Hard gate for the technician-compliance capability: scheduling refuses to
confirm a booking for a TDA-licensed service unless the assigned
technician currently has an active license.
"""

LICENSE_REQUIRED_SERVICES = frozenset({"pesticide_application"})


def gate_licensed_service_booking(service_type, technician_license_status, license_service_reachable):
    """Decide whether a booking may be confirmed.

    Blocks confirmation of a licensed service (pesticide application
    today) unless the technician's license_status is "active".

    OPEN QUESTION (deliberately unresolved as of quarter end): if the TDA
    license service is unreachable at write time, this currently FAILS
    OPEN -- an unreachable license service does NOT block the booking.
    That is a real product/compliance tradeoff (a missed pesticide-license
    check vs. blocking bookings whenever TDA's lookup happens to be down)
    that product/legal has not decided. Do not silently change this to
    fail closed without that conversation happening first.
    """
    if service_type not in LICENSE_REQUIRED_SERVICES:
        return True, "service_not_licensed"
    if not license_service_reachable:
        # Fails open -- see the OPEN QUESTION above.
        return True, "license_service_unreachable_failed_open"
    if technician_license_status == "active":
        return True, "license_active"
    return False, "license_not_active"


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
