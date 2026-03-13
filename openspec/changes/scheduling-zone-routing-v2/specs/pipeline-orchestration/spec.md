# pipeline-orchestration Delta

Change `scheduling-zone-routing-v2`: Move zone grouping and stop ordering into scheduling, delete the DAB config knob

## REMOVED Requirements

### Requirement: DAB job-parameter config: control zone grouping and stop ordering ownership moved

The DAB job-parameter config SHALL control zone grouping and stop ordering (ownership moved to scheduling).

**Reason**: superseded by the requirement this change adds; the behaviour no longer holds.

#### Scenario: Control zone grouping and stop ordering ownership moved

- **WHEN** the DAB job-parameter config is exercised in a published window
- **THEN** the DAB job-parameter config SHALL control zone grouping and stop ordering (ownership moved to scheduling)
- **AND** the outcome is visible in the job's emitted metrics
