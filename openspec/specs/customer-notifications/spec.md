# customer-notifications Specification

## Purpose

Reminder, confirmation, cancellation and reschedule messages, and the customer preferences that govern whether they may be sent.

## Requirements

### Requirement: Send: deliver to a recipient who has opted out

Send SHALL NOT deliver to a recipient who has opted out of the channel, and SHALL enforce that inside `NotificationSender.send` so that no caller performs its own preference check or can bypass it.

#### Scenario: Deliver to a recipient who has opted out

- **WHEN** a send is exercised in a published window
- **THEN** a send SHALL NOT deliver to a recipient who has opted out of the channel, regardless of message type
- **AND** the outcome is visible in the job's emitted metrics

#### Scenario: Reschedule cannot bypass the opt-out check

- **WHEN** send is exercised in a published window
- **THEN** send SHALL NOT deliver to a recipient who has opted out of the channel, and SHALL enforce that inside `NotificationSender.send` so that no caller performs its own preference check or can bypass it
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

### Requirement: Notification sends: go through the NotificationSender interface

Notification sends SHALL go through the `NotificationSender` interface; capability code SHALL NOT reference a provider SDK directly.

#### Scenario: Go through the NotificationSender interface

- **WHEN** notification sends is exercised in a published window
- **THEN** notification sends SHALL go through the `NotificationSender` interface; capability code SHALL NOT reference a provider SDK directly
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Provider: register against one or more channels

A provider SHALL register against one or more channels, and `send` SHALL resolve to the registered provider for the recipient's channel.

#### Scenario: Register against one or more channels

- **WHEN** a provider is exercised in a published window
- **THEN** a provider SHALL register against one or more channels, and `send` SHALL resolve to the registered provider for the recipient's channel
- **AND** the outcome is visible in the job's emitted metrics
