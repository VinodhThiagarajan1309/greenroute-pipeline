# Proposal: Job-level retry policy: classify failures retryable vs fatal

- **Change id:** `orchestration-retry-policy`
- **Author:** Sofia Alvarez
- **Sprint:** 6

## Why

A blanket retry-3-times policy was fine when every failure was infrastructure. It stopped
being fine the moment we added gates that are supposed to fail
(`completeness-source-window-closure`, `correctness-recon-baseline`). A gate failure is
deterministic - the same input fails the same way on attempt two and attempt three.
Retrying it doesn't fix anything, it delays the page by however long the backoff takes and
lets that delay pass for resilience.

Same shape as the compliance gate landing this sprint: a control that a well-meaning
general-purpose behavior can defeat without anyone deciding to defeat it. There it was
retry-around-a-check; here it would be silently swallowing a real failure inside three
retry attempts. Writing the classification into the spec so the next job someone adds
doesn't inherit "retry everything" as the default.

## What Changes

Job-level retry policy. Retryable failure classes (timeouts, throttling, transient
connection errors) retry with backoff up to 3 attempts. Everything else - specifically a
failed completeness or correctness gate - pages on the first failure and does not retry.

- **ADDED** requirement: a job failure SHALL be classified retryable or fatal at the point it is raised, not inferred later from the exception type.
- **ADDED** requirement: a failed data-completeness or data-correctness gate SHALL be classified fatal and SHALL NOT be retried.
- **ADDED** requirement: a retryable failure SHALL retry at most 3 times with backoff before paging.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `pipeline-orchestration`: requirements change as listed above.

## Impact

Affected code: `src/greenroute/orchestration/`, `tests/orchestration/`.
