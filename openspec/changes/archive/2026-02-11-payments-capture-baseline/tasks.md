# Tasks: payments-capture-baseline

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review
- [x] 1.2 Added requirement in the delta spec: Payments: own capture; verify with `openspec validate payments-capture-baseline --strict`
- [x] 1.3 Added requirement in the delta spec: Payment event without a provider-issued event: be rejected; verify with `openspec validate payments-capture-baseline --strict`

## 2. Implementation

- [x] 2.1 Add silver_payment_events with an explicit state column; verify with the tests in this change
- [x] 2.2 Add bronze payment event ingest from processor webhooks; verify with the tests in this change
- [x] 2.3 Add gold_payment_ledger aggregation; verify with the tests in this change
- [x] 2.4 Reject webhook payloads missing provider_event_id rather than generating a; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [x] 3.3 Review addressed and change archived with `openspec archive payments-capture-baseline`
