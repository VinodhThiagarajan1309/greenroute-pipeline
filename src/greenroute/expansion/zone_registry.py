# -*- coding: utf-8 -*-
"""
zone_registry: the single source of truth for zip -> zone, for the
neighborhood-expansion capability. Pricing tier hangs off zone, not zip --
callers should only ever need to ask zone, never zip, once a zip has been
resolved to its zone here.

The pyspark schema and greenroute.common are imported lazily, inside the
functions that need them, so the pure zip->zone lookups here stay
importable in a pytest-only environment with no Spark installed.
"""


def zone_registry_schema():
    from pyspark.sql import types as T

    return T.StructType([
        T.StructField("zip", T.StringType(), False),
        T.StructField("zone", T.StringType(), False),
        T.StructField("effective_date", T.DateType(), False),
        T.StructField("source_note", T.StringType(), False),
    ])


def zone_for_zip(zip_code, registry_by_zip):
    """Resolve a zip to its zone via the registry. No fallback to a local dict."""
    entry = registry_by_zip.get(zip_code)
    if entry is None:
        return None
    return entry["zone"]


def find_source_disagreements(registry_by_zip, other_source_by_zip):
    """Compare zone_registry against another zip->zone source (the old
    routing dict, the DAB CSV, ops' spreadsheet) and return the zips where
    they disagree, so reconciliation has a concrete worklist instead of a
    hand audit.
    """
    disagreements = []
    for zip_code, other_zone in other_source_by_zip.items():
        registry_entry = registry_by_zip.get(zip_code)
        registry_zone = registry_entry["zone"] if registry_entry else None
        if registry_zone != other_zone:
            disagreements.append({
                "zip": zip_code,
                "registry_zone": registry_zone,
                "other_source_zone": other_zone,
            })
    return disagreements
