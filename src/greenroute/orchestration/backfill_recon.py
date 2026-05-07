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
