# Proposal: Rename data-completeness to data-freshness-guarantees

- **Change id:** `rename-completeness-to-freshness-guarantees`
- **Author:** Sofia Alvarez
- **Sprint:** 7

## Why

The current name describes the mechanism - are all the rows here - not the promise it
makes to the two consumers who actually read this spec: finance and the ops dashboard.
Neither of them asks "is it complete", they ask "can I trust the number I'm looking at
right now", which is a freshness question wearing a completeness name. Renaming it to
match what we actually promise seemed like the kind of thing that gets more expensive
the longer we wait.

## What Changes

Proposes renaming the `data-completeness` capability to `data-freshness-guarantees`.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `data-completeness`: requirements change as listed above.

## Impact

Affected code: `src/greenroute/completeness/`, `tests/completeness/`.
