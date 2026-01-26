# Tasks: scheduling-baseline

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review
- [x] 1.2 Added requirement in the delta spec: Scheduling: own booking; verify with `openspec validate scheduling-baseline --strict`
- [x] 1.3 Added requirement in the delta spec: Booking that cannot be resolved: be quarantined; verify with `openspec validate scheduling-baseline --strict`

## 2. Implementation

- [x] 2.1 feat: bronze booking events ingest; verify with the tests in this change
- [x] 2.2 add rejected-rows table so quarantined bookings are visible somewhere; verify with the tests in this change
- [x] 2.3 fix: quarantine null neighborhood_id rows instead of dropping them silently; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [x] 3.3 Review addressed and change archived with `openspec archive scheduling-baseline`
