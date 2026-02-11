# Design: payments-capture-baseline

## Context

See proposal.md for motivation. This change touches `payments`.

## Goals / Non-Goals

**Goals:**

- Introduces `payments` and the capture path from processor webhook through to `gold_payment_ledger`.

**Non-Goals:**

- Anything not listed in the proposal. If this change grows a second purpose, it is split into two changes rather than widened.

## Decisions

- The approach in the proposal, over the obvious cheaper alternative, for the reason given under *Why*. Recorded here so the next person does not rediscover the trade-off.

## Risks / Trade-offs

> **Sofia Alvarez:** Explicit state column rather than deriving state from which timestamps
> are non-null. Good. Derived state is fine until you need to know the difference between
> "not refunded" and "refund attempted and failed".
