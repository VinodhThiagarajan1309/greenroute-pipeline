# Proposal: Make backfill non-destructive, and add the archive-drift CI check

- **Change id:** `orchestration-backfill-tooling`
- **Author:** Wes Turner
- **Sprint:** 4

## Why

Closes {{I6}} and {{I8}}.

Backfill read by `event_ts` partition and overwrote it. Late cancellations land in an old
`event_ts` partition *after* it was backfilled, so the rewrite deleted them. Re-running the
January backfill produced 1.2% fewer rows than the incremental run and nobody noticed
because backfill reported success. Now it merges on event key.

The drift check exists because twice this sprint a change merged whose delta never made it
into the capability spec. If the archive and `openspec/specs/` disagree, the spec is no
longer the source of truth and the whole exercise is theatre.

## What Changes

Two things, both plumbing. Backfill stops being destructive, and CI starts catching
spec drift.

- **ADDED** requirement: backfill SHALL merge on event key and SHALL NOT reduce the row count of a previously published partition.
- **ADDED** requirement: CI SHALL fail when an archived change's deltas do not reconcile against current capability specs.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `pipeline-orchestration`: requirements change as listed above.

## Impact

Affected code: `src/greenroute/orchestration/`, `tests/orchestration/`.

Closes {{I6}}, {{I8}}.
