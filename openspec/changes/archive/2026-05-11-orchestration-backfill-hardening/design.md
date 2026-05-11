# Design: orchestration-backfill-hardening

## Context

See proposal.md for motivation. This change touches `pipeline-orchestration`.

## Goals / Non-Goals

**Goals:**

- Backfill's row-count invariant gets a value check to go with it, and the comparison logic stops treating "nothing to compare" as "passed."

**Non-Goals:**

- Anything not listed in the proposal. If this change grows a second purpose, it is split into two changes rather than widened.

## Decisions

- The approach in the proposal, over the obvious cheaper alternative, for the reason given under *Why*. Recorded here so the next person does not rediscover the trade-off.

## Risks / Trade-offs

> **Aisha Bello:** This is the follow-up I asked for back in sprint 4. Ran it against the
> January backfill that started this whole thread - value parity holds, for what it's worth
> this many months later.

> **Wes Turner:** Checked too. It was fine, this time. Wasn't going to find that out by
> trusting the count again.
