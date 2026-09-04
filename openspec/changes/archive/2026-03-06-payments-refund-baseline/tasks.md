# Tasks: payments-refund-baseline

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review
- [x] 1.2 Added requirement in the delta spec: Refund: reference the capture it reverses; verify with `openspec validate payments-refund-baseline --strict`
- [x] 1.3 Added requirement in the delta spec: Total refunded amount for a capture: exceed the captured amount; verify with `openspec validate payments-refund-baseline --strict`

## 2. Implementation

- [x] 2.1 Add refund state transitions to the payments capability; verify with the tests in this change
- [x] 2.2 Store partial refund amount explicitly rather than inferring it from the capture; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [x] 3.3 Review addressed and change archived with `openspec archive payments-refund-baseline`
