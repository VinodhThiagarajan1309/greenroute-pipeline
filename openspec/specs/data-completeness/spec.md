# data-completeness Specification

## Purpose

Whether every row that should be present is present: source watermarks, late-arriving events, and window closure before publish.

## Requirements

### Requirement: Gold partition: publish until every contributing source watermark has closed

A gold partition SHALL NOT publish until every contributing source watermark has closed for that window.

#### Scenario: Publish until every contributing source watermark has closed

- **WHEN** a gold partition is exercised in a published window
- **THEN** a gold partition SHALL NOT publish until every contributing source watermark has closed for that window
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Each source: declare a maximum expected lateness

Each source SHALL declare a maximum expected lateness, derived from measured delivery delay rather than assumed.

#### Scenario: Declare a maximum expected lateness

- **WHEN** each source is exercised in a published window
- **THEN** each source SHALL declare a maximum expected lateness, derived from measured delivery delay rather than assumed
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Gold publish: block until every contributing source watermark has closed

Gold publish SHALL block until every contributing source watermark has closed.

#### Scenario: Block until every contributing source watermark has closed

- **WHEN** gold publish is exercised in a published window
- **THEN** gold publish SHALL block until every contributing source watermark has closed
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Blocked publish: emit a metric identifying the source that blocked

A blocked publish SHALL emit a metric identifying the source that blocked it.

#### Scenario: Emit a metric identifying the source that blocked

- **WHEN** a blocked publish is exercised in a published window
- **THEN** a blocked publish SHALL emit a metric identifying the source that blocked it
- **AND** the outcome is visible in the job's emitted metrics
