# Design: correctness-recon-baseline

## Context

See proposal.md for motivation. This change touches `data-correctness`.

## Goals / Non-Goals

**Goals:**

- Adds `data-correctness`, whose first invariant is that incremental output equals a full recompute of the same window.

**Non-Goals:**

- Anything not listed in the proposal. If this change grows a second purpose, it is split into two changes rather than widened.

## Decisions

- The approach in the proposal, over the obvious cheaper alternative, for the reason given under *Why*. Recorded here so the next person does not rediscover the trade-off.

## Risks / Trade-offs

None recorded at the time of writing.
