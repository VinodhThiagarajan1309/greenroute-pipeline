# Tasks: expansion-zip-onboarding-workflow

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review
- [x] 1.2 Modified requirement in the delta spec: Zone registry: be the authoritative source for zip-to-zone mapping; verify with `openspec validate expansion-zip-onboarding-workflow --strict`
- [x] 1.3 Modified requirement in the delta spec: Scheduling: own both zone grouping and within-zone stop ordering; verify with `openspec validate expansion-zip-onboarding-workflow --strict`

## 2. Implementation

- [x] 2.1 Migrate zip-to-zone mapping into the zone registry table; verify with the tests in this change
- [x] 2.2 Reconcile the 4 disagreeing zips in the Round Rock / Pflugerville seam; verify with the tests in this change
- [x] 2.3 Delete the hardcoded zip->zone dict in the routing module and the CSV in DAB; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [x] 3.3 Review addressed and change archived with `openspec archive expansion-zip-onboarding-workflow`
