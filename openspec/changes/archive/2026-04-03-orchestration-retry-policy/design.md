# Design: orchestration-retry-policy

## Context

See proposal.md for motivation. This change touches `pipeline-orchestration`.

## Goals / Non-Goals

**Goals:**

- Job-level retry policy. Retryable failure classes (timeouts, throttling, transient connection errors) retry with backoff up to 3 attempts. Everything else - specifically a failed completeness or correctness gate - pages on the first failure and does not retry.

**Non-Goals:**

- Anything not listed in the proposal. If this change grows a second purpose, it is split into two changes rather than widened.

## Decisions

- The approach in the proposal, over the obvious cheaper alternative, for the reason given under *Why*. Recorded here so the next person does not rediscover the trade-off.

## Risks / Trade-offs

> **Derek Chen:** Where does a payment capture failure land in this - retryable or fatal? A
> processor timeout on capture looks like transient infra 95% of the time, and the other 5%
> it's a duplicate-capture risk if we retry blind.

> **Sofia Alvarez:** Retryable. Idempotency is what makes that safe, not this policy -
> `payments-idempotent-capture` from sprint 3 already covers it. This classifies the
> failure; payments still owns making its own retries safe. Different job.
