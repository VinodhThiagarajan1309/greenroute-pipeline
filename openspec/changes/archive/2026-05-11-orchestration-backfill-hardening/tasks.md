# Tasks: orchestration-backfill-hardening

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review
- [x] 1.2 Added requirement in the delta spec: Backfill run: be verified against a value-level parity check; verify with `openspec validate orchestration-backfill-hardening --strict`
- [x] 1.3 Added requirement in the delta spec: Parity comparison over an empty window: report INCONCLUSIVE; verify with `openspec validate orchestration-backfill-hardening --strict`

## 2. Implementation

- [x] 2.1 Backfill recon now diffs values per event key using the; verify with the tests in this change
- [x] 2.2 Row-count-never-decreases doesn't catch value corruption. Fixed; verify with the tests in this change
- [x] 2.3 Empty-vs-empty comparison now reports INCONCLUSIVE, never PASS; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [x] 3.3 Review addressed and change archived with `openspec archive orchestration-backfill-hardening`
