# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""scheduling capability: booking, reschedule and cancellation state; zone
routing; the cancellation window; the pesticide license gate; notification
hooks.
"""

import pyspark.sql.functions as F
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    TimestampType,
)

from greenroute.common import spark_session, read_table, write_table, quarantine

BOOKING_EVENT_SCHEMA = StructType([
    StructField("booking_id", StringType(), nullable=False),
    StructField("customer_id", StringType(), nullable=False),
    StructField("service_type_id", StringType(), nullable=False),
    StructField("neighborhood_id", StringType(), nullable=True),
    StructField("zip_code", StringType(), nullable=True),
    StructField("service_window_start", TimestampType(), nullable=False),
    StructField("technician_id", StringType(), nullable=True),
    StructField("status", StringType(), nullable=False),
    StructField("event_ts", TimestampType(), nullable=False),
])


def bronze_booking_events(spark=None):
    """Ingest raw booking events into bronze_booking_events, typed on write."""
    spark = spark or spark_session()
    raw = read_table("raw_booking_events")
    typed = spark.createDataFrame(raw.rdd, schema=BOOKING_EVENT_SCHEMA)
    write_table(typed, "bronze_booking_events")
    return typed
