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


def run_recon(table_name, incremental_rows, batch_rows, key_fields, value_fields):
    """Run one incremental-vs-batch parity check and return its full result.

    Pure function: callers are responsible for fetching `incremental_rows`
    (the already-published gold rows) and `batch_rows` (a full recompute of
    the same window) -- no Spark session or I/O happens in here.
    """
    mismatches = compare_rows(incremental_rows, batch_rows, key_fields, value_fields)
    return {
        "table": table_name,
        "incremental_row_count": len(incremental_rows),
        "batch_row_count": len(batch_rows),
        "mismatch_count": len(mismatches),
        "mismatches": mismatches,
    }


INCONCLUSIVE = "INCONCLUSIVE"
PASS = "PASS"
FAIL = "FAIL"


def classify_recon_result(incremental_row_count, batch_row_count, mismatch_count):
    """Classify one recon result as PASS, FAIL, or INCONCLUSIVE.

    This is the guard for the sprint-7 incident: a partition-pruning bug
    built its predicate against the wrong column, both sides of the
    comparison came back empty, and an empty-vs-empty comparison trivially
    "passed" for four days because nothing was actually compared. An
    empty-vs-empty comparison must report INCONCLUSIVE, never PASS -- PASS
    means rows were actually checked and matched.
    """
    if incremental_row_count == 0 and batch_row_count == 0:
        return INCONCLUSIVE
    if mismatch_count > 0:
        return FAIL
    return PASS


def recon_result_row(recon_result, checked_at):
    """Build one row of the recon result table: per-check row counts.

    Status is classified via classify_recon_result so an empty-vs-empty
    comparison is never reported as a silent PASS.
    """
    status = classify_recon_result(
        recon_result["incremental_row_count"],
        recon_result["batch_row_count"],
        recon_result["mismatch_count"],
    )
    return {
        "table": recon_result["table"],
        "checked_at": checked_at,
        "incremental_row_count": recon_result["incremental_row_count"],
        "batch_row_count": recon_result["batch_row_count"],
        "mismatch_count": recon_result["mismatch_count"],
        "status": status,
    }
