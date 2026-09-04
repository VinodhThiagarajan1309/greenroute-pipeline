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
