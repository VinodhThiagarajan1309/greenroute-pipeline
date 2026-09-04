# Design: pesticide-license-gate

## Context

See proposal.md for motivation. This change touches `scheduling`, `technician-compliance`.

## Goals / Non-Goals

**Goals:**

- Hard gate in the scheduling write path: a booking for a service with `license_required` SHALL NOT be confirmed unless the assigned technician's `license_status` is `active`.

**Non-Goals:**

- Anything not listed in the proposal. If this change grows a second purpose, it is split into two changes rather than widened.

## Decisions

- The approach in the proposal, over the obvious cheaper alternative, for the reason given under *Why*. Recorded here so the next person does not rediscover the trade-off.

## Risks / Trade-offs

> **Aisha Bello:** Approving to get this merged today, but writing this down before it goes
> in: what happens if the TDA lookup is unreachable at write time? Right now unreachable
> reads as "not blocked" - this ships failing open. Right call to ship fast on a Saturday,
> not a decision I want us to have made by accident. Opening a follow-up, not blocking here.

> **Sofia Alvarez:** Agreed on both halves. Merge it, then we schedule the fail-open vs
> fail-closed decision properly instead of leaving it as whatever the code happens to do.

## Open Questions

- Fail-open or fail-closed when the TDA licence lookup is unreachable at write time? Shipped failing open on purpose (Aisha Bello, Sofia Alvarez, Apr 4). Not decided. Do not change silently; product and legal decide.
