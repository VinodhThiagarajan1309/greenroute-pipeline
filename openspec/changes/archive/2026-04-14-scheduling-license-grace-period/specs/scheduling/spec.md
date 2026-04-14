# scheduling Delta

Change `scheduling-license-grace-period`: License gate accepts a pending TDA renewal inside the 30-day grace period

## MODIFIED Requirements

### Requirement: Scheduling: reject confirmation of a licensed-service booking

Scheduling SHALL reject confirmation of a licensed-service booking when the assigned technician's license_status is not active, unless the status is pending_renewal, the renewal was filed on or before the expiry date, and the booking date is within 30 days of expiry.

#### Scenario: Reject confirmation of a licensed-service booking when the assigned

- **WHEN** scheduling is exercised in a published window
- **THEN** scheduling SHALL reject confirmation of a licensed-service booking when the assigned technician's license_status is not active
- **AND** the outcome is visible in the job's emitted metrics

#### Scenario: Pending renewal filed before expiry is accepted for 30 days

- **WHEN** scheduling is exercised in a published window
- **THEN** scheduling SHALL reject confirmation of a licensed-service booking when the assigned technician's license_status is not active, unless the status is pending_renewal, the renewal was filed on or before the expiry date, and the booking date is within 30 days of expiry
- **AND** the outcome is visible in the job's emitted metrics
