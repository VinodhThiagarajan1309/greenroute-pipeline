# Design: license-gate-all-licensed-services

## Context

See proposal.md for motivation. This change touches `scheduling`, `service-catalog`.

## Goals / Non-Goals

**Goals:**

- The requirement has said "licensed-service" since Apr 4, but the scenario, the tests and the catalog only ever meant pesticide. TDA licenses herbicide and fertilizer application under the same rule. This change makes the requirement say so, and flags those two service types `license_required` in the catalog, which is the only thing the gate reads.

**Non-Goals:**

- Anything not listed in the proposal. If this change grows a second purpose, it is split into two changes rather than widened.

## Decisions

- The approach in the proposal, over the obvious cheaper alternative, for the reason given under *Why*. Recorded here so the next person does not rediscover the trade-off.

## Risks / Trade-offs

> **Maya Patel:** Your first delta restated the requirement without my grace-period scenario.
> `openspec archive` caught it before I did. The refresh commit is exactly right.

> **Sofia Alvarez:** This is the tool doing its job. The current spec is the merge base, not the
> branch you started from.
