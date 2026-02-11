# payments Specification

## Purpose

Capture, refund and dispute state for customer payments, and the gold ledger finance reads.

## Requirements

### Requirement: Payments: own capture

Payments SHALL own capture, refund and dispute state transitions.

#### Scenario: Own capture

- **WHEN** payments is exercised in a published window
- **THEN** payments SHALL own capture, refund and dispute state transitions
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Payment event without a provider-issued event: be rejected

A payment event without a provider-issued event id SHALL be rejected, not assigned a surrogate.

#### Scenario: Be rejected

- **WHEN** a payment event without a provider-issued event id is exercised in a published window
- **THEN** a payment event without a provider-issued event id SHALL be rejected, not assigned a surrogate
- **AND** the outcome is visible in the job's emitted metrics
