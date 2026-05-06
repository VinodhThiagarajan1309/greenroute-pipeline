# Proposal: Automate the full neighborhood onboarding flow

- **Change id:** `expansion-auto-onboard-zips`
- **Author:** Tariq Osman
- **Sprint:** 9

## Why

{{I17}} measured onboarding at ~5 hours of work spread across 3 days, and the long pole is
the weekly zone-dimension rebuild. Wanted to close the whole gap in one pass rather than
leave it half done.

## What Changes

Attempts the full neighborhood onboarding flow in one change: migrate routing and the CSV
onto the registry, rebuild the zone dimension nightly instead of weekly, auto-assign a
pricing tier, check technician coverage, and verify the result.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `neighborhood-expansion`: requirements change as listed above.

## Impact

Affected code: `src/greenroute/expansion/`, `tests/expansion/`.
