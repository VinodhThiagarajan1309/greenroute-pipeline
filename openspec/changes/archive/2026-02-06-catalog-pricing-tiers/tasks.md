# Tasks: catalog-pricing-tiers

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review
- [x] 1.2 Added requirement in the delta spec: Each service type: resolve to exactly one active price per zone; verify with `openspec validate catalog-pricing-tiers --strict`
- [x] 1.3 Added requirement in the delta spec: Overlapping active price rows: be rejected at write time; verify with `openspec validate catalog-pricing-tiers --strict`

## 2. Implementation

- [x] 2.1 Backfill tier assignment for the 38 zones we currently service; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [x] 3.3 Review addressed and change archived with `openspec archive catalog-pricing-tiers`
