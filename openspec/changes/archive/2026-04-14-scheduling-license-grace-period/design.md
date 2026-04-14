# Design: scheduling-license-grace-period

## Context

See proposal.md for motivation. This change touches `scheduling`, `technician-compliance`.

## Goals / Non-Goals

**Goals:**

- Relaxes the licence gate by exactly one case. A technician whose TDA renewal was filed on or before the expiry date stays bookable for 30 days after expiry, which is the TDA grace rule. Everything else the gate did on Apr 4 it still does, and the requirement block says so in full - this is a MODIFIED requirement, restated, not a second requirement next to the first.

**Non-Goals:**

- Anything not listed in the proposal. If this change grows a second purpose, it is split into two changes rather than widened.

## Decisions

- The approach in the proposal, over the obvious cheaper alternative, for the reason given under *Why*. Recorded here so the next person does not rediscover the trade-off.

## Risks / Trade-offs

> **Derek Chen:** MODIFIED and restated in full - the Apr 4 scenario is still in the block. I
> checked that before I read a line of code, which is the point of the block.

> **Jonah Kim:** The original gate was mine and this is the case I did not know about. Approving.
> Heads up that I have a delta open against this same requirement (herbicide and fertilizer
> are TDA-licensed too). I'll sort out the overlap on my side.

> **Sofia Alvarez:** Two changes on one requirement in one sprint. Whoever archives second has
> to restate what the first one added. Watch for it.
