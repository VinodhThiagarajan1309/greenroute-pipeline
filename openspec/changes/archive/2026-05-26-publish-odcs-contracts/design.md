# Design: publish-odcs-contracts

## Context

See proposal.md for motivation. This change touches `payments`, `scheduling`.

## Goals / Non-Goals

**Goals:**

- Publishes ODCS v3.1.0 contracts for `gold_payment_ledger` and `gold_schedule_events`, and adds a CI check that fails the build when a gold table's actual schema drifts from what its contract promises.

**Non-Goals:**

- Anything not listed in the proposal. If this change grows a second purpose, it is split into two changes rather than widened.

## Decisions

- The approach in the proposal, over the obvious cheaper alternative, for the reason given under *Why*. Recorded here so the next person does not rediscover the trade-off.

## Risks / Trade-offs

> **Aisha Bello:** Does the CI check cover semantic drift, or only schema shape? A column
> that keeps its name and type but changes meaning - `status` gaining a new enum value,
> say - would pass this check and still break the dashboard.

> **Derek Chen:** Only shape - name, type, nullability. You're right that a new enum value
> passes silently. I don't want to solve that in this PR; catching meaning drift is a
> different, harder problem and bolting it onto a schema-shape check would make the check
> unreliable at the one thing it's supposed to be good at. Noted the gap explicitly in
> design.md rather than letting the CI green light imply more coverage than it has.

> **Wes Turner:** Confirmed the CI job fails correctly against a seeded column drop before
> merging this. Wanted that checked given the last check that couldn't fail.
