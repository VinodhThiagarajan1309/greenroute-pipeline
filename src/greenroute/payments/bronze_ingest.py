# -*- coding: utf-8 -*-
"""payments: bronze ingest of raw processor (Stripe-style) webhook deliveries."""


def bronze_payment_events_schema():
    from pyspark.sql import types as T

    return T.StructType(
        [
            T.StructField("provider_event_id", T.StringType(), True),
            T.StructField("event_type", T.StringType(), True),
            T.StructField("booking_id", T.StringType(), True),
            T.StructField("capture_id", T.StringType(), True),
            T.StructField("amount_cents", T.LongType(), True),
            T.StructField("currency", T.StringType(), True),
            T.StructField("event_ts", T.TimestampType(), True),
            T.StructField("settlement_date", T.DateType(), True),
            T.StructField("raw_payload", T.StringType(), True),
        ]
    )


def ingest_bronze_payment_events(webhook_batch_df, spark=None):
    """Spark entry point: raw webhook payloads -> bronze_payment_events.

    Every row is run through ``validate_webhook_payload`` before it is
    written; rows that fail validation are quarantined, never dropped.
    """
    from greenroute.common import quarantine, spark_session, write_table

    spark = spark or spark_session()
    rows = [r.asDict() for r in webhook_batch_df.collect()]
    accepted = []
    for row in rows:
        ok, reason = validate_webhook_payload(row)
        if ok:
            accepted.append(row)
        else:
            quarantine(spark, "bronze_payment_events", row, reason=reason)
    accepted_df = spark.createDataFrame(accepted, schema=bronze_payment_events_schema())
    write_table(accepted_df, "bronze_payment_events", mode="append")
    return accepted_df
