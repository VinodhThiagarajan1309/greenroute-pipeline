# -*- coding: utf-8 -*-
"""
Bronze ingestion of the Texas Department of Agriculture (TDA) applicator
license roster for the technician-compliance capability.

Imports pyspark/greenroute.common lazily, inside the function that needs
them, so this module stays importable (for its pure-function siblings'
tests) in a pytest-only environment with no Spark installed.
"""


def _tda_license_schema():
    from pyspark.sql import types as T

    return T.StructType([
        T.StructField("license_number", T.StringType(), False),
        T.StructField("licensee_name", T.StringType(), False),
        T.StructField("license_status", T.StringType(), False),
        T.StructField("expiry_date", T.DateType(), False),
        T.StructField("fetched_at", T.TimestampType(), False),
    ])


def ingest_bronze_tda_licenses(raw_rows):
    """Land raw TDA licensee-lookup responses as bronze_tda_licenses.

    `raw_rows` comes from the TDA lookup, one license number per request
    (there is no bulk endpoint). This just types and writes them; the
    per-license rate limiting lives in refresh.py.
    """
    from pyspark.sql import functions as F
    from greenroute.common import spark_session, write_table, quarantine

    spark = spark_session()
    df = spark.createDataFrame(raw_rows, schema=_tda_license_schema())
    good = df.filter(F.col("license_number").isNotNull())
    bad = df.filter(F.col("license_number").isNull())
    quarantine(bad, table="bronze_tda_licenses", reason="missing_license_number")
    write_table(good, "bronze_tda_licenses", mode="merge", key="license_number")
    return good
