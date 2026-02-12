# Design: payments-idempotent-capture

## Context

See proposal.md for motivation. This change touches `payments`.

## Goals / Non-Goals

**Goals:**

- Adds an idempotency key on `provider_event_id`, enforced at write time, and repairs the four duplicate captures already in production.

**Non-Goals:**

- Anything not listed in the proposal. If this change grows a second purpose, it is split into two changes rather than widened.

## Decisions

- The approach in the proposal, over the obvious cheaper alternative, for the reason given under *Why*. Recorded here so the next person does not rediscover the trade-off.

## Risks / Trade-offs

None recorded at the time of writing.
