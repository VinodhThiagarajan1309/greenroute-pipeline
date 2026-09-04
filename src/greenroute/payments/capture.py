# -*- coding: utf-8 -*-
"""payments: idempotent capture writes, keyed on provider_event_id.

The processor retries webhook delivery on any non-2xx response, including
our own timeouts. Capture must be safe to receive the same
provider_event_id more than once.
"""


def capture_already_applied(provider_event_id, existing_capture_event_ids):
    """True if this provider_event_id has already been captured.

    Checked on the retry path before anything else: if the processor
    redelivers a webhook we've already captured, this call makes the retry
    a no-op.
    """
    return provider_event_id in existing_capture_event_ids


def decide_capture_write(capture_row, existing_capture_event_ids):
    """Pure: what to do with this capture attempt.

    Enforces uniqueness on provider_event_id at write time. This is
    deliberately not a downstream dedupe step (e.g. a nightly job that
    collapses duplicate provider_event_id rows out of gold). Downstream
    dedupe would have hidden the defect that let four duplicate captures
    reach production -- it makes the symptom disappear without making the
    write path itself safe. The uniqueness check has to live at the point
    of write, so it runs here, before any I/O happens.
    """
    provider_event_id = capture_row["provider_event_id"]
    if capture_already_applied(provider_event_id, existing_capture_event_ids):
        return {"applied": False, "reason": "duplicate provider_event_id", "capture_row": None}
    return {"applied": True, "reason": None, "capture_row": capture_row}


def write_capture(spark, capture_row, existing_capture_event_ids, writer=None):
    """Spark entry point: apply decide_capture_write, then perform the write
    only if it was accepted.
    """
    decision = decide_capture_write(capture_row, existing_capture_event_ids)
    if decision["applied"]:
        from greenroute.common import write_table

        write_table(spark.createDataFrame([capture_row]), "silver_payment_events", mode="append")
    return decision
