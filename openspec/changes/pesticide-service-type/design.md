# Design: pesticide-service-type

## Context

See proposal.md for motivation. This change touches `service-catalog`.

## Goals / Non-Goals

**Goals:**

- Adds pesticide application as a catalog service type, carrying a `license_required` flag.

**Non-Goals:**

- Anything not listed in the proposal. If this change grows a second purpose, it is split into two changes rather than widened.

## Decisions

- The approach in the proposal, over the obvious cheaper alternative, for the reason given under *Why*. Recorded here so the next person does not rediscover the trade-off.

## Risks / Trade-offs

> **Derek Chen:** The flag is right, but I want to flag the gap explicitly: we now *record*
> that a license is required and we still have nothing that *checks* it. That's a
> half-implemented control, which can read as safer than no control at all. Please make
> that limitation loud in design.md.

> **Jonah Kim:** Done - design.md now says plainly that nothing enforces this yet and that
> enforcement needs a capability that doesn't exist.
