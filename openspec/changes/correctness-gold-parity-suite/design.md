# Design: correctness-gold-parity-suite

## Context

See proposal.md for motivation. This change touches `data-correctness`.

## Goals / Non-Goals

**Goals:**

- Generalizes the parity check from S4 so it runs against every published gold table instead of only `gold_schedule_events`, and speeds up the batch-side scan while we're in there.

**Non-Goals:**

- Anything not listed in the proposal. If this change grows a second purpose, it is split into two changes rather than widened.

## Decisions

- The approach in the proposal, over the obvious cheaper alternative, for the reason given under *Why*. Recorded here so the next person does not rediscover the trade-off.

## Risks / Trade-offs

> **Derek Chen:** Payment ledger and schedule events don't necessarily partition the same
> way. What column is the pruning predicate built against, and did you confirm it against
> each table rather than assuming one column works everywhere?

> **Aisha Bello:** It's parameterized, not hardcoded - same `event_date` window the recon
> job already resolves once per run, passed down to every table's scan. That's the point
> of doing it this way: one predicate, no per-table drift.

> **Derek Chen:** That answers it. Approved.

> **Wes Turner:** Scan-bytes metric is the right call. Otherwise "60% less scanned" is a
> number in a PR description that nobody can check six months from now.
