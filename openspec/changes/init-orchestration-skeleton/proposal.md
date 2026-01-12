# Proposal: Bootstrap repo layout and the pipeline-orchestration capability

- **Change id:** `init-orchestration-skeleton`
- **Author:** Sofia Alvarez
- **Sprint:** 1

## Why

We have two pipelines and three naming conventions. Fixing that costs an afternoon now
and a migration later. Making layer naming a *requirement* in a capability spec rather
than a convention in a README is the whole point of adopting OpenSpec here - conventions
in READMEs are advisory and get ignored.

## What Changes

Stands up the repository and the first OpenSpec capability, `pipeline-orchestration`.
It owns two things: how the Databricks jobs are wired together, and what the medallion
layers are called.

- **ADDED** requirement: every published table SHALL carry a `bronze_` / `silver_` / `gold_` prefix matching its layer.
- **ADDED** requirement: each layer SHALL live in its own Unity Catalog schema, one catalog per environment.

## Capabilities

### New Capabilities

- `pipeline-orchestration`: How GreenRoute's Databricks jobs are wired together, deployed and retried, and what the medallion layers are called.

### Modified Capabilities

- None.

## Impact

Affected code: `src/greenroute/orchestration/`, `tests/orchestration/`.
