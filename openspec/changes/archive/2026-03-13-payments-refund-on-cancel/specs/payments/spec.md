# payments Delta

Change `payments-refund-on-cancel`: Payments reads scheduling's cancellation threshold instead of holding its own

## ADDED Requirements

### Requirement: Refund auto-approval: read the cancellation chargeable/free determination from scheduling

Refund auto-approval SHALL read the cancellation chargeable/free determination from scheduling and SHALL NOT hold an independently configured threshold.

#### Scenario: Read the cancellation chargeable/free determination from scheduling

- **WHEN** refund auto-approval is exercised in a published window
- **THEN** refund auto-approval SHALL read the cancellation chargeable/free determination from scheduling and SHALL NOT hold an independently configured threshold
- **AND** the outcome is visible in the job's emitted metrics

## REMOVED Requirements

### Requirement: Payments: apply a private auto-refund threshold independent of scheduling

Payments SHALL apply a private auto-refund threshold independent of scheduling.

**Reason**: superseded by the requirement this change adds; the behaviour no longer holds.

#### Scenario: Apply a private auto-refund threshold independent of scheduling

- **WHEN** payments is exercised in a published window
- **THEN** payments SHALL apply a private auto-refund threshold independent of scheduling
- **AND** the outcome is visible in the job's emitted metrics
