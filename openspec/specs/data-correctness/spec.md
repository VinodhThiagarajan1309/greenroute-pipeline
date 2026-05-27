# data-correctness Specification

## Purpose

Whether the rows that are present are right: incremental-versus-batch parity and reconciliation of the gold tables.

## Requirements

### Requirement: Incremental output: match a full recompute of the same window

Incremental output SHALL match a full recompute of the same window, for every published gold table, not only `gold_schedule_events`.

#### Scenario: Match a full recompute of the same window

- **WHEN** incremental output is exercised in a published window
- **THEN** incremental output SHALL match a full recompute of the same window
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Parity check: report differing rows

The parity check SHALL report differing rows, and SHALL block merge of the change that caused them rather than only the downstream gold publish.

#### Scenario: Report differing rows

- **WHEN** the parity check is exercised in a published window
- **THEN** the parity check SHALL report differing rows, not only a pass/fail verdict
- **AND** the outcome is visible in the job's emitted metrics

#### Scenario: A parity failure blocks the causing change

- **WHEN** the parity check is exercised in a published window
- **THEN** the parity check SHALL report differing rows, and SHALL block merge of the change that caused them rather than only the downstream gold publish
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Parity check: be verified against a seeded mismatch on every

The parity check SHALL be verified against a seeded mismatch on every CI run.

#### Scenario: Be verified against a seeded mismatch on every CI

- **WHEN** the parity check is exercised in a published window
- **THEN** the parity check SHALL be verified against a seeded mismatch on every CI run
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Parity check: compare a bounded lookback window on incremental runs

The parity check SHALL compare a bounded lookback window on incremental runs, not full history.

#### Scenario: Compare a bounded lookback window on incremental runs

- **WHEN** the parity check is exercised in a published window
- **THEN** the parity check SHALL compare a bounded lookback window on incremental runs, not full history
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Parity check's lookback window: be strictly wider than the data-completeness watermark

The parity check's lookback window SHALL be strictly wider than the data-completeness watermark for every source it reconciles.

#### Scenario: Be strictly wider than the data-completeness watermark for every

- **WHEN** the parity check's lookback window is exercised in a published window
- **THEN** the parity check's lookback window SHALL be strictly wider than the data-completeness watermark for every source it reconciles
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Each gold table covered by parity: have its own seeded-mismatch test

Each gold table covered by parity SHALL have its own seeded-mismatch test; coverage of one table SHALL NOT be assumed to cover another.

#### Scenario: Have its own seeded-mismatch test

- **WHEN** each gold table covered by parity is exercised in a published window
- **THEN** each gold table covered by parity SHALL have its own seeded-mismatch test; coverage of one table SHALL NOT be assumed to cover another
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Parity comparison in which both sides: be reported as INCONCLUSIVE

A parity comparison in which both sides read zero rows SHALL be reported as INCONCLUSIVE, and SHALL NOT be reported as PASS.

#### Scenario: Be reported as INCONCLUSIVE

- **WHEN** a parity comparison in which both sides read zero rows is exercised in a published window
- **THEN** a parity comparison in which both sides read zero rows SHALL be reported as INCONCLUSIVE, and SHALL NOT be reported as PASS
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Any change to a parity check's: be accompanied by a seeded-mismatch test exercised

Any change to a parity check's scan filtering SHALL be accompanied by a seeded-mismatch test exercised against the filtered path, for the specific table being changed.

#### Scenario: Be accompanied by a seeded-mismatch test exercised

- **WHEN** any change to a parity check's scan filtering is exercised in a published window
- **THEN** any change to a parity check's scan filtering SHALL be accompanied by a seeded-mismatch test exercised against the filtered path, for the specific table being changed
- **AND** the outcome is visible in the job's emitted metrics
