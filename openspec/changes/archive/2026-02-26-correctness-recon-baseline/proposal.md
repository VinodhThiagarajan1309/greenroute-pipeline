# Proposal: Add the data-correctness capability and the incremental/batch parity check

- **Change id:** `correctness-recon-baseline`
- **Author:** Aisha Bello
- **Sprint:** 4

## Why

We have two code paths producing the same tables - the incremental daily job and the
backfill recompute - and nothing has ever compared them. They have almost certainly
disagreed already; we would not know.

The seeded-mismatch test is the important one. Its job is to prove the check is capable of
failing. Every reconciliation system I have worked with has eventually degraded into
comparing an empty set to an empty set and reporting success.

## What Changes

Adds `data-correctness`, whose first invariant is that incremental output equals a full
recompute of the same window.

- **ADDED** requirement: incremental output SHALL match a full recompute of the same window.
- **ADDED** requirement: the parity check SHALL report differing rows, not only a pass/fail verdict.
- **ADDED** requirement: the parity check SHALL be verified against a seeded mismatch on every CI run.

## Capabilities

### New Capabilities

- `data-correctness`: Whether the rows that are present are right: incremental-versus-batch parity and reconciliation of the gold tables.

### Modified Capabilities

- None.

## Impact

Affected code: `src/greenroute/correctness/`, `tests/correctness/`.
