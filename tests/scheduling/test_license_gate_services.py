# -*- coding: utf-8 -*-
"""Sprint 7: the gate reads the catalog flag, not a list of service names."""
from greenroute.scheduling.license_gate import gate_licensed_service_booking
from greenroute.service_catalog.catalog import seed_service_type_rows


def _row(service_type_id):
    return next(r for r in seed_service_type_rows() if r["service_type_id"] == service_type_id)


def test_herbicide_with_expired_licence_is_blocked():
    allowed, reason = gate_licensed_service_booking(_row("herbicide_application"), "expired", True)
    assert not allowed and reason == "license_not_active"


def test_fertilizer_with_expired_licence_is_blocked():
    allowed, _ = gate_licensed_service_booking(_row("fertilizer_application"), "expired", True)
    assert not allowed


def test_mowing_with_the_same_technician_is_not_gated():
    allowed, reason = gate_licensed_service_booking(_row("mowing"), "expired", True)
    assert allowed and reason == "service_not_licensed"


def test_catalog_declares_the_flag_on_every_row():
    assert all("license_required" in r for r in seed_service_type_rows())
