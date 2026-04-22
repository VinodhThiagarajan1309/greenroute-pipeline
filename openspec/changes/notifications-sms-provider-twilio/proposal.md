# Proposal: SMS delivery via Twilio

- **Change id:** `notifications-sms-provider-twilio`
- **Author:** Priya Nair
- **Sprint:** 8

## Why

Fastest way to get real SMS out instead of the stubbed sender from the last PR. Retries once
on a transient failure, logs and gives up on the second, so a Twilio blip doesn't silently
eat a reschedule notice.

**Update:** closing this in favor of {{PR:notifications-provider-abstraction}}. Sofia raised
{{I16}} asking the team to decide on purpose between committing to Twilio here versus a
provider-agnostic seam, rather than let whichever PR merges first decide it by default. The
team went with the seam. The Twilio client and retry logic below aren't wrong, they're not
wasted - they move under the new interface in the next PR basically unchanged.

## What Changes

Direct Twilio integration for the four sends from `notifications-baseline` - no abstraction
layer, `TwilioClient.send_sms()` called from each send path.

- **ADDED** requirement: SMS delivery SHALL use the Twilio Messages API and SHALL retry once on transient failure before logging.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `customer-notifications`: requirements change as listed above.

## Impact

Affected code: `src/greenroute/notifications/`, `tests/notifications/`.
