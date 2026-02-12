# payments Delta

Change `payments-idempotent-capture`: Make payment capture idempotent on provider_event_id

## ADDED Requirements

### Requirement: Capture: be idempotent on provider_event_id

Capture SHALL be idempotent on `provider_event_id`; a repeated delivery SHALL NOT create a second ledger entry.

#### Scenario: Be idempotent on provider_event_id

- **WHEN** capture is exercised in a published window
- **THEN** capture SHALL be idempotent on `provider_event_id`; a repeated delivery SHALL NOT create a second ledger entry
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Payment event ingest: reject duplicates at write time rather than resolving

Payment event ingest SHALL reject duplicates at write time rather than resolving them downstream.

#### Scenario: Reject duplicates at write time rather than resolving them

- **WHEN** payment event ingest is exercised in a published window
- **THEN** payment event ingest SHALL reject duplicates at write time rather than resolving them downstream
- **AND** the outcome is visible in the job's emitted metrics
