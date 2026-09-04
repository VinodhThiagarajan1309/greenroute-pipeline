# Design: notifications-baseline

## Context

See proposal.md for motivation. This change touches `customer-notifications`.

## Goals / Non-Goals

**Goals:**

- Adds `customer-notifications`: SMS sends for booking confirmation, the T-24h reminder, cancellation, and reschedule. Every send checks `notification_preference` before delivery.

**Non-Goals:**

- Anything not listed in the proposal. If this change grows a second purpose, it is split into two changes rather than widened.

## Decisions

- The approach in the proposal, over the obvious cheaper alternative, for the reason given under *Why*. Recorded here so the next person does not rediscover the trade-off.

## Risks / Trade-offs

> **Priya Nair:** First delta spec I've written end to end - is `ADDED: Requirement - a send
> SHALL NOT deliver to an opted-out recipient` the right shape, or should the
> `notification_preference` table get its own ADDED requirement separate from the send
> behavior?

> **Sofia Alvarez:** Split them. One requirement per testable behavior - "the table exists
> with these columns" isn't a statement about system behavior, it's a data model note that
> belongs in design.md, not the spec. Keep the requirement as the SHALL NOT and move the
> table shape out.

> **Priya Nair:** Done - table description is in design.md now, the requirement is just the
> SHALL NOT.

> **Aisha Bello:** Copy review flagged one thing before we signed off: the original reminder
> text said "Reply STOP to opt out." STOP-reply handling isn't built yet, so until it is,
> `notification_preference` is the *only* real opt-out path, and it has to actually work, not
> just exist.

> **Priya Nair:** Right - dropped the STOP-reply line from the copy for now and pointed
> customers at the app toggle instead, which does write to `notification_preference`. Will
> add STOP-reply as a second write path once it exists rather than promise it early.
