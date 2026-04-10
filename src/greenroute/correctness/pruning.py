# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""data-correctness: prune the batch-side recon scan to the affected window.

Instead of rescanning full history for the batch recompute, restrict the
scan to the date range recon actually needs.
"""
from __future__ import annotations




def estimate_scan_bytes(row_count, avg_row_bytes):
    """Rough scan-bytes-read estimate for one recon run, so the pruning win
    (or, later, a pruning bug) is visible on the recon dashboard instead of
    only in row counts.
    """
    return row_count * avg_row_bytes


def scan_bytes_metric_row(table_name, predicate, row_count, avg_row_bytes):
    return {
        "table": table_name,
        "predicate_column": predicate["column"],
        "predicate_start": predicate["start"],
        "predicate_end": predicate["end"],
        "scan_bytes_read": estimate_scan_bytes(row_count, avg_row_bytes),
    }


def batch_scan_predicate(window_start, window_end, partition_column=None):
    """Reverted: the pruning predicate here was built against `event_date`
    unconditionally. gold_payment_ledger is partitioned on settlement_date,
    so the predicate matched nothing on that table -- both sides of the
    comparison came back empty, and parity trivially "passed" for four days
    (Apr 4 - Apr 8) because nothing was actually compared.

    Reverted to no pruning (full scan) until pruning can be made
    partition-aware per table.
    """
    return None
