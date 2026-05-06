# Tasks: expansion-auto-onboard-zips

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review

## 2. Implementation

- [x] 2.1 Add nightly zone dimension rebuild replacing the weekly job; verify with the tests in this change
- [x] 2.2 wip: end-to-end zip onboarding; verify with the tests in this change
- [x] 2.3 Add technician coverage check gating onboarding completion; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [ ] 3.3 Review addressed and change archived with `openspec archive expansion-auto-onboard-zips`
