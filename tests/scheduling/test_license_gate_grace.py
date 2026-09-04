# -*- coding: utf-8 -*-
"""Sprint 7: the TDA 30-day renewal grace window on the licence gate."""
import datetime as dt

from greenroute.scheduling.license_gate import gate_licensed_service_booking

EXPIRY = dt.date(2026, 4, 1)


def _gate(booking_date, filed=dt.date(2026, 3, 28), status="pending_renewal"):
    return gate_licensed_service_booking(
        "pesticide_application", status, True,
        renewal_filed_date=filed, expiry_date=EXPIRY, booking_date=booking_date,
    )


def test_renewal_filed_before_expiry_passes_through_day_30():
    allowed, reason = _gate(EXPIRY + dt.timedelta(days=30))
    assert allowed and reason == "license_pending_renewal_grace"


def test_renewal_is_blocked_from_day_31():
    allowed, reason = _gate(EXPIRY + dt.timedelta(days=31))
    assert not allowed and reason == "license_not_active"


def test_renewal_filed_after_expiry_never_passes():
    allowed, _ = _gate(EXPIRY + dt.timedelta(days=1), filed=EXPIRY + dt.timedelta(days=1))
    assert not allowed


def test_expired_without_renewal_is_still_blocked():
    allowed, reason = _gate(EXPIRY + dt.timedelta(days=1), filed=None, status="expired")
    assert not allowed and reason == "license_not_active"
