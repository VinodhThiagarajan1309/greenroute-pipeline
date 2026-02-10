# -*- coding: utf-8 -*-
"""payments: explicit payment state for every processor webhook event.

State is a column, never derived from which timestamp fields happen to be
non-null -- we need to be able to tell "not refunded" apart from "refund
attempted and failed" without guessing from NULLs.
"""

PAYMENT_STATE_CAPTURED = "captured"
PAYMENT_STATE_CAPTURE_FAILED = "capture_failed"
PAYMENT_STATE_REFUND_PENDING = "refund_pending"
PAYMENT_STATE_REFUNDED = "refunded"
PAYMENT_STATE_REFUND_FAILED = "refund_failed"
PAYMENT_STATE_DISPUTED = "disputed"

VALID_PAYMENT_STATES = frozenset(
    [
        PAYMENT_STATE_CAPTURED,
        PAYMENT_STATE_CAPTURE_FAILED,
        PAYMENT_STATE_REFUND_PENDING,
        PAYMENT_STATE_REFUNDED,
        PAYMENT_STATE_REFUND_FAILED,
        PAYMENT_STATE_DISPUTED,
    ]
)

EVENT_TYPE_TO_STATE = {
    "capture.succeeded": PAYMENT_STATE_CAPTURED,
    "capture.failed": PAYMENT_STATE_CAPTURE_FAILED,
    "refund.pending": PAYMENT_STATE_REFUND_PENDING,
    "refund.succeeded": PAYMENT_STATE_REFUNDED,
    "refund.failed": PAYMENT_STATE_REFUND_FAILED,
    "dispute.opened": PAYMENT_STATE_DISPUTED,
}


def build_payment_event_record(raw_event):
    """Turn one validated bronze webhook payload into a silver row (plain dict).

    ``state`` is set explicitly from the processor event type. It is never
    left to be reconstructed later from which timestamp columns are set.
    """
    event_type = raw_event["event_type"]
    state = EVENT_TYPE_TO_STATE.get(event_type)
    if state is None:
        raise ValueError("unrecognised processor event_type: %r" % (event_type,))
    return {
        "provider_event_id": raw_event["provider_event_id"],
        "booking_id": raw_event["booking_id"],
        "capture_id": raw_event.get("capture_id"),
        "amount_cents": int(raw_event["amount_cents"]),
        "currency": raw_event["currency"],
        "state": state,
        "event_ts": raw_event["event_ts"],
        "settlement_date": raw_event.get("settlement_date"),
    }


def silver_payment_events_schema():
    from pyspark.sql import types as T

    return T.StructType(
        [
            T.StructField("provider_event_id", T.StringType(), False),
            T.StructField("booking_id", T.StringType(), False),
            T.StructField("capture_id", T.StringType(), True),
            T.StructField("amount_cents", T.LongType(), False),
            T.StructField("currency", T.StringType(), False),
            T.StructField("state", T.StringType(), False),
            T.StructField("event_ts", T.TimestampType(), False),
            T.StructField("settlement_date", T.DateType(), True),
        ]
    )


def build_silver_payment_events(spark=None):
    """Spark entry point: bronze payment events -> silver_payment_events."""
    from greenroute.common import read_table, spark_session

    spark = spark or spark_session()
    bronze = read_table(spark, "bronze_payment_events")
    rows = [build_payment_event_record(r.asDict()) for r in bronze.collect()]
    return spark.createDataFrame(rows, schema=silver_payment_events_schema())
