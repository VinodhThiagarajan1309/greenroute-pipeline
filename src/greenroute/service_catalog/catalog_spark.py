# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""service-catalog capability: Spark transform for silver_service_catalog.

Pure decision logic (service-type resolution, pricing, add-ons) lives in
greenroute.service_catalog.catalog and is never imported by tests through
this module - this file only wraps the real Spark read/write.
"""

import pyspark.sql.functions as F
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    BooleanType,
    DecimalType,
    TimestampType,
)

from greenroute.common import spark_session, read_table, write_table, quarantine

SERVICE_CATALOG_SCHEMA = StructType([
    StructField("service_type_id", StringType(), nullable=False),
    StructField("display_name", StringType(), nullable=False),
    StructField("unit_price", DecimalType(10, 2), nullable=False),
    StructField("license_required", BooleanType(), nullable=False),
    StructField("zone_tier", StringType(), nullable=True),
    StructField("is_active", BooleanType(), nullable=False),
    StructField("effective_start", TimestampType(), nullable=False),
    StructField("effective_end", TimestampType(), nullable=True),
])


def silver_service_catalog(spark=None):
    """bronze_service_catalog -> silver_service_catalog.

    A service_type_id with more than one active row is quarantined rather
    than dropped or arbitrarily collapsed to one - exactly one active row
    per billable service type is a hard invariant. unit_price is carried
    as DECIMAL(10,2) to match the billing system exactly.
    """
    spark = spark or spark_session()
    bronze = read_table("bronze_service_catalog")

    active = bronze.where(F.col("is_active") == F.lit(True))
    dupes = (
        active.groupBy("service_type_id")
        .count()
        .where(F.col("count") > 1)
        .select("service_type_id")
    )
    bad = active.join(dupes, "service_type_id", "left_semi")
    good = active.join(dupes, "service_type_id", "left_anti")

    quarantine(bad, "silver_service_catalog", reason="duplicate_active_service_type")
    write_table(good, "silver_service_catalog", schema=SERVICE_CATALOG_SCHEMA)
    return good
