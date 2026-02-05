# service-catalog Delta

Change `catalog-pricing-tiers`: Add zone-based pricing tiers to the catalog

## ADDED Requirements

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
