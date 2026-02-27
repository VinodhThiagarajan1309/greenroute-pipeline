# pipeline-orchestration Delta

Change `orchestration-backfill-tooling`: Make backfill non-destructive, and add the archive-drift CI check

## ADDED Requirements

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
