# Design: expansion-zone-registry-baseline

## Context

See proposal.md for motivation. This change touches `neighborhood-expansion`.

## Goals / Non-Goals

**Goals:**

- Adds `neighborhood-expansion` and stands up `zone_registry` as the table meant to become the single source of truth for zip-to-zone mapping.

**Non-Goals:**

- Anything not listed in the proposal. If this change grows a second purpose, it is split into two changes rather than widened.

## Decisions

- The approach in the proposal, over the obvious cheaper alternative, for the reason given under *Why*. Recorded here so the next person does not rediscover the trade-off.

## Risks / Trade-offs

> **Jonah Kim:** This is the thing I said back in catalog-pricing-tiers - zone should own
> the zip mapping and everything else just asks zone. Glad to see it actually land as its
> own table instead of implied by whoever got there first.

> **Sofia Alvarez:** Agreed on shipping the registry before the migration. One ask: put the
> 4 disagreeing zips and how each was resolved in design.md, not just in this PR
> description. In six months this thread is gone and someone will hit zip 78660
> disagreeing with itself again.

> **Tariq Osman:** Done. I'll say plainly what I don't have an opinion on yet: whether zone
> boundaries should eventually be geofenced polygons instead of zip lists. The DAB CSV has
> a `boundary_wkt` column that's empty for every row, which makes me think someone started
> that and stopped. Not touching it this change - registry stays zip-list, matching what
> routing already assumes.
