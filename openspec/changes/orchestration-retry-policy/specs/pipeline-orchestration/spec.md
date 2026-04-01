# pipeline-orchestration Delta

Change `orchestration-retry-policy`: Job-level retry policy: classify failures retryable vs fatal

## ADDED Requirements

### Requirement: Job failure: be classified retryable or fatal at the point

A job failure SHALL be classified retryable or fatal at the point it is raised, not inferred later from the exception type.

#### Scenario: Be classified retryable or fatal at the point

- **WHEN** a job failure is exercised in a published window
- **THEN** a job failure SHALL be classified retryable or fatal at the point it is raised, not inferred later from the exception type
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Failed data-completeness or data-correctness gate: be classified fatal

A failed data-completeness or data-correctness gate SHALL be classified fatal and SHALL NOT be retried.

#### Scenario: Be classified fatal

- **WHEN** a failed data-completeness or data-correctness gate is exercised in a published window
- **THEN** a failed data-completeness or data-correctness gate SHALL be classified fatal and SHALL NOT be retried
- **AND** the outcome is visible in the job's emitted metrics

### Requirement: Retryable failure: retry at most 3 times with backoff

A retryable failure SHALL retry at most 3 times with backoff before paging.

#### Scenario: Retry at most 3 times with backoff before paging

- **WHEN** a retryable failure is exercised in a published window
- **THEN** a retryable failure SHALL retry at most 3 times with backoff before paging
- **AND** the outcome is visible in the job's emitted metrics
