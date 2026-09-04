# Tasks: expansion-zone-registry-baseline

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review
- [x] 1.2 Added requirement in the delta spec: Zone registry: be the authoritative source for zip-to-zone mapping; verify with `openspec validate expansion-zone-registry-baseline --strict`
- [x] 1.3 Added requirement in the delta spec: Zip with conflicting zone assignments across: be flagged for manual resolution before the registry; verify with `openspec validate expansion-zone-registry-baseline --strict`
- [x] 1.4 Added requirement in the delta spec: Quarantined booking whose zip resolves: become eligible for re-processing; verify with `openspec validate expansion-zone-registry-baseline --strict`

## 2. Implementation

- [x] 2.1 Add zone_registry table: zip, zone, effective_date, source_note; verify with the tests in this change
- [x] 2.2 Re-run scheduling-baseline's quarantined bookings against the registry; verify with the tests in this change
- [x] 2.3 Seed zone_registry from the routing module dict, the current de facto source; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [x] 3.3 Review addressed and change archived with `openspec archive expansion-zone-registry-baseline`
