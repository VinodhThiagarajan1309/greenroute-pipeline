# Tasks: revert-recon-partition-pruning

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review
- [x] 1.2 Added requirement in the delta spec: Parity comparison in which both sides: be reported as INCONCLUSIVE; verify with `openspec validate revert-recon-partition-pruning --strict`
- [x] 1.3 Added requirement in the delta spec: Any change to a parity check's: be accompanied by a seeded-mismatch test exercised; verify with `openspec validate revert-recon-partition-pruning --strict`

## 2. Implementation

- [x] 2.1 Revert "Prune the batch-side scan to the affected date range instead of rescanning full"; verify with the tests in this change
- [x] 2.2 Recon now reports INCONCLUSIVE instead of PASS when both sides of a comparison; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [x] 3.3 Review addressed and change archived with `openspec archive revert-recon-partition-pruning`
