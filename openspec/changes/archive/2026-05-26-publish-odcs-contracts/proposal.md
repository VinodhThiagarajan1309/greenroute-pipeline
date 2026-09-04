# Proposal: Publish ODCS contracts for the gold tables

- **Change id:** `publish-odcs-contracts`
- **Author:** Derek Chen
- **Sprint:** 10

## Why

Closes {{I19}}. Two consumers outside this repo now read gold - the ops dashboard and
finance's month-end close - and I confirmed with both teams that they learned the schema
by opening the table and looking at it. Neither has anything to point at when a column
changes. That means every gold schema change we make is, from their side, an unannounced
breaking change.

A capability spec and a data contract answer different questions. The spec says what the
system must do - scheduling owns cancellation state, payments owns refund state. The
contract says what an external consumer may rely on - these columns, these types, this
grain, don't build on anything else. Nothing before this PR made those two documents talk
to each other, so they could drift into two different descriptions of the same table with
nobody noticing until someone downstream broke.

Each contract's `customProperties.openspec_capabilities` points back at the capability
that owns the underlying table, which is how the spec and the contract stay pointed at
the same reality instead of drifting into their own versions of it.

Small thing I want on the record: `gold_payment_ledger` is a clean external-facing name
because it was named for a business concept in the very first PR to this repo, not for
the processor. If it had shipped as `gold_stripe_events` this contract would be
explaining a vendor's event model to finance instead of a ledger.

## What Changes

Publishes ODCS v3.1.0 contracts for `gold_payment_ledger` and `gold_schedule_events`, and
adds a CI check that fails the build when a gold table's actual schema drifts from what
its contract promises.

- **ADDED** requirement: `gold_payment_ledger` SHALL publish and maintain an ODCS contract linked to this capability via `customProperties`.
- **ADDED** requirement: `gold_schedule_events` SHALL publish and maintain an ODCS contract linked to this capability via `customProperties`.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `payments`: requirements change as listed above.
- `scheduling`: requirements change as listed above.

## Impact

Affected code: `src/greenroute/payments/`, `src/greenroute/scheduling/`, `tests/payments/`, `tests/scheduling/`.

Closes {{I19}}.
