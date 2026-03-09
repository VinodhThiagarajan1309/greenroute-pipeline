# Proposal: Rewrite reschedule so it invalidates derived route state instead of leaving it behind

- **Change id:** `scheduling-reschedule-v2`
- **Author:** Maya Patel
- **Sprint:** 5

## Why

Closes {{I9}}. reschedule updated the booking row and stopped there. Route assignment is
built from booking + date, and nothing ever told it the booking's date had changed, so the
old assignment sat there looking valid. Two crews drove to Zilker on Tuesday for a job that
had moved to Thursday. Picked this up first since I'm on-call this sprint and an orphan
route assignment is exactly the kind of thing that pages me at 6am.

First pass modeled reschedule as cancel-the-old-booking-and-rebook-a-new-one, which fixes
the orphan cleanly because cancel already tears down route assignment. Backed that out - it
also erases the link between the two dates, and ops wants "this booking moved," not "this
booking was cancelled and an unrelated one appeared." Landed on explicit invalidation
instead: reschedule now emits the same kind of event cancel already emits, and route
assignment listens for it.

## What Changes

Rewrites reschedule so moving a booking's date also invalidates the route assignment for
the original date, instead of leaving it in place as derived state nobody re-derives.

- **ADDED** requirement: reschedule SHALL invalidate every derived route assignment for the booking's original date, in the same transaction as the date change.
- **ADDED** requirement: a reschedule SHALL preserve the booking's identity and history, and SHALL NOT be represented internally as a cancellation followed by a new booking.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `scheduling`: requirements change as listed above.

## Impact

Affected code: `src/greenroute/scheduling/`, `tests/scheduling/`.

Closes {{I9}}.
