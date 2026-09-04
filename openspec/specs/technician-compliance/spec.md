# technician-compliance Specification

## Purpose

Texas Department of Agriculture applicator licensing: which technicians may perform which services, and when their licenses expire.

## Requirements

### Requirement: Each technician performing a licensed service: have a recorded TDA license_status and expiry_date

Each technician performing a licensed service SHALL have a recorded TDA license_status and expiry_date.

#### Scenario: Have a recorded TDA license_status and expiry_date

- **WHEN** each technician performing a licensed service is exercised in a published window
- **THEN** each technician performing a licensed service SHALL have a recorded TDA license_status and expiry_date
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: License_status: be derived from expiry_date against the current date

License_status SHALL be derived from expiry_date against the current date, not stored as an independently mutable field.

#### Scenario: Be derived from expiry_date against the current date

- **WHEN** license_status is exercised in a published window
- **THEN** license_status SHALL be derived from expiry_date against the current date, not stored as an independently mutable field
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Technician: be matched to TDA license records by license

A technician SHALL be matched to TDA license records by license number, not by name.

#### Scenario: Be matched to TDA license records by license number

- **WHEN** a technician is exercised in a published window
- **THEN** a technician SHALL be matched to TDA license records by license number, not by name
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: License data: refresh on a per-license TTL

License data SHALL refresh on a per-license TTL rather than a single fleet-wide batch.

#### Scenario: Refresh on a per-license TTL rather than a single

- **WHEN** license data is exercised in a published window
- **THEN** license data SHALL refresh on a per-license TTL rather than a single fleet-wide batch
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Refresh requests: be distributed across the refresh window

Refresh requests SHALL be distributed across the refresh window so no rolling 60-second period exceeds the TDA rate limit.

#### Scenario: Be distributed across the refresh window so no rolling

- **WHEN** refresh requests is exercised in a published window
- **THEN** refresh requests SHALL be distributed across the refresh window so no rolling 60-second period exceeds the TDA rate limit
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: License data exceeding its TTL: be flagged stale rather than treated as current

License data exceeding its TTL SHALL be flagged stale rather than treated as current.

#### Scenario: Be flagged stale rather than treated as current

- **WHEN** license data exceeding its TTL is exercised in a published window
- **THEN** license data exceeding its TTL SHALL be flagged stale rather than treated as current
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Technician license records: carry renewal_filed_date from the TDA lookup

Technician license records SHALL carry renewal_filed_date from the TDA lookup so the grace window can be computed at booking time.

#### Scenario: Renewal filed date is carried from the TDA record

- **WHEN** technician license records is exercised in a published window
- **THEN** technician license records SHALL carry renewal_filed_date from the TDA lookup so the grace window can be computed at booking time
- **AND** the outcome is visible in the job's emitted metrics
