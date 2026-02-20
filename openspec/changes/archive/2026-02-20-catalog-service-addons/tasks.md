# Tasks: catalog-service-addons

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review
- [x] 1.2 Added requirement in the delta spec: Add-on: attach to a booking; verify with `openspec validate catalog-service-addons --strict`
- [x] 1.3 Added requirement in the delta spec: Add-on price: be resolved and frozen at booking time; verify with `openspec validate catalog-service-addons --strict`

## 2. Implementation

- [x] 2.1 Freeze add-on price at booking time so later price changes don't rewrite history; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [x] 3.3 Review addressed and change archived with `openspec archive catalog-service-addons`
