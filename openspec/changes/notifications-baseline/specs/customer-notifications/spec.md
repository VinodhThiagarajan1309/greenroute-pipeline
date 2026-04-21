# customer-notifications Delta

Change `notifications-baseline`: Add the customer-notifications capability: confirmation, reminder, cancellation, reschedule

## Purpose

Reminder, confirmation, cancellation and reschedule messages, and the customer preferences that govern whether they may be sent.

## ADDED Requirements

### Requirement: Send: deliver to a recipient who has opted out

A send SHALL NOT deliver to a recipient who has opted out of the channel, regardless of message type.

#### Scenario: Deliver to a recipient who has opted out

- **WHEN** a send is exercised in a published window
- **THEN** a send SHALL NOT deliver to a recipient who has opted out of the channel, regardless of message type
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Reminder notifications: fire at T-24h relative to the service window

Reminder notifications SHALL fire at T-24h relative to the service window start.

#### Scenario: Fire at T-24h relative to the service window start

- **WHEN** reminder notifications is exercised in a published window
- **THEN** reminder notifications SHALL fire at T-24h relative to the service window start
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Opt-out: apply per channel

Opt-out SHALL apply per channel; opting out of SMS SHALL NOT affect other channels.

#### Scenario: Apply per channel

- **WHEN** opt-out is exercised in a published window
- **THEN** opt-out SHALL apply per channel; opting out of SMS SHALL NOT affect other channels
- **AND** the outcome is visible in the job's emitted metrics
