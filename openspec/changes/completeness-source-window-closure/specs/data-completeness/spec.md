# data-completeness Delta

Change `completeness-source-window-closure`: Gate gold publish on source-window closure

## ADDED Requirements

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
