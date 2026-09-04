# Tasks: init-orchestration-skeleton

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review
- [x] 1.2 Added requirement in the delta spec: Every published table: carry a bronze_ / silver_ / gold_ prefix; verify with `openspec validate init-orchestration-skeleton --strict`
- [x] 1.3 Added requirement in the delta spec: Each layer: live in its own Unity Catalog schema; verify with `openspec validate init-orchestration-skeleton --strict`

## 2. Implementation

- [x] 2.1 Add bronze/silver/gold job stubs with explicit layer prefixes; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [x] 3.3 Review addressed and change archived with `openspec archive init-orchestration-skeleton`
