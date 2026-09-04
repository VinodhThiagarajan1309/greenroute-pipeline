# Tasks: docs-and-stabilization

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review
- [x] 1.2 Modified requirement in the delta spec: CI: fail when an archived change's deltas do; verify with `openspec validate docs-and-stabilization --strict`
- [x] 1.3 Modified requirement in the delta spec: Parity check: report differing rows; verify with `openspec validate docs-and-stabilization --strict`

## 2. Implementation

- [x] 2.1 Fix: drift check false-negative when a delta's only change is a REMOVED; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [x] 3.3 Review addressed and change archived with `openspec archive docs-and-stabilization`
