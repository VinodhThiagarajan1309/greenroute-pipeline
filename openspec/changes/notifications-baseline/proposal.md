# Proposal: Add the customer-notifications capability: confirmation, reminder, cancellation, reschedule

- **Change id:** `notifications-baseline`
- **Author:** Priya Nair
- **Sprint:** 8

## Why

These have been going out ad hoc - reminder copy lived in one script, confirmation copy in
another, neither aware a customer could opt out of anything. Making the preference check
part of the capability's first requirement, not something bolted on after support forwards
the first complaint. An SMS to someone who opted out isn't a formatting bug, it's a consent
problem, and I'd rather the spec say so from the first line.

Copy for all four templates reviewed by Aisha and the support team lead - support owns the
words a customer actually reads, not engineering.

## What Changes

Adds `customer-notifications`: SMS sends for booking confirmation, the T-24h reminder,
cancellation, and reschedule. Every send checks `notification_preference` before delivery.

- **ADDED** requirement: a send SHALL NOT deliver to a recipient who has opted out of the channel, regardless of message type.
- **ADDED** requirement: reminder notifications SHALL fire at T-24h relative to the service window start.
- **ADDED** requirement: opt-out SHALL apply per channel; opting out of SMS SHALL NOT affect other channels.

## Capabilities

### New Capabilities

- `customer-notifications`: Reminder, confirmation, cancellation and reschedule messages, and the customer preferences that govern whether they may be sent.

### Modified Capabilities

- None.

## Impact

Affected code: `src/greenroute/notifications/`, `tests/notifications/`.
