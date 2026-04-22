# Design: notifications-sms-provider-twilio

## Context

See proposal.md for motivation. This change touches `customer-notifications`.

## Goals / Non-Goals

**Goals:**

- Direct Twilio integration for the four sends from `notifications-baseline` - no abstraction layer, `TwilioClient.send_sms()` called from each send path.

**Non-Goals:**

- Anything not listed in the proposal. If this change grows a second purpose, it is split into two changes rather than widened.

## Decisions

- The approach in the proposal, over the obvious cheaper alternative, for the reason given under *Why*. Recorded here so the next person does not rediscover the trade-off.

## Risks / Trade-offs

> **Sofia Alvarez:** See {{I16}} before this goes further - I want us to decide this on
> purpose rather than by whichever PR lands first.

> **Priya Nair:** Makes sense, and honestly I don't have a strong read yet on how likely a
> second channel is - I've been here three weeks. Closing this; the Twilio client moves over
> to the abstraction PR pretty much unchanged.
