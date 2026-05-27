# data-correctness Delta

Change `docs-and-stabilization`: End-of-quarter docs and stabilization pass

## MODIFIED Requirements

### Requirement: Parity check: report differing rows

The parity check SHALL report differing rows, and SHALL block merge of the change that caused them rather than only the downstream gold publish.

#### Scenario: Report differing rows

- **WHEN** the parity check is exercised in a published window
- **THEN** the parity check SHALL report differing rows, not only a pass/fail verdict
- **AND** the outcome is visible in the job's emitted metrics

#### Scenario: A parity failure blocks the causing change

- **WHEN** the parity check is exercised in a published window
- **THEN** the parity check SHALL report differing rows, and SHALL block merge of the change that caused them rather than only the downstream gold publish
- **AND** the outcome is visible in the job's emitted metrics
