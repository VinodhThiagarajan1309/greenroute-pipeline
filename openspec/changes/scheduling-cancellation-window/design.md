# Design: scheduling-cancellation-window

## Context

See proposal.md for motivation. This change touches `scheduling`.

## Goals / Non-Goals

**Goals:**

- Implements the cancellation window: cancellations arriving less than 2 hours before the service window start are chargeable, everything earlier is free.

**Non-Goals:**

- Anything not listed in the proposal. If this change grows a second purpose, it is split into two changes rather than widened.

## Decisions

- The approach in the proposal, over the obvious cheaper alternative, for the reason given under *Why*. Recorded here so the next person does not rediscover the trade-off.

## Risks / Trade-offs

> **Derek Chen:** Second requirement matters more than the first. The threshold existing in
> exactly one place is what stops payments and scheduling drifting apart later.
