# Tasks: correctness-gold-parity-suite

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review
- [x] 1.2 Modified requirement in the delta spec: Incremental output: match a full recompute of the same window; verify with `openspec validate correctness-gold-parity-suite --strict`
- [x] 1.3 Added requirement in the delta spec: Each gold table covered by parity: have its own seeded-mismatch test; verify with `openspec validate correctness-gold-parity-suite --strict`

## 2. Implementation

- [x] 2.1 Generalize recon job to iterate gold tables from the catalog registry instead; verify with the tests in this change
- [x] 2.2 Add parity check for gold_service_catalog; verify with the tests in this change
- [x] 2.3 Add parity check for gold_payment_ledger; verify with the tests in this change
- [x] 2.4 Prune the batch-side scan to the affected date range instead of rescanning full; verify with the tests in this change
- [x] 2.5 Add scan-bytes-read metric per table so the pruning win shows up on the recon; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [x] 3.3 Review addressed and change archived with `openspec archive correctness-gold-parity-suite`
