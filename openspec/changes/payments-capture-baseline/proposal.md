# Proposal: Add the payments capability and the capture pipeline

- **Change id:** `payments-capture-baseline`
- **Author:** Derek Chen
- **Sprint:** 3

## Why

Payment state has been inferred from booking state, which is wrong in every case where
they disagree - and they disagree exactly when it matters (failed captures, disputes,
partial refunds). Payments needs to be its own capability with its own state machine.

The last commit is worth calling out: when a webhook arrives without `provider_event_id`
we reject it. The tempting alternative is to synthesise a surrogate key so the row can
land. That would make the pipeline look healthier and make idempotency impossible.

## What Changes

Introduces `payments` and the capture path from processor webhook through to
`gold_payment_ledger`.

- **ADDED** requirement: payments SHALL own capture, refund and dispute state transitions.
- **ADDED** requirement: a payment event without a provider-issued event id SHALL be rejected, not assigned a surrogate.

## Capabilities

### New Capabilities

- `payments`: Capture, refund and dispute state for customer payments, and the gold ledger finance reads.

### Modified Capabilities

- None.

## Impact

Affected code: `src/greenroute/payments/`, `tests/payments/`.
