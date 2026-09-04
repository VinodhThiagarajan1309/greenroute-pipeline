# -*- coding: utf-8 -*-
"""payments: gold_payment_ledger, the ledger finance reads. Partitioned on settlement_date."""
from collections import defaultdict

GOLD_PAYMENT_LEDGER_PARTITION_COLUMNS = ["settlement_date"]


def build_gold_payment_ledger_rows(silver_events):
    """Pure aggregation: list[dict] silver_payment_events -> list[dict] ledger rows.

    One row per (booking_id, capture_id, settlement_date). Refund and
    dispute activity is aggregated onto the capture it reverses, never onto
    the booking directly -- a booking can have several captures.
    """
    buckets = defaultdict(
        lambda: {"captured_amount_cents": 0, "refunded_amount_cents": 0, "state": None, "event_ts": None}
    )
    for event in silver_events:
        key = (event["booking_id"], event["capture_id"], event["settlement_date"])
        bucket = buckets[key]
        if event["state"] == "captured":
            bucket["captured_amount_cents"] += event["amount_cents"]
        elif event["state"] == "refunded":
            bucket["refunded_amount_cents"] += event["amount_cents"]
        if bucket["event_ts"] is None or event["event_ts"] > bucket["event_ts"]:
            bucket["state"] = event["state"]
            bucket["event_ts"] = event["event_ts"]

    rows = []
    for (booking_id, capture_id, settlement_date), bucket in buckets.items():
        rows.append(
            {
                "booking_id": booking_id,
                "capture_id": capture_id,
                "settlement_date": settlement_date,
                "captured_amount_cents": bucket["captured_amount_cents"],
                "refunded_amount_cents": bucket["refunded_amount_cents"],
                "net_amount_cents": bucket["captured_amount_cents"] - bucket["refunded_amount_cents"],
                "state": bucket["state"],
            }
        )
    return rows


def build_gold_payment_ledger(spark=None):
    """Spark entry point. gold_payment_ledger is partitioned on settlement_date."""
    from greenroute.common import read_table, spark_session, write_table

    spark = spark or spark_session()
    silver = read_table(spark, "silver_payment_events")
    rows = build_gold_payment_ledger_rows([r.asDict() for r in silver.collect()])
    ledger_df = spark.createDataFrame(rows)
    write_table(
        ledger_df,
        "gold_payment_ledger",
        mode="overwrite",
        partition_by=GOLD_PAYMENT_LEDGER_PARTITION_COLUMNS,
    )
    return ledger_df
