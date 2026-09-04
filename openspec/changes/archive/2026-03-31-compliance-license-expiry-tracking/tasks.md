# Tasks: compliance-license-expiry-tracking

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review
- [x] 1.2 Added requirement in the delta spec: License data: refresh on a per-license TTL; verify with `openspec validate compliance-license-expiry-tracking --strict`
- [x] 1.3 Added requirement in the delta spec: Refresh requests: be distributed across the refresh window; verify with `openspec validate compliance-license-expiry-tracking --strict`
- [x] 1.4 Added requirement in the delta spec: License data exceeding its TTL: be flagged stale rather than treated as current; verify with `openspec validate compliance-license-expiry-tracking --strict`

## 2. Implementation

- [x] 2.1 Spread refresh across the day by hashing license_number; verify with the tests in this change
- [x] 2.2 Add per-license TTL and staggered refresh for TDA lookups; verify with the tests in this change
- [x] 2.3 Flag license data stale when it exceeds its TTL instead of trusting whatever's; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [x] 3.3 Review addressed and change archived with `openspec archive compliance-license-expiry-tracking`
