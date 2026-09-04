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
