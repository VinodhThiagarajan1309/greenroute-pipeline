# Design: scheduling-zone-routing

## Context

See proposal.md for motivation. This change touches `scheduling`.

## Goals / Non-Goals

**Goals:**

- First pass at a zone-based route optimizer that groups a day's stops by zone before ordering them.

**Non-Goals:**

- Anything not listed in the proposal. If this change grows a second purpose, it is split into two changes rather than widened.

## Decisions

- The approach in the proposal, over the obvious cheaper alternative, for the reason given under *Why*. Recorded here so the next person does not rediscover the trade-off.

## Risks / Trade-offs

None recorded at the time of writing.
