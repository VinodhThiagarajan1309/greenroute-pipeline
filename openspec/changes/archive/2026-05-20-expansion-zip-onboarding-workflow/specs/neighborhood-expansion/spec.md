# neighborhood-expansion Delta

Change `expansion-zip-onboarding-workflow`: Zone registry becomes the single source of truth for zip -> zone

## MODIFIED Requirements

### Requirement: Zone registry: be the authoritative source for zip-to-zone mapping

The zone registry SHALL be the authoritative source for zip-to-zone mapping, read at resolution time by every consumer; no routing-module constant or bundle resource file may hold a copy.

#### Scenario: Be the authoritative source for zip-to-zone mapping

- **WHEN** the zone registry is exercised in a published window
- **THEN** the zone registry SHALL be the authoritative source for zip-to-zone mapping
- **AND** the outcome is visible in the job's emitted metrics

#### Scenario: Every consumer resolves zip to zone through the registry

- **WHEN** the zone registry is exercised in a published window
- **THEN** the zone registry SHALL be the authoritative source for zip-to-zone mapping, read at resolution time by every consumer; no routing-module constant or bundle resource file may hold a copy
- **AND** the outcome is visible in the job's emitted metrics
