# scheduling Delta

Change `expansion-zip-onboarding-workflow`: Zone registry becomes the single source of truth for zip -> zone

## MODIFIED Requirements

### Requirement: Scheduling: own both zone grouping and within-zone stop ordering

Scheduling SHALL own both zone grouping and within-zone stop ordering, resolving each stop's zone through the neighborhood-expansion registry rather than a local zip mapping.

#### Scenario: Own both zone grouping and within-zone stop ordering

- **WHEN** scheduling is exercised in a published window
- **THEN** scheduling SHALL own both zone grouping and within-zone stop ordering for a day's route
- **AND** the outcome is visible in the job's emitted metrics

#### Scenario: Stop zone is resolved through the registry, not a local map

- **WHEN** scheduling is exercised in a published window
- **THEN** scheduling SHALL own both zone grouping and within-zone stop ordering, resolving each stop's zone through the neighborhood-expansion registry rather than a local zip mapping
- **AND** the outcome is visible in the job's emitted metrics
