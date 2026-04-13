# technician-compliance Delta

Change `scheduling-license-grace-period`: License gate accepts a pending TDA renewal inside the 30-day grace period

## ADDED Requirements

### Requirement: Technician license records: carry renewal_filed_date from the TDA lookup

Technician license records SHALL carry renewal_filed_date from the TDA lookup so the grace window can be computed at booking time.

#### Scenario: Renewal filed date is carried from the TDA record

- **WHEN** technician license records is exercised in a published window
- **THEN** technician license records SHALL carry renewal_filed_date from the TDA lookup so the grace window can be computed at booking time
- **AND** the outcome is visible in the job's emitted metrics
