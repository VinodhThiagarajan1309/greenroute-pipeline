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
