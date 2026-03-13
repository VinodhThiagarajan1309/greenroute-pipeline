# Proposal: Payments reads scheduling's cancellation threshold instead of holding its own

- **Change id:** `payments-refund-on-cancel`
- **Author:** Derek Chen
- **Sprint:** 5

## Why

Closes {{I10}}. scheduling treats a cancellation as free before T-2h. payments auto-refunded
only before T-4h, a constant written down when refunds were built and never revisited. A
customer cancelling at T-3h was told "no charge" by the app and was then, in fact, charged.
Support has been eating the difference by hand.

The fix is not "T-4h is wrong, use T-2h." The fix is that a threshold owned in two places
will drift again the next time either capability changes independently of the other,
exactly like it did here. {{PR:scheduling-cancellation-window}} already put this in writing
in sprint 2: the threshold SHALL be a single configured value, no capability may hold its
own copy. Payments never honoring that from the start is the actual defect.

## What Changes

Payments stops hardcoding its own T-4h auto-refund threshold and reads scheduling's
cancellation threshold instead.

- **REMOVED** requirement: payments SHALL apply a private auto-refund threshold independent of scheduling.
- **ADDED** requirement: refund auto-approval SHALL read the cancellation chargeable/free determination from scheduling and SHALL NOT hold an independently configured threshold.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `payments`: requirements change as listed above.
- `scheduling`: requirements change as listed above.

## Impact

Affected code: `src/greenroute/payments/`, `src/greenroute/scheduling/`, `tests/payments/`, `tests/scheduling/`.

Closes {{I10}}.
