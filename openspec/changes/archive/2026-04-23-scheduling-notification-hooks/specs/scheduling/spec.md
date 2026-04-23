# scheduling Delta

Change `scheduling-notification-hooks`: Make the opted-out check unbypassable: move it inside NotificationSender.send

## ADDED Requirements

### Requirement: Reschedule path: send notifications through NotificationSender

The reschedule path SHALL send notifications through `NotificationSender`, not a direct send call.

#### Scenario: Send notifications through NotificationSender

- **WHEN** the reschedule path is exercised in a published window
- **THEN** the reschedule path SHALL send notifications through `NotificationSender`, not a direct send call
- **AND** the outcome is visible in the job's emitted metrics
