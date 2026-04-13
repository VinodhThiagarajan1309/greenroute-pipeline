# Tasks: license-gate-all-licensed-services

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review
- [x] 1.2 Modified requirement in the delta spec: Scheduling: reject confirmation of a licensed-service booking; verify with `openspec validate license-gate-all-licensed-services --strict`
- [x] 1.3 Added requirement in the delta spec: Each service type: declare license_required explicitly; verify with `openspec validate license-gate-all-licensed-services --strict`

## 2. Implementation

- [x] 2.1 Flag herbicide_application and fertilizer_application license_required in the; verify with the tests in this change
- [x] 2.2 Gate reads the catalog row's license_required flag; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [x] 3.3 Review addressed and change archived with `openspec archive license-gate-all-licensed-services`
