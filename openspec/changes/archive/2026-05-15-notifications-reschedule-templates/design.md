# Design: notifications-reschedule-templates

## Context

See proposal.md for motivation. This change touches `customer-notifications`.

## Goals / Non-Goals

**Goals:**

- Adds message templates for reschedule and cancellation sends, both routed through the provider-agnostic interface from last sprint.

**Non-Goals:**

- Anything not listed in the proposal. If this change grows a second purpose, it is split into two changes rather than widened.

## Decisions

- The approach in the proposal, over the obvious cheaper alternative, for the reason given under *Why*. Recorded here so the next person does not rediscover the trade-off.

## Risks / Trade-offs

> **Maya Patel:** dumb question maybe, does reschedule sms and reschedule email pick their
> own copy or is there one template that renders to both?

> **Priya Nair:** Not a dumb question, that was the whole point of the abstraction. One
> template per event type, rendered per-channel by the provider interface, so the copy only
> needs review once instead of once per channel. If email and SMS need different wording
> later that's a provider-side concern, not a second template to keep in sync.
