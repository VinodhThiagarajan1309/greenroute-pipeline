# Design: scheduling-zone-routing-v2

## Context

See proposal.md for motivation. This change touches `scheduling`, `pipeline-orchestration`.

## Goals / Non-Goals

**Goals:**

- v2 of the zone-based route optimizer. Zone grouping and stop ordering both move into `scheduling`, and the DAB job-parameter config knob that used to also decide stop order is deleted.

**Non-Goals:**

- Anything not listed in the proposal. If this change grows a second purpose, it is split into two changes rather than widened.

## Decisions

- The approach in the proposal, over the obvious cheaper alternative, for the reason given under *Why*. Recorded here so the next person does not rediscover the trade-off.

## Risks / Trade-offs

> **Wes Turner:** the migration commit and the config-knob-removal commit are separate right
> now. If this ever gets reverted, reverting just the migration commit leaves scheduling not
> ordering anything and the config knob still gone. Put them in one commit or the revert
> story is broken.

> **Maya Patel:** good catch, hadn't thought about revert. squashing those two into one and
> force-pushing, one sec

> **Sofia Alvarez:** +1 to Wes. Also flagging: this now touches two capability specs in one
> change. Fine here since the whole point is transferring ownership - don't let that become
> a habit for anything that isn't a migration.

> **Maya Patel:** force-pushed - migration and config removal are one commit now. the wip
> commit from testing the port is gone too, branch history is cleaner.
