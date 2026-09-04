# Tasks: publish-odcs-contracts

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review
- [x] 1.2 Added requirement in the delta spec: Gold_payment_ledger: publish and maintain an ODCS contract linked; verify with `openspec validate publish-odcs-contracts --strict`
- [x] 1.3 Added requirement in the delta spec: Gold_schedule_events: publish and maintain an ODCS contract linked; verify with `openspec validate publish-odcs-contracts --strict`

## 2. Implementation

- [x] 2.1 Add contracts/gold-schedule-events.odcs.yaml (ODCS v3.1.0); verify with the tests in this change
- [x] 2.2 Add contracts/gold-payment-ledger.odcs.yaml (ODCS v3.1.0); verify with the tests in this change
- [x] 2.3 Link each contract to its owning capability via; verify with the tests in this change
- [x] 2.4 Add CI: fail the build when a gold table's schema drifts from its published; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [x] 3.3 Review addressed and change archived with `openspec archive publish-odcs-contracts`
