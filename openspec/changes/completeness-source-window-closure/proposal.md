# Proposal: Gate gold publish on source-window closure

- **Change id:** `completeness-source-window-closure`
- **Author:** Aisha Bello
- **Sprint:** 4

## Why

The previous change gave us watermarks that nothing consulted. This makes them load-bearing.

The blocked-publish metric matters as much as the gate. A gate that never fires is
indistinguishable from a gate that isn't wired up, and I would like to be able to tell
those apart without reading the code.

## What Changes

Turns the watermark from a recorded number into an enforced gate: gold publish blocks
until every contributing source has closed its window.

- **ADDED** requirement: gold publish SHALL block until every contributing source watermark has closed.
- **ADDED** requirement: a blocked publish SHALL emit a metric identifying the source that blocked it.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `data-completeness`: requirements change as listed above.

## Impact

Affected code: `src/greenroute/completeness/`, `tests/completeness/`.
