# payments Delta

Change `payments-refund-baseline`: Add refund state transitions to payments

## ADDED Requirements

### Requirement: Refund: reference the capture it reverses

A refund SHALL reference the capture it reverses.

#### Scenario: Reference the capture it reverses

- **WHEN** a refund is exercised in a published window
- **THEN** a refund SHALL reference the capture it reverses
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Total refunded amount for a capture: exceed the captured amount

Total refunded amount for a capture SHALL NOT exceed the captured amount.

#### Scenario: Exceed the captured amount

- **WHEN** total refunded amount for a capture is exercised in a published window
- **THEN** total refunded amount for a capture SHALL NOT exceed the captured amount
- **AND** the outcome is visible in the job's emitted metrics
