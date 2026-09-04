# customer-notifications Delta

Change `notifications-provider-abstraction`: Provider-agnostic NotificationSender, Twilio as the first implementation

## ADDED Requirements

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
