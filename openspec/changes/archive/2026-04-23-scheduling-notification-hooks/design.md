# Design: scheduling-notification-hooks

## Context

See proposal.md for motivation. This change touches `scheduling`, `customer-notifications`.

## Goals / Non-Goals

**Goals:**

- Closes the gap from {{I15}}: reschedule built its own send call and skipped the preference lookup entirely. Fixes it by making `NotificationSender.send` itself refuse to deliver to an opted-out recipient, so no caller can bypass the check by forgetting it.

**Non-Goals:**

- Anything not listed in the proposal. If this change grows a second purpose, it is split into two changes rather than widened.

## Decisions

- The approach in the proposal, over the obvious cheaper alternative, for the reason given under *Why*. Recorded here so the next person does not rediscover the trade-off.

## Risks / Trade-offs

> **Maya Patel:** first pass checks preference at the top of the reschedule handler, same
> pattern as the other three. should be equivalent to checking inside send()?

> **Priya Nair:** equivalent today, but it's the exact same shape as {{I15}} - confirmation
> and reminder both "correctly" checked preference at their own call site, and reschedule
> just didn't, because someone wrote a new call site and had no way to know to copy the
> check. if the check lives at N call sites we will be back here at N+1.

> **Derek Chen:** Agreed. A control that has to be remembered separately at every call site
> is not a control, it's a convention, and conventions are exactly what got us three opted-out
> customers texted. If `send` refuses on its own, no caller can get this wrong even by
> omission.

> **Maya Patel:** ok that's fair. force-pushed - check is inside NotificationSender.send now,
> reschedule handler doesn't know preferences exist at all anymore. genuinely nicer than what
> i had, not just safer
