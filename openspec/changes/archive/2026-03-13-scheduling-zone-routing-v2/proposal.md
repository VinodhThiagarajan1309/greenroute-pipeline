# Proposal: Move zone grouping and stop ordering into scheduling, delete the DAB config knob

- **Change id:** `scheduling-zone-routing-v2`
- **Author:** Maya Patel
- **Sprint:** 5

## Why

{{PR:scheduling-zone-routing}} was closed in sprint 4 because zone grouping already existed
as a DAB config knob, and that PR would have left two systems deciding stop order. This
version does the whole migration in one change: ordering moves into scheduling, the config
knob goes away, there's one owner. The haversine-vs-drive-time fix from the closed PR
carries over unchanged - it was correct then and nothing about the migration touches it.

## What Changes

v2 of the zone-based route optimizer. Zone grouping and stop ordering both move into
`scheduling`, and the DAB job-parameter config knob that used to also decide stop order is
deleted.

- **ADDED** requirement: scheduling SHALL own both zone grouping and within-zone stop ordering for a day's route.
- **ADDED** requirement: stop distance used for ordering SHALL be computed as drive time, not straight-line distance.
- **REMOVED** requirement: the DAB job-parameter config SHALL control zone grouping and stop ordering (ownership moved to scheduling).

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `scheduling`: requirements change as listed above.
- `pipeline-orchestration`: requirements change as listed above.

## Impact

Affected code: `src/greenroute/orchestration/`, `src/greenroute/scheduling/`, `tests/orchestration/`, `tests/scheduling/`.
