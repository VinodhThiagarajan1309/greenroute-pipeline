# customer-notifications Delta

Change `scheduling-notification-hooks`: Make the opted-out check unbypassable: move it inside NotificationSender.send

## MODIFIED Requirements

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
