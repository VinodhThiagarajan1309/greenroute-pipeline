# Tasks: service-catalog-baseline

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review
- [x] 1.2 Added requirement in the delta spec: Catalog: define exactly one active row per billable service; verify with `openspec validate service-catalog-baseline --strict`
- [x] 1.3 Added requirement in the delta spec: Booking referencing an unknown service type: be quarantined; verify with `openspec validate service-catalog-baseline --strict`

## 2. Implementation

- [x] 2.1 Add silver_service_catalog transform; verify with the tests in this change
- [x] 2.2 Tighten unit_price to DECIMAL(10,2) to match the billing system exactly; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [x] 3.3 Review addressed and change archived with `openspec archive service-catalog-baseline`
