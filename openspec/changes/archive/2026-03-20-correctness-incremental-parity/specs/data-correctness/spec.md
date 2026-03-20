# data-correctness Delta

Change `correctness-incremental-parity`: Bound the incremental/batch parity check to a lookback wider than the completeness watermark

## ADDED Requirements

### Requirement: Parity check: compare a bounded lookback window on incremental runs

The parity check SHALL compare a bounded lookback window on incremental runs, not full history.

#### Scenario: Compare a bounded lookback window on incremental runs

- **WHEN** the parity check is exercised in a published window
- **THEN** the parity check SHALL compare a bounded lookback window on incremental runs, not full history
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Parity check's lookback window: be strictly wider than the data-completeness watermark

The parity check's lookback window SHALL be strictly wider than the data-completeness watermark for every source it reconciles.

#### Scenario: Be strictly wider than the data-completeness watermark for every

- **WHEN** the parity check's lookback window is exercised in a published window
- **THEN** the parity check's lookback window SHALL be strictly wider than the data-completeness watermark for every source it reconciles
- **AND** the outcome is visible in the job's emitted metrics
