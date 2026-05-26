# pipeline-orchestration Delta

Change `docs-and-stabilization`: End-of-quarter docs and stabilization pass

## MODIFIED Requirements

### Requirement: CI: fail when an archived change's deltas do

CI SHALL fail when an archived change's deltas do not match the capability spec, including a delta whose only change is a REMOVED requirement.

#### Scenario: Fail when an archived change's deltas do not reconcile

- **WHEN** CI is exercised in a published window
- **THEN** CI SHALL fail when an archived change's deltas do not reconcile against current capability specs
- **AND** the outcome is visible in the job's emitted metrics

#### Scenario: A REMOVED-only delta is detected as drift

- **WHEN** CI is exercised in a published window
- **THEN** CI SHALL fail when an archived change's deltas do not match the capability spec, including a delta whose only change is a REMOVED requirement
- **AND** the outcome is visible in the job's emitted metrics
