# Proposal: Verify backfill on value parity, not row count alone

- **Change id:** `orchestration-backfill-hardening`
- **Author:** Wes Turner
- **Sprint:** 9

## Why

Aisha called this out when the row-count invariant landed in sprint 4: it's one-directional.
A backfill that keeps the count and corrupts every value passes it. Recon didn't exist yet
to check values at the time. It does now, so there's no excuse left.

Also wiring in the lesson from {{I13}} - a parity check that compares an empty set to an
empty set and calls it PASS is worse than no check, because it looks like coverage.
Backfill's value comparison can legitimately hit an empty window (a source with no writes
that day), and that has to come back INCONCLUSIVE, not PASS. This should have existed
when the recon job did. Doing it now.

## What Changes

Backfill's row-count invariant gets a value check to go with it, and the comparison logic
stops treating "nothing to compare" as "passed."

- **ADDED** requirement: a backfill run SHALL be verified against a value-level parity check, not row count alone.
- **ADDED** requirement: a parity comparison over an empty window on both sides SHALL report INCONCLUSIVE and SHALL NOT report PASS.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `pipeline-orchestration`: requirements change as listed above.

## Impact

Affected code: `src/greenroute/orchestration/`, `tests/orchestration/`.
