# Tasks: pesticide-license-gate

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review
- [x] 1.2 Added requirement in the delta spec: Scheduling: reject confirmation of a licensed-service booking; verify with `openspec validate pesticide-license-gate --strict`
- [x] 1.3 Added requirement in the delta spec: Blocked confirmation: emit a metric identifying the technician and service; verify with `openspec validate pesticide-license-gate --strict`

## 2. Implementation

- [x] 2.1 hotfix: scheduling won't confirm a licensed-service booking unless technician; verify with the tests in this change
- [x] 2.2 Emit license_gate_blocked metric with technician and service; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [x] 3.3 Review addressed and change archived with `openspec archive pesticide-license-gate`
