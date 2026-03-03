# Tasks: scheduling-zone-routing

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review
- [x] 1.2 Added requirement in the delta spec: Day's stops: be ordered within zone before across zone; verify with `openspec validate scheduling-zone-routing --strict`

## 2. Implementation

- [x] 2.1 wip: zone-based route optimizer; verify with the tests in this change
- [x] 2.2 fix: route optimizer was using haversine instead of actual drive time; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [ ] 3.3 Review addressed and change archived with `openspec archive scheduling-zone-routing`
