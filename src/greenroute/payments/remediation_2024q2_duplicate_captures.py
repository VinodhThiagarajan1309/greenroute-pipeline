# -*- coding: utf-8 -*-
"""payments: one-time remediation collapsing the duplicate captures that
reached production before write-time idempotency (see capture.py) landed.
"""
from collections import OrderedDict

# The four duplicate captures seen in prod: two provider_event_ids, each
# redelivered by the processor once after we returned a timeout.
KNOWN_DUPLICATE_CAPTURE_EVENT_IDS = ("evt_7f3a1c9d2b", "evt_c19e04aab7")


def collapse_duplicate_captures(capture_events):
    """Given capture events that may contain duplicate provider_event_id
    rows, keep the earliest row per provider_event_id and return the rest
    tagged for reversal.

    Returns (kept_rows, reversed_rows).
    """
    kept = OrderedDict()
    reversed_rows = []
    for event in sorted(capture_events, key=lambda e: e["event_ts"]):
        key = event["provider_event_id"]
        if key not in kept:
            kept[key] = event
        else:
            reversed_rows.append(dict(event, reversal_of=kept[key]["capture_id"]))
    return list(kept.values()), reversed_rows
