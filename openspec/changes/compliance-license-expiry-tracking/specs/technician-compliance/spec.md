# technician-compliance Delta

Change `compliance-license-expiry-tracking`: Staggered per-license TTL refresh for TDA license data

## ADDED Requirements

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
