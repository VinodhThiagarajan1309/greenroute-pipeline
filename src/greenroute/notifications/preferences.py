# -*- coding: utf-8 -*-
"""
notification_preference table definition and pure opt-in lookup logic for
the customer-notifications capability.

The pyspark schema is built lazily inside a function, not as a module-
level constant, so this module (and its pure is_opted_in) stays
importable in a pytest-only environment with no Spark installed.
"""


def notification_preference_schema():
    from pyspark.sql import types as T

    return T.StructType([
        T.StructField("customer_id", T.StringType(), False),
        T.StructField("channel", T.StringType(), False),
        T.StructField("opted_in", T.BooleanType(), False),
        T.StructField("updated_at", T.TimestampType(), False),
    ])


def is_opted_in(customer_id, channel, preferences_by_customer_channel):
    """Pure opt-in lookup: True only when a preference row says opted_in.

    Absence of a preference row defaults to NOT opted in -- consent is a
    correctness concern, so silence is never treated as consent.
    """
    key = (customer_id, channel)
    pref = preferences_by_customer_channel.get(key)
    if pref is None:
        return False
    return bool(pref.get("opted_in", False))
