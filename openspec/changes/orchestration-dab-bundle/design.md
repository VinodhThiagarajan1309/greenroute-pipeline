# Design: orchestration-dab-bundle

## Context

See proposal.md for motivation. This change touches `pipeline-orchestration`.

## Goals / Non-Goals

**Goals:**

- Adds `databricks.yml` plus per-target overrides so the pipeline deploys the same way in all three environments, and makes CI validate the bundle on every PR.

**Non-Goals:**

- Anything not listed in the proposal. If this change grows a second purpose, it is split into two changes rather than widened.

## Decisions

- The approach in the proposal, over the obvious cheaper alternative, for the reason given under *Why*. Recorded here so the next person does not rediscover the trade-off.

## Risks / Trade-offs

None recorded at the time of writing.
