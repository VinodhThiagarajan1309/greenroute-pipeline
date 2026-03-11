# scheduling Specification

## Purpose

Booking, rescheduling and cancellation of lawn-care jobs, including zone routing and the cancellation window.

## Requirements

### Requirement: Scheduling: own booking

Scheduling SHALL own booking, reschedule and cancellation state transitions.

#### Scenario: Own booking

- **WHEN** scheduling is exercised in a published window
- **THEN** scheduling SHALL own booking, reschedule and cancellation state transitions
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Booking that cannot be resolved: be quarantined

A booking that cannot be resolved to a zone SHALL be quarantined and SHALL NOT be silently discarded.

#### Scenario: Be quarantined

- **WHEN** a booking that cannot be resolved to a zone is exercised in a published window
- **THEN** a booking that cannot be resolved to a zone SHALL be quarantined and SHALL NOT be silently discarded
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Cancellation received at or after service_window_start: be marked chargeable

A cancellation received at or after (service_window_start - 2h) SHALL be marked chargeable.

#### Scenario: Be marked chargeable

- **WHEN** a cancellation received at or after (service_window_start - 2h) is exercised in a published window
- **THEN** a cancellation received at or after (service_window_start - 2h) SHALL be marked chargeable
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Cancellation threshold: be a single configured value

The cancellation threshold SHALL be a single configured value; no capability may hold its own copy.

#### Scenario: Be a single configured value

- **WHEN** the cancellation threshold is exercised in a published window
- **THEN** the cancellation threshold SHALL be a single configured value; no capability may hold its own copy
- **AND** the outcome is visible in the job's emitted metrics

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
