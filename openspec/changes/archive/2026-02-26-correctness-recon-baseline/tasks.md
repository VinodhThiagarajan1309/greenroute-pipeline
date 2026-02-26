# Tasks: correctness-recon-baseline

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review
- [x] 1.2 Added requirement in the delta spec: Incremental output: match a full recompute of the same window; verify with `openspec validate correctness-recon-baseline --strict`
- [x] 1.3 Added requirement in the delta spec: Parity check: report differing rows; verify with `openspec validate correctness-recon-baseline --strict`
- [x] 1.4 Added requirement in the delta spec: Parity check: be verified against a seeded mismatch on every; verify with `openspec validate correctness-recon-baseline --strict`

## 2. Implementation

- [x] 2.1 Report mismatches as rows, not a boolean; verify with the tests in this change
- [x] 2.2 Add recon job comparing incremental gold against a batch recompute; verify with the tests in this change
- [x] 2.3 Add recon result table with per-check row counts; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [x] 3.3 Review addressed and change archived with `openspec archive correctness-recon-baseline`
