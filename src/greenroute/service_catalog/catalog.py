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
