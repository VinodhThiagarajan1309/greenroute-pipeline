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
