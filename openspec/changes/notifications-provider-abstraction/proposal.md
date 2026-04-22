# Proposal: Provider-agnostic NotificationSender, Twilio as the first implementation

- **Change id:** `notifications-provider-abstraction`
- **Author:** Sofia Alvarez
- **Sprint:** 8

## Why

Decided in {{I16}}: provider-agnostic now rather than committing to Twilio and unwinding it
later. Notifications is the capability most likely to grow a second channel - email, push,
the in-app inbox ops keeps asking for - and those need the same seam, not a second special
case bolted on next to the first.

The Twilio client and retry behavior come from {{PR:notifications-sms-provider-twilio}}
basically unchanged. That PR closed, the work in it didn't - it moved one layer down.

## What Changes

`NotificationSender` interface with `twilio_sms` registered as the first provider.
Confirmation, reminder, cancellation and reschedule sends now go through
`send(recipient, channel, template, payload)` instead of calling Twilio directly.

- **ADDED** requirement: notification sends SHALL go through the `NotificationSender` interface; capability code SHALL NOT reference a provider SDK directly.
- **ADDED** requirement: a provider SHALL register against one or more channels, and `send` SHALL resolve to the registered provider for the recipient's channel.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `customer-notifications`: requirements change as listed above.

## Impact

Affected code: `src/greenroute/notifications/`, `tests/notifications/`.
