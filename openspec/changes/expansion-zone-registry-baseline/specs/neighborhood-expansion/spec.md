# neighborhood-expansion Delta

Change `expansion-zone-registry-baseline`: Add the neighborhood-expansion capability and the zone registry

## Purpose

Onboarding new Austin-area zones and ZIP codes into the pipeline.

## ADDED Requirements

### Requirement: Zone registry: be the authoritative source for zip-to-zone mapping

The zone registry SHALL be the authoritative source for zip-to-zone mapping.

#### Scenario: Be the authoritative source for zip-to-zone mapping

- **WHEN** the zone registry is exercised in a published window
- **THEN** the zone registry SHALL be the authoritative source for zip-to-zone mapping
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Zip with conflicting zone assignments across: be flagged for manual resolution before the registry

A zip with conflicting zone assignments across ingest sources SHALL be flagged for manual resolution before the registry accepts a value for it.

#### Scenario: Be flagged for manual resolution before the registry accepts

- **WHEN** a zip with conflicting zone assignments across ingest sources is exercised in a published window
- **THEN** a zip with conflicting zone assignments across ingest sources SHALL be flagged for manual resolution before the registry accepts a value for it
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Quarantined booking whose zip resolves: become eligible for re-processing

A quarantined booking whose zip resolves to a registered zone SHALL become eligible for re-processing.

#### Scenario: Become eligible for re-processing

- **WHEN** a quarantined booking whose zip resolves to a registered zone is exercised in a published window
- **THEN** a quarantined booking whose zip resolves to a registered zone SHALL become eligible for re-processing
- **AND** the outcome is visible in the job's emitted metrics
