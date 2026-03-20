# Tasks: correctness-incremental-parity

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review
- [x] 1.2 Added requirement in the delta spec: Parity check: compare a bounded lookback window on incremental runs; verify with `openspec validate correctness-incremental-parity --strict`
- [x] 1.3 Added requirement in the delta spec: Parity check's lookback window: be strictly wider than the data-completeness watermark; verify with `openspec validate correctness-incremental-parity --strict`

## 2. Implementation

- [x] 2.1 Add bounded incremental lookback to recon instead of rescanning full history; verify with the tests in this change
- [x] 2.2 Set lookback to 72h - wider than the 48h completeness watermark, with headroom; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [x] 3.3 Review addressed and change archived with `openspec archive correctness-incremental-parity`
