# scheduling Delta

Change `scheduling-zone-routing`: Zone-based route optimizer

## ADDED Requirements

### Requirement: Day's stops: be ordered within zone before across zone

A day's stops SHALL be ordered within zone before across zone.

#### Scenario: Be ordered within zone before across zone

- **WHEN** a day's stops is exercised in a published window
- **THEN** a day's stops SHALL be ordered within zone before across zone
- **AND** the outcome is visible in the job's emitted metrics
