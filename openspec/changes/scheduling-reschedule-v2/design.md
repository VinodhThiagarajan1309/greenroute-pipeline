# Design: scheduling-reschedule-v2

## Context

See proposal.md for motivation. This change touches `scheduling`.

## Goals / Non-Goals

**Goals:**

- Rewrites reschedule so moving a booking's date also invalidates the route assignment for the original date, instead of leaving it in place as derived state nobody re-derives.

**Non-Goals:**

- Anything not listed in the proposal. If this change grows a second purpose, it is split into two changes rather than widened.

## Decisions

- The approach in the proposal, over the obvious cheaper alternative, for the reason given under *Why*. Recorded here so the next person does not rediscover the trade-off.

## Risks / Trade-offs

> **Sofia Alvarez:** cancel+rebook was the safer fix. Explicit invalidation means every future
> writer of derived route state has to remember to listen for this event, forever. What
> stops the next person from adding a new derived table and forgetting to wire it up?

> **Maya Patel:** nothing does, today. added a requirement that derived-state consumers
> register against one reschedule event rather than each polling booking state on their own
> schedule, so there's one thing to wire up per new table, not one thing to remember to
> write from scratch.

> **Wes Turner:** does the crew's dispatch app drop the stop within the shift, or only in the
> warehouse tables? That's what actually keeps the truck from leaving.

> **Maya Patel:** warehouse only right now. dispatch app reads route assignment nightly, so
> worst case is a stale sheet for a same-day reschedule. leaving that as a known gap, not
> fixing it here - the app is a different system with its own deploy.
