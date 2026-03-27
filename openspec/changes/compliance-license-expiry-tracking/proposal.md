# Proposal: Staggered per-license TTL refresh for TDA license data

- **Change id:** `compliance-license-expiry-tracking`
- **Author:** Aisha Bello
- **Sprint:** 6

## Why

Aisha's rate-limit writeup (I12) laid out the numbers:

| applicators | requests | time at 60/min |
|---|---|---|
| 47 (today) | 47 | 47s |
| 400 (projected) | 400 | ~7 min |

Not urgent at 47. At the ~400 technicians the expansion plan implies, a full refresh is
7+ minutes of sustained requests against a government endpoint with no SLA and no bulk
mode, and I'd rather not discover that the first morning it happens. Hashing license_number
to pick each license's refresh slot spreads those 400 requests across the day, so the
fleet's own refresh never competes with itself for the 60/min ceiling.

TTL is flat for now, not scaled to proximity-to-expiry. A license two days from expiry
refreshing on the same cadence as one renewed last month is not ideal, it's just not the
problem this PR is solving. Noted in design.md as the next step.

## What Changes

Adds staggered, per-license TTL refresh for TDA license data instead of one fleet-wide
nightly pull.

- **ADDED** requirement: license data SHALL refresh on a per-license TTL rather than a single fleet-wide batch.
- **ADDED** requirement: refresh requests SHALL be distributed across the refresh window so no rolling 60-second period exceeds the TDA rate limit.
- **ADDED** requirement: license data exceeding its TTL SHALL be flagged stale rather than treated as current.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `technician-compliance`: requirements change as listed above.

## Impact

Affected code: `src/greenroute/compliance/`, `tests/compliance/`.
