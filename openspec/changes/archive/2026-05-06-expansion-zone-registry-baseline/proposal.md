# Proposal: Add the neighborhood-expansion capability and the zone registry

- **Change id:** `expansion-zone-registry-baseline`
- **Author:** Tariq Osman
- **Sprint:** 9

## Why

Filed {{I18}} after finding the mapping in three places - a hardcoded dict in the routing
module, a CSV in the DAB resources folder, and ops' spreadsheet. Reconciling all three:
they agree everywhere except 4 zips, and all 4 are in the Round Rock / Pflugerville seam,
which is exactly where we're expanding right now. Not a coincidence - that's the boundary
nobody has needed to be precise about until this quarter.

This change stands up the registry and its requirements. It does not migrate or delete the
other two copies yet - that's a bigger change with its own decisions (does routing read the
registry directly or get a materialized view? what happens to the CSV in the interim
deploys?) and I'd rather ship the source of truth first and the migration second.

Also closes out an old loose end: `scheduling-baseline` quarantined ~40 bookings with no
resolvable `neighborhood_id` back in sprint 2, and Jonah flagged at the time that 31 of them
were concentrated in two new Pflugerville subdivisions, not scattered edge cases. Both
subdivisions are now in the registry. Re-ran the quarantine table against it - 31 of 40
resolve.

## What Changes

Adds `neighborhood-expansion` and stands up `zone_registry` as the table meant to become
the single source of truth for zip-to-zone mapping.

- **ADDED** requirement: the zone registry SHALL be the authoritative source for zip-to-zone mapping.
- **ADDED** requirement: a zip with conflicting zone assignments across ingest sources SHALL be flagged for manual resolution before the registry accepts a value for it.
- **ADDED** requirement: a quarantined booking whose zip resolves to a registered zone SHALL become eligible for re-processing.

## Capabilities

### New Capabilities

- `neighborhood-expansion`: Onboarding new Austin-area zones and ZIP codes into the pipeline.

### Modified Capabilities

- None.

## Impact

Affected code: `src/greenroute/expansion/`, `tests/expansion/`.
