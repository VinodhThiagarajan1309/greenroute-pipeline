# Proposal: Extend incremental/batch parity to every gold table

- **Change id:** `correctness-gold-parity-suite`
- **Author:** Aisha Bello
- **Sprint:** 7

## Why

We built one recon job and pointed it at one table. The other two gold tables have been
unreconciled since they existed, which is exactly the gap the original recon change was
supposed to close and quietly didn't.

The scan-time change is separate but landed in the same PR because it's a direct
consequence of generalizing the job: once recon runs against three tables instead of one
on every schedule, the full-history batch-side scan on `gold_payment_ledger` alone was
adding real minutes. Filtering that scan to the window the job already resolves for
`event_date` before reading, rather than after, cuts bytes scanned by about 60% on that
check with no change to what gets compared.

## What Changes

Generalizes the parity check from S4 so it runs against every published gold table
instead of only `gold_schedule_events`, and speeds up the batch-side scan while we're
in there.

- **MODIFIED** requirement: incremental output SHALL match a full recompute of the same window, for every published gold table, not only `gold_schedule_events`.
- **ADDED** requirement: each gold table covered by parity SHALL have its own seeded-mismatch test; coverage of one table SHALL NOT be assumed to cover another.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `data-correctness`: requirements change as listed above.

## Impact

Affected code: `src/greenroute/correctness/`, `tests/correctness/`.
