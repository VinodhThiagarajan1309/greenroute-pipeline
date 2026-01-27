# Proposal: Add the scheduling capability and bronze booking ingest

- **Change id:** `scheduling-baseline`
- **Author:** Maya Patel
- **Sprint:** 2

## Why

Closes {{I2}}. Bookings with a null `neighborhood_id` were being dropped by schema
enforcement with no error and no log line - about 40 addresses, mostly new Round Rock
builds we haven't zoned yet. They weren't rejected, they just stopped existing.

Product's answer to "quarantine or sentinel zone" was quarantine: an unzoned booking is
a real booking that we can't route yet, and pretending it belongs to a fake zone would
put it on a real crew's sheet.

## What Changes

Adds the `scheduling` capability and the bronze ingest for booking events, including a
quarantine path for rows we can't zone.

- **ADDED** requirement: scheduling SHALL own booking, reschedule and cancellation state transitions.
- **ADDED** requirement: a booking that cannot be resolved to a zone SHALL be quarantined and SHALL NOT be silently discarded.

## Capabilities

### New Capabilities

- `scheduling`: Booking, rescheduling and cancellation of lawn-care jobs, including zone routing and the cancellation window.

### Modified Capabilities

- None.

## Impact

Affected code: `src/greenroute/scheduling/`, `tests/scheduling/`.

Closes {{I2}}.
