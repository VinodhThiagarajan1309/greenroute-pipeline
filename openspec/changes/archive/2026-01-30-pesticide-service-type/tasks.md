# Tasks: pesticide-service-type

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review
- [x] 1.2 Added requirement in the delta spec: Service type: declare whether it requires a licensed applicator; verify with `openspec validate pesticide-service-type --strict`

## 2. Implementation

- [x] 2.1 Record license_required as a flag on the catalog row; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [x] 3.3 Review addressed and change archived with `openspec archive pesticide-service-type`
