# Proposal: End-of-quarter docs and stabilization pass

- **Change id:** `docs-and-stabilization`
- **Author:** Sofia Alvarez
- **Sprint:** 10

## Why

Nine capabilities now: pipeline-orchestration, service-catalog, scheduling, payments,
data-completeness, data-correctness, technician-compliance, customer-notifications,
neighborhood-expansion. None of that was written down anywhere a new person could read
in ten minutes, so Wes and I wrote it down. The CONTRIBUTING doc is the OpenSpec loop as
we actually run it - proposal, delta spec, review, merge, archive - not the idealized
version.

The drift-check fix is Derek's: the archive-drift job from {{PR:orchestration-backfill-tooling}}
compared requirement text, and a delta whose only change is a REMOVED requirement leaves
nothing to diff against, so it passed by omission. Same failure mode as the recon check in
{{I13}}, smaller blast radius. Fixed by asserting the removed requirement is actually gone
from the capability spec, not just absent from the diff.

What got harder than expected this quarter: the capability boundary between scheduling and
payments (the cancellation window) took a full sprint to get one shared threshold, and the
zone-registry seam took another. Both were worth it. Neither was fast.

What's knowingly left open, in order of how much it worries me:

- {{I20}} - technician-compliance is the least test-covered capability we have (3 of 7
  requirements), and nobody has decided whether an unreachable TDA license service should
  fail open or fail closed. It fails open today. That's a decision, not a default, and it
  was never made as one.
- {{I17}} - zone onboarding is still a 3-day process because the zone dimension rebuilds
  weekly. Tariq scoped the fix; picking the approach is next quarter's problem.
- {{I14}} - the recon partition-pruning optimization is still reverted. The predicate fix
  is understood, nobody has picked it up, and the acceptance bar (parity check must fail
  loudly on a seeded mismatch) is written down so whoever does pick it up can't skip it.

## What Changes

README, a CONTRIBUTING doc, the quarter's changes archived, and one drift-check bug fixed.
Closing PR for the quarter, not a feature.

- **MODIFIED** requirement: CI SHALL fail when an archived change's deltas do not match the capability spec, including a delta whose only change is a REMOVED requirement.
- **MODIFIED** requirement: the parity check SHALL report differing rows, and SHALL block merge of the change that caused them rather than only the downstream gold publish.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `pipeline-orchestration`: requirements change as listed above.
- `data-correctness`: requirements change as listed above.

## Impact

Affected code: `src/greenroute/correctness/`, `src/greenroute/orchestration/`, `tests/correctness/`, `tests/orchestration/`.
