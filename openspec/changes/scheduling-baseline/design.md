# Design: scheduling-baseline

## Context

See proposal.md for motivation. This change touches `scheduling`.

## Goals / Non-Goals

**Goals:**

- Adds the `scheduling` capability and the bronze ingest for booking events, including a quarantine path for rows we can't zone.

**Non-Goals:**

- Anything not listed in the proposal. If this change grows a second purpose, it is split into two changes rather than widened.

## Decisions

- The approach in the proposal, over the obvious cheaper alternative, for the reason given under *Why*. Recorded here so the next person does not rediscover the trade-off.

## Risks / Trade-offs

> **Sofia Alvarez:** The rejected-rows table should be a first-class output, not a debugging
> aid. If nothing reads it, we're back to dropping rows with extra steps.

> **Maya Patel:** fair. added a row count metric on it so it shows up on the job dashboard.
