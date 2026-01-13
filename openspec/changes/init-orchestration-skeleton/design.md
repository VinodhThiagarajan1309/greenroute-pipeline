# Design: init-orchestration-skeleton

## Context

See proposal.md for motivation. This change touches `pipeline-orchestration`.

## Goals / Non-Goals

**Goals:**

- Stands up the repository and the first OpenSpec capability, `pipeline-orchestration`. It owns two things: how the Databricks jobs are wired together, and what the medallion layers are called.

**Non-Goals:**

- Anything not listed in the proposal. If this change grows a second purpose, it is split into two changes rather than widened.

## Decisions

- The approach in the proposal, over the obvious cheaper alternative, for the reason given under *Why*. Recorded here so the next person does not rediscover the trade-off.

## Risks / Trade-offs

> **Derek Chen:** Agreed on the prefixes. One thing I want to be explicit about: `gold_` is
> named for a business concept, not for a source system. `gold_payment_ledger`, not
> `gold_stripe_events`. Otherwise we'll leak the processor's vocabulary into the layer
> that finance reads.

> **Sofia Alvarez:** Good call, folded that into the requirement text rather than leaving it
> as a comment here.
