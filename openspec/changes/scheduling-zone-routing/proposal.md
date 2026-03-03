# Proposal: Zone-based route optimizer

- **Change id:** `scheduling-zone-routing`
- **Author:** Maya Patel
- **Sprint:** 4

## Why

Crews currently get stops in booking order, which means driving Zilker -> Round Rock ->
Zilker in a morning. Grouping by zone first should cut drive time substantially.

Opening early as a WIP to get direction feedback before I build out the rest - I would
rather find out now if this is the wrong layer for it.

## What Changes

First pass at a zone-based route optimizer that groups a day's stops by zone before
ordering them.

- **ADDED** requirement: a day's stops SHALL be ordered within zone before across zone.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `scheduling`: requirements change as listed above.

## Impact

Affected code: `src/greenroute/scheduling/`, `tests/scheduling/`.
