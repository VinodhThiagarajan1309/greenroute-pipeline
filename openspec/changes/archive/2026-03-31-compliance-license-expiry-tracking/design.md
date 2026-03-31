# Design: compliance-license-expiry-tracking

## Context

See proposal.md for motivation. This change touches `technician-compliance`.

## Goals / Non-Goals

**Goals:**

- Adds staggered, per-license TTL refresh for TDA license data instead of one fleet-wide nightly pull.

**Non-Goals:**

- Anything not listed in the proposal. If this change grows a second purpose, it is split into two changes rather than widened.

## Decisions

- The approach in the proposal, over the obvious cheaper alternative, for the reason given under *Why*. Recorded here so the next person does not rediscover the trade-off.

## Risks / Trade-offs

> **Wes Turner:** Hashing on license_number for the stagger slot - that's deterministic
> across redeploys, right? Don't want the whole fleet's refresh schedule reshuffling every
> time this job gets redeployed.

> **Aisha Bello:** Right, hash is deterministic and independent of run order. Added a test
> for exactly that after this comment - a redeploy shouldn't move anyone's slot.
