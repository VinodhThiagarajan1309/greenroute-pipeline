# Proposal: Add the cancellation window to scheduling

- **Change id:** `scheduling-cancellation-window`
- **Author:** Maya Patel
- **Sprint:** 2

## Why

Closes {{I3}}. We had three rules in production simultaneously - ops said "before the crew
rolls", the website said 24 hours, and billing was refunding same-day cancels by hand.
Product picked T-2h relative to the service window start, and this makes that the single
answer.

Chose service-window-relative over dispatch-relative because we don't have dispatch events
in the pipeline yet. Noted in design.md as the thing to revisit if we ever do.

## What Changes

Implements the cancellation window: cancellations arriving less than 2 hours before the
service window start are chargeable, everything earlier is free.

- **ADDED** requirement: a cancellation received at or after (service_window_start - 2h) SHALL be marked chargeable.
- **ADDED** requirement: the cancellation threshold SHALL be a single configured value; no capability may hold its own copy.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `scheduling`: requirements change as listed above.

## Impact

Affected code: `src/greenroute/scheduling/`, `tests/scheduling/`.

Closes {{I3}}.
