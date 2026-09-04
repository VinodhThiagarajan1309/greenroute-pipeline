# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""Tests for the INCONCLUSIVE guard (the sprint-7 empty-vs-empty incident).

A check that can silently report PASS on an empty-vs-empty comparison is not
a check: this module's central guard makes sure that never happens again,
and the seeded-mismatch tests make sure the check can still fail.
"""
from greenroute.correctness.recon import (
    classify_recon_result,
    recon_result_row,
    run_recon,
    INCONCLUSIVE,
    PASS,
    FAIL,
)


def test_seeded_mismatch_on_gold_payment_ledger_fails_the_check():
    incremental_rows = [{"payment_id": "pay-1", "amount_cents": 4500}]
    batch_rows = [{"payment_id": "pay-1", "amount_cents": 4600}]

    result = run_recon(
        "gold_payment_ledger", incremental_rows, batch_rows,
        ["payment_id"], ["amount_cents"],
    )
    row = recon_result_row(result, checked_at="2026-04-09T00:00:00Z")

    assert row["status"] == FAIL
    assert row["mismatch_count"] == 1


def test_empty_vs_empty_is_inconclusive_not_pass():
    # This is exactly the sprint-7 bug: the pruning predicate matched
    # nothing on either side, so both row counts are zero. That must never
    # report PASS -- PASS implies rows were actually compared.
    assert classify_recon_result(0, 0, 0) == INCONCLUSIVE


def test_matching_nonempty_comparison_is_pass():
    assert classify_recon_result(5, 5, 0) == PASS


def test_nonempty_comparison_with_mismatches_is_fail():
    assert classify_recon_result(5, 5, 2) == FAIL


def test_one_side_empty_and_other_nonempty_is_not_inconclusive():
    # Only a true empty-vs-empty is inconclusive; one side being empty while
    # the other has rows is a real, detectable mismatch.
    assert classify_recon_result(3, 0, 3) == FAIL


def test_recon_result_row_reports_inconclusive_for_empty_vs_empty():
    result = run_recon("gold_payment_ledger", [], [], ["payment_id"], ["amount_cents"])
    row = recon_result_row(result, checked_at="2026-04-08T00:00:00Z")

    assert row["status"] == INCONCLUSIVE
