# Tasks: notifications-reschedule-templates

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review
- [x] 1.2 Added requirement in the delta spec: Reschedule send: use the reschedule template; verify with `openspec validate notifications-reschedule-templates --strict`
- [x] 1.3 Added requirement in the delta spec: Cancellation send: render correctly for a booking with zero add-ons; verify with `openspec validate notifications-reschedule-templates --strict`

## 2. Implementation

- [x] 2.1 Add reschedule and cancellation notification templates; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [x] 3.3 Review addressed and change archived with `openspec archive notifications-reschedule-templates`
