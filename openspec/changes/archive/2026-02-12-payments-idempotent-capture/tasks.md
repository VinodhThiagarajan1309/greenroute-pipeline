# Tasks: payments-idempotent-capture

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review
- [x] 1.2 Added requirement in the delta spec: Capture: be idempotent on provider_event_id; verify with `openspec validate payments-idempotent-capture --strict`
- [x] 1.3 Added requirement in the delta spec: Payment event ingest: reject duplicates at write time rather than resolving; verify with `openspec validate payments-idempotent-capture --strict`

## 2. Implementation

- [x] 2.1 Add idempotency check to the payment-capture retry path; verify with the tests in this change
- [x] 2.2 Enforce uniqueness at write time; downstream dedupe hides the defect; verify with the tests in this change
- [x] 2.3 Collapse the four known duplicate captures in prod; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [x] 3.3 Review addressed and change archived with `openspec archive payments-idempotent-capture`
