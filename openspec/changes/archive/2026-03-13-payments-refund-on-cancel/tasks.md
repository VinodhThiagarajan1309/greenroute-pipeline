# Tasks: payments-refund-on-cancel

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review
- [x] 1.2 Removed requirement in the delta spec: Payments: apply a private auto-refund threshold independent of scheduling; verify with `openspec validate payments-refund-on-cancel --strict`
- [x] 1.3 Added requirement in the delta spec: Refund auto-approval: read the cancellation chargeable/free determination from scheduling; verify with `openspec validate payments-refund-on-cancel --strict`

## 2. Implementation

- [x] 2.1 Remove payments' private T-4h auto-refund threshold constant; verify with the tests in this change
- [x] 2.2 Add read-only client for scheduling's cancellation threshold config; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [x] 3.3 Review addressed and change archived with `openspec archive payments-refund-on-cancel`
