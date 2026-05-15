# customer-notifications Delta

Change `notifications-reschedule-templates`: Add reschedule and cancellation notification templates

## ADDED Requirements

### Requirement: Reschedule send: use the reschedule template

A reschedule send SHALL use the reschedule template, not the booking-confirmation template with substituted fields.

#### Scenario: Use the reschedule template

- **WHEN** a reschedule send is exercised in a published window
- **THEN** a reschedule send SHALL use the reschedule template, not the booking-confirmation template with substituted fields
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Cancellation send: render correctly for a booking with zero add-ons

A cancellation send SHALL render correctly for a booking with zero add-ons.

#### Scenario: Render correctly for a booking with zero add-ons

- **WHEN** a cancellation send is exercised in a published window
- **THEN** a cancellation send SHALL render correctly for a booking with zero add-ons
- **AND** the outcome is visible in the job's emitted metrics
