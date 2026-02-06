# service-catalog Specification

## Purpose

What GreenRoute sells: service types, add-ons, pricing tiers, and the constraints that attach to selling a given service.

## Requirements

### Requirement: Catalog: define exactly one active row per billable service

The catalog SHALL define exactly one active row per billable service type.

#### Scenario: Define exactly one active row per billable service type

- **WHEN** the catalog is exercised in a published window
- **THEN** the catalog SHALL define exactly one active row per billable service type
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Booking referencing an unknown service type: be quarantined

A booking referencing an unknown service type SHALL be quarantined, not defaulted.

#### Scenario: Be quarantined

- **WHEN** a booking referencing an unknown service type is exercised in a published window
- **THEN** a booking referencing an unknown service type SHALL be quarantined, not defaulted
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Service type: declare whether it requires a licensed applicator

A service type SHALL declare whether it requires a licensed applicator.

#### Scenario: Declare whether it requires a licensed applicator

- **WHEN** a service type is exercised in a published window
- **THEN** a service type SHALL declare whether it requires a licensed applicator
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Each service type: resolve to exactly one active price per zone

Each service type SHALL resolve to exactly one active price per zone tier.

#### Scenario: Resolve to exactly one active price per zone tier

- **WHEN** each service type is exercised in a published window
- **THEN** each service type SHALL resolve to exactly one active price per zone tier
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Overlapping active price rows: be rejected at write time

Overlapping active price rows for the same (service, tier) SHALL be rejected at write time.

#### Scenario: Be rejected at write time

- **WHEN** overlapping active price rows for the same (service, tier) is exercised in a published window
- **THEN** overlapping active price rows for the same (service, tier) SHALL be rejected at write time
- **AND** the outcome is visible in the job's emitted metrics
