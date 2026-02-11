# Design: completeness-watermarks

## Context

See proposal.md for motivation. This change touches `data-completeness`.

## Goals / Non-Goals

**Goals:**

- Adds `data-completeness` and the watermark mechanism that stops a gold partition publishing while one of its sources is still open.

**Non-Goals:**

- Anything not listed in the proposal. If this change grows a second purpose, it is split into two changes rather than widened.

## Decisions

- The approach in the proposal, over the obvious cheaper alternative, for the reason given under *Why*. Recorded here so the next person does not rediscover the trade-off.

## Risks / Trade-offs

> **Derek Chen:** 48h of latency on the schedule ledger is a real cost and worth naming.
> I still think it is the right trade: late and correct beats prompt and wrong for anything
> finance reads.

> **Aisha Bello:** Agreed, and the watermark is per-source, so a source that is never late
> doesn't inherit the 48h. Only cancellations pay for cancellations.
