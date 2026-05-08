# pipeline-orchestration Delta

Change `orchestration-backfill-hardening`: Verify backfill on value parity, not row count alone

## ADDED Requirements

### Requirement: Backfill run: be verified against a value-level parity check

A backfill run SHALL be verified against a value-level parity check, not row count alone.

#### Scenario: Be verified against a value-level parity check

- **WHEN** a backfill run is exercised in a published window
- **THEN** a backfill run SHALL be verified against a value-level parity check, not row count alone
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Parity comparison over an empty window: report INCONCLUSIVE

A parity comparison over an empty window on both sides SHALL report INCONCLUSIVE and SHALL NOT report PASS.

#### Scenario: Report INCONCLUSIVE

- **WHEN** a parity comparison over an empty window on both sides is exercised in a published window
- **THEN** a parity comparison over an empty window on both sides SHALL report INCONCLUSIVE and SHALL NOT report PASS
- **AND** the outcome is visible in the job's emitted metrics
