# scheduling Delta

Change `pesticide-license-gate`: Hard gate: scheduling blocks a licensed-service booking without an active technician license

## ADDED Requirements

### Requirement: Scheduling: reject confirmation of a licensed-service booking

Scheduling SHALL reject confirmation of a licensed-service booking when the assigned technician's license_status is not active.

#### Scenario: Reject confirmation of a licensed-service booking when the assigned

- **WHEN** scheduling is exercised in a published window
- **THEN** scheduling SHALL reject confirmation of a licensed-service booking when the assigned technician's license_status is not active
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Blocked confirmation: emit a metric identifying the technician and service

A blocked confirmation SHALL emit a metric identifying the technician and service.

#### Scenario: Emit a metric identifying the technician and service

- **WHEN** a blocked confirmation is exercised in a published window
- **THEN** a blocked confirmation SHALL emit a metric identifying the technician and service
- **AND** the outcome is visible in the job's emitted metrics
