# Proposal: Make the opted-out check unbypassable: move it inside NotificationSender.send

- **Change id:** `scheduling-notification-hooks`
- **Author:** Maya Patel
- **Sprint:** 8

## Why

Closes {{I15}}. Three confirmed customers who opted out of SMS got reschedule texts anyway,
because reschedule never called the preference lookup that confirmation and reminder use.
Support has the tickets.

First pass here checked preference at the top of the reschedule handler, matching what
confirmation and reminder already did at their own call sites. Priya pointed out that's the
same bug shape as the one filed in {{I15}} - a check that lives at N call sites gets missed
at call site N+1, and reschedule is proof it already happened once. Force-pushed the version
where the check lives inside `send()` instead: the reschedule handler no longer knows
`notification_preference` exists, and there is no call site left to forget it at.

## What Changes

Closes the gap from {{I15}}: reschedule built its own send call and skipped the preference
lookup entirely. Fixes it by making `NotificationSender.send` itself refuse to deliver to an
opted-out recipient, so no caller can bypass the check by forgetting it.

- **MODIFIED** requirement: send SHALL NOT deliver to a recipient who has opted out of the channel, and SHALL enforce that inside `NotificationSender.send` so that no caller performs its own preference check or can bypass it.
- **ADDED** requirement: the reschedule path SHALL send notifications through `NotificationSender`, not a direct send call.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `scheduling`: requirements change as listed above.
- `customer-notifications`: requirements change as listed above.

## Impact

Affected code: `src/greenroute/notifications/`, `src/greenroute/scheduling/`, `tests/notifications/`, `tests/scheduling/`.

Closes {{I15}}.
