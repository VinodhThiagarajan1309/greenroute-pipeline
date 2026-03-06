# Proposal: Add refund state transitions to payments

- **Change id:** `payments-refund-baseline`
- **Author:** Derek Chen
- **Sprint:** 4

## Why

Refunds have been issued through the processor dashboard and never reached the warehouse,
so the ledger has overstated revenue by however much support has refunded since January.

A refund references its capture. Not the booking - the capture. A booking can have several
captures over its life (rescheduled jobs, add-ons billed separately) and "refund the
booking" is ambiguous the moment there is more than one.

## What Changes

Adds refunds to the payments state machine, including partial refunds.

- **ADDED** requirement: a refund SHALL reference the capture it reverses.
- **ADDED** requirement: total refunded amount for a capture SHALL NOT exceed the captured amount.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `payments`: requirements change as listed above.

## Impact

Affected code: `src/greenroute/payments/`, `tests/payments/`.
