# Design: service-catalog-baseline

## Context

See proposal.md for motivation. This change touches `service-catalog`.

## Goals / Non-Goals

**Goals:**

- Introduces `service-catalog`: the capability that decides what GreenRoute sells, what it costs, and what constraints attach to selling it.

**Non-Goals:**

- Anything not listed in the proposal. If this change grows a second purpose, it is split into two changes rather than widened.

## Decisions

- The approach in the proposal, over the obvious cheaper alternative, for the reason given under *Why*. Recorded here so the next person does not rediscover the trade-off.

## Risks / Trade-offs

> **Sofia Alvarez:** Quarantine-not-default is the right instinct. Defaulting is how you get
> six months of revenue booked against the wrong service type and nobody notices.
