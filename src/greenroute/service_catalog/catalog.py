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
