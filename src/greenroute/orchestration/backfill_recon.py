# -*- coding: utf-8 -*-
"""pipeline-orchestration: backfill reconciliation.

Row-count-never-decreases (see backfill.py's assert_row_count_not_decreased)
catches deletion but not corruption -- a backfill that overwrites values in
place for the same set of keys passes that check every time. This module
diffs values per event key instead of just counting rows.
"""

RECON_PASS = "PASS"
RECON_FAIL = "FAIL"
RECON_INCONCLUSIVE = "INCONCLUSIVE"


def row_count_check(before_count, after_count):
    """The old check, kept because it's cheap and still catches deletion.
    Does not catch value corruption where the row count is unchanged.
    """
    return RECON_PASS if after_count >= before_count else RECON_FAIL


def checksum_record(record, value_fields):
    """Pure: a stable per-record checksum over the given value columns."""
    return hash(tuple(record.get(k) for k in sorted(value_fields)))


def diff_by_event_key(before_records, after_records, event_key_field, value_fields):
    """Pure: per-event-key value diff between the pre- and post-backfill data.

    Returns a dict with 'changed_keys' (same key, different checksum) and
    'missing_keys' (present before, absent after).
    """
    before_by_key = dict((r[event_key_field], r) for r in before_records)
    after_by_key = dict((r[event_key_field], r) for r in after_records)
    changed = [
        key
        for key in (set(before_by_key) & set(after_by_key))
        if checksum_record(before_by_key[key], value_fields) != checksum_record(after_by_key[key], value_fields)
    ]
    missing = sorted(set(before_by_key) - set(after_by_key))
    return {"changed_keys": sorted(changed), "missing_keys": missing}


def value_parity_check(before_records, after_records, event_key_field, value_fields):
    """Recon verdict using value parity, not just row count."""
    diff = diff_by_event_key(before_records, after_records, event_key_field, value_fields)
    if diff["changed_keys"] or diff["missing_keys"]:
        print(
            "METRIC backfill_recon_fired=1 verdict=FAIL changed=%d missing=%d"
            % (len(diff["changed_keys"]), len(diff["missing_keys"]))
        )
        return RECON_FAIL
    return RECON_PASS
