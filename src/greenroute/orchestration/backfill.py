# -*- coding: utf-8 -*-
"""pipeline-orchestration: backfill must never reduce the row count of a
previously published partition.

The original bug: backfill read and overwrote by event_ts partition, so a
late-arriving cancellation that landed in an already-backfilled partition
was silently dropped -- a re-run produced 1.2% fewer rows and reported
success. Backfill now merges by event key instead of overwriting the
partition (see run_backfill_merge below).
"""


def event_key(record):
    """Pure: the merge key backfill upserts on. Never the event_ts partition."""
    return record["event_key"]


def plan_backfill_merge(existing_records, incoming_records):
    """Pure: MERGE semantics for a backfill batch, keyed on event_key.

    Existing rows not present in the incoming batch are always kept --
    backfill only adds/updates rows by key, it never overwrites a whole
    partition. Returns the merged record list.
    """
    merged = dict((event_key(r), r) for r in existing_records)
    for record in incoming_records:
        merged[event_key(record)] = record
    return list(merged.values())
