# pipeline-orchestration Delta

Change `orchestration-dab-bundle`: Wire the Databricks Asset Bundle for dev/staging/prod

## ADDED Requirements

### Requirement: Every job: be defined as bundle configuration in the repo

Every job SHALL be defined as bundle configuration in the repo; no job is configured through the workspace UI.

#### Scenario: Be defined as bundle configuration in the repo

- **WHEN** every job is exercised in a published window
- **THEN** every job SHALL be defined as bundle configuration in the repo; no job is configured through the workspace UI
- **AND** the outcome is visible in the job's emitted metrics
