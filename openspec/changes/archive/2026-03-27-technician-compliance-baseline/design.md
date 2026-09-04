# Design: technician-compliance-baseline

## Context

See proposal.md for motivation. This change touches `technician-compliance`.

## Goals / Non-Goals

**Goals:**

- Adds `technician-compliance`, which tracks Texas Department of Agriculture (TDA) applicator license status and expiry per technician.

**Non-Goals:**

- Anything not listed in the proposal. If this change grows a second purpose, it is split into two changes rather than widened.

## Decisions

- The approach in the proposal, over the obvious cheaper alternative, for the reason given under *Why*. Recorded here so the next person does not rediscover the trade-off.

## Risks / Trade-offs

> **Derek Chen:** This is the second half of a control we flagged as half-built four sprints
> ago, and it's landing without the half that actually blocks anything. I want to be sure
> this doesn't sit for a sprint the way the flag did. What's the plan for the gate?

> **Jonah Kim:** Next PR, same week. Wanted this reviewed on its own so the license-matching
> logic gets real attention instead of getting skimmed as the boring half of a bigger diff.
