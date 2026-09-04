# Tasks: orchestration-dab-bundle

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review
- [x] 1.2 Added requirement in the delta spec: Every job: be defined as bundle configuration in the repo; verify with `openspec validate orchestration-dab-bundle --strict`

## 2. Implementation

- [x] 2.1 Wire Databricks Asset Bundle for dev/staging/prod targets; verify with the tests in this change
- [x] 2.2 Pin bundle host per target, drop the hardcoded workspace URL; verify with the tests in this change
- [x] 2.3 Add CI: bundle validate on every PR; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [x] 3.3 Review addressed and change archived with `openspec archive orchestration-dab-bundle`
