# Design: expansion-auto-onboard-zips

## Context

See proposal.md for motivation. This change touches `neighborhood-expansion`.

## Goals / Non-Goals

**Goals:**

- Attempts the full neighborhood onboarding flow in one change: migrate routing and the CSV onto the registry, rebuild the zone dimension nightly instead of weekly, auto-assign a pricing tier, check technician coverage, and verify the result.

**Non-Goals:**

- Anything not listed in the proposal. If this change grows a second purpose, it is split into two changes rather than widened.

## Decisions

- The approach in the proposal, over the obvious cheaper alternative, for the reason given under *Why*. Recorded here so the next person does not rediscover the trade-off.

## Risks / Trade-offs

> **Sofia Alvarez:** This is five different changes wearing one PR. Registry migration and
> the nightly rebuild are uncontroversial - ship those. Pricing tier auto-assignment and
> the coverage-check gate are both decisions nobody has actually made (auto-assign by what
> rule? does a failed coverage check block onboarding or just warn?). Bundled together,
> none of it can be reviewed on its own terms and none of it can be reverted independently
> if one part turns out wrong.

> **Tariq Osman:** Fair, I got excited and tried to finish the thing I filed {{I17}} about
> in one go. Splitting: registry migration + nightly rebuild becomes its own change, and
> I'll bring pricing tier assignment and the coverage gate back separately once there's an
> actual answer on both, instead of guessing.

> **Sofia Alvarez:** That's the right split. Closing this one, not rejecting it - the
> uncontroversial half should show up as its own PR next sprint.
