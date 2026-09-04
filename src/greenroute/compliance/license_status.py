# -*- coding: utf-8 -*-
"""
Pure resolution logic for the technician-compliance capability: turns a
raw TDA licensee record plus an as-of date into the license_status
GreenRoute actually trusts, and builds silver_technician_compliance.

pyspark/greenroute.common are imported lazily inside the Spark wrapper
below, not at module scope, so resolve_license_status stays importable
(and testable) with only pytest installed.
"""

_TERMINAL_STATUSES = ("revoked", "suspended")


def resolve_license_status(raw_status, expiry_date, as_of_date):
    """Resolve the license_status GreenRoute trusts for one technician.

    A license is still active ON its expiry_date and becomes expired only
    the day AFTER, regardless of what TDA's own status string says --
    unless TDA already reports a terminal status (revoked/suspended),
    which always wins over the date math.
    """
    if raw_status in _TERMINAL_STATUSES:
        return raw_status
    if as_of_date > expiry_date:
        return "expired"
    return "active"


def build_silver_technician_compliance(bronze_tda_df, technician_df, as_of_date):
    """Spark wrapper: resolve license_status per technician into
    silver_technician_compliance. Contains no decision logic of its own --
    it wraps resolve_license_status.
    """
    from pyspark.sql import functions as F
    from greenroute.common import spark_session, write_table

    spark = spark_session()
    resolve_udf = F.udf(
        lambda raw_status, expiry_date: resolve_license_status(
            raw_status, expiry_date, as_of_date
        )
    )
    joined = technician_df.join(bronze_tda_df, on="license_number", how="left")
    resolved = joined.withColumn(
        "license_status",
        resolve_udf(F.col("license_status"), F.col("expiry_date")),
    )
    write_table(resolved, "silver_technician_compliance", mode="overwrite")
    return resolved


# Match technicians to TDA records by license number, not name -- name
# matching produced silent false negatives on hyphenated and maiden names
# during the sprint 6 pilot.

def match_technician_to_license(technician_record, tda_records_by_license):
    """Match one technician to their TDA licensee record by license_number."""
    license_number = technician_record.get("license_number")
    if not license_number:
        return None
    return tda_records_by_license.get(license_number)


def match_technicians_to_licenses(technician_records, tda_records):
    """Batch version of match_technician_to_license."""
    by_license = {
        r["license_number"]: r for r in tda_records if r.get("license_number")
    }
    return {
        tech["technician_id"]: match_technician_to_license(tech, by_license)
        for tech in technician_records
    }


def carry_renewal_filed_date(tda_record):
    """The TDA lookup returns renewal_filed_date alongside status; carry it
    into silver_technician_compliance untouched so the scheduling gate can
    compute the grace window at booking time instead of re-querying TDA."""
    return {
        "license_number": tda_record.get("license_number"),
        "license_status": tda_record.get("license_status"),
        "expiry_date": tda_record.get("expiry_date"),
        "renewal_filed_date": tda_record.get("renewal_filed_date"),
    }
