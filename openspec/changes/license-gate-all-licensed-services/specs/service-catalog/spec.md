# service-catalog Delta

Change `license-gate-all-licensed-services`: License gate covers every service the catalog flags license_required, not only pesticide

## ADDED Requirements

### Requirement: Each service type: declare license_required explicitly

Each service type SHALL declare license_required explicitly, and the scheduling gate SHALL read that flag rather than a list of service names.

#### Scenario: Catalog declares license_required per service type

- **WHEN** each service type is exercised in a published window
- **THEN** each service type SHALL declare license_required explicitly, and the scheduling gate SHALL read that flag rather than a list of service names
- **AND** the outcome is visible in the job's emitted metrics
