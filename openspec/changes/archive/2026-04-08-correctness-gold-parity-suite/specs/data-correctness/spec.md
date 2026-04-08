# data-correctness Delta

Change `correctness-gold-parity-suite`: Extend incremental/batch parity to every gold table

## ADDED Requirements

### Requirement: Each gold table covered by parity: have its own seeded-mismatch test

Each gold table covered by parity SHALL have its own seeded-mismatch test; coverage of one table SHALL NOT be assumed to cover another.

#### Scenario: Have its own seeded-mismatch test

- **WHEN** each gold table covered by parity is exercised in a published window
- **THEN** each gold table covered by parity SHALL have its own seeded-mismatch test; coverage of one table SHALL NOT be assumed to cover another
- **AND** the outcome is visible in the job's emitted metrics

## MODIFIED Requirements

### Requirement: Incremental output: match a full recompute of the same window

Incremental output SHALL match a full recompute of the same window, for every published gold table, not only `gold_schedule_events`.

#### Scenario: Match a full recompute of the same window

- **WHEN** incremental output is exercised in a published window
- **THEN** incremental output SHALL match a full recompute of the same window
- **AND** the outcome is visible in the job's emitted metrics
