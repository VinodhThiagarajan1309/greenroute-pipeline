# -*- coding: utf-8 -*-
from decimal import Decimal

from greenroute.service_catalog.catalog import (
    attach_addon_to_booking,
    billable_addon_amount,
)


def test_addon_on_cancelled_booking_not_billed():
    addon_row = {"addon_type_id": "fire_ant_treatment", "unit_price": Decimal("15.00")}
    booking_addon = attach_addon_to_booking(addon_row, "bk-1")
    assert billable_addon_amount(booking_addon, "cancelled") == Decimal("0.00")


def test_addon_on_active_booking_is_billed():
    addon_row = {"addon_type_id": "fire_ant_treatment", "unit_price": Decimal("15.00")}
    booking_addon = attach_addon_to_booking(addon_row, "bk-2")
    assert billable_addon_amount(booking_addon, "confirmed") == Decimal("15.00")


def test_addon_price_frozen_survives_later_catalog_price_change():
    addon_row = {"addon_type_id": "mulch_upgrade", "unit_price": Decimal("20.00")}
    booking_addon = attach_addon_to_booking(addon_row, "bk-3", quantity=2)
    addon_row["unit_price"] = Decimal("35.00")  # later catalog price change
    assert booking_addon["frozen_amount"] == Decimal("40.00")
