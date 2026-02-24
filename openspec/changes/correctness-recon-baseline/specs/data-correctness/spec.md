# data-correctness Delta

Change `correctness-recon-baseline`: Add the data-correctness capability and the incremental/batch parity check

## Purpose

Whether the rows that are present are right: incremental-versus-batch parity and reconciliation of the gold tables.

## ADDED Requirements

### Requirement: Incremental output: match a full recompute of the same window

Incremental output SHALL match a full recompute of the same window.

#### Scenario: Match a full recompute of the same window

- **WHEN** incremental output is exercised in a published window
- **THEN** incremental output SHALL match a full recompute of the same window
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Parity check: report differing rows

The parity check SHALL report differing rows, not only a pass/fail verdict.

#### Scenario: Report differing rows

- **WHEN** the parity check is exercised in a published window
- **THEN** the parity check SHALL report differing rows, not only a pass/fail verdict
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Parity check: be verified against a seeded mismatch on every

The parity check SHALL be verified against a seeded mismatch on every CI run.

#### Scenario: Be verified against a seeded mismatch on every CI

- **WHEN** the parity check is exercised in a published window
- **THEN** the parity check SHALL be verified against a seeded mismatch on every CI run
- **AND** the outcome is visible in the job's emitted metrics
