# Proposal: License gate accepts a pending TDA renewal inside the 30-day grace period

- **Change id:** `scheduling-license-grace-period`
- **Author:** Maya Patel
- **Sprint:** 7

## Why

Closes {{I21}}. 11 manual overrides in 5 working days. Ops was being asked to decide, at the
door, whether a blocked technician was actually illegal or just mid-renewal. That decision
belongs in the spec, once, not in 11 Slack threads.

The gate reads `license_status`. TDA reports `pending_renewal` as a distinct status and the
renewal filing date is in the same lookup response, so the data was already there - the same
shape as {{I11}}, in the other direction: this time the data existed and we were too strict
rather than not reading it at all.

## What Changes

Relaxes the licence gate by exactly one case. A technician whose TDA renewal was filed on or
before the expiry date stays bookable for 30 days after expiry, which is the TDA grace rule.
Everything else the gate did on Apr 4 it still does, and the requirement block says so in
full - this is a MODIFIED requirement, restated, not a second requirement next to the first.

- **MODIFIED** requirement: scheduling SHALL reject confirmation of a licensed-service booking when the assigned technician's license_status is not active, unless the status is pending_renewal, the renewal was filed on or before the expiry date, and the booking date is within 30 days of expiry.
- **ADDED** requirement: technician license records SHALL carry renewal_filed_date from the TDA lookup so the grace window can be computed at booking time.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `scheduling`: requirements change as listed above.
- `technician-compliance`: requirements change as listed above.

## Impact

Affected code: `src/greenroute/compliance/`, `src/greenroute/scheduling/`, `tests/compliance/`, `tests/scheduling/`.

Closes {{I21}}.
