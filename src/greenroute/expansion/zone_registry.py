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


def seed_registry_from_routing_dict(routing_zip_to_zone, effective_date):
    """Turn the routing module's hardcoded zip->zone dict into
    zone_registry rows. That dict is today's de facto source of truth;
    seeding from it gives zone_registry a starting point before
    reconciliation replaces it entirely (see
    expansion-zip-onboarding-workflow).
    """
    return [
        {
            "zip": zip_code,
            "zone": zone,
            "effective_date": effective_date,
            "source_note": "seeded_from_routing_module_dict",
        }
        for zip_code, zone in routing_zip_to_zone.items()
    ]


def write_zone_registry(spark_rows):
    """Spark wrapper: write seeded/updated rows into the zone_registry table."""
    from greenroute.common import spark_session, write_table

    spark = spark_session()
    df = spark.createDataFrame(spark_rows, schema=zone_registry_schema())
    write_table(df, "zone_registry", mode="merge", key="zip")
    return df


def migrate_legacy_mapping_to_registry(legacy_zip_to_zone, effective_date, source_note="migrated_from_legacy_sources"):
    """Migrate a legacy zip->zone mapping (the routing dict, or the DAB
    CSV) into zone_registry rows. zone_registry is now the single source
    of truth for zip -> zone; this is the one-time migration path, not an
    ongoing sync.
    """
    return [
        {
            "zip": zip_code,
            "zone": zone,
            "effective_date": effective_date,
            "source_note": source_note,
        }
        for zip_code, zone in legacy_zip_to_zone.items()
    ]


# The 4 zips where the old routing dict / DAB CSV disagreed with ops'
# spreadsheet, all in the Round Rock / Pflugerville seam -- exactly where
# GreenRoute is expanding. Ops' spreadsheet is authoritative here.
SEAM_ZIP_RESOLUTIONS = {
    "78664": "pflugerville",
    "78665": "round_rock",
    "78681": "pflugerville",
    "78660": "pflugerville",
}


def apply_seam_reconciliation(registry_rows, effective_date):
    """Overwrite the seam zips' zone with the reconciled (ops' spreadsheet)
    value, tagging the source_note so the reconciliation is auditable.
    """
    reconciled = []
    for row in registry_rows:
        if row["zip"] in SEAM_ZIP_RESOLUTIONS:
            reconciled.append({
                "zip": row["zip"],
                "zone": SEAM_ZIP_RESOLUTIONS[row["zip"]],
                "effective_date": effective_date,
                "source_note": "reconciled_round_rock_pflugerville_seam",
            })
        else:
            reconciled.append(row)
    return reconciled
