# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""CI: schema-drift check for gold table registry entries.

Backfill hardening reuses recon's comparison machinery to verify actual
values, not just row counts -- schema drift detection is the same idea one
level up: it must detect a column being ADDED, its type CHANGED, or a
column being REMOVED. This fixes a false negative where a delta whose only
change was a REMOVED column was reported as no drift at all, because the
old implementation only walked the new schema's columns looking for
additions and changes and never noticed a column present in the old schema
that was simply gone from the new one.
"""
from __future__ import annotations


def detect_schema_drift(old_schema, new_schema):
    """Diff two {column_name: dtype} schemas.

    Returns a list of {"column": ..., "change": "ADDED"|"REMOVED"|"CHANGED", ...}
    covering every difference in either direction -- including a column that
    was only REMOVED, which is real drift even though the new schema has
    nothing new to show for it.
    """
    changes = []
    for column in sorted(set(old_schema) | set(new_schema)):
        in_old = column in old_schema
        in_new = column in new_schema

        if in_old and not in_new:
            changes.append({"column": column, "change": "REMOVED", "old_type": old_schema[column]})
        elif in_new and not in_old:
            changes.append({"column": column, "change": "ADDED", "new_type": new_schema[column]})
        elif old_schema[column] != new_schema[column]:
            changes.append({
                "column": column, "change": "CHANGED",
                "old_type": old_schema[column], "new_type": new_schema[column],
            })

    return changes


def test_drift_check_detects_a_removed_only_column():
    # This is the false-negative this fix closes: a delta whose ONLY change
    # is a removed column must still be reported as drift.
    old_schema = {"payment_id": "string", "amount_cents": "long", "legacy_flag": "boolean"}
    new_schema = {"payment_id": "string", "amount_cents": "long"}

    changes = detect_schema_drift(old_schema, new_schema)

    assert changes == [{"column": "legacy_flag", "change": "REMOVED", "old_type": "boolean"}]


def test_drift_check_detects_added_column():
    old_schema = {"payment_id": "string"}
    new_schema = {"payment_id": "string", "settlement_date": "date"}

    changes = detect_schema_drift(old_schema, new_schema)

    assert changes == [{"column": "settlement_date", "change": "ADDED", "new_type": "date"}]


def test_drift_check_detects_changed_type():
    old_schema = {"amount_cents": "int"}
    new_schema = {"amount_cents": "long"}

    changes = detect_schema_drift(old_schema, new_schema)

    assert changes == [{"column": "amount_cents", "change": "CHANGED", "old_type": "int", "new_type": "long"}]


def test_drift_check_reports_no_drift_for_identical_schemas():
    schema = {"payment_id": "string", "amount_cents": "long"}
    assert detect_schema_drift(schema, schema) == []
