# Tasks: orchestration-backfill-tooling

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review
- [x] 1.2 Added requirement in the delta spec: Backfill: merge on event key; verify with `openspec validate orchestration-backfill-tooling --strict`
- [x] 1.3 Added requirement in the delta spec: CI: fail when an archived change's deltas do; verify with `openspec validate orchestration-backfill-tooling --strict`

## 2. Implementation

- [x] 2.1 Backfill job was silently dropping late-arriving cancellations. Fixed; verify with the tests in this change
- [x] 2.2 Backfill now merges by event key instead of overwriting the partition; verify with the tests in this change
- [x] 2.3 Add CI job: OpenSpec archive-drift check; verify with the tests in this change
- [x] 2.4 Drift check fails the build if a merged delta never made it into the capability; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [x] 3.3 Review addressed and change archived with `openspec archive orchestration-backfill-tooling`
