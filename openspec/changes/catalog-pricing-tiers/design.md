# Design: catalog-pricing-tiers

## Context

See proposal.md for motivation. This change touches `service-catalog`.

## Goals / Non-Goals

**Goals:**

- Adds pricing tiers so the same service can carry different prices in core Austin versus the outer ring, and enforces that exactly one price is active per (service, tier) at a time.

**Non-Goals:**

- Anything not listed in the proposal. If this change grows a second purpose, it is split into two changes rather than widened.

## Decisions

- The approach in the proposal, over the obvious cheaper alternative, for the reason given under *Why*. Recorded here so the next person does not rediscover the trade-off.

## Risks / Trade-offs

None recorded at the time of writing.
