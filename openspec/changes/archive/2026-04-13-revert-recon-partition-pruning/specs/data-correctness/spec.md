# data-correctness Delta

Change `revert-recon-partition-pruning`: Revert the gold-parity partition pruning; recon has been comparing empty to empty since Apr 8

## ADDED Requirements

### Requirement: Parity comparison in which both sides: be reported as INCONCLUSIVE

A parity comparison in which both sides read zero rows SHALL be reported as INCONCLUSIVE, and SHALL NOT be reported as PASS.

#### Scenario: Be reported as INCONCLUSIVE

- **WHEN** a parity comparison in which both sides read zero rows is exercised in a published window
- **THEN** a parity comparison in which both sides read zero rows SHALL be reported as INCONCLUSIVE, and SHALL NOT be reported as PASS
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Any change to a parity check's: be accompanied by a seeded-mismatch test exercised

Any change to a parity check's scan filtering SHALL be accompanied by a seeded-mismatch test exercised against the filtered path, for the specific table being changed.

#### Scenario: Be accompanied by a seeded-mismatch test exercised

- **WHEN** any change to a parity check's scan filtering is exercised in a published window
- **THEN** any change to a parity check's scan filtering SHALL be accompanied by a seeded-mismatch test exercised against the filtered path, for the specific table being changed
- **AND** the outcome is visible in the job's emitted metrics
