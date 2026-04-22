# customer-notifications Delta

Change `notifications-sms-provider-twilio`: SMS delivery via Twilio

## ADDED Requirements

### Requirement: SMS delivery: use the Twilio Messages API

SMS delivery SHALL use the Twilio Messages API and SHALL retry once on transient failure before logging.

#### Scenario: Use the Twilio Messages API

- **WHEN** SMS delivery is exercised in a published window
- **THEN** SMS delivery SHALL use the Twilio Messages API and SHALL retry once on transient failure before logging
- **AND** the outcome is visible in the job's emitted metrics
