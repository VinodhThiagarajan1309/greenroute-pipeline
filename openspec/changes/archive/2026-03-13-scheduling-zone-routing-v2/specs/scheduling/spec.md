# scheduling Delta

Change `scheduling-zone-routing-v2`: Move zone grouping and stop ordering into scheduling, delete the DAB config knob

## ADDED Requirements

### Requirement: Scheduling: own both zone grouping and within-zone stop ordering

Scheduling SHALL own both zone grouping and within-zone stop ordering for a day's route.

#### Scenario: Own both zone grouping and within-zone stop ordering

- **WHEN** scheduling is exercised in a published window
- **THEN** scheduling SHALL own both zone grouping and within-zone stop ordering for a day's route
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Stop distance used for ordering: be computed as drive time

Stop distance used for ordering SHALL be computed as drive time, not straight-line distance.

#### Scenario: Be computed as drive time

- **WHEN** stop distance used for ordering is exercised in a published window
- **THEN** stop distance used for ordering SHALL be computed as drive time, not straight-line distance
- **AND** the outcome is visible in the job's emitted metrics
