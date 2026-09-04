# Design: expansion-zip-onboarding-workflow

## Context

See proposal.md for motivation. This change touches `neighborhood-expansion`, `scheduling`.

## Goals / Non-Goals

**Goals:**

- Does the uncontroversial three-quarters of {{PR:expansion-auto-onboard-zips}}, which a senior closed last sprint because it bundled five things and two of them needed decisions nobody had made yet. This PR: migrates the zip -> zone mapping into the registry, deletes the two other copies, and reconciles the zips where they disagreed.

**Non-Goals:**

- Anything not listed in the proposal. If this change grows a second purpose, it is split into two changes rather than widened.

## Decisions

- The approach in the proposal, over the obvious cheaper alternative, for the reason given under *Why*. Recorded here so the next person does not rediscover the trade-off.

## Risks / Trade-offs

> **Jonah Kim:** Did reconciling these change any pricing tier assignments? Tier hangs off
> zone, so if 78660 moved from round_rock to pflugerville its price moves with it.

> **Tariq Osman:** Checked before merging. 78660 and 78717 are both outer-ring either way,
> so same tier, no price change. 78664 and 78681 stay core in both scenarios too. Got
> lucky this time - I added a note in design.md that the next seam reconciliation needs
> to check this explicitly, since it won't always be free.

> **Sofia Alvarez:** Good that you checked instead of assuming. Merging as a merge commit
> rather than squash so the reconciliation table stays visible in the log - it's the kind
> of thing someone will grep for in six months.
