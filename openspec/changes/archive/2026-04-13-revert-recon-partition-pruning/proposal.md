# Proposal: Revert the gold-parity partition pruning; recon has been comparing empty to empty since Apr 8

- **Change id:** `revert-recon-partition-pruning`
- **Author:** Wes Turner
- **Sprint:** 7

## Why

Closes {{I13}}. The pruning predicate was built against `event_date`. `gold_payment_ledger`
is partitioned on `settlement_date`. The predicate matched nothing on either side, both
scans came back empty, and an empty set trivially equals an empty set - so the check has
been passing on the payment ledger since Apr 8 by comparing nothing to nothing.

I'd rather revert than fix forward. Correcting the predicate is a real fix, but it's not
a fix I want to make under the pressure of a payments check that's currently blind, and
every hour it stays blind is an hour we'd have to explain later if something real slipped
through underneath it. Reverting gets the check back to actually checking something today.
Aisha's out until the 16th, and I'm on call this sprint, so this one's mine.

The INCONCLUSIVE guard is the part of this PR that matters more than the revert. The
revert fixes this incident. The guard is what stops the next predicate mistake - on this
table or any other gold table the parity suite now covers - from looking identical to a
clean pass. Filed {{I14}} to retry the pruning correctly against `settlement_date`; it's
not going in until a seeded mismatch on the pruned path can be shown failing first.

## What Changes

Reverts the partition-pruning commit from {{PR:correctness-gold-parity-suite}} and adds a
guard so an empty-vs-empty comparison can never be reported as a pass again.

- **ADDED** requirement: a parity comparison in which both sides read zero rows SHALL be reported as INCONCLUSIVE, and SHALL NOT be reported as PASS.
- **ADDED** requirement: any change to a parity check's scan filtering SHALL be accompanied by a seeded-mismatch test exercised against the filtered path, for the specific table being changed.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `data-correctness`: requirements change as listed above.

## Impact

Affected code: `src/greenroute/correctness/`, `tests/correctness/`.

Closes {{I13}}.
