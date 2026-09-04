# -*- coding: utf-8 -*-
"""Tests for technician-compliance license status resolution."""
import datetime as dt

from greenroute.compliance.license_status import resolve_license_status


def test_license_active_before_expiry():
    status = resolve_license_status(
        raw_status="active",
        expiry_date=dt.date(2026, 9, 10),
        as_of_date=dt.date(2026, 9, 9),
    )
    assert status == "active"


def test_license_still_active_on_expiry_date_itself():
    status = resolve_license_status(
        raw_status="active",
        expiry_date=dt.date(2026, 9, 10),
        as_of_date=dt.date(2026, 9, 10),
    )
    assert status == "active"


def test_license_expired_the_day_after_expiry_not_before():
    status = resolve_license_status(
        raw_status="active",
        expiry_date=dt.date(2026, 9, 10),
        as_of_date=dt.date(2026, 9, 11),
    )
    assert status == "expired"


def test_terminal_status_wins_regardless_of_expiry_date():
    status = resolve_license_status(
        raw_status="revoked",
        expiry_date=dt.date(2027, 1, 1),
        as_of_date=dt.date(2026, 9, 9),
    )
    assert status == "revoked"
