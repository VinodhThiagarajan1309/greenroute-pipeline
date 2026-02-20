# service-catalog Delta

Change `catalog-service-addons`: Add booking add-ons to the catalog

## ADDED Requirements

### Requirement: Add-on: attach to a booking

An add-on SHALL attach to a booking and SHALL NOT be modelled as a service type variant.

#### Scenario: Attach to a booking

- **WHEN** an add-on is exercised in a published window
- **THEN** an add-on SHALL attach to a booking and SHALL NOT be modelled as a service type variant
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Add-on price: be resolved and frozen at booking time

Add-on price SHALL be resolved and frozen at booking time.

#### Scenario: Be resolved and frozen at booking time

- **WHEN** add-on price is exercised in a published window
- **THEN** add-on price SHALL be resolved and frozen at booking time
- **AND** the outcome is visible in the job's emitted metrics
