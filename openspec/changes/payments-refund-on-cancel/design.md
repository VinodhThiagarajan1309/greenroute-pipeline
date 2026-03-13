# Design: payments-refund-on-cancel

## Context

See proposal.md for motivation. This change touches `payments`, `scheduling`.

## Goals / Non-Goals

**Goals:**

- Payments stops hardcoding its own T-4h auto-refund threshold and reads scheduling's cancellation threshold instead.

**Non-Goals:**

- Anything not listed in the proposal. If this change grows a second purpose, it is split into two changes rather than widened.

## Decisions

- The approach in the proposal, over the obvious cheaper alternative, for the reason given under *Why*. Recorded here so the next person does not rediscover the trade-off.

## Risks / Trade-offs

> **Maya Patel:** could payments just cache the threshold value on deploy instead of calling
> scheduling on every refund decision? seems like a lot of coupling for one number

> **Derek Chen:** that's what got us here. A cached copy is still a second copy, it's just one
> with a delay instead of no delay. The requirement scheduling wrote in sprint 2 is specific
> about this - no capability holds its own, cached or otherwise. Payments reads at decision
> time.

> **Sofia Alvarez:** Derek's right and it's already the spec, not really up for renegotiation
> in this PR. If the read-at-decision-time cost ever matters, we solve it as a caching
> problem with an invalidation story, not by growing a second copy again.
