# Tasks: technician-compliance-baseline

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review
- [x] 1.2 Added requirement in the delta spec: Each technician performing a licensed service: have a recorded TDA license_status and expiry_date; verify with `openspec validate technician-compliance-baseline --strict`
- [x] 1.3 Added requirement in the delta spec: License_status: be derived from expiry_date against the current date; verify with `openspec validate technician-compliance-baseline --strict`
- [x] 1.4 Added requirement in the delta spec: Technician: be matched to TDA license records by license; verify with `openspec validate technician-compliance-baseline --strict`

## 2. Implementation

- [x] 2.1 Ingest TDA applicator license roster into bronze_tda_licenses; verify with the tests in this change
- [x] 2.2 Resolve license_status per technician in silver_technician_compliance; verify with the tests in this change
- [x] 2.3 Match technicians to TDA records by license number, not name; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [x] 3.3 Review addressed and change archived with `openspec archive technician-compliance-baseline`
