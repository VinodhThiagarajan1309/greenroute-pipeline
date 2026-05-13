# Proposal: Add reschedule and cancellation notification templates

- **Change id:** `notifications-reschedule-templates`
- **Author:** Priya Nair
- **Sprint:** 9

## Why

`scheduling-notification-hooks` gave every send path one place to check opt-out. This gives
reschedule and cancellation their own copy instead of reusing the booking-confirmation
template with fields substituted in, which read wrong on tense every time.

Copy for both templates was reviewed by the support team lead before this went up, same as
the confirmation templates.

## What Changes

Adds message templates for reschedule and cancellation sends, both routed through the
provider-agnostic interface from last sprint.

- **ADDED** requirement: a reschedule send SHALL use the reschedule template, not the booking-confirmation template with substituted fields.
- **ADDED** requirement: a cancellation send SHALL render correctly for a booking with zero add-ons.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `customer-notifications`: requirements change as listed above.

## Impact

Affected code: `src/greenroute/notifications/`, `tests/notifications/`.
