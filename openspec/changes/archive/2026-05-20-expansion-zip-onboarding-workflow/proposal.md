# Proposal: Zone registry becomes the single source of truth for zip -> zone

- **Change id:** `expansion-zip-onboarding-workflow`
- **Author:** Tariq Osman
- **Sprint:** 10

## Why

Closes {{I18}}. The mapping lived in three places - a hardcoded dict in the routing
module, a CSV in the DAB resources folder, and ops' spreadsheet - and they disagreed on
4 zips, all in the Round Rock / Pflugerville seam.

| zip | dict said | CSV said | ops said | resolved to |
|---|---|---|---|---|
| 78660 | round_rock | pflugerville | pflugerville | pflugerville |
| 78664 | round_rock | round_rock | pflugerville | round_rock |
| 78681 | pflugerville | round_rock | round_rock | round_rock |
| 78717 | round_rock | round_rock | pflugerville | pflugerville |

Resolved each one by calling ops and asking which crew actually covers that block today,
not by picking the majority answer. Majority would have gotten 78664 wrong.

This does **not** touch the nightly-vs-event-driven zone rebuild question from {{I17}}.
I still don't know which way that should go - I understand nightly (it's a one-line
change) but I don't understand the downstream fan-out well enough to say event-driven is
safe, so I'm not guessing. Leaving {{I17}} open.

## What Changes

Does the uncontroversial three-quarters of {{PR:expansion-auto-onboard-zips}}, which a
senior closed last sprint because it bundled five things and two of them needed decisions
nobody had made yet. This PR: migrates the zip -> zone mapping into the registry, deletes
the two other copies, and reconciles the zips where they disagreed.

- **MODIFIED** requirement: the zone registry SHALL be the authoritative source for zip-to-zone mapping, read at resolution time by every consumer; no routing-module constant or bundle resource file may hold a copy.
- **MODIFIED** requirement: scheduling SHALL own both zone grouping and within-zone stop ordering, resolving each stop's zone through the neighborhood-expansion registry rather than a local zip mapping.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `neighborhood-expansion`: requirements change as listed above.
- `scheduling`: requirements change as listed above.

## Impact

Affected code: `src/greenroute/expansion/`, `src/greenroute/scheduling/`, `tests/expansion/`, `tests/scheduling/`.

Closes {{I18}}.
