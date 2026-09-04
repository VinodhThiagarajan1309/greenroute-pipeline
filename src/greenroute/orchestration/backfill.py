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


def assert_row_count_not_decreased(before_count, after_count, partition):
    """Anything that gates or blocks must emit a metric saying it fired."""
    if after_count < before_count:
        print(
            "METRIC backfill_row_count_guard_fired=1 partition=%s before=%d after=%d"
            % (partition, before_count, after_count)
        )
        raise ValueError(
            "backfill for partition %s would reduce row count from %d to %d"
            % (partition, before_count, after_count)
        )
    return True


def run_backfill_merge(spark, table_name, partition, incoming_records):
    """Spark entry point: MERGE incoming_records into table_name on event_key.

    Never overwrites the partition wholesale -- that's the bug this
    replaced.
    """
    from greenroute.common import read_table, write_table

    existing_df = read_table(spark, table_name).filter("settlement_date = '%s'" % partition)
    existing_records = [r.asDict() for r in existing_df.collect()]
    before_count = len(existing_records)
    merged_records = plan_backfill_merge(existing_records, incoming_records)
    assert_row_count_not_decreased(before_count, len(merged_records), partition)
    merged_df = spark.createDataFrame(merged_records)
    write_table(merged_df, table_name, mode="overwrite", partition_by=["settlement_date"])
    return merged_df
