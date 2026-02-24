# Design: completeness-source-window-closure

## Context

See proposal.md for motivation. This change touches `data-completeness`.

## Goals / Non-Goals

**Goals:**

- Turns the watermark from a recorded number into an enforced gate: gold publish blocks until every contributing source has closed its window.

**Non-Goals:**

- Anything not listed in the proposal. If this change grows a second purpose, it is split into two changes rather than widened.

## Decisions

- The approach in the proposal, over the obvious cheaper alternative, for the reason given under *Why*. Recorded here so the next person does not rediscover the trade-off.

## Risks / Trade-offs

None recorded at the time of writing.
