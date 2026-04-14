# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""service-catalog capability: service types, add-ons, zone pricing tiers,
and the license-required flag scheduling gates on.

Pure functions only - no pyspark import here on purpose, so this module
(and the pytest suite that exercises it) never needs Spark installed. The
Spark transform that writes silver_service_catalog lives in
greenroute.service_catalog.catalog_spark and wraps these functions.
"""

from decimal import Decimal
from datetime import datetime


class UnknownServiceType(Exception):
    """Raised when a booking references a service_type_id with no active
    catalog row. Callers must quarantine on this error, never default."""


def resolve_service_type(catalog_rows, service_type_id):
    """Return the single active catalog row for service_type_id.

    Exactly one active row must exist per billable service type. A booking
    referencing an unknown service type is quarantined by the caller,
    never defaulted.
    """
    matches = [
        row for row in catalog_rows
        if row["service_type_id"] == service_type_id and row.get("is_active")
    ]
    if not matches:
        raise UnknownServiceType(service_type_id)
    if len(matches) > 1:
        raise ValueError("multiple active catalog rows for %r" % (service_type_id,))
    return matches[0]


def to_billing_decimal(value):
    """Coerce a price to the DECIMAL(10,2) shape the billing system
    expects - tightened from an earlier DECIMAL(10,4) representation used
    when the silver_service_catalog transform was first added; the
    billing system stores unit_price as DECIMAL(10,2) exactly."""
    return Decimal(str(value)).quantize(Decimal("0.01"))


def build_catalog_row(
    service_type_id,
    display_name,
    unit_price,
    license_required,
    zone_tier=None,
    is_active=True,
    effective_start=None,
    effective_end=None,
):
    """Construct a service-catalog row.

    license_required is always an explicit flag stored on the row - it is
    never inferred from service_type_id or display_name. Renaming
    "pesticide-application" to something else can never silently disable
    the license gate, because the gate reads this flag, not the name.
    """
    return {
        "service_type_id": service_type_id,
        "display_name": display_name,
        "unit_price": to_billing_decimal(unit_price),
        "license_required": bool(license_required),
        "zone_tier": zone_tier,
        "is_active": is_active,
        "effective_start": effective_start,
        "effective_end": effective_end,
    }


# Backfilled zone -> pricing tier assignment for the zones GreenRoute
# served as of sprint 2 (38 zones total; a representative subset is shown
# here). New zones must be assigned a tier explicitly - there is no
# default tier.
ZONE_TIER_BY_ZONE = {
    "zilker": "tier_1",
    "mueller": "tier_1",
    "circle_c": "tier_2",
    "round_rock": "tier_2",
    "pflugerville": "tier_2",
    "hyde_park": "tier_1",
    "south_congress": "tier_1",
    "cedar_park": "tier_3",
    "manor": "tier_3",
    "del_valle": "tier_3",
}


def zone_tier_for(zone_id):
    """Look up the pricing tier for a zone. Unknown zones are not
    defaulted - callers must quarantine bookings whose zone has no tier
    assignment rather than guess a tier."""
    return ZONE_TIER_BY_ZONE.get(zone_id)


class OverlappingActivePrice(Exception):
    """Raised when two active price rows for the same (service_type_id,
    zone_tier) have overlapping effective date ranges."""


def _date_ranges_overlap(start_a, end_a, start_b, end_b):
    end_a = end_a or datetime.max
    end_b = end_b or datetime.max
    return start_a < end_b and start_b < end_a


def validate_no_overlapping_active_prices(price_rows):
    """Reject AT WRITE TIME if two active price rows exist for the same
    (service_type_id, zone_tier) with overlapping effective date ranges.
    Exactly one active price per (service_type, zone_tier) is a hard
    invariant.
    """
    by_key = {}
    for row in price_rows:
        if not row.get("is_active"):
            continue
        key = (row["service_type_id"], row["zone_tier"])
        for other in by_key.get(key, []):
            if _date_ranges_overlap(
                row["effective_start"], row.get("effective_end"),
                other["effective_start"], other.get("effective_end"),
            ):
                raise OverlappingActivePrice(key)
        by_key.setdefault(key, []).append(row)
    return price_rows


def resolve_active_price(price_rows, service_type_id, zone_tier):
    """Return the single active price row for (service_type_id, zone_tier)."""
    matches = [
        row for row in price_rows
        if row["service_type_id"] == service_type_id
        and row["zone_tier"] == zone_tier
        and row.get("is_active")
    ]
    if not matches:
        raise UnknownServiceType((service_type_id, zone_tier))
    if len(matches) > 1:
        raise OverlappingActivePrice((service_type_id, zone_tier))
    return matches[0]


def attach_addon_to_booking(addon_row, booking_id, quantity=1):
    """Attach a catalog add-on to a booking, freezing its price at the
    moment of attachment.

    Add-ons attach to a BOOKING, never to a service type, and this frozen
    amount is what gets billed - later changes to addon_row's unit_price
    must never rewrite history.
    """
    frozen_unit_price = to_billing_decimal(addon_row["unit_price"])
    return {
        "booking_id": booking_id,
        "addon_type_id": addon_row["addon_type_id"],
        "frozen_unit_price": frozen_unit_price,
        "quantity": quantity,
        "frozen_amount": (frozen_unit_price * quantity).quantize(Decimal("0.01")),
    }


def billable_addon_amount(booking_addon, booking_status):
    """An add-on on a cancelled booking is not billed, regardless of its
    frozen price."""
    if booking_status == "cancelled":
        return Decimal("0.00")
    return booking_addon["frozen_amount"]


# Every service type declares license_required explicitly. The scheduling
# gate reads this flag and nothing else, so adding a licensed service is a
# catalog row, never a scheduling change.
LICENSED_SERVICE_TYPES = ("pesticide_application", "herbicide_application", "fertilizer_application")


def seed_service_type_rows():
    """Catalog seed rows with the licence flag set per TDA rules."""
    rows = [
        ("mowing", "Lawn mowing", "45.00", False),
        ("mulching", "Mulching", "80.00", False),
        ("pesticide_application", "Pesticide application", "120.00", True),
        ("herbicide_application", "Herbicide application", "95.00", True),
        ("fertilizer_application", "Fertilizer application", "70.00", True),
    ]
    return [build_catalog_row(sid, name, price, lic) for sid, name, price, lic in rows]
