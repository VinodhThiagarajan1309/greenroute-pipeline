# Proposal: Wire the Databricks Asset Bundle for dev/staging/prod

- **Change id:** `orchestration-dab-bundle`
- **Author:** Sofia Alvarez
- **Sprint:** 1

## Why

Deployment was one person running one command from one laptop. `bundle validate` in CI
means a malformed job definition fails in the PR instead of at deploy time.

## What Changes

Adds `databricks.yml` plus per-target overrides so the pipeline deploys the same way in
all three environments, and makes CI validate the bundle on every PR.

- **ADDED** requirement: every job SHALL be defined as bundle configuration in the repo; no job is configured through the workspace UI.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `pipeline-orchestration`: requirements change as listed above.

## Impact

Affected code: `src/greenroute/orchestration/`, `tests/orchestration/`.
