# Design: correctness-incremental-parity

## Context

See proposal.md for motivation. This change touches `data-correctness`.

## Goals / Non-Goals

**Goals:**

- Replaces the full-history rescan in the incremental/batch parity check with a bounded lookback.

**Non-Goals:**

- Anything not listed in the proposal. If this change grows a second purpose, it is split into two changes rather than widened.

## Decisions

- The approach in the proposal, over the obvious cheaper alternative, for the reason given under *Why*. Recorded here so the next person does not rediscover the trade-off.

## Risks / Trade-offs

> **Wes Turner:** 72h - measured or padded? "wider than 48h" doesn't have to mean 72, it could
> be 49.

> **Aisha Bello:** padded, on purpose. 49h technically satisfies the requirement and leaves
> zero margin if the watermark itself ever moves without someone remembering to bump this
> number too. 72h is a full extra day of headroom over the 48h watermark, cheap given recon
> is bounded either way now.

> **Sofia Alvarez:** good, and I would rather the requirement say "strictly wider than the
> watermark" than "72h" for exactly that reason - the number can move, the relationship
> shouldn't be able to drift without someone noticing it in review.
