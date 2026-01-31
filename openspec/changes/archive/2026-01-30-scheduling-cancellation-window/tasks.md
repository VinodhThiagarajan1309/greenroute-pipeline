# Tasks: scheduling-cancellation-window

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review
- [x] 1.2 Added requirement in the delta spec: Cancellation received at or after service_window_start: be marked chargeable; verify with `openspec validate scheduling-cancellation-window --strict`
- [x] 1.3 Added requirement in the delta spec: Cancellation threshold: be a single configured value; verify with `openspec validate scheduling-cancellation-window --strict`

## 2. Implementation

- [x] 2.1 feat: cancellation window evaluation on the booking event stream; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [x] 3.3 Review addressed and change archived with `openspec archive scheduling-cancellation-window`
