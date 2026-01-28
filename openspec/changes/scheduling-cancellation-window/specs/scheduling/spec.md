# scheduling Delta

Change `scheduling-cancellation-window`: Add the cancellation window to scheduling

## ADDED Requirements

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
