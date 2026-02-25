# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""data-correctness: incremental/batch parity checks for gold tables.

Incremental output must match a full recompute of the same window. The
parity check reports the differing rows, not merely a pass/fail boolean --
a count tells you nothing about what broke.
"""
from __future__ import annotations


def compare_rows(incremental_rows, batch_rows, key_fields, value_fields):
    """Compare two row sets keyed by `key_fields`, checking `value_fields`.

    Returns a list of mismatch records -- never a bool. Each record says
    which key mismatched and, per value field, the incremental value vs the
    batch value, so an engineer can see what actually broke.
    """
    def key_of(row):
        return tuple(row[k] for k in key_fields)

    incremental_by_key = {key_of(r): r for r in incremental_rows}
    batch_by_key = {key_of(r): r for r in batch_rows}

    mismatches = []
    all_keys = set(incremental_by_key) | set(batch_by_key)
    for key in sorted(all_keys):
        inc_row = incremental_by_key.get(key)
        batch_row = batch_by_key.get(key)

        if inc_row is None:
            mismatches.append({"key": key, "kind": "missing_from_incremental", "diffs": None})
            continue
        if batch_row is None:
            mismatches.append({"key": key, "kind": "missing_from_batch", "diffs": None})
            continue

        diffs = {}
        for field in value_fields:
            inc_val = inc_row.get(field)
            batch_val = batch_row.get(field)
            if inc_val != batch_val:
                diffs[field] = {"incremental": inc_val, "batch": batch_val}

        if diffs:
            mismatches.append({"key": key, "kind": "value_mismatch", "diffs": diffs})

    return mismatches
