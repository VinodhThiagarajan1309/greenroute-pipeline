# Proposal: Add the data-completeness capability and per-source watermarks

- **Change id:** `completeness-watermarks`
- **Author:** Aisha Bello
- **Sprint:** 3

## Why

Closes {{I5}}. Measured 14 days of booking events: cancellation delay is p50 4 min, p90
51 min, p99 11 h, max 36 h 12 min. The cause is the mobile app queueing offline actions -
technicians cancel on-site in the Circle C dead zone and the phone syncs later.

Any daily job that closes yesterday's window at midnight therefore under-counts
cancellations, permanently and silently. Set the watermark at 48h, which is the observed
max rounded up with headroom, not a number anyone guessed.

## What Changes

Adds `data-completeness` and the watermark mechanism that stops a gold partition
publishing while one of its sources is still open.

- **ADDED** requirement: a gold partition SHALL NOT publish until every contributing source watermark has closed for that window.
- **ADDED** requirement: each source SHALL declare a maximum expected lateness, derived from measured delivery delay rather than assumed.

## Capabilities

### New Capabilities

- `data-completeness`: Whether every row that should be present is present: source watermarks, late-arriving events, and window closure before publish.

### Modified Capabilities

- None.

## Impact

Affected code: `src/greenroute/completeness/`, `tests/completeness/`.

Closes {{I5}}.
