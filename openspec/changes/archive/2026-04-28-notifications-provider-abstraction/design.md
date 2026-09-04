# Design: notifications-provider-abstraction

## Context

See proposal.md for motivation. This change touches `customer-notifications`.

## Goals / Non-Goals

**Goals:**

- `NotificationSender` interface with `twilio_sms` registered as the first provider. Confirmation, reminder, cancellation and reschedule sends now go through `send(recipient, channel, template, payload)` instead of calling Twilio directly.

**Non-Goals:**

- Anything not listed in the proposal. If this change grows a second purpose, it is split into two changes rather than widened.

## Decisions

- The approach in the proposal, over the obvious cheaper alternative, for the reason given under *Why*. Recorded here so the next person does not rediscover the trade-off.

## Risks / Trade-offs

> **Priya Nair:** Should the registry error if two providers register for the same channel,
> or does last-registered win? Twilio's the only one today so it doesn't matter yet, but I'd
> rather ask than assume.

> **Sofia Alvarez:** Error. Silent last-write-wins is how you get a provider swap nobody
> intended, just because of import order. Raise on duplicate registration.

> **Priya Nair:** Added - raises `DuplicateProviderError` naming both providers.
