# scheduling Delta

Change `license-gate-all-licensed-services`: License gate covers every service the catalog flags license_required, not only pesticide

## MODIFIED Requirements

### Requirement: Scheduling: reject confirmation of a licensed-service booking

Scheduling SHALL reject confirmation of a licensed-service booking when the assigned technician's license_status is not active, for every service type the catalog flags license_required, unless the status is pending_renewal filed on or before expiry and within 30 days of it.

#### Scenario: Reject confirmation of a licensed-service booking when the assigned

- **WHEN** scheduling is exercised in a published window
- **THEN** scheduling SHALL reject confirmation of a licensed-service booking when the assigned technician's license_status is not active
- **AND** the outcome is visible in the job's emitted metrics

#### Scenario: Pending renewal filed before expiry is accepted for 30 days

- **WHEN** scheduling is exercised in a published window
- **THEN** scheduling SHALL reject confirmation of a licensed-service booking when the assigned technician's license_status is not active, unless the status is pending_renewal, the renewal was filed on or before the expiry date, and the booking date is within 30 days of expiry
- **AND** the outcome is visible in the job's emitted metrics

#### Scenario: Herbicide booking with an expired licence is blocked

- **WHEN** scheduling is exercised in a published window
- **THEN** scheduling SHALL reject confirmation of a licensed-service booking when the assigned technician's license_status is not active, for every service type the catalog flags license_required, unless the status is pending_renewal filed on or before expiry and within 30 days of it
- **AND** the outcome is visible in the job's emitted metrics
