# -*- coding: utf-8 -*-
"""payments: read-only client for scheduling's cancellation threshold config.

Payments must not hold its own copy of this threshold (see
cancellation_refund.py for why).
"""


def parse_cancellation_threshold_row(row):
    """Pure: turn one scheduling config row into a threshold in hours."""
    value = row.get("config_value")
    if value is None:
        raise ValueError("scheduling cancellation_threshold_hours config is missing")
    return float(value)


def get_cancellation_threshold_hours(spark=None):
    """Read-only: fetch scheduling's cancellation threshold. Never cached
    locally as a payments constant.
    """
    from greenroute.common import read_table, spark_session

    spark = spark or spark_session()
    config_df = read_table(spark, "silver_scheduling_config")
    row = config_df.filter(config_df.config_key == "cancellation_threshold_hours").first()
    return parse_cancellation_threshold_row(row.asDict())
