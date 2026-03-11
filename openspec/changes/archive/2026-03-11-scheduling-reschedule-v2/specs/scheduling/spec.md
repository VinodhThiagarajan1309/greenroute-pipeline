# scheduling Delta

Change `scheduling-reschedule-v2`: Rewrite reschedule so it invalidates derived route state instead of leaving it behind

## ADDED Requirements

### Requirement: Reschedule: invalidate every derived route assignment for the booking's

Reschedule SHALL invalidate every derived route assignment for the booking's original date, in the same transaction as the date change.

#### Scenario: Invalidate every derived route assignment for the booking's original

- **WHEN** reschedule is exercised in a published window
- **THEN** reschedule SHALL invalidate every derived route assignment for the booking's original date, in the same transaction as the date change
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Reschedule: preserve the booking's identity and history

A reschedule SHALL preserve the booking's identity and history, and SHALL NOT be represented internally as a cancellation followed by a new booking.

#### Scenario: Preserve the booking's identity and history

- **WHEN** a reschedule is exercised in a published window
- **THEN** a reschedule SHALL preserve the booking's identity and history, and SHALL NOT be represented internally as a cancellation followed by a new booking
- **AND** the outcome is visible in the job's emitted metrics
