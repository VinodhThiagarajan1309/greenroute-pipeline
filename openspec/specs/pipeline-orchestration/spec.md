# pipeline-orchestration Specification

## Purpose

How GreenRoute's Databricks jobs are wired together, deployed and retried, and what the medallion layers are called.

## Requirements

### Requirement: Every published table: carry a bronze_ / silver_ / gold_ prefix

Every published table SHALL carry a `bronze_` / `silver_` / `gold_` prefix matching its layer.

#### Scenario: Carry a bronze_ / silver_ / gold_ prefix matching

- **WHEN** every published table is exercised in a published window
- **THEN** every published table SHALL carry a `bronze_` / `silver_` / `gold_` prefix matching its layer
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Each layer: live in its own Unity Catalog schema

Each layer SHALL live in its own Unity Catalog schema, one catalog per environment.

#### Scenario: Live in its own Unity Catalog schema

- **WHEN** each layer is exercised in a published window
- **THEN** each layer SHALL live in its own Unity Catalog schema, one catalog per environment
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Every job: be defined as bundle configuration in the repo

Every job SHALL be defined as bundle configuration in the repo; no job is configured through the workspace UI.

#### Scenario: Be defined as bundle configuration in the repo

- **WHEN** every job is exercised in a published window
- **THEN** every job SHALL be defined as bundle configuration in the repo; no job is configured through the workspace UI
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Backfill: merge on event key

Backfill SHALL merge on event key and SHALL NOT reduce the row count of a previously published partition.

#### Scenario: Merge on event key

- **WHEN** backfill is exercised in a published window
- **THEN** backfill SHALL merge on event key and SHALL NOT reduce the row count of a previously published partition
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: CI: fail when an archived change's deltas do

CI SHALL fail when an archived change's deltas do not reconcile against current capability specs.

#### Scenario: Fail when an archived change's deltas do not reconcile

- **WHEN** CI is exercised in a published window
- **THEN** CI SHALL fail when an archived change's deltas do not reconcile against current capability specs
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Job failure: be classified retryable or fatal at the point

A job failure SHALL be classified retryable or fatal at the point it is raised, not inferred later from the exception type.

#### Scenario: Be classified retryable or fatal at the point

- **WHEN** a job failure is exercised in a published window
- **THEN** a job failure SHALL be classified retryable or fatal at the point it is raised, not inferred later from the exception type
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Failed data-completeness or data-correctness gate: be classified fatal

A failed data-completeness or data-correctness gate SHALL be classified fatal and SHALL NOT be retried.

#### Scenario: Be classified fatal

- **WHEN** a failed data-completeness or data-correctness gate is exercised in a published window
- **THEN** a failed data-completeness or data-correctness gate SHALL be classified fatal and SHALL NOT be retried
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Retryable failure: retry at most 3 times with backoff

A retryable failure SHALL retry at most 3 times with backoff before paging.

#### Scenario: Retry at most 3 times with backoff before paging

- **WHEN** a retryable failure is exercised in a published window
- **THEN** a retryable failure SHALL retry at most 3 times with backoff before paging
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Backfill run: be verified against a value-level parity check

A backfill run SHALL be verified against a value-level parity check, not row count alone.

#### Scenario: Be verified against a value-level parity check

- **WHEN** a backfill run is exercised in a published window
- **THEN** a backfill run SHALL be verified against a value-level parity check, not row count alone
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Parity comparison over an empty window: report INCONCLUSIVE

A parity comparison over an empty window on both sides SHALL report INCONCLUSIVE and SHALL NOT report PASS.

#### Scenario: Report INCONCLUSIVE

- **WHEN** a parity comparison over an empty window on both sides is exercised in a published window
- **THEN** a parity comparison over an empty window on both sides SHALL report INCONCLUSIVE and SHALL NOT report PASS
- **AND** the outcome is visible in the job's emitted metrics
