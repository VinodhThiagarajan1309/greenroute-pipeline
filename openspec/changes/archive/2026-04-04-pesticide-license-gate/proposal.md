# Proposal: Hard gate: scheduling blocks a licensed-service booking without an active technician license

- **Change id:** `pesticide-license-gate`
- **Author:** Jonah Kim
- **Sprint:** 6

## Why

Closes {{I11}}. Sev-2 this morning - a pesticide application at a Mueller address was
dispatched to a technician whose TDA license expired 2026-03-11. He caught it himself at
the door before touching anything. The data to catch this in software has existed since
{{PR:technician-compliance-baseline}} landed last week. Nothing read it. Fixing that today.

## What Changes

Hard gate in the scheduling write path: a booking for a service with `license_required`
SHALL NOT be confirmed unless the assigned technician's `license_status` is `active`.

- **ADDED** requirement: scheduling SHALL reject confirmation of a licensed-service booking when the assigned technician's license_status is not active.
- **ADDED** requirement: a blocked confirmation SHALL emit a metric identifying the technician and service.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `scheduling`: requirements change as listed above.
- `technician-compliance`: requirements change as listed above.

## Impact

Affected code: `src/greenroute/compliance/`, `src/greenroute/scheduling/`, `tests/compliance/`, `tests/scheduling/`.

Closes {{I11}}.
