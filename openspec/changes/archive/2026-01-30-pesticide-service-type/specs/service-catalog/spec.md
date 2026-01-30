# service-catalog Delta

Change `pesticide-service-type`: Add the pesticide-application service type

## ADDED Requirements

### Requirement: Service type: declare whether it requires a licensed applicator

A service type SHALL declare whether it requires a licensed applicator.

#### Scenario: Declare whether it requires a licensed applicator

- **WHEN** a service type is exercised in a published window
- **THEN** a service type SHALL declare whether it requires a licensed applicator
- **AND** the outcome is visible in the job's emitted metrics
