# Proposal: Bound the incremental/batch parity check to a lookback wider than the completeness watermark

- **Change id:** `correctness-incremental-parity`
- **Author:** Aisha Bello
- **Sprint:** 5

## Why

Closes {{I7}}. Recon takes 41 minutes on full history today at ~2.8M gold rows and it grows
linearly - it does not get better on its own, and it sits on the critical path before gold
publish, so it is 41 minutes of added latency for a check that almost always passes.

The constraint that matters more than the speedup: the lookback has to be strictly wider
than the completeness watermark from {{PR:completeness-watermarks}} (48h, set from measured
p99 11h / max 36h), or the two checks stop agreeing with each other. If recon's window is
narrower than or equal to the watermark, a row can be inside its completeness window and
outside recon's lookback at the same time - recon would call that window fully reconciled
while completeness still considers it open, and whoever debugs the mismatch loses a week to
a phantom. Writing that relationship into the spec rather than leaving it next to a number
in a comment, because the whole point of {{I7}} was a config value that looked arbitrary and
someone was about to make it arbitrary again.

## What Changes

Replaces the full-history rescan in the incremental/batch parity check with a bounded
lookback.

- **ADDED** requirement: the parity check SHALL compare a bounded lookback window on incremental runs, not full history.
- **ADDED** requirement: the parity check's lookback window SHALL be strictly wider than the data-completeness watermark for every source it reconciles.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `data-correctness`: requirements change as listed above.

## Impact

Affected code: `src/greenroute/correctness/`, `tests/correctness/`.

Closes {{I7}}.
