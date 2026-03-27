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
