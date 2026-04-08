# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""data-correctness: prune the batch-side recon scan to the affected window.

Instead of rescanning full history for the batch recompute, restrict the
scan to the date range recon actually needs.
"""
from __future__ import annotations


def batch_scan_predicate(window_start, window_end):
    """Predicate for the batch-side scan, bounded to the affected window.

    NOTE: this predicate is built against `event_date` for every table.
    """
    return {
        "column": "event_date",
        "start": window_start,
        "end": window_end,
    }


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
