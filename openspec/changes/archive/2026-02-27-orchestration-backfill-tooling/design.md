# Design: orchestration-backfill-tooling

## Context

See proposal.md for motivation. This change touches `pipeline-orchestration`.

## Goals / Non-Goals

**Goals:**

- Two things, both plumbing. Backfill stops being destructive, and CI starts catching spec drift.

**Non-Goals:**

- Anything not listed in the proposal. If this change grows a second purpose, it is split into two changes rather than widened.

## Decisions

- The approach in the proposal, over the obvious cheaper alternative, for the reason given under *Why*. Recorded here so the next person does not rediscover the trade-off.

## Risks / Trade-offs

None recorded at the time of writing.
